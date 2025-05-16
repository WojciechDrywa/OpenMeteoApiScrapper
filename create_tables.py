from sqlalchemy import text
from storage.db_config import get_db_engine

def create_tables_from_sql_file(filepath: str = "storage/schema.sql"):
    """
    Create tables in the database using the SQL schema file.
    
    Args:
        filepath (str): Path to the SQL schema file.
    """
    engine = get_db_engine()
    try:
        with engine.begin() as connection:
            with open(filepath, 'r') as file:
                sql_script = file.read()
            connection.execute(text(sql_script))
            print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
    create_tables_from_sql_file()
    