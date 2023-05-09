import sys
import tkinter as tk

class Console(tk.Text):
    def __init__(self, master, **kwargs):
        tk.Text.__init__(self, master, **kwargs)
        self.config(state="disabled")
        self.tag_configure("stdout", foreground="black")
        self.tag_configure("stderr", foreground="red")

    def write(self, text, tags=(), end="\n"):
        self.config(state="normal")
        self.insert("end", text, tags)
        self.see("end")
        self.config(state="disabled")

    def flush(self):
        pass

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Création de la console Python sur le côté droit
        console = Console(self, height=30, width=50)
        console.pack(side=tk.RIGHT)

        # Redirection du flux de sortie standard vers la console
        sys.stdout = console
        sys.stderr = console

        # Affichage d'un message dans la console

if __name__ == "__main__":
    root = tk.Tk()
    
    app = Application(master=root)
    while True:
        print("Hello, world!")
        app.mainloop()