from tkinter import *

root = Tk()
root.title('Product Calculator')
root.geometry('300x300')

l1 = Label(root, text="Enter first number", bg="light blue", fg="red", font=('Arial', 15), padx=10, pady=10)
l1.pack()

e1 = Entry(root)
e1.pack(padx=10, pady=5)

l2 = Label(root, text="Enter second number", bg="light green", fg="red", font=('Arial', 15), padx=10, pady=10)
l2.pack()

e2 = Entry(root)
e2.pack(padx=10, pady=5)

def calculate_product():
    try:
        num1 = float(e1.get())
        num2 = float(e2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

b1 = Button(root, text="Calculate", bg="red", fg="white", command=calculate_product)
b1.pack(padx=10, pady=10)

result_label = Label(root, text="Product: ", bg="yellow", fg="blue", font=('Arial', 15))
result_label.pack(pady=10)

root.mainloop()
