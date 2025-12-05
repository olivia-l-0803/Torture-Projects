<<<<<<< HEAD
import PIL
name = input("What is your name ")

print("You are smelly, " + name)
print("You are smelly," , name)
print(f"You are smelly, {name}.....................")

x = input("are you bald..? ")
while "yes" not in x:
    print("Stop lying.")
    x = input("Are you bald? ")


print("hahahahahahhhhhahhahhahahhaahhahhahhahhahhahhhhaahhaa")
=======
import tkinter as tk
>>>>>>> 7e8847f1456e4c49fe2dba5ee8da0bb475cdbbe3

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