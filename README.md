Explanation (Step by step)


![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/ae4fce4a-adce-4073-847c-cf6837c08072)

•	Libraries Import: This block imports necessary libraries for GUI creation (tkinter), web scraping (requests, BeautifulSoup), threading, data handling (pandas), and introducing delays (time).
 ![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/00f449d4-9183-471b-ad56-7c7bc3f8d737)

•	Initializing a class: The class named MovieScraperApp initializes the GUI window, sets its title, dimensions, and styles using tkinter and ttk.
 ![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/558caa88-bb7a-4289-b35b-fff01bf3ec31)

•	Creating Widgets: This function creates and packs the widgets (labels, combo boxes, buttons, and text area) into the window. It includes selection options for genres and the number of movies to fetch, as well as buttons to fetch movies and clear the screen.
 ![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/d286421c-2a88-40b8-996e-2a9fb7523911)

•	Fetching and Displaying Movies: This function gets the selected genre and number of movies, displays a fetching message, and starts a new thread to fetch movies to keep the GUI responsive.
![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/f95f928c-4f60-4579-bdfe-d4b8343467f2)

•	Fetching Movies: This function builds the URL for scraping, makes the HTTP request, parses the HTML response to extract movie titles, and exports the data to an Excel file. It handles errors and updates the GUI.
![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/d15055db-f1ce-43ea-a668-b6346aba60db)
 
•	Exporting to Excel: This function takes a list of movies and exports it to an Excel file named based on the genre.
 ![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/2068f6c2-7910-4c7e-9846-d5b29cd20d09)

•	Reading from Excel and Displaying: This function reads the movie list from the Excel file using pandas, extracts the top movies and displays them in the GUI.
 ![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/6f574b9c-ae3d-44f4-885d-b0202b4ed967)

•	Clearing the Screen: This function resets the genre and top number selections and clears the text area in the GUI and then creates the main Tkinter window, initializes the MovieScraperApp class, and starts the Tkinter main loop.

Important - For Executing the Python code, download the exe file naming "Movie_Suggestion_App" run the code.
A GUI will popup as per the screeenshot below :
![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/87052dfe-7052-4011-b1b2-fb1c3e7a288e)

Click on Genre dropdown and select the preffered genre.
![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/f7c76e91-cc36-4dc5-87b3-e901b565622e)

Then select the number of movies suggestion required:
![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/f1a85035-87ca-4882-a666-cef408777093)

Once all the options are select Click on "Fetch Movies" button and the movies will be display in the GUI display:
![image](https://github.com/suchargs/Python-Project-Submission/assets/174418092/d5647462-101c-4004-a10f-dd69e68fe69a)

Note: Use "Clear Screen" button for rerunning it.

