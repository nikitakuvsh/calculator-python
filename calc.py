import tkinter as tk
from time import sleep


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1: value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calc_answer():
    answer = eval(calc.get().replace(',', '.'))
    calc.delete(0, tk.END)
    if answer == int(answer):
        answer = str(int(answer))
    answer = str(answer).replace('.', ',')
    calc.insert(0, answer)


def delete_lust_num():
    calc_win = calc.get()
    if len(calc_win) == 1 and calc_win == '0':
        pass
    elif len(calc_win) == 1:
        calc.delete(0, tk.END)
        calc.insert(0, '0')
    else:
        calc.delete(0, tk.END)
        calc.insert(0, calc_win[:-1])


def pow():
    num = calc.get().replace(',', '.')
    calc.delete(0, tk.END)
    try:
        calc.insert(0, int(num) ** 2)
    except ValueError:
        calc.insert(0, round(float(num) ** 2))


def sqrt():
    try:
        num = int(calc.get().replace(',', '.'))
        calc.delete(0, tk.END)
        if num ** (0.5) == int(num ** 0.5):
            calc.insert(0, str(int(num ** (0.5))))
        else:
            calc.insert(0, str(num ** (0.5)).replace('.', ','))
    except ValueError:
        calc.delete(0, tk.END)
        calc.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: calc_answer())


def make_delete_last_num_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: delete_lust_num())


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: clear())


def make_pow_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: pow())


def make_sqrt_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: sqrt())


win = tk.Tk()
win.geometry(f"240x325+900+100")
win['bg'] = '#33ffe6'
win.title('Калькулятор')
win.resizable(False, False)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_delete_last_num_button('<<<').grid(row=1, column=2, stick='wens', padx=5, pady=5)

make_digit_button('7').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('1').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=5, column=1, stick='wens', padx=5, pady=5)
make_digit_button(',').grid(row=5, column=2, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=5, column=3, stick='wens', padx=5, pady=5)

make_clear_button('CE').grid(row=1, column=1, stick='wens', padx=5, pady=5)

make_pow_button('x^2').grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_sqrt_button('sqrt').grid(row=1, column=0, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()
