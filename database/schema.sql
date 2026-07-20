CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Phone NVARCHAR(20),
    City NVARCHAR(50),
    Country NVARCHAR(50),
    RegistrationDate DATE NOT NULL DEFAULT GETDATE()
);

CREATE TABLE Categories (
    CategoryID INT IDENTITY(1,1) PRIMARY KEY,
    CategoryName NVARCHAR(100) NOT NULL UNIQUE,
    Description NVARCHAR(255)
);

CREATE TABLE Suppliers (
    SupplierID INT IDENTITY(1,1) PRIMARY KEY,
    SupplierName NVARCHAR(100) NOT NULL,
    ContactPerson NVARCHAR(100),
    Email NVARCHAR(100),
    Phone NVARCHAR(20),
    City NVARCHAR(50),
    Country NVARCHAR(50)
);

CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(150) NOT NULL,

    CategoryID INT NOT NULL,
    SupplierID INT NOT NULL,

    UnitPrice DECIMAL(10,2) NOT NULL,
    UnitCost DECIMAL(10,2) NOT NULL,

    StockQuantity INT NOT NULL DEFAULT 0,

    CreatedDate DATE DEFAULT GETDATE(),

    CONSTRAINT FK_Product_Category
        FOREIGN KEY(CategoryID)
        REFERENCES Categories(CategoryID),

    CONSTRAINT FK_Product_Supplier
        FOREIGN KEY(SupplierID)
        REFERENCES Suppliers(SupplierID)
);

CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE,
    Department NVARCHAR(50),
    JobTitle NVARCHAR(100),
    HireDate DATE,
    Salary DECIMAL(10,2)
);
CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,

    CustomerID INT NOT NULL,
    EmployeeID INT NOT NULL,

    OrderDate DATETIME DEFAULT GETDATE(),

    Status NVARCHAR(30),

    TotalAmount DECIMAL(12,2),

    CONSTRAINT FK_Order_Customer
        FOREIGN KEY(CustomerID)
        REFERENCES Customers(CustomerID),

    CONSTRAINT FK_Order_Employee
        FOREIGN KEY(EmployeeID)
        REFERENCES Employees(EmployeeID)
);

CREATE TABLE OrderItems (
    OrderItemID INT IDENTITY(1,1) PRIMARY KEY,

    OrderID INT NOT NULL,
    ProductID INT NOT NULL,

    Quantity INT NOT NULL,

    UnitPrice DECIMAL(10,2),

    Discount DECIMAL(5,2) DEFAULT 0,

    CONSTRAINT FK_OrderItems_Order
        FOREIGN KEY(OrderID)
        REFERENCES Orders(OrderID),

    CONSTRAINT FK_OrderItems_Product
        FOREIGN KEY(ProductID)
        REFERENCES Products(ProductID)
);

CREATE TABLE Inventory (
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,

    ProductID INT NOT NULL,

    Warehouse NVARCHAR(100),

    StockQuantity INT,

    ReorderLevel INT,

    LastUpdated DATETIME DEFAULT GETDATE(),

    CONSTRAINT FK_Inventory_Product
        FOREIGN KEY(ProductID)
        REFERENCES Products(ProductID)
);