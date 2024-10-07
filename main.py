import flet as ft
from flet import Page, Text, ListView, ListTile, Image, Container, Column, Row, BorderRadius, colors, alignment, ElevatedButton
import os  # For dynamic port handling in Azure

# Function to display the cart
cart = []

def display_cart():
    return "\n".join([f"{item['name']} - ${item['price']}" for item in cart])

def main(page: Page):
    page.title = "Tasty Bites"
    page.padding = 20
    page.bgcolor = colors.BLUE_GREY_50
    page.theme_mode = ft.ThemeMode.LIGHT

    # Title
    title = Text("Welcome to Tasty Bites!", size=32, weight="bold", color=colors.BLUE_700)

    # Search bar
    search_input = ft.TextField(label="Search Menu", expand=True)
    search_button = ElevatedButton(text="Search", on_click=lambda e: search_food(search_input.value))

    def search_food(query):
        if query:
            food_list.controls.clear()
            filtered_items = [item for item in food_items if query.lower() in item["name"].lower()]
            for item in filtered_items:
                food_card = create_food_card(item)
                food_list.controls.append(food_card)
            page.update()
        else:
            populate_food_list()

    # Menu bars
    menu_bar = ListView(
        controls=[
            ListTile(title=Text("Food"), on_click=lambda e: populate_food_list("food")),
            ListTile(title=Text("Drinks"), on_click=lambda e: populate_food_list("drink")),
            ListTile(title=Text("Smoothies"), on_click=lambda e: populate_food_list("smoothie")),
            ListTile(title=Text("Snacks"), on_click=lambda e: populate_food_list("snack")),
        ]
    )

    # Food list
    food_list = ListView(
        spacing=20,
        padding=20,
        expand=True,
    )

    # Food items with images, descriptions, and prices
    food_items = [
        {
            "name": "Pizza Margherita",
            "description": "Classic Italian pizza with tomatoes, mozzarella, and basil",
            "image": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg",
            "price": 12.99,
            "category": "food"
        },
        {
            "name": "Cheeseburger Deluxe",
            "description": "Juicy beef patty with melted cheese, lettuce, and special sauce",
            "image": "https://cdn.pixabay.com/photo/2022/08/31/10/20/burger-7422970_1280.jpg",
            "price": 10.99,
            "category": "food"
        },
        {
            "name": "Sushi Platter",
            "description": "Assorted fresh sushi rolls with wasabi and pickled ginger",
            "image": "https://cdn.pixabay.com/photo/2017/10/15/11/41/sushi-2853382_1280.jpg",
            "price": 18.99,
            "category": "food"
        },
        {
            "name": "Pasta Carbonara",
            "description": "Creamy pasta with pancetta, eggs, and Parmesan cheese",
            "image": "https://cdn.pixabay.com/photo/2015/04/08/13/13/pasta-712664_1280.jpg",
            "price": 14.99,
            "category": "food"
        },
        {
            "name": "Gelato Trio",
            "description": "Three scoops of artisanal Italian ice cream in various flavors",
            "image": "https://cdn.pixabay.com/photo/2018/08/16/22/59/ice-cream-3611698_1280.jpg",
            "price": 6.99,
            "category": "food"
        },
        {
            "name": "Lemonade",
            "description": "Refreshing cold lemonade with a hint of mint",
            "image": "https://cdn.pixabay.com/photo/2017/03/27/14/56/lemonade-2173498_1280.jpg",
            "price": 3.99,
            "category": "drink"
        },
        {
            "name": "Strawberry Smoothie",
            "description": "Creamy strawberry smoothie made with fresh fruit",
            "image": "https://cdn.pixabay.com/photo/2018/05/31/18/43/smoothie-3444348_1280.jpg",
            "price": 5.99,
            "category": "smoothie"
        },
        {
            "name": "Potato Chips",
            "description": "Crispy seasoned potato chips",
            "image": "https://cdn.pixabay.com/photo/2015/03/16/16/33/chips-675056_1280.jpg",
            "price": 2.99,
            "category": "snack"
        },
    ]

    def create_food_card(item):
        return Container(
            content=Column([
                Image(
                    src=item["image"],
                    width=400,
                    height=200,
                    fit=ft.ImageFit.COVER,
                    border_radius=BorderRadius(10, 10, 0, 0),
                ),
                Container(
                    content=Column([
                        Text(item["name"], size=20, weight="bold"),
                        Text(item["description"], size=16, color=colors.GREY_700),
                        Text(f"${item['price']}", size=16, color=colors.GREEN_700),
                        ElevatedButton(text="Add to Cart", on_click=lambda e: add_to_cart(item)),
                    ]),
                    padding=10,
                ),
            ]),
            bgcolor=colors.WHITE,
            border_radius=10,
            ink=True,
        )

    def add_to_cart(item):
        cart.append(item)
        page.update()

    def populate_food_list(category=None):
        food_list.controls.clear()
        for item in food_items:
            if category is None or item["category"] == category:
                food_card = create_food_card(item)
                food_list.controls.append(food_card)
        page.update()

    # Add elements to the page
    page.add(
        Column([
            title,
            Row([search_input, search_button]),
            menu_bar,
            Container(
                content=food_list,
                expand=True,
            ),
            Text("Cart:", size=20, weight="bold"),
            Text(display_cart(), size=14, color=colors.GREY_700),
        ])
    )

    # Populate the initial list
    populate_food_list()

# This part is crucial for Replit and Azure deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Dynamically fetch the port from environment
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port)
    
