from sqlalchemy import text
from storage.db_config import get_db_engine
from weather_data_loader.logger_config import logger

def create_table(filepath = "storage/schema.sql"):
    engine = get_db_engine()
    with engine.connect() as connection:
        with open(filepath, 'r') as file:
            connection.execute(text(file.read()))
            
def save_dataframe_to_db(df, table_name: str):
    engine = get_db_engine()
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    logger.info(f"DataFrame saved to {table_name} table in the database.")
