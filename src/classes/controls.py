import flet as ft
from .functions import Functions

class ControlsPage:
    def __init__(self):
        self.balance = 1
        self.balance_value_text = ft.Text(str(self.balance))
        self.risk = 1
        self.risk_value_text = ft.Text(str(self.risk)) 
        self.pipet_size = 1
        self.pipet_value_text = ft.Text(f"{self.pipet_size}%")
        self.symbol = "XAUUSD"
        self.leverage = 1
        self.leverage_value_text = ft.Text(str(self.leverage), color=ft.Colors.RED)
        self.tick_size = 1
        self.tick_size_value_text = ft.Text(str(self.tick_size))
        self.tick_value = 1
        self.tick_value_text = ft.Text(str(self.tick_value))
        self.contract_size = 1
        self.contract_size_text = ft.Text(str(self.contract_size))
        self.digit = 1
        self.digit_text = ft.Text(str(self.digit))
        self.volume_step = 1
        self.volume_step_text = ft.Text(str(self.volume_step))
        self.lot_size = 0
        self.lot_size_text = ft.Text(str(self.lot_size), color=ft.Colors.GREEN_400)
        self.symbol_price = 0
        self.symbol_price_text = ft.Text(str(self.symbol_price), color=ft.Colors.BLUE_400)
        self.margin_size = 0
        self.margin_size_text = ft.Text(str(self.margin_size), color=ft.Colors.ORANGE_400)
        self.stop_loss_distance = 0
        self.stop_loss_text = ft.Text(str(self.stop_loss_distance), color=ft.Colors.RED_400)

    async def run(self, page: ft.Page):
        if page.web:
            await page.browser_context_menu.disable()

        async def exit_app(e):
            Functions.shutdown_mt5()
            await page.window.close()

        def update_symbol(_e):
            Functions.update_symbol_dropdown(_e, self, page)
            # Single page.update() via refresh() - no duplicate
            Functions.refresh(_e, self, page, show_dialog=False)


        stop_text_field = ft.TextField(
            label="Stop %",
            value=str(self.pipet_size),
            width=120, height=40,
            border=ft.OutlineInputBorder(side=ft.BorderSide(color=ft.Colors.WHITE_38)),
            on_change=lambda e: Functions.update_pipet_text(e, self, page),
        )

        risk_text_field = ft.TextField(
            label="Risk %",
            value=str(self.risk),
            width=120, height=40,
            border=ft.OutlineInputBorder(side=ft.BorderSide(color=ft.Colors.WHITE_38)),
            on_change=lambda e: Functions.update_risk(e, self, page),
        )

        symbol_dropdown = ft.Dropdown(
            width=170,
            height=45,
            menu_width=220,
            menu_height=200,
            border=ft.OutlineInputBorder(side=ft.BorderSide(color=ft.Colors.WHITE_38)),
            content_padding=10,
            label="Symbol",
            hint_text="Search symbol",
            leading_icon=ft.Icons.SEARCH,
            enable_search=True,
            enable_filter=True,
            editable=True,
            value=self.symbol,
            text_size=11,
            options=Functions.get_symbol(),
            on_select=update_symbol,
        )

        main = ft.Column(spacing=2, alignment=ft.MainAxisAlignment.START)

        footer = ft.Container(
            padding=ft.Padding.symmetric(vertical=2),
            alignment=ft.Alignment.BOTTOM_CENTER,
            content=ft.Row(
                [
                    ft.FilledButton("Calculate", width=120,  on_click=lambda _e: Functions.calc_from_percent(self , page)),
                    ft.OutlinedButton("Exit", width=120, on_click=exit_app),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        )

        main.controls.append(
            ft.Row(
                [
                    ft.Text("Balance:"),
                    self.balance_value_text,
                    ft.Container(expand=True),
                    symbol_dropdown,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        main.controls.append(
            ft.Row(
                [
                    ft.Text("Risk:"),
                    risk_text_field,
                    ft.Container(expand=True), 
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        main.controls.append(
            ft.Row(
                [
                    ft.Text("Stop %:"),
                    stop_text_field,
                    self.pipet_value_text,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        main.controls.append(
            Functions.div
        )
        main.controls.append(
            ft.Row(
                [
                            ft.Text("Tick Size:"),
                            self.tick_size_value_text,
                            # ft.Container(expand=True),
                            ft.Row(
                                controls=[
                                    ft.Text("Leverage:", color=ft.Colors.ORANGE),
                                    self.leverage_value_text,
                                ]
                            ),
                    ft.Row(
                        controls=[
                            ft.Text("Tick Value:"),
                            self.tick_value_text,
                        ]
                    ) 
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        main.controls.append(
            ft.Row(
                [
                    ft.Text("Contract Size:"),
                    self.contract_size_text,
                    # ft.Container(expand=True),
                    ft.Row(
                        controls=[
                            ft.Text("Digits:"),
                            self.digit_text,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Volume Step:"),
                            self.volume_step_text,
                        ]
                    ) 
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

        main.controls.append(
            Functions.div
        )
        main.controls.append(
            ft.Row(
                controls=[
                    ft.Text("Lot Size:"),
                    self.lot_size_text,
                    ft.Container(expand=True),
                    ft.Text("Potential Loss:"),
                    self.stop_loss_text,
                ]
            )
        )
        main.controls.append(
            ft.Row(
                controls=[
                    ft.Text("Price:"),
                    self.symbol_price_text,
                    ft.Container(expand=True),
                    ft.Text("Margin:"),
                    self.margin_size_text,
                ]
            )
        )

        panel = ft.SafeArea(
            expand=True,
            content=ft.ContextMenu(
                primary_trigger=ft.ContextMenuTrigger.DOWN,
                secondary_items=[
                    ft.PopupMenuItem(content="Refresh", on_click=lambda e: Functions.refresh(e, self, page)),
                    ft.PopupMenuItem(content="Exit", on_click=exit_app),
                ],
                content=ft.Container(
                    key="safe_area_container",
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    # border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            main,
                            ft.Container(expand=True),
                            footer,
                        ]
                    )
                )
            )
        )

        page.add(panel)
        Functions.refresh(None, self, page, show_dialog=False)
