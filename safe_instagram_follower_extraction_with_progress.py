# Import necessary libraries
from instagrapi import Client
import pandas as pd
import time
import random

# Initialize the Instagram API client
cl = Client()

# Function to print and track progress
def print_progress(current, total):
    print(f"Fetching follower {current} of {total}...")

# Login with your username and password
# NOTE: Replace USERNAME and PASSWORD with your Instagram username and password
USERNAME = "your_username"
PASSWORD = "your_password"

cl.login(USERNAME, PASSWORD)

# Add a random delay between 1 and 3 seconds after each request
cl.delay_range = [1, 3]

# Fetch the list of follower ids
followers = cl.user_followers(cl.user_id, amount=0)

# Extracting follower information into a list of dictionaries
follower_list = []
total_followers = len(followers)
for idx, (follower_id, follower_info) in enumerate(followers.items()):
    print_progress(idx + 1, total_followers)
    
    follower_dict = {
        "ID": follower_id,
        "Username": follower_info.username,
        "Full Name": follower_info.full_name,
    }
    follower_list.append(follower_dict)
    
    # Adding random delay to mimic user behavior
    time.sleep(random.uniform(1, 3))

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(follower_list)

# Save the DataFrame to an Excel file
df.to_excel("Instagram_Followers.xlsx", index=False)

print("Successfully saved the follower list to 'Instagram_Followers.xlsx'")
