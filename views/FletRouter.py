import flet as ft

# imported views

from views.menu_view import MenuView
from views.register_view import RegisterView
from views.loading_view import LoadingView
from views.finish_view import FinishView

# Router

class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            '/menu': MenuView(page),
            '/reg': RegisterView(page),
            '/loading': LoadingView(page),
            '/finish': FinishView(page),
            
        }
        self.body = ft.Container(content=self.routes['/menu'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()