import flet as ft
import MetaTrader5 as mt5
from decimal import Decimal, ROUND_DOWN, InvalidOperation


class Functions:
    div = ft.Divider(height=2, color=ft.Colors.WHITE_38, thickness=1, opacity=0.5, expand=True)
    symbol_name = "XAUUSD"  # Default symbol name

    @staticmethod
    def calc(e, controls, page):
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
        else:
            controls.lot_size_text.value = format(lot_size, "f")

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
    def update_symbol_dropdown(e, controls, page):
        controls.symbol = e.control.value
        Functions.symbol_name = controls.symbol
        page.update()

    @staticmethod
    def refresh(e, controls, page, show_dialog=True):
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


        if show_dialog:
            dialog = ft.AlertDialog(
                title=ft.Text("Refreshed"),
                content=ft.Text("The values have been refreshed."),
            )
            page.open = dialog
        page.update()

    @staticmethod
    def get_symbol() -> list[ft.DropdownOption]:
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            return []

        symbols = mt5.symbols_get()
        if symbols is None:
            print("Failed to get Symbol, error code:", mt5.last_error())
            mt5.shutdown()
            return []

        options = [ft.dropdown.Option(symbol.name) for symbol in symbols]
        mt5.shutdown()
        return options

    @staticmethod
    def get_data():
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            return {"balance": 0, "leverage": 0}

        account_info = mt5.account_info()
        symbol_info = mt5.symbol_info(Functions.symbol_name)
        if account_info is not None:
            _balance = account_info.balance
            _leverage = account_info.leverage
            _tick_size = symbol_info.trade_tick_size
            _tick_value = symbol_info.trade_tick_value
            _contract_size = symbol_info.trade_contract_size
            _digit = symbol_info.digits
            _volume_step = symbol_info.volume_step
        else:
            print("Failed to get account info, error code =", mt5.last_error())
            _balance = 0
            _leverage = 0
            _tick_size = 0
            _tick_value = 0

        mt5.shutdown()
        return {
            "balance": _balance,
            "leverage": _leverage,
            "tick_size": _tick_size,
            "tick_value": _tick_value,
            "contract_size": _contract_size,
            "digit": _digit,
            "volume_step": _volume_step,
        }
