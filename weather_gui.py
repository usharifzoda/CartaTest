import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "002c3ceedee6bd9c6f5abbb7b476b0da"


def get_weather():
    zip_code = zip_entry.get()
    if not zip_code:
        messagebox.showwarning("Input Error", "Please enter a ZIP code")
        return
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={API_KEY}&units=imperial"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", str(e))
        return
    data = r.json()
    if data.get("cod") != 200:
        messagebox.showerror("Error", data.get("message", "Unknown error"))
        return
    city = data.get("name")
    desc = data.get("weather", [{}])[0].get("description", "No description")
    temp = data.get("main", {}).get("temp")
    result_var.set(f"{city}: {desc}, {temp}°F")


root = tk.Tk()
root.title("Weather by ZIP")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

zip_label = tk.Label(frame, text="ZIP Code:")
zip_label.grid(row=0, column=0, sticky="e")

zip_entry = tk.Entry(frame)
zip_entry.grid(row=0, column=1)

get_button = tk.Button(frame, text="Get Weather", command=get_weather)
get_button.grid(row=0, column=2, padx=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, pady=10)
result_label.pack()

root.mainloop()
