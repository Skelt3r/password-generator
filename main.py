from math import floor
from random import choice, choices
from string import ascii_letters, ascii_lowercase, digits
from tkinter import *


def init():
    def generate_password(length, uppercase=True, numbers=True, symbols=True):
        pool = []
        sequence = str()
        symbol_list = ['!', '?', '@', '#', '$', '%', '&', '*', '+', '-', '=', '_']

        if uppercase:
            pool += [letter for letter in ascii_letters]
            alpha = choice(ascii_letters)
        else:
            pool += [letter for letter in ascii_lowercase]
            alpha = choice(ascii_lowercase)

        if len(pool) != 0:
            for _x in range(1, length):
                sequence += choice(pool)

        if numbers:
            for letter in choices(population=sequence, k=floor(len(sequence)/3)+1):
                sequence = sequence.replace(letter, choice(digits))
            
        if symbols:
            for letter in choices(population=sequence, k=floor(len(sequence)/6)+1):
                sequence = sequence.replace(letter, choice(symbol_list))

        if int(length_display.get()) > 48:
            result_entry['font'] = small_font
        else:
            result_entry['font'] = default_font
        
        result_entry.delete(0, len(result_entry.get()))
        result_entry.insert(0, f'{alpha}{sequence}')


    def copy_password():
        root.clipboard_clear()
        root.clipboard_append(result_entry.get())


    def check_uncheck(var, arg):
        if var.get() == 1:
            arg.set(True)
        else:
            arg.set(False)


    root = Tk()
    root.geometry('800x600')
    root.title('Password Generator')

    default_font = ('SysFixed', 16)
    small_font = ('SysFixed', 12)

    border = Frame(root, bg='lightgrey')
    border.place(relwidth=1, relheight=1)

    background = Frame(border, bg='white', relief='groove', bd=5)
    background.place(relx=0.5, rely= 0.5, relwidth=0.975, relheight=0.975, anchor='c')

    logo = Label(background, bg='white', text='P@s5wORd-G3nER4t0R', font=('Terminal', 32, 'bold', 'underline'))
    logo.place(relx=0.5, rely=0.1, anchor='c')

    length_label = Label(background, bg='white', text='Password Length:', font=default_font)
    uppercase_label = Label(background, bg='white', text='Include Uppercase?', font=default_font)
    numbers_label = Label(background, bg='white', text='Include Numbers?', font=default_font)
    symbols_label = Label(background, bg='white', text='Include Symbols?', font=default_font)
    
    length_label.place(relx=0.01, rely=0.25)
    uppercase_label.place(relx=0.01, rely=0.325)
    numbers_label.place(relx=0.01, rely=0.4)
    symbols_label.place(relx=0.01, rely=0.475)

    length_opts = [8, 12, 16, 24, 32, 48, 64]

    length_display = StringVar()
    length_display.set(length_opts[1])

    length_menu = OptionMenu(background, length_display, *length_opts)
    length_menu.config(bg='white', font='SysFixed')
    length_menu['menu'].config(bg='white', font='SysFixed')
    length_menu.place(relx=0.275, rely=0.25)

    include_uppercase = BooleanVar()
    include_numbers = BooleanVar()
    include_symbols = BooleanVar()

    uppercase_var = IntVar()
    numbers_var = IntVar()
    symbols_var = IntVar()

    uppercase_check = Checkbutton(background,
                                bg='white',
                                activebackground='white',
                                variable=uppercase_var,
                                command=lambda:check_uncheck(uppercase_var, include_uppercase))

    numbers_check = Checkbutton(background,
                                bg='white',
                                activebackground='white',
                                variable=numbers_var,
                                command=lambda:check_uncheck(numbers_var, include_numbers))

    symbols_check = Checkbutton(background,
                                bg='white',
                                activebackground='white',
                                variable=symbols_var,
                                command=lambda:check_uncheck(symbols_var, include_symbols))

    uppercase_check.place(relx=0.275, rely=0.33)
    numbers_check.place(relx=0.275, rely=0.405)
    symbols_check.place(relx=0.275, rely=0.48)

    result_entry = Entry(background, bg='white', relief='sunken', justify='center', font=default_font)
    result_entry.place(relx=0.01, rely=0.6, relheight=0.05, relwidth=0.925)

    copy_button = Button(background, text='Copy', font=small_font, command=lambda:copy_password())
    copy_button.place(relx=0.925, rely=0.595)

    gen_button = Button(background,
                        text='Generate',
                        font=('Terminal', 20),
                        bd=5,
                        relief='ridge',
                        command=lambda:generate_password(int(length_display.get()),
                                                        include_uppercase.get(),
                                                        include_numbers.get(),
                                                        include_symbols.get()))

    gen_button.place(relx=0.5, rely=0.75, anchor='c')

    include_uppercase.set(True)
    include_numbers.set(True)
    include_symbols.set(True)

    uppercase_check.toggle()
    numbers_check.toggle()
    symbols_check.toggle()

    root.mainloop()


if __name__ == '__main__':
    init()
