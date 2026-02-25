<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Smart Inventory & Sales Management System V2 by Salmane SHAME and Youssra SIFFEDINE</h3>

  <p align="center">
    A complete business management system using OOP, MySQL persistence, Django web interface, and Pandas/NumPy analytics
    <br />
    <a href="https://github.com/salmanesh212/smart_inventoryV2"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/salmanesh212/smart_inventoryV2/issues">Report Bug</a>
    ·
    <a href="https://github.com/salmanesh212/smart_inventoryV2/issues">Request Feature</a>
  </p>
</div>

<div align="center">

![GitHub contributors](https://img.shields.io/github/contributors/salmanesh212/smart_inventoryV2?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/salmanesh212/smart_inventoryV2?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/salmanesh212/smart_inventoryV2?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/salmanesh212/smart_inventoryV2?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/salmanesh212/smart_inventoryV2?style=for-the-badge)

</div>

<details>
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-capabilities">Key Capabilities</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## 🚀 About The Project

This system is designed to manage the full lifecycle of a small company's operations, from inventory tracking and customer management to deep data analysis of sales trends. It utilizes a clean architecture to ensure that the business logic is decoupled from the database and the web interface.

### Key Capabilities:
* **Core Business Logic (OOP):** Implementation of Product, Customer, and Order models with strict validation.
* **Advanced Error Handling:** Use of custom exceptions like `OutOfStockException` and `InvalidEmailException` to maintain system stability.
* **Data Access Layer (DAO):** Abstracted database interactions using the DAO pattern and MySQL transactions.
* **Web Management:** A Django-powered interface for CRUD operations on products, customers, and orders with inventory tracking.
* **Analytics Dashboard:** Real-time business insights including monthly revenue trends, best-selling products, customer frequency analysis, and inventory value calculations.
* **Inventory Management:** Track product stock levels with automatic deduction on order creation and stock validation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 🛠️ Built With

* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
* ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
* ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
* ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
* ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
* ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 📂 Project Structure

The project follows a modular structure:

```bash
smart_inventory/
├── core/                                   # Domain Layer (OOP Logic & Services)
│   ├── models/                             # Product, Customer, Order, OrderItem classes
│   ├── services/                           # Business logic services
│   └── exceptions/                         # Custom exception classes
├── database/                               # Data Layer (MySQL Persistence)
│   ├── dao/                                # Data Access Objects (CRUD logic)
│   ├── schema.sql                          # SQL table definitions
│   └── populate.sql                        # Sample data population script
├── web/                                    # Presentation Layer (Django Web Interface)
│   └── django_project/                     
│       ├── business_app/                   # Main Django app with models, views, templates
│       │   ├── models.py                   # Django ORM models
│       │   ├── views.py                    # CRUD views & analytics dashboard
│       │   ├── templates/                  # HTML templates for all pages
│       │   └── migrations/                 # Database migration history
│       ├── project_business_system/        # Django project settings & configuration
│       └── manage.py                       # Django management script
└── analytics/                              # Analysis Layer (Data Science)
    └── analysis.ipynb                      # Jupyter notebook for Pandas/NumPy analysis
```

**Key Models (Django):**
- `Product`: name, category, price, quantity_in_stock
- `Customer`: name, email (unique)
- `Order`: customer (FK), order_date (auto)
- `OrderItem`: order (FK), product (FK), quantity

## ⚡ Getting Started

Follow these steps to set up the project locally on your machine.

### Prerequisites

Ensure you have Python installed.
*   **Python 3.8+**
    ```bash
    python --version
    ```

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/salmanesh212/smart_inventoryV2.git
    cd smart_inventoryV2
    ```

2.  **Create and activate a Virtual Environment** (Recommended)
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navigate to Django project**
    ```bash
    cd web/django_project
    ```

5.  **Apply Database Migrations**
    ```bash
    python manage.py migrate
    ```
    This creates all necessary tables including:
    - `business_app_product` (products with inventory)
    - `business_app_customer` (registered customers)
    - `business_app_order` (customer orders)
    - `business_app_orderitem` (line items within orders)

6.  **Create a Superuser** (Admin Access - Optional)
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Server**
    ```bash
    python manage.py runserver
    ```
    Server runs on `http://127.0.0.1:8000`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📖 Usage

### Web Application
Once the server is running, navigate to `http://127.0.0.1:8000` in your browser.

**Available Pages:**
* **Home** (`/`): Landing page with navigation
* **Products** (`/products/`): List all products with browse and create options
  - Create Product: Add new products to inventory
  - View Details: Check individual product information
  - Update Product: Modify product name, category, price, or stock
  - Delete Product: Remove products from inventory
* **Customers** (`/register/`): Customer management
  - Register Customer: Add new customers with email validation
  - View Customer: See customer information
* **Orders** (`/orders/` or `/create-order/`): Order management
  - Create Order: Create new orders for customers with product selection and quantity
  - Display Orders: View all orders with their line items and product details
* **Analytics Dashboard** (`/analytics/`): Comprehensive business insights
  - Monthly Revenue Trend Chart
  - Best-Selling Products Analysis
  - Total Inventory Stock Value
  - Average Order Value
  - Customer Order Frequency
  - Key Metrics: Total Products, Customers, and Orders

*   **Admin Panel:** Access `http://127.0.0.1:8000/admin` for raw data management (requires superuser).

### Data Analysis (Jupyter)
To run the analysis notebooks:
1.  Ensure your virtual environment is active.
2.  Navigate to the project root directory.
3.  Start Jupyter Lab/Notebook:
    ```bash
    jupyter notebook
    ```
4.  Open `analytics/analysis.ipynb` to view data visualizations and analysis scripts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🗺️ Roadmap

- [x] Initial Django Project Setup
- [x] Database Models for Inventory Items
- [x] Basic HTML Templates & Views
- [ ] **Phase 2**: Integration of Pandas for Exporting Reports (CSV/Excel)
- [ ] **Phase 3**: Advanced Visualization Charts (Matplotlib/Plotly) inside Django templates
- [ ] **Phase 4**: REST API with Django Rest Framework

See the [open issues](https://github.com/salmanesh212/smart_inventoryV2/issues) for a full list of proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🤝 Contributing

Contributions are vital to the open-source community. If you have a suggestion that would make this better, please fork the repo and create a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---


## 📞 Contact

**Mohamed Salmane SHAME** - [GitHub Profile](https://github.com/salmanesh212)
**Youssra SIFEDDINE** - [GitHub Profile](https://github.com/youssrasifeddine-gif)

Project Link: [https://github.com/salmanesh212/smart_inventoryV2](https://github.com/salmanesh212/smart_inventoryV2)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
