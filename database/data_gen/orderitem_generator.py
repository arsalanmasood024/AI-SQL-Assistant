from faker import Faker
import random


fake = Faker()


def generate_order_items(
        order_ids,
        product_ids,
        n=500
):

    items=[]


    for i in range(n):

        quantity=random.randint(1,10)

        price=random.uniform(
            10,
            1000
        )


        items.append({

            "OrderID":
                random.choice(order_ids),

            "ProductID":
                random.choice(product_ids),

            "Quantity":
                quantity,

            "UnitPrice":
                round(price,2),

            "Discount":
                round(
                    random.uniform(0,30),
                    2
                )

        })


    return items



if __name__=="__main__":


    orders=list(range(1,201))

    products=list(range(1,101))


    data=generate_order_items(
        orders,
        products,
        5
    )


    for row in data:
        print(row)