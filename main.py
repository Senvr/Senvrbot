import discord, asyncio, os, re, datetime, random
from pathlib import Path
from tinytag import TinyTag
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import subprocess
from time import sleep as y
#from __future__ import absolute_import, unicode_literals
#import json
#from django.http import HttpResponse
#from django.views.decorators.http import require_POST
#from django.views.decorators.csrf import csrf_exempt
prefix = "$"

bot = commands.Bot(command_prefix=prefix)
TOKEN="NTEyMDUyNjI1NTA0NDY4OTkz.Dsz2YQ.0PEntI1IeK4Qgo36crDrmB6w1Fs"
  # Where 'TOKEN' is your bot token
#@require_POST()
#@csrf_exempt()
#def handle_article_published(request):
	#payload = json.loads(request.body)
	#print('A :{0[ref]}'.format(payload))
@bot.event
async def on_ready():
	print('------')

	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(TOKEN)
	await bot.change_presence(game=discord.Game(name='Mk8'))
	p=open("pid","w")
	p.write(str(os.getpid())+'\n')
	p.close
	print("pid="+str(os.getpid()))

	print('------')
@bot.event
async def on_message(msg):

	if msg.author == bot.user:
		return
	if " ping " in str(msg.content).lower().strip():
		await bot.send_message(msg.channel, "pong")
		msg=""
		return
	if " liberal" in str(msg.content).lower().strip() or " socialism" in str(msg.content).lower().strip() or " communism" in str(msg.content).lower().strip() or " pro-choice" in str(msg.content).lower().strip()or " communist" in str(msg.content).lower().strip()or " socialist" in str(msg.content).lower().strip():
		img = "shapiro/" + random.choice(os.listdir("shapiro/"))
		await bot.send_message(msg.channel, 'Ben Shapiro TRIGGERS Liberal by SENDING them to NAZI DEATH CAMPS using pure CONSERVATIVE LOGIC and REASONING and then ANGERS SJW by GOING on a RAMPAGE literally RAPING and MURDERING every single MINORITY within a 200 MILE RADIUS then TROLLS Libtard with TRUMP DERANGEMENT SYNDROME by licking Donald Trumps MICROPENIS of all the DRIED CUM from the CONCEPTION of Barron Trump and he ANGERS democrat by FEEDING upon the FLESH of ABORTED FETUSES and the BLOOD of EVERY single LIBTARD to literally BECOME a GOD AMONG MEN which TROLLS idiot COMMIES by OPENING the seals of HELL and CAUSING the APOCALYPSE in which the DEVIL RAPES CHILDREN and TEARS OFF the heads of Liberal TODDLERS and LITERALLY setting WOMEN’s RIGHTS a THOUSAND YEARS and also Ben TRIGGERS the SOCIALISTS by RAPING the UNDEAD CORPSE of LEON TROTSKY and JOSEPH STALIN and he PISSES OFF the LEFTISTS by ESTABLISHING a NEW WORLD ORDER in which he is the SUPREME GOD EMPEROR OF ALL OF THE AMERICAS, CHINA, EUROPE, BRITAIN, TAIWAN, and THAT RANDOM ISLAND IN THE MIDDLE OF THE PACIFIC OCEAN and MURDERS all POLITICAL DISSIDENTS within the government and then he LITERALLY summons CTHULHU and have home and the DEVIL FUCK HIM IN THE ASS while he CUMS all OVER the BOTTLE of LIBERAL TEARS and then he PRANKS Chink Ugayer by IMITATING him and literally dying from the ANAL WOUNDS from Literally being FUCKED IN THE ASS by SATAN and CTHULHU and then ENRAGES the COMMIES by RAPING GOD and BECOMING the NEW ABSOLUTE RULER OF THE UNIVERSE!!!!! (LIBERALS TROLLED) (NOT CLICKBAIT) (SJWs and FEMINISTS OWNED)')
		await bot.send_file(msg.channel, img)
		msg=""
		return
	await bot.process_commands(msg)
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
	regex = re.compile('[^a-zA-Z0-9 ,.!?/]')
	f = open("quotes.txt","a")
	MSG = regex.sub('', str("**`"+ctx.message.content+"`** by "+ctx.message.author.name).replace('$quoteadd ','')).strip()
	if len(ctx.message.content.replace('$quoteadd ','')) < 200 and len(MSG) > 11:
				if MSG.lower() in open("quotes.txt").read().lower():
					await bot.say("ERROR: Already entered, or your message is too big/small! Must be above 2 characters and be under 200.")
				else:
					f.write(format(MSG)+'\n')
					await bot.say("added, thanks for contribution. your quote displays as: "+MSG)
	else:
		await bot.say("ERROR: Too long or too short!")
	f.close()

@bot.command(pass_context=True)
async def quote(ctx):
	embedQuote=discord.Embed(title="A random quote:", description=random.choice(list(open('quotes.txt'))).strip(), color=0x00ffff)
	await bot.send_message(ctx.message.channel, embed=embedQuote)
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
	await bot.say("This command no longer works. Please wait as I unfuck my own ass.")
	return;
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
	await bot.send_message(ctx.message.channel,"uh oh spaghetti-o's: @Senvr")
	await bot.send_message(ctx.message.channel, "`"+str(error)+"`")
	print(error)
	await bot.change_presence(game=discord.Game(name='ERROR:'+str(error)))
#@bot.command(pass_context = True)
#async def guessinggame(ctx, guess):
	#await bot.say("You guessed: "+str(guess))
	#number=
def isSudoer(person, ctx):
	print("0")
	print(str(ctx.message.server.id)+"/sudoers.conf")
	if not Path(str(ctx.message.server.id)+"/sudoers.conf").exists():
		os.mkdir(str(ctx.message.server.id))
		open(str(ctx.message.server.id)+"/sudoers.conf","x")
	print("2")
	sudofile=open(str(ctx.message.server.id)+"/sudoers.conf","r")
	regex = re.compile('[^0-9]')
	sudoers=sudofile.read().strip().split()
	sudofile.close
	print(sudoers)
	owner=ctx.message.server.owner.id
	if person == owner:
		print(str(person)+" is a sudoer. Owner, infact.")
		return True;
	elif person in sudoers:
		print(str(person)+" is a sudoer.")
		return True;
	else:
		print(str(person)+" is not a sudoer.")
		return False;
	#await bot.say('ERROR: Something weird happened. Tell Senvr if you arent him. [1]')
@bot.command(pass_context=True)
async def adduser(ctx, Member : discord.Member):
	await bot.say("Attempting to adduser to sudoers...")
	if isSudoer(str(ctx.message.author.id), ctx):
		print("1")
		if isSudoer(str(Member.id),ctx):
			await bot.send_message(ctx.message.channel,"They're already a sudoer.")
			print("C")
			return
		else:
				sudofile=open(str(ctx.message.server.id)+"/sudoers.conf","r+")
				sudofile.write(str(Member.id)+"\n")
				print("B")
				regex = re.compile('[^0-9]')
				sudoers=sudofile.read().strip().split()
				print(sudoers)
				await bot.send_message(ctx.message.channel, "OK, added the user. They're a sudoer.")
				sudofile.close
				return;
	else:
		await bot.send_message(ctx.message.channel, "ERROR: 401")
		return;
	print("EOC")
	#sudofile.close
@bot.command(pass_context=True)
async def resetUserData(ctx):
	if isSudoer(ctx.message.author.id,ctx):
		await bot.say("Removing all userdata!")
		folder = 'userdata/'
		for files in os.listdir(folder):
			os.remove(folder+files)
@bot.command(pass_context=True)
async def gayrate(ctx, Member : discord.Member):
	gayRating=""
	if int(Member.id) == int(bot.user.id):
		await bot.say("[GG] Your gay rating is: -999")
		return;
	if Path("userdata/"+Member.id).is_file():
		print("Exists!")
		f=open("userdata/"+str(Member.id),"r")
		await bot.say("[MEM] Your gay rating is: "+f.read())
		gayrating=f.read()
		#if gayrating > 50:
			#await bot.say("Yikes, that's quite big")
		f.close
		return
	else:
		print("Generating new!")
		gayRating=str(random.randint(-100,100))
		print(gayRating)
		f=open("userdata/"+str(Member.id),"w")
		print("assigned new gay rating to "+Member.name+" with id "+Member.id)
		print(gayRating)
		f.write(str(gayRating))
		f.close
		f=open("userdata/"+str(Member.id),"r")
		await bot.say("[RAND] Your gay rating is: "+f.read())
	f.close

bot.run(TOKEN)
