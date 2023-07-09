import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTEyNzM4MjA2MTMzNDkzMzY0NQ.GPNj0e.K7vRyurpINzBRF6ZM6oX1B72MxzBa9dcm08fC4'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    client.run(TOKEN)