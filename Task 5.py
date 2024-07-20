import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch exchange rates
def fetch_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']

# Function to convert USD to selected currency
def convert_currency():
    usd_amount = float(entry_usd.get())
    target_currency = combo_currency.get()
    conversion_rate = exchange_rates.get(target_currency, 1)
    converted_amount = usd_amount * conversion_rate
    label_result.config(text=f'{usd_amount} USD = {converted_amount:.2f} {target_currency}')

# Fetch exchange rates
exchange_rates = fetch_exchange_rates()

# Initialize GUI
root = tk.Tk()
root.title("Currency Converter")

# USD amount entry
label_usd = tk.Label(root, text="Amount in USD:")
label_usd.pack(pady=5)

entry_usd = tk.Entry(root)
entry_usd.pack(pady=5)

# Currency selection dropdown
label_currency = tk.Label(root, text="Select currency:")
label_currency.pack(pady=5)

combo_currency = ttk.Combobox(root, values=list(exchange_rates.keys()))
combo_currency.pack(pady=5)
combo_currency.set('EUR')  # Set default currency to EUR

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack(pady=5)

# Result label
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# Start the GUI event loop
root.mainloop()
