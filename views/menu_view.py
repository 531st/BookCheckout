import flet as ft
from modules.record_model import Record
from modules.qr_scanner import read_qr_code
from modules.colors import color_mint2, color_mint3


def MenuView(page):    

    content = ft.Row(
            controls=
                [
                    ft.ElevatedButton(
                    on_click=lambda _:page.go('/reg'),
                    content=ft.Text(value="Взять Книгу", size=80,color=ft.colors.WHITE),
                    height=680, width=620,
                    style=ft.ButtonStyle(
                    color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLUE,
                    },
                    bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.with_opacity(0,color_mint2)},
                    padding={ft.MaterialState.HOVERED: 20},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0, "": 1},
                    animation_duration=500,
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(1, color_mint3),
                        ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                    },
                    shape={
                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                    },
                        ),
                    ),

                    ft.ElevatedButton(
                    on_click = lambda _:Record.from_qr_string(read_qr_code(page), 'returned', 'Stock').record(),
                    content=ft.Text(value="Вернуть Книгу", size=80,color=ft.colors.WHITE),
                    height=680, width=620,
                    style=ft.ButtonStyle(
                    color={
                    ft.MaterialState.HOVERED: ft.colors.WHITE,
                    ft.MaterialState.FOCUSED: ft.colors.BLUE,
                    ft.MaterialState.DEFAULT: ft.colors.BLUE,
                    },
                    bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.with_opacity(0,color_mint2)},
                    padding={ft.MaterialState.HOVERED: 20},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0, "": 1},
                    animation_duration=500,
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(1, color_mint3),
                        ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                    },
                    shape={
                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                    },
                        ),
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            )

    page.update()
    return content