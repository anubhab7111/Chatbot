# Gemini Chatbot

💬 A simple command-line chatbot powered by Google Gemini, allowing users to interact with a generative AI model for real-time responses.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)

## Features

- Interactive command-line interface for chatting.
- Real-time response generation using Google Gemini.
- Maintains chat history for a continuous conversational experience.

## Technologies Used

- [Google Gemini](https://cloud.google.com/generative-ai) - For natural language processing and response generation.
- Python - Programming language used to build the application.

## Installation

1. **Clone the repository**:
   ```bash
   $ git clone https://github.com/yourusername/chatbot.git
   $ cd chatbot

2. **Install the requirements**

   ```bash
   $ pip install -r requirements.txt
   
## Usage 
1. Set up your API key: Ensure you have a Google API key. You can set the key in your environment variables:
   - On macOS/Linux:
      ```bash
      export GOOGLE_API_KEY='your_api_key_here'

   - On Windows
      ```bash 
      set GOOGLE_API_KEY='your_api_key_here'

2. Run the application: Execute your Python script:
      ```bash
      python gemini_bot.py

3. Start chatting: You will be prompted to ask anything. Type your message and hit Enter. Type exit to stop the chatbot.

## Environment Variables
This application uses the GOOGLE_API_KEY environment variable for authentication. Make sure to keep your API key confidential and never share it publicly.