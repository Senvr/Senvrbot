import discord, asyncio, os, re, datetime, random
from tinytag import TinyTag
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
prefix = "$"

bot = commands.Bot(command_prefix=prefix)
TOKEN = 'NDgyMDc3NzIyMTY0NzIzNzEz.DmA49A.-7wd0vV-wUN2fwBn7IfyioM_cKs'
  # Where 'TOKEN' is your bot token
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def ping():
	await bot.say("reply")

@bot.command(pass_context=True)
async def quoteadd(ctx):
	f = open("quotes.txt","a")
	MSG = ctx.message.content.replace('$quoteadd ','')
	print(MSG)
	if len(MSG) < 32 and len(MSG) > 2:
			regex = re.compile('[^a-zA-Z0-9 ]')
			quote = regex.sub('', MSG.strip(',.').lower())
			f.write(format('*'+quote+'*'+'\n'))
			await bot.say("added, thanks for contribution")
	else:
		bot.say("There was an error adding your message. Try reducing its length.")
	f.close()

@bot.command()
async def quote():
	quote = random.choice(list(open('quotes.txt')))
	await bot.say(quote)
	print(quote)


@bot.command(pass_context=True)
async def play(ctx):
	audio = "audio/" + random.choice(os.listdir("audio/"))
	bot.say(audio)
	Author = ctx.message.author
	Channel = Author.voice_channel
	voice = await bot.join_voice_channel(Channel)
	player = voice.create_ffmpeg_player(audio)
	player.start()
	tag = TinyTag.get(audio)
	duration = tag.duration
	print(duration)
	if duration > 30:
		await asyncio.sleep(15)
		await bot.say("DURATION IS LONG."+duration)
		await voice.disconnect()
	await asyncio.sleep(duration)
	await voice.disconnect()
	
bot.run(TOKEN)
