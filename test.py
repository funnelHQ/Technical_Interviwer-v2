import requests

# Provide the path to your audio file
audio_file_path = 'Recording.m4a'

# URL of your Flask endpoint
url = 'http://127.0.0.1:5000/test_correctness'

# Read the audio file
audio_file = open(audio_file_path, 'rb')

# Set the files parameter with the audio file
files = {'audio': audio_file}

# Make a POST request to the endpoint with the audio file
response = requests.post(url, files=files)

# Close the file after the request
audio_file.close()

# Print the response from the server
print(response.json())
