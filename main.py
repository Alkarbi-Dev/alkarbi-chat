import flet as ft

def main(page: ft.Page):
    page.title = "تطبيق الكربي للمراسلة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 0
    
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", [
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.icons.SECURITY, size=100, color="yellow"),
                            ft.Text("تطبيق الكربي", size=40, weight="bold", color="white"),
                            ft.Text("تواصل آمن . خصوصية تامة", size=16, color="white70"),
                            ft.ElevatedButton(
                                "دخول إلى الكربي",
                                on_click=lambda _: page.go("/chats"),
                                style=ft.ButtonStyle(bgcolor="white", color="#075E54")
                            )
                        ], alignment="center", horizontal_alignment="center"),
                        expand=True,
                        gradient=ft.LinearGradient(["#075E54", "#128C7E"])
                    )
                ], padding=0)
            )
        elif page.route == "/chats":
            page.views.append(
                ft.View("/chats", [
                    ft.AppBar(title=ft.Text("الكربي - المحادثات"), bgcolor="#075E54", color="white"),
                    ft.ListView(expand=True, controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PERSON),
                            title=ft.Text("مجموعة أصدقاء الكربي"),
                            subtitle=ft.Text("مرحباً بكم في التطبيق الرسمي"),
                            on_click=lambda _: print("تم الضغط")
                        )
                    ])
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)

