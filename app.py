import flet as ft
from view import View
from controller import Controller


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c)
    v.loadInterface()

ft.app(target = main)
