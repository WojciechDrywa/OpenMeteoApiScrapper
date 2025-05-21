import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from storage.db_config import get_db_engine
from weather_data_loader.logger_config import logger
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
            
from weather.service import WeatherService
from config.locations import LOCATIONS
from config.weather_variables import HOURLY, DAILY
from datetime import date, timedelta
from weather.writer import WeatherWriter
from weather_data_loader.weather_data_loader import WeatheDataLoader

def run_etl_pipline():
    for place_key, location in LOCATIONS.items():
        location = LOCATIONS[place_key]
        lat = location["latitude"]
        lon = location["longitude"]
        start_date = (date.today() - timedelta(days=10)).strftime("%Y-%m-%d")
        end_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

        service = WeatherService()
        writer = WeatherWriter()

        historical_data = service.get_historical_weather(lat, lon, start_date, end_date)
        writer.save_hourly_data_to_csv(historical_data, HOURLY, f"data/hourly/historical/historical_{place_key}_{start_date}_{end_date}_weather.csv")
        writer.save_daily_data_to_csv(historical_data, DAILY, f"data/daily/historical/historical_{place_key}_{start_date}_{end_date}_weather.csv")

        current_weather_data = service.get_weather(lat, lon)
        writer.save_hourly_data_to_csv(current_weather_data, HOURLY, f"data/hourly/current/current_{place_key}_{date.today().isoformat()}_weather.csv")
        writer.save_daily_data_to_csv(current_weather_data, DAILY, f"data/daily/current/current_{place_key}_{date.today().isoformat()}_weather.csv")

        forecast_data = service.get_weather_forecast(lat, lon)
        writer.save_hourly_data_to_csv(forecast_data, HOURLY, f"data/hourly/forecast/forecast_{place_key}_{date.today().isoformat()}_weather.csv")
        writer.save_daily_data_to_csv(forecast_data, DAILY, f"data/daily/forecast/forecast_{place_key}_{date.today().isoformat()}_weather.csv")

        hourly_forecast_file = f"data/hourly/forecast/forecast_{place_key}_{date.today().isoformat()}_weather.csv"
        hourly_current_file = f"data/hourly/current/current_{place_key}_{date.today().isoformat()}_weather.csv"
        hourly_historical_file = f"data/hourly/historical/historical_{place_key}_{start_date}_{end_date}_weather.csv"
        
        daily_forecast_file = f"data/daily/forecast/forecast_{place_key}_{date.today().isoformat()}_weather.csv"
        daily_current_file = f"data/daily/current/current_{place_key}_{date.today().isoformat()}_weather.csv"
        daily_historical_file = f"data/daily/historical/historical_{place_key}_{start_date}_{end_date}_weather.csv"

        loader = WeatheDataLoader(location=LOCATIONS[place_key]["name"])

        for file, table in [
            (hourly_forecast_file, 'hourly_forecast'),
            (hourly_current_file, 'hourly_current'),
            (hourly_historical_file, 'hourly_historical'),
            (daily_forecast_file, 'daily_forecast'),
            (daily_current_file, 'daily_current'),
            (daily_historical_file, 'daily_historical')
        ] :
            df = loader.load_from_csv(file)
            loader.save_to_db(df, table_name=table)
            