'''
Create a shopping cart application based on various GUI controls.
'''

import tkinter as tk
from tkinter import messagebox

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart App")

        # Initialize variables
        self.items = {
            'Item 1': 10.0,
            'Item 2': 20.0,
            'Item 3': 15.0
        }
        self.cart = {}

        # Create GUI components
        self.item_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.populate_item_listbox()

        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.cart_label = tk.Label(root, text="Shopping Cart")
        self.cart_listbox = tk.Listbox(root)

        self.remove_button = tk.Button(root, text="Remove from Cart", command=self.remove_from_cart)
        self.checkout_button = tk.Button(root, text="Checkout", command=self.checkout)

        # Place GUI components on the grid
        self.item_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        self.cart_label.grid(row=0, column=2, padx=10, pady=10)
        self.cart_listbox.grid(row=0, column=3, padx=10, pady=10)
        self.remove_button.grid(row=1, column=2, padx=10, pady=10)
        self.checkout_button.grid(row=1, column=3, padx=10, pady=10)

    def populate_item_listbox(self):
        for item in self.items:
            self.item_listbox.insert(tk.END, item)

    def add_to_cart(self):
        selected_items = self.item_listbox.curselection()
        for index in selected_items:
            item = self.item_listbox.get(index)
            if item not in self.cart:
                self.cart[item] = self.items[item]
                self.cart_listbox.insert(tk.END, f"{item} - ${self.items[item]:.2f}")

    def remove_from_cart(self):
        selected_items = self.cart_listbox.curselection()
        for index in selected_items:
            item = self.cart_listbox.get(index).split(' - ')[0]
            del self.cart[item]
            self.cart_listbox.delete(index)

    def checkout(self):
        total_cost = sum(self.cart.values())
        messagebox.showinfo("Checkout", f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
