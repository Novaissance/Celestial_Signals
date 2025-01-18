import requests
import pandas as pd
from typing import Dict, Any
from datetime import datetime, timedelta

class MarketData:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.base_url = "https://api.coingecko.com/api/v3"
    
    def get_current_data(self, symbol: str) -> Dict[str, Any]:
        """Get current market data for symbol."""
        endpoint = f"/simple/price"
        params = {
            'ids': symbol,
            'vs_currencies': 'usd',
            'include_24hr_vol': True,
            'include_24hr_change': True
        }
        
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()
    
    def get_historical_data(self, symbol: str, days: int = 30) -> pd.DataFrame:
        """Get historical market data."""
        endpoint = f"/coins/{symbol}/market_chart"
        params = {
            'vs_currency': 'usd',
            'days': days,
            'interval': 'daily'
        }
        
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        data = response.json()
        
        df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df.set_index('date')