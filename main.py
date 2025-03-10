import streamlit as st
import pandas as pd
import csv
import os  
import datetime

# Page Config with custom icon
st.set_page_config(page_title="Mood Tracker 😊", page_icon="📊", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #ff6f61;
            text-align: center;
        }
        .stButton>button {
            background-color: #ff6f61;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            width: 100%;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #ff3b2f;
        }
    </style>
""", unsafe_allow_html=True)

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    """Load mood data from CSV"""
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE, encoding="utf-8")

def save_mood_data(date, mood):
    """Save mood data to CSV"""
    with open(MOOD_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

def delete_mood(index):
    """Delete selected mood entry"""
    data = load_mood_data()
    if not data.empty and index < len(data):
        data = data.drop(index)
        data.to_csv(MOOD_FILE, index=False, encoding="utf-8")  # Save updated data

# Main App Container
with st.container():
    st.title("🌟 Mood Tracker App 🌟")

    st.subheader("How are you feeling today? 😊")

    date = datetime.date.today()

    # Mood Selection
    mood = st.selectbox("Select your mood", ["Happy 😊", "Sad 😢", "Angry 😠", "Neutral 😐", "Stress 😫"])

    # Log Mood Button
    if st.button("Log Mood"):
        save_mood_data(date, mood)
        st.success(f"✅ Mood logged Successfully for {date}!")

    # Load and Display Mood Data
    data = load_mood_data()

    if not data.empty:
        st.subheader("📊 Mood Trends Over Time")

        data["Date"] = pd.to_datetime(data["Date"])
        mood_counts = data.groupby("Mood").count()["Date"]

        # Displaying Data as a Chart
        st.bar_chart(mood_counts)

      
# Footer
st.write("💡 **Build with ❤️ by [Ayesha](https://github.com/ayesha-aziz123)**")
