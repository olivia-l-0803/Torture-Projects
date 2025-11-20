import tkinter as tk

class MyCustomWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello from a custom widget!")
        self.label.pack()

        self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Class-Based Tkinter")

    custom_widget = MyCustomWidget(root)
    custom_widget.pack(pady=20)

    root.mainloop()