use db-daily-currency-rate;

CREATE TABLE IF NOT EXISTS currency_rates (
    date DATE NOT NULL,
    currency_code VARCHAR(10) NOT NULL,
    rate DECIMAL(15, 6) NOT NULL,
    PRIMARY KEY (date, currency_code)
);