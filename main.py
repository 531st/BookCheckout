import flet as ft
from views.FletRouter import Router

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
        myRouter.body
    )

    page.go('/menu')
   
ft.app(target=main, assets_dir='source')