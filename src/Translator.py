from tkinter import ttk
import tkinter as tk
from deep_translator import GoogleTranslator
from langdetect import detect
from typing import List
import pandas as pd
import re

import time

class Translator:
    def __init__(self, path, root):
        self.google_translator = GoogleTranslator(source='auto', target='en')
        self.data = pd.read_csv(path)
        self.path = path

        self.root = root

        self.progress_label = tk.Label(root, text="Data Scraping Progress:    ")
        self.progress_label.place(x=10, y=340)

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.place(x=10, y=370)

        self.idx = 0
        file = open("src/not_scrapping_indicators.txt", "r")
        self.mask = file.readlines()
        file.close()
        self.mask = [x.strip() for x in self.mask]

    def update_progress(self, current, total, text):
        # Oranı hesapla ve progress bar'ı güncelle
        progress = (current / total) * 100
        self.progress_bar["value"] = progress
        self.progress_label["text"] = f"{text} Progress: {current} / {total}    "
        self.root.update()

    def batch_created(self, text: str, max_length: int = 3000) -> List[str]:
        """
        Splits the text into parts based on a specified character limit.

        Args:
            text (str): The text to be split.
            max_length (int): The maximum character length of each part.

        Returns:
            List[str]: A list of text parts.
        """
        sentences = text.split(". ")  # Split the text into sentences
        batch_list = []
        tmp_string = ""

        for sentence in sentences:
            if len(tmp_string) + len(sentence) + 2 <= max_length:
                tmp_string += (". " if tmp_string else "") + sentence
            else:
                batch_list.append(tmp_string)
                tmp_string = sentence

        if tmp_string:
            batch_list.append(tmp_string)

        return batch_list


    def clean_text(self, text: str) -> str:
        """
        Replaces "\n" characters in the text with a space and reduces multiple spaces to a single space.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        if self.idx == 0:self.update_progress(self.idx, len(self.data), "Data Cleaning")
        self.idx += 1

        text = text.replace("\n", " ")
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space

        self.update_progress(self.idx, len(self.data), "Data Cleaning")
        return text.strip()


    def translate_to_english(self, text: str) -> str:
        """
        Translates the given text to English.

        Args:
            text (str): The text to be translated.

        Returns:
            str: The translated text in English.
        """

        # Detect the source language of the text
        source_language = detect(text).lower()

        if self.idx == 0:self.update_progress(self.idx, len(self.data), "Data Translation")
        self.idx += 1

        if source_language != 'en':  # If the source language is not English
            batch_list = self.batch_created(text)
            translated_text = ""
            for batch in batch_list:
                check = True
                while check:
                    try:
                        tmp_text = self.google_translator.translate(batch)
                        if len(translated_text) == 0: translated_text += tmp_text
                        else: translated_text += (". " + tmp_text)
                        check = False
                    except Exception as e:
                        self.google_translator = GoogleTranslator(source='auto', target='en')
                        time.sleep(10)
        else:
            translated_text = text

        self.update_progress(self.idx, len(self.data), "Data Translation")
        return translated_text



    def get_translate(self):
        self.data = self.data.dropna(subset=['source_text'], axis=0, how='any')
        self.data.reset_index(drop=True, inplace=True)

        self.idx = 0
        print("Clean Text")
        self.data['source_text'] = self.data['source_text'].apply(self.clean_text)

        self.idx = 0
        print("\nTranslate Text")
        self.data['text_en'] = self.data['source_text'].apply(self.translate_to_english)

        self.data = self.data[~self.data['text_en'].str.contains('|'.join(self.mask), case=False, na=False)]

        self.data.to_csv(self.path, index=False)