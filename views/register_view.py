import flet as ft
from modules.record_model import Record
from modules.qr_scanner import read_qr_code

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
                ft.Text('Введите свой логин:', expand=True, size=100, text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ), 
        ft.Row(
            [
                ft.TextField(label='Например: ivanov.a.3 / alekseeva.rv', border_color='#DFE1E5', expand=True, text_size=80,
                on_change=login_changed)
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            ),
        ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Text('Далее', size=80, color='#DFE1E5'),
                    #expand=True,
                    width=600,
                    on_click=lambda _: Record.from_qr_string(read_qr_code(page), 'taken', actor_login).record() #upd_book_taken(actor_login, page)
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ],
        spacing=85
       ),
    )
    page.update()
    return content