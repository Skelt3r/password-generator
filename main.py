from math import floor
from random import choice, choices
from string import ascii_letters, ascii_lowercase, digits
from tkinter import *


# Password generator class with standalone generator function and full GUI
class PasswordGenerator():
    # Generate a random password based on the arguments given
    def generate_password(self, length=12, uppercase=True, numbers=True, symbols=True, standalone=False):
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

        if standalone:
            return f'{alpha}{sequence}'
        else:
            try:
                if int(self.current_length.get()) > 48:
                    self.result_entry['font'] = self.small_font
                else:
                    self.result_entry['font'] = self.default_font

                self.result_entry.delete(0, len(self.result_entry.get()))
                self.result_entry.insert(0, f'{alpha}{sequence}')
            except:
                return 'ERROR: Pass standalone=True if using the generate_password() function independently.'


    # Function for copy button
    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result_entry.get())


    # Function for checkboxes
    def check_uncheck(self, var, arg):
        arg.set(True) if var.get() == 1 else arg.set(False)


    def init(self):
        # Initialize Tkinter
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title('Password Generator')

        # Fonts
        self.default_font = ('SysFixed', 16)
        self.small_font = ('SysFixed', 12)

        # Frames
        border = Frame(self.root, bg='lightgrey')
        background = Frame(border, bg='white', relief='groove', bd=5)

        border.place(relwidth=1, relheight=1)
        background.place(relx=0.5, rely= 0.5, relwidth=0.975, relheight=0.975, anchor='c')

        # Labels
        logo = Label(background, bg='white', text='P@s5wORd-G3nER4t0R', font=('Terminal', 32, 'bold', 'underline'))
        length_label = Label(background, bg='white', text='Password Length:', font=self.default_font)
        uppercase_label = Label(background, bg='white', text='Include Uppercase?', font=self.default_font)
        numbers_label = Label(background, bg='white', text='Include Numbers?', font=self.default_font)
        symbols_label = Label(background, bg='white', text='Include Symbols?', font=self.default_font)
        
        logo.place(relx=0.5, rely=0.1, anchor='c')
        length_label.place(relx=0.01, rely=0.25)
        uppercase_label.place(relx=0.01, rely=0.325)
        numbers_label.place(relx=0.01, rely=0.4)
        symbols_label.place(relx=0.01, rely=0.475)

        # Password length menu
        length_opts = [8, 12, 16, 24, 32, 48, 64]

        self.current_length = StringVar()
        self.current_length.set(length_opts[1])

        length_menu = OptionMenu(background, self.current_length, *length_opts)
        length_menu.config(bg='white', font='SysFixed')
        length_menu['menu'].config(bg='white', font='SysFixed')
        length_menu.place(relx=0.275, rely=0.25)

        # Checkbox variables
        include_uppercase = BooleanVar()
        include_numbers = BooleanVar()
        include_symbols = BooleanVar()

        uppercase_var = IntVar()
        numbers_var = IntVar()
        symbols_var = IntVar()

        # Checkboxes
        uppercase_check = Checkbutton(background,
                                    bg='white',
                                    activebackground='white',
                                    variable=uppercase_var,
                                    command=lambda:self.check_uncheck(uppercase_var, include_uppercase))

        numbers_check = Checkbutton(background,
                                    bg='white',
                                    activebackground='white',
                                    variable=numbers_var,
                                    command=lambda:self.check_uncheck(numbers_var, include_numbers))

        symbols_check = Checkbutton(background,
                                    bg='white',
                                    activebackground='white',
                                    variable=symbols_var,
                                    command=lambda:self.check_uncheck(symbols_var, include_symbols))

        uppercase_check.place(relx=0.275, rely=0.33)
        numbers_check.place(relx=0.275, rely=0.405)
        symbols_check.place(relx=0.275, rely=0.48)

        # Result field
        self.result_entry = Entry(background, bg='white', relief='sunken', justify='center', font=self.default_font)
        self.result_entry.place(relx=0.01, rely=0.6, relheight=0.05, relwidth=0.925)

        # Buttons
        copy_button = Button(background, text='Copy', font=self.small_font, command=lambda:self.copy_password())
        copy_button.place(relx=0.925, rely=0.595)

        gen_button = Button(background,
                            text='Generate',
                            font=('Terminal', 20),
                            bd=5,
                            relief='ridge',
                            command=lambda:self.generate_password(int(self.current_length.get()),
                                                                  include_uppercase.get(),
                                                                  include_numbers.get(),
                                                                  include_symbols.get()))

        gen_button.place(relx=0.5, rely=0.75, anchor='c')

        # Activate checkboxes on startup
        include_uppercase.set(True)
        include_numbers.set(True)
        include_symbols.set(True)

        uppercase_check.toggle()
        numbers_check.toggle()
        symbols_check.toggle()

        # Initialize program
        self.root.mainloop()


# Python go brrrrr
if __name__ == '__main__':
    PasswordGenerator().init()
