from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934)

    converter_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=3, row=0)


is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=2)


converter_label = Label(text="0", font=("Arial", 12))
converter_label.grid(column=2, row=2)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=3, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)



miles_input = Entry(width=7)
miles_input.grid(column=2, row=0)

window.mainloop()
