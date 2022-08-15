import tkinter as tk
import tkinter.ttk as ttk
from app import constants


class Interface(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title('Tk - Weather')
        self.resizable(False, False)

        self.header_image = tk.PhotoImage(file=constants.HEADER_IMAGE)
        self.search_image = tk.PhotoImage(file=constants.SEARCH_IMAGE)
        self.iconphoto(False, self.header_image)

        container = ttk.Frame(self)
        container.config(padding=15)
        container.pack(side='top', fill='both', expand=True)

        header = ttk.Label(container)
        header.config(text='Type city name')
        header.config(anchor='center')
        header.config(image=self.header_image, compound='top')
        header.pack(side='top', fill='x', pady=10)

        self.inp_city_var = tk.StringVar()
        self.inp_city = ttk.Entry(container)
        self.inp_city.config(textvariable=self.inp_city_var)
        self.inp_city.config(justify='center')
        self.inp_city.config(style='App.TEntry')
        self.inp_city.config(font='Arial 18 normal')
        self.inp_city.focus()
        self.inp_city.pack(side='top')

        self.feedback_var = tk.StringVar()
        self.feedback = ttk.Label(container)
        self.feedback.config(textvariable=self.feedback_var)
        self.feedback.config(anchor='center')
        self.feedback.config(foreground='red')
        self.feedback.pack(side='top', fill='x')

        self.button = ttk.Button(container)
        self.button.config(command=None)
        self.button.config(text='Search')
        self.button.config(image=self.search_image, compound='left')
        self.button.pack(pady=20)

        self.table = Table(container)

        style = ttk.Style()
        style.theme_use('clam')
        self.config(background='#fff')
        style.configure('.', background='white')
        style.configure('.', font='Consolas 18 bold')
        style.configure('Treeview', rowheight=40)

        style.map(
            'TButton',
            foreground=[('active', '#fff')],
            background=[('active', '#0801DB')],
        )

    def city(self) -> str:
        return self.inp_city_var.get()

    def set_city(self, city: str) -> None:
        self.inp_city_var.set(city)

    def set_feedback(self, feedback: str) -> None:
        self.feedback_var.set(feedback)
        self.inp_city.focus()

    def add_info(self, description: str, info: str) -> None:
        self.table.treeview.insert('', 'end', values=(description, info))

    def clear_info(self) -> None:
        self.table.treeview.delete(*self.table.treeview.get_children())

    def show_info(self) -> None:
        self.table.pack(side='top', fill='both', expand=True)

    def hide_info(self) -> None:
        self.table.pack_forget()


class Table(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.treeview = ttk.Treeview(self)
        self.treeview.config(show='headings')
        self.treeview.config(columns=('key', 'value'))
        self.treeview.column('key', anchor='center')
        self.treeview.column('value', anchor='center')

        self.hor_scrollbar = ttk.Scrollbar(self, orient='horizontal')
        self.hor_scrollbar.config(command=self.treeview.xview)
        self.treeview.config(xscrollcommand=self.hor_scrollbar.set)

        self.ver_scrollbar = ttk.Scrollbar(self, orient='vertical')
        self.ver_scrollbar.config(command=self.treeview.yview)
        self.treeview.config(yscrollcommand=self.ver_scrollbar.set)

        self.hor_scrollbar.pack(side='bottom', fill='x')
        self.treeview.pack(side='left', fill='both', expand=True)
        self.ver_scrollbar.pack(side='right', fill='y')
