import pandas as pd
import numpy as np
import os
from typing import Any, List
from weather_data_loader.logger_config import logger

class WeatherWriter:
    def save_hourly_data_to_csv(self, response: Any, variable_names: List[str], filename: str):
        folder = os.path.dirname(filename)
        if folder:
            os.makedirs(folder, exist_ok=True)

        hourly = response.Hourly()
        data = {}

        try:
            start = pd.to_datetime(hourly.Time(), unit='s', utc=True)
            end = pd.to_datetime(hourly.TimeEnd(), unit='s', utc=True)
            freq = pd.Timedelta(seconds=hourly.Interval())
            timestamps = pd.date_range(start=start, end=end, freq=freq, inclusive='left')
        except Exception as e:
            logger.error(f"Błąd przy przetwarzaniu czasu: {e}")
            return

        if not hasattr(timestamps, '__len__') or len(timestamps) == 0:
            logger.warning("Brak danych do zapisania.")
            return

        data["time"] = timestamps

        available_variables = {}

        for i, name in enumerate(variable_names):
            try:
                if i + 1 >= hourly.VariablesLength():
                    logger.warning(f"Zmienna {name} nie została zwrócona przez API. Pominięto.")
                    continue

                variable = hourly.Variables(i)
                values = variable.ValuesAsNumpy()

                if not isinstance(values, np.ndarray) or values.ndim != 1:
                    logger.warning(f"Pominięto zmienną {name} – nieprawidłowy typ lub wymiar.")
                    continue

                if len(values) != len(timestamps):
                    logger.warning(f"Pominięto zmienną {name} – nieprawidłowy rozmiar ({len(values)}).")
                    continue

                available_variables[name] = values
            except Exception as e:
                logger.error(f"Cannot reach variable {name}: {e}")

        data.update(available_variables)

        df = pd.DataFrame(data)

        try:
            df.to_csv(filename, index=False)
            logger.info(f"Dane pogodowe zapisane do pliku: {filename}")
        except Exception as e:
            logger.error(f"Błąd przy zapisie CSV: {e}")
            
    def save_daily_data_to_csv(self, response: Any, variable_names: List[str], filename: str):
        folder = os.path.dirname(filename)
        if folder:
            os.makedirs(folder, exist_ok=True)

        daily = response.Daily()
        data = {}

        try:
            start = pd.to_datetime(daily.Time(), unit='s', utc=True)
            end = pd.to_datetime(daily.TimeEnd(), unit='s', utc=True)
            freq = pd.Timedelta(seconds=daily.Interval())
            timestamps = pd.date_range(start=start, end=end, freq=freq, inclusive='left')
        except Exception as e:
            logger.error(f"Błąd przy przetwarzaniu czasu: {e}")
            return

        if not hasattr(timestamps, '__len__') or len(timestamps) == 0:
            logger.warning("Brak danych do zapisania.")
            return

        data["time"] = timestamps

        available_variables = {}

        for i, name in enumerate(variable_names):
            try:
                if i + 1 >= daily.VariablesLength():
                    logger.warning(f"Zmienna {name} nie została zwrócona przez API. Pominięto.")
                    continue

                variable = daily.Variables(i)
                values = variable.ValuesAsNumpy()

                if not isinstance(values, np.ndarray) or values.ndim != 1:
                    logger.warning(f"Pominięto zmienną {name} – nieprawidłowy typ lub wymiar.")
                    continue

                if len(values) != len(timestamps):
                    logger.warning(f"Pominięto zmienną {name} – nieprawidłowy rozmiar ({len(values)}).")
                    continue

                available_variables[name] = values
            except Exception as e:
                logger.error(f"Cannot reach variable {name}: {e}")

        data.update(available_variables)

        df = pd.DataFrame(data)

        try:
            df.to_csv(filename, index=False)
            logger.info(f"Dane pogodowe zapisane do pliku: {filename}")
        except Exception as e:
            logger.error(f"Błąd przy zapisie CSV: {e}")
            