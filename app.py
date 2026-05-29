# Continue with AI backend:
# Build the Flask AI backend

# Import libraries, Flask tools and the OpenAI API library
from flask import Flask, render_template, request
from openai import OpenAI

# Loads secret variables from the .env file
from dotenv import load_dotenv

# Allows Python to access environment variables and operating system functions
import os

# Load the API key from the .env file
load_dotenv()

# Create the Flask web application
app = Flask(__name__)

# Connect the application to OpenAI using the API key
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create the homepage route
# GET = show the page
# POST = receive the user's question from the form
@app.route("/", methods=["GET", "POST"])
def home():

    # Empty variable where the AI answer will be stored
    response_text = ""

    # Check if the user submitted the form
    if request.method == "POST":

        # Get the text/question the user typed into the webpage
        user_input = request.form["prompt"]

        # Send the user's question to the OpenAI GenAI model
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI study assistant. Format answers clearly using headings, bullet points, and short explanations."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        # Extract the generated AI answer from the OpenAI response
        response_text = response.choices[0].message.content

    # Show the index.html page and send the AI response to it
    return render_template(
        "index.html",
        response=response_text
    )

# Run the Flask application
# host="0.0.0.0" allows access from outside the computer/server
# port=5000 means the app runs on port 5000
# debug=True helps show errors while developing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
