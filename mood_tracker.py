import streamlit as st # for Creating eb Interface
import pandas as pd # Data Manipulation
import datetime # for handling Dates
import csv # for reading adn writing CSV files
import os # for file operations

# Define the file name for storting mood data
MOOD_FILE = "mood_log.csv"

# Dunction to rad mood data from the CSV file
def load_mood_data():

     # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # if no file, create empty DataFrame with Columns
        return pd.DataFrame(columns=["Date",  "Mood"])
    
        # Read and return existing mood data
    return pd.read_csv(MOOD_FILE)

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    # Open file in append mode
    with open(MOOD_FILE, "a") as file:

        # Create CSV writer
        writer= csv.writer(file)

        # Add new mood entry
        writer.writerow([date, mood])

# Stream Lit TITLE
st.title("Mood Tracker")

# Get Today's Date
today = datetime.date.today()

# Create subheader for mood input
st.subheader("How are you feeling today?")

# Create dropdown for mood selection
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Create button to save mode
if st.button("Log Mood"):

    #save mood when button is clicked
    save_mood_data(today, mood)

    #success message show    
    st.success("Mood Logged Succesfully")

# Load existing mood data
data = load_mood_data()

# If there is data to display
if not data.empty:

    # Create section  foe visualization
    st.subheader("Mood Trends Over Time")

    # Convert date stings to dateTime Objects
    data["Date"] = pd.to_datetime(data["Date"])

    # Count frequnecy of each mood
    mood_counts = data.groupby(["Mood"]).count()["Date"]

    # Display the bar chart of mood frequency
    st.bar_chart(mood_counts)

    # Build by Jawad

    st.write ("Build by Jawad")