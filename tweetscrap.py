# importing libraries#
import streamlit as st
from scrapper import scrap
from db_interactions import pushtodb
from data_formats import to_csv, to_json

#creating a dedicated search by putting a sidebar
st.sidebar.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #92a8d1; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.header('Tweets Searcher')

def query():
    hash = st.sidebar.text_input('Twitter Username to scrape')
    limit = int(st.sidebar.text_input('Enter the number of data to be scraped: (1 to 100)', value=100))
    sdate = st.sidebar.date_input("Start Date")
    edate = st.sidebar.date_input("End Date")
    fetch = st.sidebar.button("Submit")
    sav = st.sidebar.button("Upload")
    reset=st.sidebar.button("Reset")

    scrapd = None

    # Resetting the search bar
    if reset:
        hash = ""
        limit = ""  # Default limit value
        sdate = ""
        edate = ""



    # Fetch scrapped data and display
    if fetch:
        scrapd = scrap(hash, limit, sdate, edate)
        st.write(f"Scraped {len(scrapd)} tweets.")


     # Title and scrap data column
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #F796F7; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("TWEET SCRAPPER")
    st.markdown("The data scrapped from Twitter:")
    st.divider()


    #Displaying scrapped data
    if scrapd is not None:
        st.write(scrapd)
        st.write("Data Scrapped Successfully")


    # Download options -CSV or JSON
    choice = st.radio("Select the Format to download", ["CSV", "JSON"], index=0)
    if st.button("Download"):
        if choice == "CSV":
            to_csv(hash, scrapd)
        elif choice == "JSON":
            to_json(hash, scrapd)


    # Saving scrapped data to MongoDB
    if sav:
        if sav and scrapd is not None:
            pushtodb(hash, scrapd)
            st.write("Data Saved/Uploaded Successfully")
        else:
            st.write("No Data to Save")

#Main menu calling
if __name__ == "__main__":
    query()

