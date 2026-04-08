import flet as ft

def main(page: ft.Page):
    page.title = "Проверка возраста"

    def check_age(e):
        age = input_age.value.strip()

        if not age or not age.isdigit():
            result.value = "Введите корректный возраст"
            result.color = ft.Colors.YELLOW

        else:
            age = int(age)
            if age >= 18:
                result.value = "Доступ разрешен"
                result.color = ft.Colors.GREEN
            else:
                result.value = "Доступ запрещен"
                result.color = ft.Colors.RED

        page.update()

    input_age = ft.TextField(
        label="Введите возраст",on_submit=check_age)

    result = ft.Text(value="", size=20)

    btn = ft.ElevatedButton("Проверить", on_click=check_age)

    page.add(input_age, btn, result)

ft.app(target=main)