# Cocktail-App

Welcome my Cocktail Application!

## Table of Contents
- [Cocktail-App](#cocktail-app)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [App File Structure](#app-file-structure)
  - [Features](#features)
  - [Screenshots](#screenshots)
  - [Technologies Used](#technologies-used)
  - [Installation and Operation](#installation-and-operation)
    - [Option 1 - Run Locally:](#option-1---run-locally)
    - [Option 2 - Use Docker:](#option-2---use-docker)
    - [App Operation:](#app-operation)
  - [Attributions](#attributions)
## Overview

This application allows users to explore a vast collection of cocktails. The user interface is designed to be intuitive and user-friendly, employing aspects of Cognitive Syle Heuristics (CSH). Users can search for drinks by name and filter the results to display specific information on the page, such as ingredients or instructions. Additionally, a browse-by-index feature (e.g., alphabetical) is available for users who prefer not to search by typing a name.

> [!NOTE]
>This application originally utilized a microservice architecture for the "Random Pick" functionality. However, the microservice is no longer being hosted at AWS. For demonstration purposes, the GET request on line 213 of app.py calls an external API directly. To integrate a future microservice, some code modifications would be necessary to re-establish the communication layer.


## App File Structure
The following is a brief overview of the file structure

[./app.py]() - Main entry point and route handler

[./templates/home.html](https://github.com/voyagerfan/Cocktail-App/blob/main/templates/home.html) - The home page

[./templates/browse.html](https://github.com/voyagerfan/Cocktail-App/blob/main/templates/browse.html) - The browse screen

[./Dockerfile](https://github.com/voyagerfan/Cocktail-App/blob/main/Dockerfile) - To create a docker image

## Features

This web applcation the following features: 
* <u>Effortless Exploration:</u> Search for your favorite drinks by name or browse our extensive cocktail index.
* <u>Customizable Output</u>: Choose to display the information you're most interested in, whether it's a captivating picture, a detailed list of ingredients, or comprehensive instructions.
* <u>Intuitive Search</u>: Find what you're looking for quickly and easily with our user-friendly search functionalities.
* <u>Built for Discovery</u> Feeling adventurous? Take a chance with our "Random Cocktail" button and explore something new!
* <u>Microservice Ready:</u> The app's design allows for future integration with additional data sources, ensuring a constantly evolving cocktail collection.
* <u>Informative User Warnings:</u> Stay informed about potential actions with clear warnings before proceeding (e.g. reset button)
* <u>Docker Deployment Potential:</u> (Optional) This application can be easily deployed using Docker containers, making it readily accessible across different platforms.

## Screenshots
Home page

![](./screenshots/homescreen.png)

Displayed data

![](./screenshots/displayed_data.png)

Browse by Index

![](./screenshots/browse_by_index.png)

Warning popup
![](./screenshots/warning_popup.png)


## Technologies Used

- **Programming Languages:** Python, HTML
- **Frameworks:** Flask
- **Plaform** Docker

## Installation and Operation

### Option 1 - Run Locally:

*Prerequisites:* An **IDE**, **Python**

>[!NOTE]
> The following instructions are for Visual Studio Code on macOS but you may use an IDE of your choosing if you can run Python code. Please install Python on your computer too (for [Windows](https://www.python.org/download/releases/2.5/msi/), for [Mac](https://docs.python.org/3/using/mac.html))

1) Clone the repository to a directory of your choosing
2) Using Visual Studio Code, open the project folder. **File** -> **Open Folder**
3) Open a terminal. **Terminal** -> **New Terminal**
4) Create a virual environment using the terminal command below
   ```bash
   python3 -m venv .venv
   ```
5) Activate the virtual environment
   ```bash
   source .venv/bin/activate
   ```
6) Install the requirements
   ```bash
   pip install -r requiremens.txt
   ```
7) Ensure that the listener is configured to run locally. It should look like this.

   ```python
   # Listener
   if __name__ == "__main__":

      # run with docker 
      #app.run(port=4000,debug=True, host='0.0.0.0')

      # run locally
      app.run(port=4000,debug=True, host='127.0.0.1')
   ```
8) Start the app
   
   ```bash
   python3 app.py
   ```

9) Open a web browser and enter the address below to view the app. 
   
   ```
   http:\\localhost:4000
   ```

### Option 2 - Use Docker:
*Prerequisites:* **Docker**, **Python**

>[!NOTE]
>The following instructions are for macOS. You may follow the general outline of these instructions for other operating systems.

1) Install and step up [Docker](https://docs.docker.com/desktop/install/mac-install/)
2) Clone the repository
3) Open a terminal and navigate to the cloned repo folder on your drive.
4) Create a virtual environment
   ```bash
   python3 -m venv .venv 
   ```
5) open the app.py (in an IDE, text editor or vim) and make sure the lister is configured as follows:
   ```python
   # Listener
   if __name__ == "__main__":

      # run with docker 
      app.run(port=4000,debug=True, host='0.0.0.0')

      # run locally
      #app.run(port=4000,debug=True, host='127.0.0.1')
   ```
6) Using the terminal, create a Docker image
   ```bash
   docker build -t cocktail_app . 
   ```
7) Build the container and start the app
   ```bash
   docker run -d -p 4000:4000 cocktail_app
   ```
8) Open a web browser and enter the following address below to view the app.
   
   ```
   http:\\localhost:4000
   ```

### App Operation:
* You may enter a cocktail name in the drink name form, use "Browse By Index" or click the "Random Pick" buttom.
  * Using "browse by index" will re-route you to the browse by index page.
  * If using the browse by index page, click a letter and press submit. A list of cocktails matching the first letter will be displayed.
  * Clicking on a cocktail will re-route you back to the homepage and your drink will be displayed in "Current Search Results"
* Using either the drink form or the random button will populate the "Current Search Results" field.
* If a cocktail is not found when using the drink name form, the "Current Search Results" field will indicate that it is not found and you may try again.
* Once the "Current Search Results" field is populated with a valid cocktail, you may chose the data you want to display. Check 1 or all 3 checkboxes and click submit. The data you request will be displayed on the page.


## Attributions
Rigoberto Mejia - Project partner


