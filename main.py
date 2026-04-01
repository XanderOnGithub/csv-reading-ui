import flet as ft
from logic import get_employee_data
from ui import create_data_table

def main(page: ft.Page):
    page.title = "Database GUI Base"
    page.scroll = ft.ScrollMode.ALWAYS 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40 

    headers, rows = get_employee_data("data.csv")
    data_table_widget = create_data_table(headers, rows)

    page.add(
        ft.Text("Employee Database Record", size=28, weight=ft.FontWeight.BOLD),
        ft.Container(
            content=data_table_widget,
            margin=ft.margin.only(top=20),
            alignment=ft.alignment.Alignment(0, 0),
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)