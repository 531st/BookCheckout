import flet as ft
from modules.record_model import Record
from modules.qr_scanner import read_qr_code
from modules.colors import color_mint1, color_mint2, color_mint3

def RegisterView(page):
    
    def login_changed(e):
        global actor_login 
        actor_login = e.control.value
        page.update()

    content = ft.Container(
       ft.Column(
        [
             ft.Row(
            [
                ft.Text('Введите свой логин:', expand=True, size=100, text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ), 
        ft.Row(
            [
                ft.TextField(
                    label='Например: ivanov.a.3 / alekseeva.rv', 
                    border_color=color_mint3, 
                    expand=True, 
                    text_size=80,
                    on_change=login_changed, 
                    label_style=ft.TextStyle(color=ft.colors.WHITE, size=40), 
                    bgcolor=ft.colors.with_opacity(0.1,color_mint2)
                    )
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            ),
        ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text('Далее', size=80, color='#DFE1E5'),
                    #expand=True,
                    width=600,
                    on_click=lambda _: Record.from_qr_string(read_qr_code(page), 'taken', actor_login).record(), #upd_book_taken(actor_login, page)
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
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text('Назад', size=80, color='#DFE1E5'),
                    #expand=True,
                    width=600,
                    on_click=lambda _: page.go('/menu'),
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
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        ),
        padding=ft.padding.symmetric(horizontal=10),
    )
    page.update()
    return content