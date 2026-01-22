# bronze_sources.py
# Central registry for bronze raw source files

BRONZE_RAW_SOURCES = {
    "customers_az12": {
        "path": "/Volumes/bike-data-lakehouse-workspace/bronze/raw_source/CUST_AZ12.csv",
        "table": "erp_customers_az12"
    },
    "locations_a101": {
        "path": "/Volumes/bike-data-lakehouse-workspace/bronze/raw_source/LOC_A101.csv",
        "table": "erp_locations_a101"
    },
    "product_category_g1v2": {
        "path": "/Volumes/bike-data-lakehouse-workspace/bronze/raw_source/PX_CAT_G1V2.csv",
        "table": "erp_erp_px_cat_g1v2"
    },
    "customer_info": {
        "path": "/Volumes/bike-data-lakehouse-workspace/bronze/raw_source/cust_info.csv",
        "table": "crm_cust_info"
    },
    "product_info": {
        "path": "/Volumes/bike-data-lakehouse-workspace/bronze/raw_source/prd_info.csv",
        "table": "crm_prd_info"
    },
    "sales_details": {
        "path": "/Volumes/bike-data-lakehouse-workspace/bronze/raw_source/sales_details.csv",
        "table": "crm_sales_details"
    }
}
