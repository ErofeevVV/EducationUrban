import tkinter as tk
from tkinter import ttk
from exchange_rate.parser_exchange_rate import exchange_rate
from watch import get_current_time


def update_time():
    current_time = get_current_time()
    root.title(f'Курсы валют | Текущее время: {current_time}')
    root.after(1000, update_time)


def on_select(event):
    selected_currency = currency_var.get()
    currency_info = currency_data[selected_currency]
    rate_label.config(text=f'Курс: {currency_info['price']:.4f} р. за {currency_info['units']}')


def update_rates():
    global currency_data
    try:
        currency_data = exchange_rate()
        currencies = list(currency_data.keys())
        currency_dropdown['values'] = currencies
        currency_var.set(currencies[0])
        on_select(None)
    except Exception as e:
        rate_label.config(text=str(e))


root = tk.Tk()
root.title('Курсы валют')

top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, padx=10, pady=10)

currency_data = exchange_rate()
currencies = list(currency_data.keys())

currency_var = tk.StringVar(value=currencies[0])

currency_dropdown = ttk.Combobox(top_frame, textvariable=currency_var, values=currencies)
currency_dropdown.bind('<<ComboboxSelected>>', on_select)
currency_dropdown.pack(side=tk.LEFT)

update_button = ttk.Button(top_frame, text='Обновить', command=update_rates)
update_button.pack(side=tk.RIGHT, padx=(20, 0))

bottom_frame = tk.Frame(root)
bottom_frame.pack(padx=20, pady=20)

rate_label = tk.Label(bottom_frame, font=('Arial', 14), width=60, anchor=tk.W)
rate_label.pack()

update_time()

update_rates()
root.mainloop()
