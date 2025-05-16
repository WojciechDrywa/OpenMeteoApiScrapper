import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from storage.db_config import get_db_engine
from logger_config import logger
from weather.validation import WeatherDataValidation

class WeatheDataLoader:
    def __init__(self, location: str):
        self.location = location
        self.engine = get_db_engine()

    def load_from_csv(self, csv_path: str):
        df = pd.read_csv(csv_path)
        df['location'] = self.location
        df = df.rename(columns={"time": "timestamp"})
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    
    def save_to_db(self, df: pd.DataFrame, table_name: str):
        try:
        
            validator = WeatherDataValidation(df)
            validator.validate_not_empty()
            validator.validate_required_columns(['timestamp', 'location'])
            validator.validate_column_types({
                'timestamp': 'datetime64[ns, UTC]',
                'location': 'object'
            })
            
            df.to_sql(
                name=table_name,
                con=self.engine,
                if_exists='append',
                index=False,
                method='multi',
            )
            logger.info(f"DataFrame {len(df)} saved to {table_name} table in the database.")
        except SQLAlchemyError as e:
            logger.error(f"Error saving DataFrame to database: {e}")
            