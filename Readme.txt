# Tweet Scrapper

## Description
This project is a Streamlit-based application that allows users to scrape and analyze tweets from Twitter. Users can input search parameters, fetch tweets, display and save data, and interact with a MongoDB database.

## Project Structure
The project is organized into modular files:
- `tweetscrap.py`: Contains the Streamlit GUI code.
- `scrapper.py`: Contains functions for data scraping.
- `db_interactions.py`: Contains functions for MongoDB interaction.
- `data_formats.py`: Contains functions for saving data in different formats.

## Usage
1. Install the required packages:

   pip install streamlit, pandas, snscrape, pymongo

# To Run the application:
Open the Command prompt navigate to the file folder and type
streamlit run tweetscrap.py

#To search Twitter
Use the sidebar to input search parameters, fetch tweets, and interact with the data.

#MongoDB Configuration
Make sure you have MongoDB installed and running.
The code is set to connect to a local MongoDB instance.
Ensure you have the Pymongo package installed.


Available Commands

scrapper.py: Contains the scrap function for scraping tweets.
db_interactions.py: Contains functions to interact with MongoDB.
data_formats.py: Contains functions to save data in CSV and JSON formats.

License
This project is for educational purposes and Feel free to modify and distribute as needed.
