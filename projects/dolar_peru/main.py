from PDolar.load_data.get_data import load_data, last_days_data, load_day_data
import pandas
from datetime import datetime as dt, timedelta

today = dt(2024, 8, 19)
day_n = dt(2024, 8, 16)

range_data = load_data(day_n, today)
a = range_data["bank"].tail()
print(range_data)
