# Medallion Architecture Project (CRM & ERP Data)

## 📌 Project Overview

This project demonstrates the implementation of the **Medallion Architecture (Bronze, Silver, Gold)** using data sourced from **CRM** and **ERP** systems. The goal is to ingest raw CSV files, clean and transform the data, and finally build an analytics-ready **Star Schema** for CRM reporting.

The project is implemented on **Databricks**, leveraging **Databricks Volumes** for data storage and structured layers for scalable data processing.

---

## 📂 Data Sources

The project uses **6 CSV files** divided as follows:

### CRM Data (3 Files)

* `crm_customer_info.csv`
* `crm_product_info.csv`
* `crm_sales_details.csv`

### ERP Data (3 Files)

* `erp_customers.csv`
* `erp_locations.csv`
* `erp_pricing_category.csv`

---

## 🏗 Architecture Overview

The project follows the **Medallion Architecture** pattern:

```
CSV Files → Bronze Layer → Silver Layer → Gold Layer
```

### 🔹 Bronze Layer (Raw Data)

* Raw CSV files are uploaded to **Databricks Volumes**.
* **PySpark** is used to ingest data from the volume into the Bronze layer.
* Data is stored as-is with no business transformations.
* Purpose:

  * Preserve original data
  * Enable reprocessing if needed

---

### 🔸 Silver Layer (Cleaned & Transformed Data)

* **PySpark** is used to move data from the Bronze layer to the Silver layer.
* Data cleansing and transformations are applied based on **each table’s business requirements**.
* Typical transformations include:

  * Data type casting
  * Removing duplicates
  * Handling null or invalid values
  * Standardizing column names
  * Applying basic business logic

Each CRM and ERP table is processed independently according to its structure and use case.

---

### ⭐ Gold Layer (Business Model)

* **PySpark** is used to move and model data from the Silver layer to the Gold layer.
* A **Star Schema** is created specifically for **CRM analytics**.
* The Gold layer is optimized for reporting and BI tools.

#### CRM Star Schema Design

* **Fact Table**:

  * Sales-related measures derived from `crm_sales_details`

* **Dimension Tables**:

  * Customer Dimension (from `crm_customer_info`)
  * Product Dimension (from `crm_product_info`)
  * Supporting attributes enriched where applicable

This structure enables efficient querying, aggregation, and analytics.

---

## 🛠 Technologies Used

* **Databricks**
* **Apache Spark (PySpark)**
* **Databricks Volumes**
* **CSV File Format**
* **Medallion Architecture**
* **Databricks**
* **Apache Spark / PySpark**
* **Databricks Volumes**
* **CSV File Format**
* **Medallion Architecture**

---

## 🎯 Key Outcomes

* Clear separation of raw, cleaned, and business-ready data
* Scalable and maintainable data pipeline
* Analytics-ready CRM star schema
* Improved data quality and consistency

---

## 🚀 Future Enhancements

* Add ERP-based star schema models
* Implement data quality checks
* Automate pipeline using Databricks Jobs
* Integrate BI tools (e.g., Power BI, Tableau)

---

## 📎 Notes

* This project focuses primarily on **CRM analytics** at the Gold layer.
* ERP data is prepared and available at the Silver layer for future modeling.

---

✅ This project serves as a practical example of implementing Medallion Architecture in a real-world CRM & ERP data scenario.
