class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item(self, item_id_suffix):
        self.page.locator(f"#add-to-cart-{item_id_suffix}").click()

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()