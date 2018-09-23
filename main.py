import discord, asyncio, os, re, datetime, random
from tinytag import TinyTag
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import subprocess
prefix = "$"

bot = commands.Bot(command_prefix=prefix)
TOKEN="REPLACEME"  # Where 'TOKEN' is your bot token
@bot.event
async def on_ready():
	print('------')

	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	await bot.change_presence(game=discord.Game(name='you suck'))
	p=open("pid","w")
	p.write(str(os.getpid())+'\n')
	p.close
	print("pid="+str(os.getpid()))

	print('------')
@bot.command()
async def ping():
	await bot.say("pong, bitch")

@bot.command(pass_context=True)
async def quoteadd(ctx):
	print(ctx.message.content)
	if len(ctx.message.content) < 5:
		await bot.say("Too short")
		return;
	else:
		await bot.say("Trying to add...")
	regex = re.compile('[^a-zA-Z0-9 ]')
	f = open("quotes.txt","a")
	MSG = regex.sub('', ctx.message.content.replace('$quoteadd ','')).lower().strip(',.').strip()
	print(len(MSG))
	if len(MSG) < 200:
				if MSG in open("quotes.txt").read():
					await bot.say("ERROR: Already entered!")
				else:
					f.write(format(MSG))
					await bot.say("added, thanks for contribution. your quote displays as: "+MSG+"\n")
	else:
		await bot.say("ERROR: Too long or too short!")
	f.close()

@bot.command()
async def quote():
	quote = '"*'+random.choice(list(open('quotes.txt')))+'*"'
	await bot.say(quote.rstrip())
	print(quote)
@bot.command(pass_context=True)
async def image(ctx):
	phrases = ["shazam", "skedush","skiddly doo","bambeen","bamboon"]
	phrase = random.choice(phrases)
	await bot.say(phrase)
	img = "images/" + random.choice(os.listdir("images/"))
	await bot.send_file(ctx.message.channel, img)

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
@bot.command(pass_context=True)
async def react(name,ctx):
	regex = re.compile('[^a-zA-Z0-9 ]')
	image = regex.sub('', name.strip(',.').lower().strip())
	img = "images/" + image +".jpg"
	
	await bot.send_file(ctx.message.channel, img)
@bot.command()
async def pid():
	await bot.say(str(os.getpid()))
@bot.command(pass_context=True)
async def isup(ctx, process):
	regex = re.compile('[^a-zA-Z0-9 ]')
	stdin=str(regex.sub('',process.strip(',.').lower())) 
	def seeIfUp( stdin):
		output = str(subprocess.getoutput('ps -A'))
		if stdin in output:
			return "true"
		else:
			return "false"
		return "error"
	if process == "minecraft":
		await bot.say(stdin+" check: ")
		await bot.say(str(seeIfUp("java")))
	elif process == "PyBot":
		await bot.say(stdin+" check: ")
		await bot.say("what the fuck do you think")
	else:
		await bot.say(stdin+" not on or found")
	
@bot.command()
async def getreactions():
	files=[]
	for filenames in os.walk('./images'):
		for filename in filenames:
			print(filenames.strip())
			files.append(filenames.strip())
	await bot.say(files[1:])
@bot.command()
async def github():
	await bot.say("https://github.com/Senvr/Senvrbot")
@bot.event
async def on_command_error(error, ctx):
	await bot.send_message(ctx.message.channel, "`"+str(error)+"`")
	print(error)

bot.run(TOKEN)
