CATEGORIES = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Sports",
    "Books",
    "Health",
    "Beauty",
    "Automotive",
    "Home & Kitchen",
    "Toys",
    "Office Supplies",
    "Pet Supplies",
    "Jewelry",
    "Garden",
    "Music",
    "Movies",
    "Baby Products",
    "Footwear",
    "Groceries",
    "Accessories"
]

def generate_categories():
    return [{"CategoryName": name, "Description": f"{name} products"} for name in CATEGORIES]


if __name__ == "__main__":
    for category in generate_categories():
        print(category)