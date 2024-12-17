import tkinter as tk
from backend import download_data

# Ana pencereyi oluşturma
root = tk.Tk()

# Pencere başlığı
root.title("İlk Tkinter Uygulamam")
root.geometry("400x400")


first_country_label = tk.Label(root, text="First Country Code:")
first_country_label.place(x=10, y=20)

first_country_entry = tk.Entry(root)
first_country_entry.place(x=150, y=20)


second_country_label = tk.Label(root, text="Second Country Code:")
second_country_label.place(x=10, y=50)

second_country_entry = tk.Entry(root)
second_country_entry.place(x=150, y=50)

start_date_label = tk.Label(root, text="Start Date:")
start_date_label.place(x=10, y=80)

start_date_entry = tk.Entry(root)
start_date_entry.place(x=150, y=80)

end_date_label = tk.Label(root, text="End Date:")
end_date_label.place(x=10, y=110)

end_date_entry = tk.Entry(root)
end_date_entry.place(x=150, y=110)

limit_label = tk.Label(root, text="Limit:")
limit_label.place(x=10, y=140)

limit_entry = tk.Entry(root)
limit_entry.place(x=150, y=140)

download_data_button = tk.Button(root, text="Download Data", command=lambda: download_data(first_country_entry.get().upper(), second_country_entry.get().upper(), start_date_entry.get(), end_date_entry.get(), limit_entry.get()))
download_data_button.place(x=150, y=170)

# Pencereyi ekranda gösterme
root.mainloop()