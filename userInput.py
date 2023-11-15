import requests
import re
from datetime import datetime
import unittest
from unittest.mock import patch


def get_stock_symbol():
    while True:
        try:
            stock_symbol = input("\nEnter the symbol for the company: ")
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&&apikey=V33ZAOO7VB64CV9C'
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                if "Meta Data" in data:
                    print("Symbol found: ", stock_symbol)
                    return stock_symbol
                else:
                    print("The Stock symbol you inputted does not exist.")
            else:
                print(f"Error: Request failed with status code {r.status_code}")
        except Exception as e:
            print("An error occurred:", e)

def get_chart_type():
  print("\n\nCHART TYPES:\n---------------------------\n1. Bar\n2. Line\n\n")
  while(True):
    chart_type = input("Enter the chart type you want (1 or 2): ")
    if(chart_type == '1' or chart_type == '2'):
      return chart_type
    else:
      print("\nInvalid entry. Please enter either 1 or 2.\n\n")

def get_time_series():
  print("\n\nSelect the time series of the chart you want to generate:\n-----------------------------------------------------\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n\n")
  while(True):
    time_series = input("Enter time series option (1, 2, 3, 4): ")
    if time_series == '1' or time_series == '2' or time_series == '3' or time_series == '4':
      return time_series
    else:
      print("\nInvalid entry. Please enter either 1, 2, 3, or 4.\n\n")


def get_start_date():
    while True:
        user_input = input("\n\nEnter the start date (YYYY-MM-DD): ")
        # Use regular expression to validate the input format
        if re.match(r'^\d{4}-\d{2}-\d{2}$', user_input):
            try:
                # Try to parse the input as a date
                date_obj = datetime.strptime(user_input, '%Y-%m-%d')
                if date_obj > datetime.strptime("2000-01-01", "%Y-%m-%d"):
                    return date_obj
                else:
                    print("Please use a date after the year 1999")
                    
            except ValueError:
                print("Invalid input. Please enter a date in YYYY-MM-DD format.")
        else:
            print("Invalid input. Please enter a date in YYYY-MM-DD format.")
            return None  # Return None for invalid inputs


def get_end_date(start_date):
    while True:
        user_input = input("\n\nEnter the end date (YYYY-MM-DD): ")
        # Use regular expression to validate the input format
        if re.match(r'^\d{4}-\d{2}-\d{2}$', user_input):
            try:
                # Try to parse the input as a date
                date_obj = datetime.strptime(user_input, '%Y-%m-%d')
                # Check if the end date is after the start date
                if date_obj > start_date:
                    if(date_obj > (datetime.now())):
                      return date_obj
                    else:
                       print("End date should be before the current date")
                else:
                    print("End date should be after the start date.")
                if date_obj > start_date:
                    return date_obj
                else:
                      print("End date should be after the start date.")
            except ValueError:
                print("Invalid input. Please enter a date in YYYY-MM-DD format.")
                pass  # Invalid date

#Unit Testing
class TestUserInputFunctions(unittest.TestCase):
    @patch('builtins.input', return_value='AAPL')
    def test_get_stock_symbol(self, mock_input):
        symbol = get_stock_symbol()
        self.assertEqual(symbol, 'AAPL')

    @patch('builtins.input', return_value='1')
    def test_get_chart_type_1(self, mock_input):
        chart_type = get_chart_type()
        self.assertEqual(chart_type, '1')

    @patch('builtins.input', return_value='2')
    def test_get_chart_type_2(self, mock_input):
        chart_type = get_chart_type()
        self.assertEqual(chart_type, '2')

    @patch('builtins.input', return_value='1')
    def test_get_time_series_1(self, mock_input):
        time_series = get_time_series()
        self.assertEqual(time_series, '1')

    @patch('builtins.input', return_value='2')
    def test_get_time_series_2(self, mock_input):
        time_series = get_time_series()
        self.assertEqual(time_series, '2')
    
    @patch('builtins.input', return_value='3')
    def test_get_time_series_3(self, mock_input):
        time_series = get_time_series()
        self.assertEqual(time_series, '3')

    @patch('builtins.input', return_value='4')
    def test_get_time_series_4(self, mock_input):
        time_series = get_time_series()
        self.assertEqual(time_series, '4')

    def test_get_start_date_invalid(self):
        with patch('builtins.input', side_effect=['invalid_date', '1800-01-01']):
            start_date = get_start_date()
            self.assertIsNone(start_date)

    def test_get_end_date_valid(self):
        start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
        with patch('builtins.input', return_value='2023-02-01'):
            end_date = get_end_date(start_date)
            self.assertEqual(end_date, datetime(2023, 2, 1))

if __name__ == '__main__':
    unittest.main()

def main():
  print("\n\nStock Data Visualizer\n---------------------------")
  stock_symbol = get_stock_symbol()
  chart_type = get_chart_type()
  time_series = get_time_series()
  start_date = get_start_date()
  end_date = get_end_date(start_date)


