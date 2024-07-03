import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd
import time

class MovieScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Suggestion App")
        self.root.geometry("600x500")

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12))

        self.create_widgets()

    def create_widgets(self):
        self.genre_label = ttk.Label(self.root, text="Select a movie genre:")
        self.genre_label.pack(pady=10)

        self.genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller']
        self.genre_combobox = ttk.Combobox(self.root, values=self.genres, state='readonly', width=30)
        self.genre_combobox.pack()

        self.top_label = ttk.Label(self.root, text="Select number of top movies:")
        self.top_label.pack(pady=10)

        self.top_combobox = ttk.Combobox(self.root, values=[3, 5, 10], state='readonly', width=10)
        self.top_combobox.pack()

        self.fetch_button = ttk.Button(self.root, text="Fetch Movies", command=self.fetch_and_display)
        self.fetch_button.pack(pady=20)

        self.clear_button = ttk.Button(self.root, text="Clear Screen", command=self.clear_screen)
        self.clear_button.pack(pady=10)

        self.results_text = scrolledtext.ScrolledText(self.root, height=15, width=70, wrap=tk.WORD)
        self.results_text.pack(pady=20)

    def fetch_and_display(self):
        genre = self.genre_combobox.get()
        if not genre:
            messagebox.showerror("Error", "Please select a genre.")
            return

        top_number = self.top_combobox.get()
        if not top_number:
            messagebox.showerror("Error", "Please select number of top movies.")
            return

        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, f"Fetching movies for {genre} genre..\n")
        self.root.update()  # Update GUI to show fetching message

        # Call method to scrape and display movies using a separate thread
        threading.Thread(target=self.fetch_movies, args=(genre, int(top_number))).start()

    def fetch_movies(self, genre, top_number):
        url = f'https://www.rottentomatoes.com/browse/movies_in_theaters/genres:{genre.lower()}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check if the request was successful

            soup = BeautifulSoup(response.content, 'html.parser')
            movies = []

            movie_tags = soup.select('span.p--small[data-qa="discovery-media-list-item-title"]')
            for tag in movie_tags:
                movie_name = tag.get_text(strip=True)
                movies.append(movie_name)

            # Export movies to an Excel file
            self.export_to_excel(movies, genre)

            # Clear results text and show movies
            self.results_text.delete('1.0', tk.END)
            self.results_text.insert(tk.END, f"Catalog Received for {genre} genre:\n\n")
            self.results_text.insert(tk.END, f"Top {top_number} {genre} movies:\n\n")
            self.root.update()  # Update GUI to show catalog received message

            # Read from Excel file and display top movies
            self.read_from_excel_and_display(genre, top_number)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", f"Failed to fetch movies: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def export_to_excel(self, movies, genre):
        """Export the list of movies to an Excel file"""
        df = pd.DataFrame(movies, columns=['Movie Name'])
        excel_filename = f"scraped_raw_{genre.lower()}_movies.xlsx"
        df.to_excel(excel_filename, index=False)
        self.results_text.insert(tk.END, f"Movies exported to {excel_filename}\n")
        self.root.update()

    def read_from_excel_and_display(self, genre, top_number):
        """Read movies from the Excel file and display the top movies"""
        excel_filename = f"scraped_raw_{genre.lower()}_movies.xlsx"
        df = pd.read_excel(excel_filename)
        top_movies = df['Movie Name'].head(top_number)

        # Print each movie with a delay
        for idx, movie in enumerate(top_movies, start=1):
            self.results_text.insert(tk.END, f"{idx}. {movie}\n")
            self.root.update()  # Update the GUI to show each movie
            time.sleep(0.5)  # Add a delay between displaying each movie

        # Add final message after displaying all movies
        self.results_text.insert(tk.END, "\nPlease enjoy the movies!\n")

    def clear_screen(self):
        self.genre_combobox.set('')  # Clear genre selection
        self.top_combobox.set('')  # Clear top number selection
        self.results_text.delete('1.0', tk.END)  # Clear text area

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieScraperApp(root)
    root.mainloop()
