# AudioVize

AudioVize is a Python-based project that allows users to extract audio from videos, perform various operations on the audio, add timestamps with comments, and navigate to specific timestamps in the audio. Users can upload videos from their local machine or provide a YouTube video URL to convert it to audio. The project also includes a sign-up and login feature for user authentication.

## Features

- Convert video to audio: Users can upload videos from their local machine or provide a YouTube video URL to extract audio.
- Timestamps: Users can add timestamps to the audio and associate comments with each timestamp.
- Navigation: By clicking on a timestamp, users can navigate to that specific time in the audio.
- Download audio: Users can download the converted audio file.
- User Authentication: Sign-up and login functionality to secure user access and manage user-specific data.

## Installation

To run AudioVize locally, follow these steps:

1. Clone the repository:

git clone https://github.com/Sid2728/Ethos

2. Navigate to the project directory:
cd Ethos

3. Install the required dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py migrate

5. Start the development server:
python manage.py runserver



6. Open your web browser and visit `http://localhost:8000` to access AudioVize.

## Dependencies

AudioVize has the following dependencies:

- Django: A high-level Python web framework for rapid development.
- Django templates: Used to create HTML templates for rendering views.
- SQLite: A lightweight, file-based database used as the default database backend in Django.

For a complete list of dependencies, refer to the `requirements.txt` file.

## Usage

1. Launch AudioVize by visiting `http://localhost:8000` in your web browser.

2. Sign up for an account:
- Click on the "Sign Up" button.
- Provide the required information, such as username and password, to create a new account.

3. Log in to your account:
- Click on the "Log In" button.
- Enter your credentials (username and password) to log in to your account.

4. Upload a video:
- To upload a video from your local machine, click on the "Upload Video" button and select the video file.
- To convert a YouTube video to audio, paste the YouTube video URL into the provided input field.

5. Perform operations on the audio:
- Add timestamps: Click on the "Add Timestamp" button to add a timestamp to the audio. Provide a time value (in minutes and seconds) and add an associated comment.
- Download audio: Click on the "Download Audio" button to save the converted audio file to your local machine.

6. Navigate to a timestamp:
- Click on any timestamp in the list to navigate to that specific time in the audio.
## Link to Site:
https://audiofy-hcx1.onrender.com





