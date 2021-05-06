import tkinter as tk
import tkinter.simpledialog

class Gui(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.init_window()
    
    def init_window(self):
        self.master.title("Tweet Miner")
        self.pack(fill=tk.BOTH, expand=1)

        twitterUsername = tk.simpledialog.askstring(title="Enter A Twitter Username", prompt='Please enter a twitter username')
        
    def exit(self):
        exit()

root = tk.Tk()
root.geometry("600x400")
app = Gui(root)
root.mainloop()