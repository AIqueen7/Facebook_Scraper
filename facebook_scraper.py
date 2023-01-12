import streamlit as st
import facebook
import requests

def scrape_fb_data(access_token, location, query):
    graph = facebook.GraphAPI(access_token)
    profiles = []
    try:
        search_results = graph.request(
            "search",
            {
                "type": "user",
                "q": query,
                "fields": "id,name",
                "location": location
            }
        )
        for profile in search_results["data"]:
            profiles.append(profile["name"])
        return profiles
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Facebook Scraper")

    access_token = st.text_input("Enter your Facebook Access Token:")
    location = st.text_input("Enter the location to search for:")
    query = st.text_input("Enter the keywords to search for:")
    if st.button("Submit"):
        profiles = scrape_fb_data(access_token, location, query)
        if profiles:
            st.write("Results:")
            for profile in profiles:
                st.write("- " + profile)
        else:
            st.warning("No results found.")

if __name__ == "__main__":
    main()