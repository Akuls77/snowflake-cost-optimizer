import snowflake.connector
import os

def get_snowflake_connection():
    """
    Create and return a Snowflake connection.
    Credentials are read from environment variables.
    """
    
    return snowflake.connector.connect(
        user = os.getenv("SNOWFLAKE_USER"),
        password = os.getenv("SNOWFLAKE_PASSWORD"),
        account = os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
        database = "COST_OPTIMIZATION_DB",
        schema = "METRICS"
    )

def get_latest_cost_summary():
    """
    Fetch latest daily cost mertrics for all warehouses.
    """

    conn = get_snowflake_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            warehouse_name,
            usage_date,
            total_credits_used
        FROM cost_metrics_daily
        ORDER BY usage_date desc
        LIMIT 10;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def get_top_warehouses(limit=5):
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    query = f"""
        SELECT
            warehouse_name,
            SUM(total_credits_used) AS total_credits
        FROM COST_METRICS_DAILY
        GROUP BY warehouse_name
        ORDER BY total_credits DESC
        LIMIT {limit};
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
