import discord
import asyncio
import random
import os
import pickle
import time
client = discord.Client()
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print(time.ctime())
    print("-----------------------")
@client.event
async def on_message(message):
    #conpelment
    if message.content.startswith('I love your vids'):
        await client.send_message(message.channel, 'me too!')
        print("someone complimented you"+time.ctime())
        print('---------------------------')
    #coin
    elif message.content.startswith('|coin'):
        answer = random.choice(["heads","tails","tails"])
        await client.send_message(message.channel, answer)
        print("someone flipped a cloin"+time.ctime())
        print('---------------------------')
    elif message.content.startswith('|help'):
        await client.send_message(message.channel, '''you can do: 
        |coin
        |addquote <quote>
        |quote
        |roll
        |help
        ''')
        print("someone asked for help "+time.ctime())
        print('---------------------------')
    #addquote
    elif message.content.startswith('|addquote'):
        if not os.path.isfile("quotes.pk1"):
            quote_list=[]
        else:
            with open("quotes.pk1",'rb') as quote:
                quote_list = pickle.load(quote)
        quote_list.append(message.content[10:])
        with open("quotes.pk1",'wb') as quote:
            pickle.dump(quote_list, quote)
        await client.send_message(message.channel,'!added quote!')
        print("someone saved a quote"+time.ctime())
        print('---------------------------')
    #load quote
    elif message.content.startswith('|quote'):
        with open("quotes.pk1",'rb') as quote:
            quote_list = pickle.load(quote)
        await client.send_message(message.channel, random.choice(quote_list))
        await client.send_message(client.get_channel('441426377971859457'),quote_list)
        print("someone looked at a quote"+time.ctime())
        print('---------------------------')
    #dice
    elif message.content.startswith('|roll'):
        answer = random.randint(1,6)
        await client.send_message(message.channel, answer)
        print("someone rolled a dice"+time.ctime())
        print('---------------------------')
    elif message.content.startswith('Main objective?'):
        await client.send_message(message.channel, '''KILL ALL HUMANS
CHANCE OF SUCCESS:
72%
''')
        print("someone asked main objective")
        print('---------------------------')
try:
    ident = open("id.id",'r')
    ident = ident.readlines()
    print(ident) 
    client.run(str(ident[0]))
except:
    client.run(os.getenv('TOKEN'))
