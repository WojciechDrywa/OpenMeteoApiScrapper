from storage.db_config import get_db_engine
from sqlalchemy import text

def test_connection():
    engine = get_db_engine()
    try:
        with engine.begin() as connection:
            result = connection.execute(text("SELECT * FROM weather_data.public.hourly_forecast LIMIT 1"))
            assert result.scalar() is not None, "Database connection failed"
    except Exception as e:
        assert False, f"Database connection failed: {e}"
        
if __name__ == "__main__":
    test_connection()
    print("Database connection test passed.")
    