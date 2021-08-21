import tkinter as tk

window = tk.Tk()
window.title('my tkinter program')
window.minsize(width=300, height=300)

input_miles = tk.Entry(width=10)
input_miles.grid(row=0, column=1)

miles_unit_label = tk.Label(
    text='miles', fg="black", font=('Arial', 12, "normal"))

miles_unit_label.grid(row=0, column=2)


def conv_to_km():
    miles = float(input_miles.get())
    km = miles * 1.60934
    km_label.config(text=km)


km_unit_label = tk.Label(text="Km", fg="black", font=('Arial', 12, "normal"))
km_unit_label.grid(row=1, column=2)

equal_to_label = tk.Label(text='is equal to', fg="black",
                          font=('Arial', 12, "normal"))


equal_to_label.grid(row=1, column=0)
result = 0
km_label = tk.Label(text="0", fg="black", font=('Arial', 12, "normal"))
km_label.grid(row=1, column=1)

calculate_button = tk.Button(text='calculate', fg="black", command=conv_to_km)
calculate_button.grid(row=2, column=1)


window.mainloop()
