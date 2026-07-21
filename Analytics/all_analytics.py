from .customer import top_customers
from .sale import monthly_sales, daily_sales
from .product import top_products, product_revenue
from .inventory import low_stock, inventory_value
from .employee import  employee_sales
from .category import category_sales
from .supplier import supplier_sales
from .order import order_status
from .kpi import dashboard_kpis


if __name__ == "__main__":

    dashboard_kpis()

    top_customers()

    monthly_sales()

    daily_sales()

    top_products()

    product_revenue()

    category_sales()

    supplier_sales()

    low_stock()

    inventory_value()

    employee_sales()

    order_status()