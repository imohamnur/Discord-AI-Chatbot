import discord
from better_profanity import profanity
import openai

TOKEN = #INSERT DISCORD BOT TOKEN HERE
client = discord.Client(intents=discord.Intents.all())
openai.api_key = #INSERT OPEN AI KEY HERE

# Sends message to channel in server
async def send_message(message, user_message):
    try:
        response = handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == "badlanguage":
        return 'That language is not allowed in this server.'

async def generate_response(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": str(prompt)}
            ]
        )
        return response['choices'][0]['message']['content']

def run_discord_bot():
    # Prints when bot is online
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # when a message is typed it will do this function 
    @client.event
    async def on_message(message):
        user = str(message.author)
        user_message = str(message.content)
        censored = profanity.censor(user_message)
        # checks if the bot typed the message
        if message.author == client.user:
            return
        if message.content.startswith('hey bot'):
            prompt = message.content.replace('hey bot', '')
            response = await generate_response(prompt)
            await message.channel.send(response)
        await send_message(message, user_message)

        # deletes message if contains inappropriate language then sends message
        for element in censored:
            if element == '*':
                await message.channel.purge(limit=1)
                await send_message(message, 'badlanguage')
                break
    
    @client.event
    async def on_member_join(member):
        channel = member.guild.system_channel
        if channel is not None:
            message = f'Welcome to the server, {member.mention}!'
            await channel.send(message)
    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()