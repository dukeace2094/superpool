# import requests

# # Define the endpoint for the login request
# url = "http://localhost:5500/login"

# # Define the data to send in the request
# data = {"passcode": "your_passcode"}

# # Send the POST request with the data
# response = requests.post(url, json=data)

# # Check the status code of the response
# if response.status_code == 200:
#     # Handle successful login
#     print("Login successful")

#     # Get the response content
#     response_content = response.json()

#     # Check if the passcode exists in the user table
#     for user in response_content['users']:
#         if user['passcode'] == data['passcode']:
#             # Show the username in the center of the header
#             print("Username: " + user['username'])
#             break
# else:
#     # Handle login error
#     print("Login error")