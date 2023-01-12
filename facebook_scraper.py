import streamlit as st
import facebook

def search_places(access_token, location, query):
    graph = facebook.GraphAPI(access_token)
    try:
        search_results = graph.request(
            "/search",
            {
                "type": "place",
                "q": query,
                "fields": "name, location",
                "center": location,
                "distance": 1000 # search for places within 1km
            }
        )
        return search_results['data']
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Facebook Place Scraper")

    access_token = st.text_input("Enter your Facebook Access Token:")
    location = st.text_input("Enter the location coordinates (lat, long):")
    query = st.text_input("Enter the keywords to search for:")
    if st.button("Submit"):
        places = search_places(access_token, location, query)
