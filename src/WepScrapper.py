from tkinter import ttk
import tkinter as tk
from newspaper import Article
from newspaper import fulltext
import pandas as pd
import urllib.request
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class WebScrapper :

    def __init__(self, path, root):
        self.data = pd.read_csv(path)

        self.root = root

        self.progress_label = tk.Label(root, text="Data Scraping Progress:")
        self.progress_label.place(x=10, y=280)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.place(x=10, y=310)

        self.idx = 0

    def update_progress(self, current, total):
        # Oranı hesapla ve progress bar'ı güncelle
        progress = (current / total) * 100
        self.progress_bar["value"] = progress
        self.progress_label["text"] = f"Data Scraping Progress: {current} / {total}"
        self.root.update()


    def get_text_method_1(self, url):
        article = Article(url)
        article.download()
        article.parse()
    
        return article.text
    
    def get_text_method_2(self, url):
        html = requests.get(url).text
        try:
            text = fulltext(html)
        except:
            text = ""
        return text
    def get_text(self, url):
        if self.idx == 0:self.update_progress(self.idx, len(self.data))
        self.idx = self.idx + 1
        try:
            text_1 = self.get_text_method_1(url)
        except:
            text_1 = ""
    
        try:
            text_2 = self.get_text_method_2(url)
        except:
            text_2 = ""
    
        text = text_1 if len(text_1) > len(text_2) else text_2
        self.update_progress(self.idx, len(self.data))
        return text
    
    def get_source_text(self):
        self.idx = 0
        self.data['source_text'] = self.data['SOURCEURL'].apply(self.get_text)
        return self.data
    