######TODO LIST/FIXME LIST
#FORMAT: [line number], [reason as to why it needs fixing/how to fix it]
#Line 30, it isnt required overall and it makes a loop for no real reason
#Line 136, finish ID system
#line 193, finish REACT system
#Line 227, ^^^
#

###LIBS (not libtards)#######
#used everywehre
import discord, asyncio, os, re, datetime, random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

#used on the isSudoer function
from pathlib import Path

#used on the play function
from tinytag import TinyTag

#used on the isup command
import subprocess

#apparently not used?
import threading

#used in guessinggame command AND ask
import random

#used in eugenics.api 
import urllib.request
##############################

#change the prefix here
prefix = "U$"

#set bot-wise here
bot = commands.Bot(command_prefix=prefix)

#changable token
TOKEN="NTI4MzM0MjQyNDY0MjY4MzAz.DwmuZA.keQk4u8o7FBYXmfQj-JbG0vWDH8"

#this is what makes the error message go away eventually
async def status_task():
    while True:
        await asyncio.sleep(10)
        VER=open("VERSION","r")
        await bot.change_presence(game=discord.Game(name=VER.read()))
        VER.close

#this displays some crap that just makes it easy to see
@bot.event
async def on_ready():
        print('------')
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print(TOKEN)
        VER=open("VERSION","r")
        await bot.change_presence(game=discord.Game(name=VER.read()))
        p=open("pid","w")
        p.write(str(os.getpid())+'\n')
        print("pid="+str(os.getpid()))
        VER.close
        p.close
        print('------')

#This is where the bot says stuff like "debian is better" and crap. 
@bot.event
async def on_message(msg):
	MSG=str(msg.content).lower().strip()
	if msg.author == bot.user or msg.author.bot:
		MSG=""
		return
	if " windows" in MSG:
		await bot.send_message(msg.channel,"linux is better")
	if " ubuntu" in MSG or " linux mint" in MSG or " fedora" in MSG or " gentoo" in MSG :
		await bot.send_message(msg.channel,"debian is better")
	if "i use debian" in MSG or "i use linux" in MSG:
		await bot.send_message(msg.channel,"good")
	if " ping" in MSG:
		await bot.send_message(msg.channel, "pong")
	if " nigger" in MSG:
		await bot.send_message(msg.channel, "you can't say that thats racist")
	if " ddos" in MSG or " ddossing" in MSG:
		await bot.send_message(msg.channel, "ddos is illegal u kno")

	#This is that "annoying" one. You can remove this if you so please.
	if "liberal" in MSG or "socialism" in MSG or " communism " in MSG or " pro-choice " in MSG or " communist " in MSG or " socialist " in MSG:
		img = "shapiro/" + random.choice(os.listdir("shapiro/"))
		await bot.send_message(msg.channel, 'Ben Shapiro TRIGGERS Liberal by SENDING them to NAZI DEATH CAMPS using pure CONSERVATIVE LOGIC and REASONING and then ANGERS SJW by GOING on a RAMPAGE literally RAPING and MURDERING every single MINORITY within a 200 MILE RADIUS then TROLLS Libtard with TRUMP DERANGEMENT SYNDROME by licking Donald Trumps MICROPENIS of all the DRIED CUM from the CONCEPTION of Barron Trump and he ANGERS democrat by FEEDING upon the FLESH of ABORTED FETUSES and the BLOOD of EVERY single LIBTARD to literally BECOME a GOD AMONG MEN which TROLLS idiot COMMIES by OPENING the seals of HELL and CAUSING the APOCALYPSE in which the DEVIL RAPES CHILDREN and TEARS OFF the heads of Liberal TODDLERS and LITERALLY setting WOMEN’s RIGHTS a THOUSAND YEARS and also Ben TRIGGERS the SOCIALISTS by RAPING the UNDEAD CORPSE of LEON TROTSKY and JOSEPH STALIN and he PISSES OFF the LEFTISTS by ESTABLISHING a NEW WORLD ORDER in which he is the SUPREME GOD EMPEROR OF ALL OF THE AMERICAS, CHINA, EUROPE, BRITAIN, TAIWAN, and THAT RANDOM ISLAND IN THE MIDDLE OF THE PACIFIC OCEAN and MURDERS all POLITICAL DISSIDENTS within the government and then he LITERALLY summons CTHULHU and have home and the DEVIL FUCK HIM IN THE ASS while he CUMS all OVER the BOTTLE of LIBERAL TEARS and then he PRANKS Chink Ugayer by IMITATING him and literally dying from the ANAL WOUNDS from Literally being FUCKED IN THE ASS by SATAN and CTHULHU and then ENRAGES the COMMIES by RAPING GOD and BECOMING the NEW ABSOLUTE RULER OF THE UNIVERSE!!!!! (LIBERALS TROLLED) (NOT CLICKBAIT) (SJWs and FEMINISTS OWNED)')
		await bot.send_file(msg.channel, img)
		msg=""
		return

	if "ooga" in MSG:
		await bot.send_message(msg.channel, "booga")

	#This line is important. Otherwise it wont process commands.
	await bot.process_commands(msg)

#Ping-pong
@bot.command()
async def ping():
	await bot.say("pong, bitch")

#Eugenics.fun api thing.
@bot.command()
async def eugenics():
	url = "http://eugenics.fun/api/random/"
	response=urllib.request.urlopen(url)
	data = response.read() 
	text = data.decode('utf-8')
	await bot.say(text+"\ngot from http://eugenics.fun/api")

#"ask" command, 1/3 chance for every answer and is intentionally simple (if you see other "ask" commands in other bots it seems like it hangs on "ask again" or "unsure" all the time)
@bot.command(pass_context=True)
async def ask(ctx):
	if len(ctx.message.content.strip()) < 2:
		await bot.send_message(ctx.message.channel, "You need to ask a question.")
		return;
	else:
		replies=["yes","no","maybe"]
		await bot.say(random.choice(replies))

#add a quote to the quotes file
@bot.command(pass_context=True)
async def quoteadd(ctx):
	print(ctx.message.content)
	await bot.say("Trying to add...")
	regex = re.compile('[^a-zA-Z0-9 ,.!?/]')
	MSG = regex.sub('', str("**'"+ctx.message.content+"'** by "+ctx.message.author.name).replace('$quoteadd ','')).strip()
	if len(ctx.message.content.replace('$quoteadd ','')) < 200 and len(MSG) > 11: #Anti-spam check, must be under 200 and above 11 characters (Note: It INCLUDES the $quoteadd command, which is 9 characters)
				if MSG.lower() in open("quotes.txt").read().lower():
					await bot.say("ERROR: Already entered, or your message is too big/small! Must be above 2 characters and be under 200.")
				else:
					f = open("quotes.txt","a")
					f.write(format(MSG)+'\n')
					ID=file_len("quotes.txt")
					await bot.say("added, thanks for contribution. your quote displays as: "+MSG+" with id "+str(ID))
					f.close()
					#ID system is a WIP
	else:
		await bot.say("ERROR: Too long or too short!")
	f.close()

#read quote command
@bot.command(pass_context=True)
async def quote(ctx):
	embedQuote=discord.Embed(title="A random quote:", description=random.choice(list(open('quotes.txt'))).strip(), color=0x00ffff) #make a fancy embed to show off our skillz
	await bot.send_message(ctx.message.channel, embed=embedQuote)
	print(quote)

#display a random image
@bot.command(pass_context=True)
async def image(ctx):
	phrases = ["shazam", "skedush","skiddly doo","bambeen","bamboon"]
	phrase = random.choice(phrases)
	await bot.say(phrase)
	img = "images/" + random.choice(os.listdir("images/"))
	await bot.send_file(ctx.message.channel, img)

#BY YESNT: display a random *cursed* image
@bot.command(pass_context=True)
async def cursed_image(ctx):
        phrases = ["shazam", "skedush","skiddly doo","bambeen","bamboon"]
        phrase = random.choice(phrases)
        await bot.say(phrase)
        img = "images/cursed/" + random.choice(os.listdir("images/cursed/"))
        await bot.send_file(ctx.message.channel, img)

#credit the friendos
@bot.command(pass_context=True)
async def credits(ctx):
	await bot.say("HELPERS:\nSenvr\nZeman\nAnOverlyComplexUsername (You're fucking right on that)\nTeenarous\nYesnt")

#play a random mp3 in a VC, usually earrape or stupid memes
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

#UNFINISHED
@bot.command(pass_context=True)
async def react(name,ctx):
	regex = re.compile('[^a-zA-Z0-9 ]')
	image = regex.sub('', name.strip(',.').lower().strip())
	img = "images/" + image +".jpg"
	
	await bot.send_file(ctx.message.channel, img)

#get PID, for the bot runner
@bot.command()
async def pid():
	await bot.say(str(os.getpid()))

#command to see if a selective process is up or not, it doesn't work but it might if you let it
@bot.command(pass_context=True)
async def isup(ctx, process):
	await bot.say("This command no longer works. Please wait as I unfuck my own ass.")
	return; #remove these two lines to enable
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
#unfinished
@bot.command()
async def getreactions():
	files=[]
	for filenames in os.walk('./images'):
		for filename in filenames:
			print(filenames.strip())
			files.append(filenames.strip())
	await bot.say(files[1:])

#show the github so people can laugh at my coding skills
@bot.command()
async def github():
	await bot.say("https://github.com/Senvr/Senvrbot")

#guessinggame, this lets you guess a number based on a difficulty value.
@bot.command(pass_context = True)
async def guessinggame(ctx, guess, difficulty):
	if int(difficulty)  == "" :
		await bot.say('Difficulty value must be a number! (math: `randint(1,1+difficulty*2)`')
		return;
	
	guess=1+int(difficulty)*2
	await bot.say("You guessed: "+str(guess)+" out of "+str(guess))
	number=random.randint(1,guess)
	if int(guess) == number:
		await bot.say("You win!")
	else:
		print("1")
		await bot.say("You lost. You were off by "+str(abs(int(guess)-number)))

#Senvrs sudo system, lets special boy users do special boy commands
def isSudoer(person, ctx):
	print("0")
	print(str(ctx.message.server.id)+"/sudoers.conf")
	print("1")
	if not Path(str(ctx.message.server.id)):
		os.mkdir(str(ctx.message.server.id))
	if not Path(str(ctx.message.server.id)+"/sudoers.conf").exists():
		print("2")
		open(str(ctx.message.server.id)+"/sudoers.conf","x")
		print("3")
	print("4")
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

#add a user/role to the sudoers file
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

#reset user data
@bot.command(pass_context=True)
async def resetUserData(ctx):
	if isSudoer(ctx.message.author.id,ctx):
		await bot.say("Removing all userdata!")
		folder = 'userdata/'
		for files in os.listdir(folder):
			os.remove(folder+files)

#display a users GayRate(tm) rating
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


#This handles errors. (Moved to bottom of script)
@bot.event
async def on_command_error(error, ctx):
	await bot.send_message(ctx.message.channel,"uh oh spaghetti-o's: @Senvr")
	await bot.send_message(ctx.message.channel, "`"+str(error)+"`")
	print(error)
	await bot.change_presence(game=discord.Game(name='ERROR:'+str(error)))
	bot.loop.create_task(status_task())

#This runs the bot itself.
bot.run(TOKEN)