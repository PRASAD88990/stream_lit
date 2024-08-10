import streamlit as st
import pandas as pd
import requests

# Example data for destinations, hotels, and restaurants
DESTINATIONS = {
    "Paris": {"description": "The city of lights", "image": "https://example.com/paris.jpg"},
    "New York": {"description": "The city that never sleeps", "image": "https://example.com/nyc.jpg"},
    "Tokyo": {"description": "The bustling metropolis", "image": "https://example.com/tokyo.jpg"}
}

HOTELS = {
    "Paris": [
        {"name": "Hotel Lumiere", "price": 120, "rating": 4.5},
        {"name": "Eiffel Inn", "price": 150, "rating": 4.7}
    ],
    "New York": [
        {"name": "Grand Plaza", "price": 200, "rating": 4.3},
        {"name": "Central Suites", "price": 180, "rating": 4.6}
    ],
    "Tokyo": [
        {"name": "Shinjuku Hotel", "price": 110, "rating": 4.4},
        {"name": "Tokyo Tower Inn", "price": 130, "rating": 4.8}
    ]
}

RESTAURANTS = {
    "Paris": [
        {"name": "Le Gourmet", "price": 50, "rating": 4.5},
        {"name": "Café Paris", "price": 40, "rating": 4.2}
    ],
    "New York": [
        {"name": "Broadway Bistro", "price": 60, "rating": 4.4},
        {"name": "NY Diner", "price": 45, "rating": 4.3}
    ],
    "Tokyo": [
        {"name": "Sushi World", "price": 55, "rating": 4.6},
        {"name": "Ramen House", "price": 35, "rating": 4.5}
    ]
}

# Streamlit app
st.title("TripSphere - Travel Planner")

# Destination selection
destination = st.selectbox("Choose a destination:", list(DESTINATIONS.keys()))

# Display destination details
if destination:
    st.image(DESTINATIONS[destination]["image"], width=600)
    st.write(DESTINATIONS[destination]["description"])

    # Display hotel information
    st.subheader("Hotels")
    hotel_df = pd.DataFrame(HOTELS[destination])
    st.write(hotel_df)

    # Display restaurant information
    st.subheader("Restaurants")
    restaurant_df = pd.DataFrame(RESTAURANTS[destination])
    st.write(restaurant_df)

# Placeholder for map integration
st.subheader("Map")
st.write("Map integration can be added here.")

# Run the app
if __name__ == "__main__":
    st.write("Run the Streamlit app by executing 'streamlit run app.py' in your terminal.")
