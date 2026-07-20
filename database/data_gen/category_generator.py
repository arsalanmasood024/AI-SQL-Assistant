def generate_categories():
    categories = [
        ("Electronics", "Electronic devices and accessories"),
        ("Furniture", "Home and office furniture"),
        ("Clothing", "Men and women clothing"),
        ("Sports", "Sports equipment"),
        ("Books", "Books and magazines"),
        ("Health", "Healthcare products"),
        ("Beauty", "Beauty and skincare"),
        ("Automotive", "Car accessories"),
        ("Home & Kitchen", "Kitchen essentials"),
        ("Toys", "Kids toys"),
        ("Office Supplies", "Office stationery"),
        ("Pet Supplies", "Pet products"),
        ("Jewelry", "Jewelry and accessories"),
        ("Garden", "Garden tools"),
        ("Music", "Musical instruments"),
        ("Movies", "Movies and entertainment"),
        ("Baby Products", "Baby essentials"),
        ("Footwear", "Shoes and sandals"),
        ("Groceries", "Daily groceries"),
        ("Accessories", "Fashion accessories")
    ]

    return [
        {
            "CategoryName": name,
            "Description": description
        }
        for name, description in categories
    ]


if __name__ == "__main__":
    print(generate_categories())