import tkinter as tk
from src.Backend import download_data
from tkcalendar import DateEntry


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

start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
start_date_entry.place(x=150, y=80)


end_date_label = tk.Label(root, text="End Date:")
end_date_label.place(x=10, y=120)

end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
end_date_entry.place(x=150, y=120)

limit_label = tk.Label(root, text="Limit:")
limit_label.place(x=10, y=160)

limit_entry = tk.Entry(root)
limit_entry.place(x=150, y=160)
limit_entry.insert(0, "1000")

download_data_button = tk.Button(root, text="Download Data", command=lambda: download_data(first_country_entry.get().upper(), second_country_entry.get().upper(), start_date_entry.get(), end_date_entry.get(), limit_entry.get()))
download_data_button.place(x=150, y=200)

# Pencereyi ekranda gösterme
root.mainloop()