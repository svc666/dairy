import streamlit as st
import pandas as pd
from datetime import datetime

# Create a session state to store diary entries
if 'diary_entries' not in st.session_state:
    st.session_state.diary_entries = []

# Function to add a diary entry
def add_entry(entry):
    date = datetime.now().strftime("%Y-%m-%d")
    st.session_state.diary_entries.append({"Date": date, "Entry": entry})

# Function to display diary entries
def display_entries():
    if st.session_state.diary_entries:
        for index, entry in enumerate(st.session_state.diary_entries):
            st.write(f"**Date:** {entry['Date']}")
            st.write(f"**Entry:** {entry['Entry']}\n")
    else:
        st.write("No entries found.")

# Streamlit UI
st.title("Virtual Diary App")

# Add a new entry
st.header("Add a New Diary Entry")
entry_text = st.text_area("Write your diary entry (end with 'END'):")
if st.button("Add Entry"):
    if entry_text.strip():
        # Remove the ending "END" if it's present
        if entry_text.endswith("END"):
            entry_text = entry_text[:-3].strip()
        add_entry(entry_text)
        st.success("Entry added!")

# View diary entries
st.header("View Diary Entries")
display_entries()

# Option to clear entries (optional)
if st.button("Clear All Entries"):
    st.session_state.diary_entries.clear()
    st.success("All entries cleared!")
