from faker import Faker
import random


fake=Faker()



def generate_inventory(product_ids):

    inventory=[]


    locations=[
        "Karachi Warehouse",
        "Islamabad Warehouse",
        "Lahore Warehouse"
    ]


    for product in product_ids:


        inventory.append({

            "ProductID":
                product,


            "StockQuantity":
                random.randint(
                    0,
                    500
                ),


            "ReorderLevel":
                random.randint(
                    10,
                    50
                ),


            "Warehouse":
                random.choice(
                    locations
                ),


            "LastUpdated":
                fake.date_between(
                    start_date="-1y",
                    end_date="today"
                )

        })


    return inventory

