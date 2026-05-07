from flet import *
from src.main.constructors.produtoConstructor import produtoConstructor

def app(page:Page):
    page.title="Controle de Estoque"

    def changeRoutes():
        page.views.clear()
        page.views.append(
            produtoConstructor(page)
        )

        page.update()

    page.on_route_change=changeRoutes
    changeRoutes()
