import requests
import mysql.connector
from datetime import date

url = "https://currencyapi.net/api/v1/rates?key=xaNgdQOpzHNaiHedgc74TJX5xjJEOTH72X1O&output=JSON"


def retrieve_currency_rates():
    try:
        response = requests.request("GET", url)
        response.raise_for_status()
        return response.json()["rates"]
    except requests.exceptions.RequestException as e:
        print("Error fetching currency rates: {}".format(e))
        return None


def store_rates(rates):
    try:
        db_connection = mysql.connector.connect(host='db', user='user', passwd='password',
                                                database='db-daily-currency-rate')

        # creating database_cursor to perform SQL operation to run queries
        db_cursor = db_connection.cursor()
        today = date.today().isoformat()

        for code, rate in rates.items():
            db_cursor.execute("""
            INSERT INTO currency_rates (date, currency_code, rate)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE rate = %s;
            """, (today, code, rate, rate))

        # Commit the changes to the database
        db_connection.commit()

        # Close the cursor and the database connection
        db_cursor.close()
        db_connection.close()

    except mysql.connector.Error as e:
        print("Error storing rates in the database: {}".format(e))


def main():
    rates = retrieve_currency_rates()
    if rates:
        store_rates(rates)
    else:
        print("No rates to store.")


if __name__ == "__main__":
    main()
