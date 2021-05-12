import tkinter as tk
import tkinter.simpledialog
import TweetMiner
from TweetMiner import tweetMiner

class Gui(tk.Frame):
    def __init__(self, numberOfTweetsToCollect = None, master = None):
        
        self.numberOfTweetsToCollect = numberOfTweetsToCollect
        
        tk.Frame.__init__(self, master)
        self.init_window()
    
    def init_window(self):
        self.master.title("Tweet Miner")
        self.pack(fill=tk.BOTH, expand=1)
        
        # Dialogs
        twitterUsername = tk.simpledialog.askstring(title="Enter A Twitter Username", prompt='Please enter a twitter username')
        
        # Buttons
        collect_tweets_button = tk.Button(self, text = "Collect Tweets", fg = "black" , bg = "gray", command = lambda:[self.request_number_of_tweets_to_collect(),tweetMiner.authenticate(), tweetMiner.getTweets(twitterUsername, self.numberOfTweetsToCollect)])
        collect_tweets_button.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        collect_tweets_button.config(height = 4, width = 20)
    
    def request_number_of_tweets_to_collect(self):
        while True:
            try:
                self.numberOfTweetsToCollect = int(tk.simpledialog.askstring(title="How many Tweets?", prompt='Please enter the # of tweets to collect'))
                break
            except ValueError:
                print("Please enter a valid number!")    
        return self.numberOfTweetsToCollect
   
    def exit(self):
        exit()

root = tk.Tk()
root.geometry("600x400")
app = Gui(root)
root.mainloop()