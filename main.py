import discord, asyncio, os, re, datetime, random
from tinytag import TinyTag
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
prefix = "$"

bot = commands.Bot(command_prefix=prefix)
TOKEN = 'jukedbb
  # Where 'TOKEN' is your bot token
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	await bot.change_presence(game=discord.Game(name='you suck'))
@bot.command()
async def ping():
	await bot.say("pong, bitch")

@bot.command(pass_context=True)
async def quoteadd(ctx):
	f = open("quotes.txt","a")
	MSG = ctx.message.content.replace('$quoteadd ','')
	print(len(MSG))
	if len(MSG) < 200 and len(MSG) > 2:
				if MSG in open("quotes.txt").read():
					await bot.say("ERROR: Already entered!")
				else:
					regex = re.compile('[^a-zA-Z0-9 ]')
					quote = regex.sub('', MSG.strip(',.').lower().strip())
					f.write(format('*'+quote+'*'+'\n'))
					await bot.say("added, thanks for contribution. your quote displays as: "+'*'+quote+'*'+'\n')
	else:
		await bot.say("ERROR: Too long or too short!")
	f.close()

@bot.command()
async def quote():
	quote = random.choice(list(open('quotes.txt')))
	await bot.say(quote)
	print(quote)
@bot.command(pass_context=True)
async def image(ctx):
	await bot.send_file(ctx.message.channel, 'image.gif')
@bot.command(pass_context=True)
async def play(ctx):
	audio = "audio/" + random.choice(os.listdir("audio/"))
	Author = ctx.message.author
	Channel = Author.voice_channel
	voice = await bot.join_voice_channel(Channel)
	player = voice.create_ffmpeg_player(audio)
	player.start()
	tag = TinyTag.get(audio)
	duration = tag.duration
	await bot.change_presence(game=discord.Game(name=str(audio)+": "+str(duration)))
	print(duration)
	await asyncio.sleep(duration)
	await voice.disconnect()
	await bot.change_presence(game=discord.Game(name="you suck"))
bot.run(TOKEN)
