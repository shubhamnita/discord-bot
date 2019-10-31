import discord
from credentials_store import TOKEN,my_api_key,my_cse_id
from search_actions import google_search,get_history
import database_connection as db


client = discord.Client()

@client.event
async def on_message(message):
    user = str(message.author.mention)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('hey'):
        #msg = 'Hello {0.author.mention}'.format(message)
        msg = 'hi'
        await message.channel.send(msg)
    elif message.content.startswith('!google'):
        search_keyword = message.content.split('!google ')[1]
        results = google_search(search_keyword, my_api_key, my_cse_id, user, num=5)
        await message.channel.send(results)
    elif message.content.startswith('!recent'):
        history_keyword = message.content.split('!recent ')[1]
        history_data = get_history(history_keyword, user)
        await message.channel.send(history_data)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    db.create_search_table()
    print('------')

#run the app    
client.run(TOKEN)