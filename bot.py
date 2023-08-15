import discord
import responses
import random


async def send_message(message, user_message, food, is_private):
    try:
        response = responses.get_response(user_message)

        if user_message.lower().find('!add') > -1:
            add_food = user_message.lower().replace('!add', '').split()
            add_food = ' '.join(map(str, add_food))
            food.append(add_food.capitalize())

        if user_message.lower().find('!list') > -1:
            response_food = '\n'.join(food)
            response = f"{response}\n**{response_food}**"
            await message.author.send(response) if is_private else await message.channel.send(response)

        elif user_message.lower() == '!pick':
            response_pick = random.choice(food)
            response = f"{response}***{response_pick}***."
            await message.author.send(response) if is_private else await message.channel.send(response)

        else:
            await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTExNzE4Njc5MTE4Nzk1MTc0MA.G_0HUu.VxwQowaW0243xi5EG1mKCVgFyYiuxuzCkHVfzI'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    food_list = []

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        elif message.content[0] != '!':
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: {user_message} ({channel})")
        print(food_list)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, food_list, is_private=True)
        else:
            await send_message(message, user_message, food_list, is_private=False)

    client.run(TOKEN)
