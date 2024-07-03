import tkinter as tk
from tkinter import ttk
from cyberscrape import krebs_news, hacker_news, dark_reading_news
import webbrowser

def open_url(event):
    webbrowser.open_new(event.widget.cget("text"))

def display_news(news_items):
    root = tk.Tk()
    root.title("Cybersecurity News")
    root.configure(bg='black')

    main_frame = tk.Frame(root, bg='black')
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame, bg='black')
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=frame, anchor="nw")

    for item in news_items:
        title_label = tk.Label(frame, text="Title: " + item['title'], wraplength=400, justify="left", bg='black', fg='white')
        title_label.pack(anchor="w")

        author_label = tk.Label(frame, text="Author: " + item['author'], wraplength=400, justify="left", bg='black', fg='white')
        author_label.pack(anchor="w")

        date_label = tk.Label(frame, text="Date: " + item['date'], wraplength=400, justify="left", bg='black', fg='white')
        date_label.pack(anchor="w")

        summary_label = tk.Label(frame, text="Summary: " + item['summary'], wraplength=400, justify="left", bg='black', fg='white')
        summary_label.pack(anchor="w")

        url_label = tk.Label(frame, text=item['url'], wraplength=400, justify="left", bg='black', fg='blue', cursor="hand2")
        url_label.pack(anchor="w")
        url_label.bind("<Button-1>", open_url)

        separator = tk.Label(frame, text="----------------------------------------------------------------", bg='black', fg='white')
        separator.pack()

    root.mainloop()

if __name__ == "__main__":
    krebs_articles = krebs_news()
    hacker_news_articles = hacker_news()
    dark_reading_articles = dark_reading_news()

    combined_news = krebs_articles + hacker_news_articles + dark_reading_articles
    display_news(combined_news)
