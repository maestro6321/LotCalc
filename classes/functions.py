import flet as ft
import MetaTrader5 as mt5
from decimal import Decimal, ROUND_DOWN, InvalidOperation


class Functions:
    div = ft.Divider(height=2, color=ft.Colors.WHITE_38, thickness=1, opacity=0.5, expand=True)
    symbol_name = "XAUUSD"  # Default symbol name

    # MT5 connection state
    _mt5_initialized = False
    _symbol_cache = None

    @staticmethod
    def ensure_mt5_initialized() -> bool:
        """Initialize MT5 once and reuse the connection. Returns True if ready."""
        if Functions._mt5_initialized:
            return True
        if mt5.initialize():
            Functions._mt5_initialized = True
            return True
        print("MT5 initialize() failed, error code =", mt5.last_error())
        return False

    @staticmethod
    def shutdown_mt5() -> None:
        """Explicit cleanup for app exit."""
        if Functions._mt5_initialized:
            mt5.shutdown()
            Functions._mt5_initialized = False

    @staticmethod
    def calc_margin(symbol_name, lot_size, price):
        if lot_size <= 0 or price <= 0:
            return Decimal("0")

        if not Functions.ensure_mt5_initialized():
            return Decimal("0")

        margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol_name, float(lot_size), float(price))

        if margin is None:
            print("Failed to calculate margin, error code =", mt5.last_error())
            return Decimal("0")

        return Decimal(str(margin))

    @staticmethod
    def calc(controls, page):
        try:
            balance = Decimal(str(controls.balance))
            risk = Decimal(str(controls.risk))
            loss_per_lot = Decimal(str(controls.pipet_size))
            volume_step = Decimal(str(controls.volume_step))

            if balance <= 0 or risk <= 0 or loss_per_lot <= 0 or volume_step <= 0:
                controls.lot_size = 0
                controls.lot_size_text.value = "Invalid input"
                page.update()
                return

            risk_amount = balance * risk / Decimal("100")
            raw_lot_size = risk_amount / loss_per_lot
            lot_size = (raw_lot_size / volume_step).to_integral_value(rounding=ROUND_DOWN) * volume_step
        except (InvalidOperation, ValueError, ZeroDivisionError):
            controls.lot_size = 0
            controls.lot_size_text.value = "Invalid input"
            page.update()
            return

        controls.lot_size = float(lot_size)
        if lot_size == 0:
            controls.lot_size_text.value = f"{raw_lot_size:.8f} (below min step {volume_step})"
            controls.margin_size = 0
            controls.margin_size_text.value = "0"
        else:
            margin_size = Functions.calc_margin(controls.symbol, lot_size, Decimal(str(controls.symbol_price)))
            controls.margin_size = float(margin_size)
            controls.lot_size_text.value = format(lot_size, "f")
            controls.margin_size_text.value = f"{margin_size:.2f}"

        page.update()

    @staticmethod
    def update_risk(e, controls, page):
        controls.risk = float(e.control.value)
        controls.risk_value_text.value = f"{controls.risk}"
        page.update()

    @staticmethod
    def update_pipet_slider(e, controls, page):
        controls.pipet_size = int(e.control.value)
        controls.pipet_value_text.value = f"{controls.pipet_size}"
        page.update()

    @staticmethod
    def update_symbol_dropdown(e, controls, _page):
        controls.symbol = e.control.value
        Functions.symbol_name = controls.symbol
        # Do not call page.update() here - caller (refresh) will do it

    @staticmethod
    def refresh(_e, controls, page, show_dialog=True):
        data = Functions.get_data()
        controls.balance = data["balance"]
        controls.balance_value_text.value = f"{controls.balance}"

        controls.leverage = data["leverage"]
        controls.leverage_value_text.value = f"{controls.leverage}"

        controls.tick_size = data["tick_size"]
        controls.tick_size_value_text.value = f"{controls.tick_size}"

        controls.tick_value = data["tick_value"]
        controls.tick_value_text.value = f"{controls.tick_value}"

        controls.contract_size = data["contract_size"]
        controls.contract_size_text.value = f"{controls.contract_size}"

        controls.digit = data["digit"]
        controls.digit_text.value = f"{controls.digit}"

        controls.volume_step = data["volume_step"]
        controls.volume_step_text.value = f"{controls.volume_step}"

        controls.symbol_price = data["symbol_price"]
        controls.symbol_price_text.value = f"{controls.symbol_price}"


        if show_dialog:
            dialog = ft.AlertDialog(
                title=ft.Text("Refreshed"),
                content=ft.Text("The values have been refreshed."),
            )
            page.open = dialog
        page.update()

    @staticmethod
    def get_symbol(force_reload: bool = False) -> list[ft.DropdownOption]:
        # Return cached symbols if available and not forcing reload
        if Functions._symbol_cache is not None and not force_reload:
            return Functions._symbol_cache

        if not Functions.ensure_mt5_initialized():
            return []

        symbols = mt5.symbols_get()
        if symbols is None:
            print("Failed to get Symbol, error code:", mt5.last_error())
            return []

        options = [ft.dropdown.Option(symbol.name) for symbol in symbols]
        Functions._symbol_cache = options
        return options

    @staticmethod
    def get_default_data():
        return {
            "balance": 0,
            "leverage": 0,
            "tick_size": 0,
            "tick_value": 0,
            "contract_size": 0,
            "digit": 0,
            "volume_step": 0,
            "symbol_price": 0,
        }

    @staticmethod
    def get_data():
        if not Functions.ensure_mt5_initialized():
            return Functions.get_default_data()

        account_info = mt5.account_info()
        symbol_info = mt5.symbol_info(Functions.symbol_name)
        if account_info is None or symbol_info is None:
            print("Failed to get account or symbol info, error code =", mt5.last_error())
            return Functions.get_default_data()

        symbol_tick = mt5.symbol_info_tick(Functions.symbol_name)
        return {
            "balance": account_info.balance,
            "leverage": account_info.leverage,
            "tick_size": symbol_info.trade_tick_size,
            "tick_value": symbol_info.trade_tick_value,
            "contract_size": symbol_info.trade_contract_size,
            "digit": symbol_info.digits,
            "volume_step": symbol_info.volume_step,
            "symbol_price": symbol_tick.ask if symbol_tick else 0,
        }

