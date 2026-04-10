import flet as ft

def main(page: ft.Page):
    page.title = "История имен"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_history = []
    
    result_text = ft.Text("")
    history_column = ft.Column()

    def update_history():
        history_column.controls.clear()
        for name in greeting_history:
            history_column.controls.append(ft.Text(name))
        page.update()

    def add_name(e):
        name = name_input.value.strip()

        if len(name) < 2:
            result_text.value = "Имя слишком короткое"
            result_text.color = "red"
        
        elif name.isdigit():
            result_text.value = "Имя не может состоять из цифр"
            result_text.color = "red"

        elif name in greeting_history:
            result_text.value = "Это имя уже в истории"
            result_text.color = "red"

        else:
            result_text.value = f"Привет, {name}"
            result_text.color = "green"
            greeting_history.insert(0, name)

            if len(greeting_history) > 5:
                greeting_history.pop()

        name_input.value = ""
        update_history()
        page.update()

    def clear_history(e):
        greeting_history.clear()
        update_history()

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    top_row = ft.Row([
        ft.ElevatedButton("Сменить тему", on_click=change_theme),
        ft.ElevatedButton("Очистить", on_click=clear_history)
    ])
    
    name_input = ft.TextField(label="Введите имя",on_submit = add_name)
    page.add(
        ft.Column([
            top_row,
            name_input,
            ft.ElevatedButton("Добавить", on_click=add_name),
            result_text,
            ft.Text("История:"),
            history_column])
    )

ft.app(target=main)