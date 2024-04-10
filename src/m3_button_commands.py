import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Fillable Form")

def print_form():
    print("Name:", name_entry.get())
    print("Address Line 1:", address1_entry.get())
    print("Address Line 2:", address2_entry.get())
    print("City:", city_entry.get())
    print("State:", state_entry.get())
    print("Zip Code:", zip_entry.get())
    print("Phone Number:", phone_entry.get())
    print("Email Address:", email_entry.get())

window.configure(bg="#F0F0F0")

form_frame = tk.Frame(window, bg="#F0F0F0")
button_frame = tk.Frame(window, bg="#F0F0F0")
form_frame.grid(row=0, column=0, padx=20, pady=20)
button_frame.grid(row=0, column=1, padx=20, pady=20)

header_label = tk.Label(form_frame, text="Please Fill out the Form", bg="#F0F0F0", fg="black", font=("Arial", 14, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(form_frame, text="Name:", bg="#F0F0F0", fg="black", font=("Arial", 10))
name_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=35)
name_entry.grid(row=1, column=1, padx=5, pady=5)

address1_label = tk.Label(form_frame, text="Address Line 1:", bg="#F0F0F0", fg="black", font=("Arial", 10))
address1_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
address1_entry = tk.Entry(form_frame, width=35)
address1_entry.grid(row=2, column=1, padx=5, pady=5)

address2_label = tk.Label(form_frame, text="Address Line 2:", bg="#F0F0F0", fg="black", font=("Arial", 10))
address2_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
address2_entry = tk.Entry(form_frame, width=35)
address2_entry.grid(row=3, column=1, padx=5, pady=5)

city_label = tk.Label(form_frame, text="City:", bg="#F0F0F0", fg="black", font=("Arial", 10))
city_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
city_entry = tk.Entry(form_frame, width=35)
city_entry.grid(row=4, column=1, padx=5, pady=5)

state_label = tk.Label(form_frame, text="State:", bg="#F0F0F0", fg="black", font=("Arial", 10))
state_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
state_entry = tk.Entry(form_frame, width=35)
state_entry.grid(row=5, column=1, padx=5, pady=5)

zip_label = tk.Label(form_frame, text="Zip Code:", bg="#F0F0F0", fg="black", font=("Arial", 10))
zip_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
zip_entry = tk.Entry(form_frame, width=35)
zip_entry.grid(row=6, column=1, padx=5, pady=5)

phone_label = tk.Label(form_frame, text="Phone Number:", bg="#F0F0F0", fg="black", font=("Arial", 10))
phone_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)
phone_entry = tk.Entry(form_frame, width=35)
phone_entry.grid(row=7, column=1, padx=5, pady=5)

email_label = tk.Label(form_frame, text="Email Address:", bg="#F0F0F0", fg="black", font=("Arial", 10))
email_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=35)
email_entry.grid(row=8, column=1, padx=5, pady=5)


submit_button = tk.Button(button_frame, text="Submit", bg="green", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5, command=print_form)
submit_button.pack()

window.mainloop()