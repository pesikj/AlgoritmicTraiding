import requests
import pandas as pd
import os
from ta import trend

DATA_FOLDER = "data"


class DataReader:
    api_key: str

    def __init__(self):
        self.api_key = os.getenv("API_KEY")

    def _send_data_request(self, symbol):
        # api_key = os.getenv("API_KEY")
        api_url = f"https://api.twelvedata.com/time_series" \
                  f"?symbol={symbol}&interval=1day&outputsize=5000&apikey={self.api_key}"
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['values']).iloc[::-1].set_index('datetime').astype(float)
        df.index = pd.to_datetime(df.index)
        df.to_csv(f"data/{symbol}.csv")

    def get_dataframe(self, symbol):
        path = os.path.join(DATA_FOLDER, f"{symbol}.csv")
        if not os.path.isfile(path):
            self._send_data_request(symbol)
        df = pd.read_csv(path)
        return df
