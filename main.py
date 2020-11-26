#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self, title, icon, theme):
        super().__init__()
        self.style = ttk.Style(self)
        self.style.theme_use(theme)
        self.resizable(False, False)
        self.title(title)
        self.iconbitmap(icon)

        self.init_UI()
        self.init_events()

    # INITIALIZER ==============================
    @classmethod
    def create_app(cls, app):
        return cls(app['title'], app['icon'], app['theme'])

    #===========================================
    def init_events(self):
        self.entry.bind('<Return>', self.evt_insert_listbox)

    def init_UI(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.entry_text = tk.StringVar()
        self.entry_text.trace('w', self.callbck_trace_entry)
        self.entry = ttk.Entry(self.frame, textvariable=self.entry_text, width=50)
        self.entry.focus()
        self.entry.pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=True, ipady=5)

        self.label = ttk.Label(self.frame, text='', textvariable=self.entry_text)
        self.label.pack(side=tk.TOP, anchor=tk.W)

        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # -------------------------------------------
    def callbck_trace_entry(self, *args):
        # print('Value Changed')
        self.label['text'] = self.entry_text.get()

    def evt_insert_listbox(self, event):
        self.listbox.insert(tk.END, self.entry_text.get())
        self.entry_text.set('')


#===========================
# Start GUI
#===========================
def main(config):
    app = App.create_app(config)
    app.mainloop()

if __name__ == '__main__':
    main({
        'title' : 'Entry To Listbox',
        'icon' : 'python.ico',
        'theme' : 'clam'
        })