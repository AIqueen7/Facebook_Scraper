# Facebook_Scraper

You can run this script using streamlit run app.py command

This app will present a simple UI with three text inputs to allow the user to enter their Facebook Access Token, the location to search for, and the keywords to search for. When the user clicks the "Submit" button, the app will  scrape_fb_data function to scrape Facebook data, and display the results in the app.

------------------------------

To get a Facebook Access Token, you'll need to create a developer account and app on the Facebook Developer website. Once you've done that, you can use the app to generate an Access Token. Here are the general steps to get the Access Token:

Go to the Facebook Developer website (https://developers.facebook.com/) and log in with your Facebook account.

Click on the "My Apps" button in the top right corner of the page, and then select "Create App".

Select the type of app you want to create (e.g., "For Everything Else").

Fill out the required fields, including the name and email of the developer and the app's purpose, and agree to the terms and conditions.

On the left-hand side of the dashboard, click on the "Graph API Explorer" link under the "Tools" section.

Select your newly created app from the top-right corner.

Select the "Get User Access Token" button.

Select the permissions you want to include in the token (e.g., user_friends, public_profile, etc.)

Click "Get Access Token"

After that, you will see your token, you can use this token to scrape facebook data or use it in your app
