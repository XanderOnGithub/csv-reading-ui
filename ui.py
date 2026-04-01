import flet as ft

def create_data_table(headers, rows):
    """Takes raw headers and rows and returns a Flet DataTable widget."""
    
    # If the logic layer returned no data, return an error message widget
    # UPDATE: Changed ft.colors to ft.Colors
    if not headers and not rows:
        return ft.Text("Error: Could not find 'data.csv'. Please ensure it is in the same folder.", color=ft.Colors.RED)

    # 1. Create the visual column headers
    table_columns = []
    for header in headers:
        table_columns.append(ft.DataColumn(ft.Text(header, weight=ft.FontWeight.BOLD)))

    # 2. Create the visual data rows
    table_rows = []
    for row in rows:
        cells = []
        for cell_data in row:
            cells.append(ft.DataCell(ft.Text(cell_data)))
        table_rows.append(ft.DataRow(cells=cells))

    return ft.DataTable(
        columns=table_columns,
        rows=table_rows,
        border=ft.border.all(1, ft.Colors.OUTLINE),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, ft.Colors.OUTLINE),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.OUTLINE),
    )