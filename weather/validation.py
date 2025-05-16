import logging

logger = logging.getLogger(__name__)

class WeatherDataValidation:
    
    def __init__(self, data):
        self.data = data

    def validate_required_columns(self, required):
        missing_columns = [col for col in required if col not in self.data.columns]
        if missing_columns:
            logger.error(f"Missing required columns: {', '.join(missing_columns)}")
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
        logger.info("All required columns are present.")
        return True
    
    def validate_not_empty(self):
        if self.data.empty:
            logger.error("DataFrame is empty.")
            raise ValueError("DataFrame is empty.")
        logger.info("DataFrame is not empty.")
    
    def validate_column_types(self, expected_types: dict):
        for col, dtype in expected_types.items():
            if col in self.data.columns and self.data[col].dtype.name != dtype:
                logger.error(f"Column {col} has incorrect type. Expected {dtype}, got {self.data[col].dtype}.")
                raise TypeError(f"Column {col} has incorrect type. Expected {dtype}, got {self.data[col].dtype}.")
        logger.info("All columns have the expected types.")
