import pytest
import pandas as pd
from weather.validation import WeatherDataValidation

def test_validate_required_columns_pass():
    df = pd.DataFrame({'a': [1], 'b': [2]})
    validator = WeatherDataValidation(df)
    assert validator.validate_required_columns(['a', 'b']) is True
    
def test_validate_required_columns_fail():
    df = pd.DataFrame({'a': [1]})
    validator = WeatherDataValidation(df)
    with pytest.raises(ValueError):
        validator.validate_required_columns(['a', 'b'])
        
def test_validate_not_empty_pass():
    df = pd.DataFrame({'a': [1]})
    validator = WeatherDataValidation(df)
    assert validator.validate_not_empty() is None
    
def test_validate_not_empty_fail():
    df = pd.DataFrame()
    validator = WeatherDataValidation(df)
    with pytest.raises(ValueError):
        validator.validate_not_empty()
        
def test_validate_column_types_pass():
    df = pd.DataFrame({'temperature': pd.Series([1.0, 2.0], dtype='float64')})
    validator = WeatherDataValidation(df)
    assert validator.validate_column_types({'temperature': 'float64'}) is None
    
def test_validate_column_types_fail():
    df = pd.DataFrame({'temperature': pd.Series(['wrong'], dtype='object')})
    validator = WeatherDataValidation(df)
    with pytest.raises(TypeError):
        validator.validate_column_types({'temperature': 'float'})
