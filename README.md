# Discord Chatbot with Profanity Filter using OpenAI

This is a Discord chatbot implemented in Python that utilizes the OpenAI GPT-3.5-turbo model for generating responses. The bot also includes a profanity filter using the `better_profanity` library to censor and handle inappropriate language.

## Prerequisites

Make sure you have the following installed before running the bot:

- Python 3.x
- discord.py library (`pip install discord.py`)
- better_profanity library (`pip install better_profanity`)
- OpenAI Python library (`pip install openai`)

Additionally, you'll need the following:

- Discord bot token: Obtain a token by creating a new bot on the Discord Developer Portal.
- OpenAI API key: Sign up for the OpenAI GPT-3 API and obtain an API key.

## Setup

1. Insert your Discord bot token and OpenAI API key in the designated places in the code (where specified).

## Usage

Run the bot and make sure you have an active internet connection, and the bot will start and log in to the specified Discord server using the provided bot token. Ideally it would be better to upload the code to a server for 24/7 uptime.

## Functionality

- The bot will respond to messages starting with "hey bot" by generating a response using the OpenAI GPT-3.5-turbo model.
- It includes a profanity filter that censors inappropriate language using the `better_profanity` library.
- If a message contains inappropriate language, the bot will delete the message and respond with a predefined message.
- The bot sends a welcome message to new members who join the server (if a system channel is available).

Feel free to modify the code to add more features or customize the bot's behavior to suit your needs.

## Disclaimer

Keep in mind that the profanity filter is not foolproof, and it may not catch all instances of inappropriate language. Adjust and enhance the filtering mechanism as needed to maintain a safe and appropriate environment.

## Troubleshooting

- Make sure you have correctly inserted the Discord bot token and OpenAI API key.
- Check that you have installed all the required libraries and dependencies.
- Verify that you have an active internet connection.
- If you encounter any errors or issues, refer to the respective documentation for the libraries or services being used.

Enjoy using your Discord chatbot with a profanity filter powered by OpenAI!

