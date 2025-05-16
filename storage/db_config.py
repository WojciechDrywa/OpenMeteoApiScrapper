from sqlalchemy import create_engine

def get_db_engine():
    return create_engine(
        "postgresql+psycopg2://postgres:Serv5541%@localhost:5432/weather_data",
        echo=True
    )
    