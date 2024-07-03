Explanation (Step by step)

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/ae4fce4a-adce-4073-847c-cf6837c08072)

•	Libraries Import: This block imports necessary libraries for GUI creation (tkinter), web scraping (requests, BeautifulSoup), threading, data handling (pandas), and introducing delays (time).

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/b33a6755-5878-4068-979f-195884e7a911)

•	Initializing a class: The class named MovieScraperApp initializes the GUI window, sets its title, dimensions, and styles using tkinter and ttk.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/e8151d86-7487-4a77-a210-c02c5abddb06)

•	Creating Widgets: This function creates and packs the widgets (labels, combo boxes, buttons, and text area) into the window. It includes selection options for genres and the number of movies to fetch, as well as buttons to fetch movies and clear the screen.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/c53f647c-d720-4e1e-a34c-45b1f98c1de0)

•	Fetching and Displaying Movies: This function gets the selected genre and number of movies, displays a fetching message, and starts a new thread to fetch movies to keep the GUI responsive.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/dd8047e8-52f2-4963-85e6-39841296778d)

•	Fetching Movies: This function builds the URL for scraping, makes the HTTP request, parses the HTML response to extract movie titles, and exports the data to an Excel file. It handles errors and updates the GUI.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/2f03d335-f0b0-4632-835b-b8a8e9188fd4)

•	Exporting to Excel: This function takes a list of movies and exports it to an Excel file named based on the genre.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/95b40d0e-3e51-457b-9bd1-ee1b7ab06fa2)

•	Reading from Excel and Displaying: This function reads the movie list from the Excel file using pandas, extracts the top movies and displays them in the GUI.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/db7c3eeb-c76c-47dc-ac34-51eb6a9f2181)

•	Clearing the Screen: This function resets the genre and top number selections and clears the text area in the GUI and then creates the main Tkinter window, initializes the MovieScraperApp class, and starts the Tkinter main loop.

Important - For Executing the Python code, download the exe file naming "Movie_Suggestion_App" run the code.
A GUI will popup as per the screeenshot below :

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/f11c67b1-f1f7-4825-ab71-5e2a6556ec8d)

Click on Genre dropdown and select the preffered genre.

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/2458a40a-1446-435e-a5d2-70a2069b675f)

Then select the number of movies suggestion required:

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/22f1ce10-de02-4fae-ba4e-fd79579e9753)

Once all the options are select Click on "Fetch Movies" button and the movies will be display in the GUI display:

![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/f2c1c626-dbe3-4802-ba4d-68c258d7f3ca)

Note: Use "Clear Screen" button for rerunning it.

