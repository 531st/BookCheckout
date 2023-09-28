import flet as ft
from views.FletRouter import Router
from modules.colors import gradient_mint1

# Main

def main(page: ft.Page):
    page.theme_mode = 'dark'
    #page.window_title_bar_hidden = True
    #page.window_title_bar_buttons_hidden = True
    page.window_frameless = True
    #page.window_height = 500
    #page.window_width = 900
    page.window_full_screen = True
    page.bgcolor = '#090C11'
    
    # Router
    myRouter = Router(page)
    page.on_route_change = myRouter.route_change

    page.add(
        ft.Container(
            content=myRouter.body,
            expand=True,
            padding=ft.padding.all(0),
            gradient=ft.LinearGradient(
                colors=gradient_mint1,
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                tile_mode=ft.GradientTileMode.MIRROR
            )
        )
    )

    page.go('/menu')
   
ft.app(target=main, assets_dir='source')