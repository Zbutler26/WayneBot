import discord
import random
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def rumor():
    names = ["Wyatt", "Wayne", "Zach", "Darrin", "David","Connor", "Amro", "Jon", "Jesse", "Justin", "Harsh", "Shivan","Donnie"]
    start_of_rumor = [
        "Word on the street is that ", 
        "I heard ", 
        "One of my contacts told me ", 
        "I have reason to believe ", 
        "Did you know? "
    ]
    rumors = [
        "was caught at the library photocopying a fruit rollup.", 
        "is a big fan of math rock.", 
        "can't get his haircut unless someone else is there to give the barber instructions.", 
        "is a regular at Burger King", 
        "cheats at poker.", 
        "thought frolicking was pronounced 'fro-licking.'"
    ]
    start = random.choice(start_of_rumor)
    name = random.choice(names)
    ending = random.choice(rumors)
    return start + name + " " + ending

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        # Hello
        if message.content.startswith(('$Hello', '$hello')):
            await message.channel.send('Hello World!')

        # Commands
        if message.content.startswith(('$Commands', '$commands')):
            await message.channel.send(
                "**Available Commands:**\n"
                "$Hello\n"
                "$Roll the dice\n"
                "$Meme\n"
                "$Rumor\n"
            )

        # Beer
        if message.content.startswith(('What time is it?', 'what time is it?')):
            await message.channel.send("It's time to get a watch!")

        # Roll
        if message.content.startswith(('$Roll the dice', '$roll the dice')):
            def roll():
                num = random.randint(1, 8)
                if num == 1:
                    return "You rolled a one, pal"
                elif num == 2:
                    return "That's a two for you."
                elif num == 3:
                    return "You certainly rolled a three."
                elif num == 4:
                    return "Wow, good job. You rolled a four. Really well done. I mean it."
                elif num == 5:
                    return "You managed to roll a five."
                elif num == 6:
                    return "My friend, that's a six you just rolled."
                elif num == 7:
                    return "No, I don't think I will."
                else:  
                    return "You rolled an eight! Jackpot!"
            await message.channel.send(roll())

        # Meme
        if message.content.startswith(('$Meme', '$meme')):
            await message.channel.send(get_meme())

        # Rumor
        if message.content.startswith(('$Rumor', '$rumor')):
            await message.channel.send(rumor())    

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')#Insert key
