# importing libraries
import asyncio
# import bitlyshortener
# from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import discord
from discord.ext import commands
from discord.ext.commands import BucketType, CheckFailure, CommandOnCooldown, CommandNotFound
from discord.ext import tasks
from discord import Webhook, RequestsWebhookAdapter
import html2text
import json
from keepAlive import keepAlive
from ordinal import ordinal
import os
import portolan
import psutil
import pytz
import random
import requests
from requests.auth import HTTPBasicAuth
import tinydb
import variables
from uuid import uuid4

# set prefix and remove default help command
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents, case_insensitive = True)

# mute json logging setup
mutes = {}
muteDatabase = tinydb.TinyDB("muteDatabase.json")
query = tinydb.Query()

async def assignments():
	s = bot.get_guild(variables.serverID)
	bot.server = bot.get_guild(variables.serverID)
	bot.welcomeChannel = bot.get_channel(variables.welcomeChannelID)
	bot.rolesChannel = bot.get_channel(variables.rolesChannelID)
	bot.rulesChannel = bot.get_channel(variables.rulesChannelID)
	bot.channelsChannel = bot.get_channel(variables.channelsChannelID)
	bot.logChannel = bot.get_channel(variables.logChannelID)
	bot.generalChannel = bot.get_channel(variables.generalChannelID)
	bot.staffOnlyChannel = bot.get_channel(variables.staffOnlyChannelID)
	bot.joinGameChannel = bot.get_channel(variables.joinGameChannelID)
	bot.botProfile = s.get_member(variables.rolesChannelID)
	bot.survivalServerBot = s.get_member(variables.survivalServerBotID)
	bot.creativeServerBot = s.get_member(variables.creativeServerBotID)
	bot.eventLabel = variables.eventLabel
	bot.commandLabel = variables.commandLabel
	bot.serverInviteURL = variables.serverInviteURL
	bot.statusPageURL = variables.statusPageURL

	bot.birthdayRole = s.get_role(variables.birthdayRoleID)
	bot.liveOnTwitchRole = s.get_role(variables.liveOnTwitchRoleID)
	bot.adminRole = s.get_role(variables.adminRoleID)
	bot.moderatorRole = s.get_role(variables.moderatorRoleID)
	bot.mutedRole = s.get_role(variables.mutedRoleID)
	bot.vipRole = s.get_role(variables.vipRoleID)
	bot.allahRole = s.get_role(variables.allahRoleID)
	bot.memberRole = s.get_role(variables.memberRoleID)
	bot.botRole = s.get_role(variables.botRoleID)
	bot.devBotRole = s.get_role(variables.devBotRoleID)
	
	bot.dividerOneRole = s.get_role(variables.dividerOneRoleID)
	bot.bellScheduleRole = s.get_role(variables.bellScheduleRoleID)
	bot.helpRole = s.get_role(variables.helpRoleID)
	bot.precalculusRole = s.get_role(variables.precalculusRoleID)
	bot.apCalcABRole = s.get_role(variables.apCalcABRoleID)
	bot.apCalcBCRole = s.get_role(variables.apCalcBCRoleID)
	bot.hPhysicsRole = s.get_role(variables.hPhysicsRoleID)
	bot.apPhysicsRole = s.get_role(variables.apPhysicsRoleID)
	bot.apBiologyRole = s.get_role(variables.apBiologyRoleID)
	bot.rushRole = s.get_role(variables.rushRoleID)
	bot.apushRole = s.get_role(variables.apushRoleID)
	bot.vsNetRole = s.get_role(variables.vsNetRoleID)
	bot.apcsRole = s.get_role(variables.apcsRoleID)
	
	bot.dividerTwoRole = s.get_role(variables.dividerTwoRoleID)
	bot.amongUsRole = s.get_role(variables.amongUsRoleID)
	bot.chessRole = s.get_role(variables.chessRoleID)
	bot.krunkerRole = s.get_role(variables.krunkerRoleID)
	bot.minecraftRole = s.get_role(variables.minecraftRoleID)
	bot.skribblRole = s.get_role(variables.skribblRoleID)
	bot.valorantRole = s.get_role(variables.valorantRoleID)

	bot.dividerThreeRole = s.get_role(variables.dividerThreeRoleID)
	bot.counterRookieRole = s.get_role(variables.counterRookieRoleID)
	bot.counterBronzeRole = s.get_role(variables.counterBronzeRoleID)
	bot.counterSilverRole = s.get_role(variables.counterSilverRoleID)
	bot.counterGoldRole = s.get_role(variables.counterGoldRoleID)
	bot.counterPlatinumRole = s.get_role(variables.counterPlatinumRoleID)
	bot.counterDiamondRole = s.get_role(variables.counterDiamondRoleID)
	bot.counterEmeraldRole = s.get_role(variables.counterEmeraldRoleID)

	bot.amongUsEmoji = bot.get_emoji(variables.amongUsEmojiID)
	bot.chessEmoji = bot.get_emoji(variables.chessEmojiID)
	bot.krunkerEmoji = bot.get_emoji(variables.krunkerEmojiID)
	bot.minecraftEmoji = bot.get_emoji(variables.minecraftEmojiID)
	bot.skribblEmoji = bot.get_emoji(variables.skribblEmojiID)
	bot.valorantEmoji = bot.get_emoji(variables.valorantEmojiID)
	bot.loadingEmoji = bot.get_emoji(variables.loadingEmojiID)
	bot.errorEmoji = bot.get_emoji(variables.errorEmojiID)
	bot.checkmarkEmoji = bot.get_emoji(variables.checkmarkEmojiID)
	bot.plusEmoji = bot.get_emoji(variables.plusEmojiID)
	bot.minusEmoji = bot.get_emoji(variables.minusEmojiID)

	bot.brainEmoji = bot.get_emoji(variables.brainEmojiID)
	bot.bellEmoji = bot.get_emoji(variables.bellEmojiID)
	bot.oneEmoji = bot.get_emoji(variables.oneEmojiID)
	bot.twoEmoji = bot.get_emoji(variables.twoEmojiID)
	bot.threeEmoji = bot.get_emoji(variables.threeEmojiID)
	bot.fourEmoji = bot.get_emoji(variables.fourEmojiID)
	bot.fiveEmoji = bot.get_emoji(variables.fiveEmojiID)
	bot.sixEmoji = bot.get_emoji(variables.sixEmojiID)
	bot.sevenEmoji = bot.get_emoji(variables.sevenEmojiID)
	bot.eightEmoji = bot.get_emoji(variables.eightEmojiID)
	bot.nineEmoji = bot.get_emoji(variables.nineEmojiID)
	bot.tenEmoji = bot.get_emoji(variables.tenEmojiID)

	bot.schoolRRDict = {variables.brainEmojiID: bot.helpRole, variables.bellEmojiID: bot.bellScheduleRole, variables.oneEmojiID: bot.precalculusRole, variables.twoEmojiID: bot.apCalcABRole, variables.threeEmojiID: bot.apCalcBCRole, variables.fourEmojiID: bot.hPhysicsRole, variables.fiveEmojiID: bot.apPhysicsRole, variables.sixEmojiID: bot.apBiologyRole, variables.sevenEmojiID: bot.rushRole, variables.eightEmojiID: bot.apushRole, variables.nineEmojiID: bot.vsNetRole, variables.tenEmojiID: bot.apcsRole}

	bot.gameRRDict = {variables.amongUsEmojiID: bot.amongUsRole, variables.chessEmojiID: bot.chessRole, variables.krunkerEmojiID: bot.krunkerRole, variables.minecraftEmojiID: bot.minecraftRole, variables.skribblEmojiID: bot.skribblRole, variables.valorantEmojiID: bot.valorantRole}
	bot.categoryDB = requests.get("https://opentdb.com/api_category.php").json()

	bot.monTimes = {"08:10 AM": "A", "08:40 AM": "Passing", "08:45 AM": "1", "09:15 AM": ":Passing","09:20 AM": "2", "09:50 AM": "Passing", "09:55 AM": "3", "10:25 AM": "Passing", "10:30 AM": "4", "11:00 AM": "Lunch", "11:30 AM": "Passing", "11:35 AM": "5", "12:05 PM": "Passing", "12:10 PM": "6"}
	bot.tuesThursTimes = {"09:35 AM": "1", "10:50 AM": "Passing", "11:05 AM": "3", "12:20 PM": "Lunch", "12:55 PM": "Passing", "01:05 PM": "5", "02:20 PM": "Passing", "02:30 PM": "Student Support"}
	bot.wedFriTimes = {"08:10 AM": "A", "09:25 AM": "Passing", "09:35 AM": "2", "10:50 AM": "Passing", "11:05 AM": "4", "12:20 PM": "Lunch", "12:55 PM": "Passing", "01:05 PM": "6", "02:20 PM": "Passing", "02:30 PM": "Student Support"}
	bot.daySchedule = {1: bot.monTimes, 2: bot.tuesThursTimes, 3: bot.wedFriTimes, 4: bot.tuesThursTimes, 5: bot.wedFriTimes}

	bot.monTimesMinutes = {}
	bot.tuesThursTimesMinutes = {}
	bot.wedFriTimesMinutes = {}

  # stringTime = time.strftime("%I:%M %p")
	for i in bot.monTimes:
		bot.monTimesMinutes[datetime.strptime(i, "%I:%M %p")] = bot.monTimes[i]
	for i in bot.tuesThursTimes:
		bot.tuesThursTimesMinutes[datetime.strptime(i, "%I:%M %p")] = bot.tuesThursTimes[i]
	for i in bot.wedFriTimes:
		bot.wedFriTimesMinutes[datetime.strptime(i, "%I:%M %p")] = bot.wedFriTimes[i]
	bot.dayScheduleMinutes = {1: bot.monTimesMinutes, 2: bot.tuesThursTimesMinutes, 3: bot.wedFriTimesMinutes, 4: bot.tuesThursTimesMinutes, 5: bot.wedFriTimesMinutes}
	


# def leaderboardTask():
# 	url = 'https://mee6.xyz/leaderboard/612059384721440789'
# 	page = requests.get(url)
# 	soup = BeautifulSoup(page.text.replace("</script\n", "</script>"), 'html.parser')
# 	results = soup.find(class_ = "leaderboardPlayersListContainer")
	
# 	usernames = results.find_all(class_ = "leaderboardPlayerUsername")
# 	usernamesList = []
# 	for i in range (0, 10):
# 		usernamesList.append(usernames[i].text.strip())

# 	levels = results.find_all(class_ = "leaderboardPlayerStatText")
# 	levelsList = []
# 	for i in range (0, 10):
# 		levelsList.append(levels[i].text.strip())

# 	return [usernamesList, levelsList]

# counts humans or bots in the server

def botOwner(ctx):
	return ctx.author.id == 410590963379994639

def staff(ctx):
	staff = [bot.adminRole, bot.moderatorRole]
	return any(role in ctx.author.roles for role in staff)

def userCount(userType: int):
	if userType == 1:
		humanCount = 0
		for member in bot.server.members:
			if not member.bot:
				humanCount += 1
		return humanCount
	else:
		botCount = 0
		for member in bot.server.members:
			if member.bot:
				botCount += 1
		return botCount

async def updateStatus():
	await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{userCount(1)} Members • !help"))

# bot startup event
@bot.event
async def on_ready():
	print(discord.__version__)
	await assignments()
	await bot.server.get_member(410590963379994639).send("Online")
	bellSchedule.start()
	bot.startTime = datetime.now()
	await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{userCount(1)} Members • !help"))
	# await bot.change_presence(activity = discord.Streaming(name = "Onlyfanz", url = "https://bit.ly/3lH4oSp"))
	print(f"""
  _______ _            ____        _   _           
 |__   __| |          |  _ \      | | | |          
    | |  | |__   ___  | |_) |_   _| |_| | ___ _ __ 
    | |  | '_ \ / _ \ |  _ <| | | | __| |/ _ \ '__|
    | |  | | | |  __/ | |_) | |_| | |_| |  __/ |   
    |_|  |_| |_|\___| |____/ \__,_|\__|_|\___|_|""")

	subjectRolesMessage = await bot.rolesChannel.fetch_message(759521601170833469)
	embed = discord.Embed(title = "School Roles :books:", description = f"Pick up some roles for any subjects you take! \n\n:brain: {bot.helpRole.mention} \nto help anyone in immediate need \n:bell: {bot.bellScheduleRole.mention} \nto receive bell schedule pings \n\n:one: {bot.precalculusRole.mention} \n:two: {bot.apCalcABRole.mention} \n:three: {bot.apCalcBCRole.mention} \n:four: {bot.hPhysicsRole.mention} \n:five: {bot.apPhysicsRole.mention} \n:six: {bot.apBiologyRole.mention} \n:seven: {bot.rushRole.mention} \n:eight: {bot.apushRole.mention} \n:nine: {bot.vsNetRole.mention} \n:keycap_ten: {bot.apcsRole.mention}", color = 0xFFFFFE)
	embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	await subjectRolesMessage.edit(embed = embed)

	gameRolesMessage = await bot.rolesChannel.fetch_message(759534246607585300)
	embed = discord.Embed(title = "Game Roles :video_game:", description = f"""Pick up some roles for any games you play! 
	
	{bot.amongUsEmoji} {bot.amongUsRole.mention} 
	{bot.chessEmoji} {bot.chessRole.mention} 
	{bot.krunkerEmoji} {bot.krunkerRole.mention} 
	{bot.minecraftEmoji} {bot.minecraftRole.mention} 
	{bot.skribblEmoji} {bot.skribblRole.mention} 
	{bot.valorantEmoji} {bot.valorantRole.mention}""", color = 0xFFFFFE)
	embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	await gameRolesMessage.edit(embed = embed)

	rulesMessage = await bot.rulesChannel.fetch_message(790036264648441897)
	embed = discord.Embed(title = "Rules :scroll:", color = 0xFFFFFE)
	embed.set_footer(text = "Server Rules", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	embed.add_field(name = "Common Sense", value = f"""
• no self promo
• follow [Discord TOS](https://discord.com/terms)
• do not diss <@533153734373539840>
• have some [common sense](https://youtu.be/YSDTPPM9qsc)
• avoid being blatantly offensive
• no annoying/unnecessary pinging
• respect da staff cuz they're kinda hot
• don't be an asshole/annoying person
• use the right channel for your topic of discussion
• no nsfw or crazy spamming (except in <#777040210005065739>)
• arguing is allowed, but if it gets too spicy, go to <#744374005280276522>""", inline = False)
	embed.add_field(name = "More Info", value = f"""
• run `!help` to see server commands
• staff can mute you at their discretion
• ignorance of the rules above is not a valid excuse
• bans and kicks generally happen after discussion in {bot.generalChannel.mention}
• rules for the **minecraft servers** are pinned (<#659885014603005953> & <#693321555366903851>)""", inline = False)
	await rulesMessage.edit(embed = embed)

	channelsMessage1 = await bot.channelsChannel.fetch_message(790467696860594207)
	embed = discord.Embed(title = "Channels :computer:", description = "ayo wtf are these channels for??", color = 0xFFFFFE)
	embed.set_footer(text = "Server Channels", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	embed.add_field(name = "Text Channels", value = f"""
• {bot.welcomeChannel.mention} user welcome and adios messages
• {bot.rolesChannel.mention} reaction roles 
• {bot.rulesChannel.mention} the constitution
• {bot.channelsChannel.mention} info on all channels
• <#635302492132999168> announcements and updates
• <#732997653394227220> suggestions posted with `s!suggest <suggestion>`
• <#745337266943164446> messages with four or more :star: reactions
• {bot.generalChannel.mention} communicate with other idiots
• <#612384531999096832> play some bangers with <@630199558294470676>""", inline = False)
	await channelsMessage1.edit(embed = embed)

	channelsMessage2 = await bot.channelsChannel.fetch_message(790467697841274890)
	embed = discord.Embed(title = "Channels :computer:", color = 0xFFFFFE)
	embed.set_footer(text = "Server Channels", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	embed.add_field(name = "Text Channels Continued...", value = f"""
• <#744374005280276522> verbally duel with another person
• <#744374515328614421> weeb territory
• <#777040210005065739> in the name, just don't be mad weird when it comes to nsfw
• <#700074631935295532> academic related discussion
• <#690647361139245136> count till the end of time and space
• <#746951407546007643> auto-posted {bot.amongUsEmoji}, {bot.chessEmoji}, and {bot.krunkerEmoji} join codes/links
• <#636071901906731010> use all bots
• <#659885014603005953> minecraft creative world chat
• <#693321555366903851> minecraft survival world chat""", inline = False)
	await channelsMessage2.edit(embed = embed)
	
	# await gameRolesMessage.add_reaction(bot.amongUsEmoji)
	# await gameRolesMessage.add_reaction(bot.chessEmoji)
	# await gameRolesMessage.add_reaction(bot.krunkerEmoji)
	# await gameRolesMessage.add_reaction(bot.minecraftEmoji)
	# await gameRolesMessage.add_reaction(bot.skribblEmoji)
	# await gameRolesMessage.add_reaction(bot.valorantEmoji)

	# await subjectRolesMessage.add_reaction("\U0001f9e0")
	# await subjectRolesMessage.add_reaction("\U0001f514")
	# await subjectRolesMessage.add_reaction("\U00000031\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000032\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000033\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000034\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000035\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000036\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000037\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000038\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U00000039\U0000fe0f\U000020e3")
	# await subjectRolesMessage.add_reaction("\U0001f51f")

	for i in muteDatabase:
		ids = i["id"].split(" ")
		server = bot.get_guild(int(ids[1]))
		member = bot.server.get_member(int(ids[0]))

		if bot.mutedRole in member.roles:
			await member.remove_roles(bot.mutedRole)
			await member.add_roles(bot.memberRole)

		muteDatabase.remove(query.id == (str(member.id) + " " + str(server.id)))

		generalChannel = bot.get_channel(variables.generalChannelID)
		embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention} was unmuted on bot startup", color = 0x00FF00, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Unmuted by {bot.user}", icon_url = bot.user.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await generalChannel.send(embed = embed)

		print(f"{bot.eventLabel} Unmuted (Automatic)")

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def eval(ctx, code):
# 	if ctx.author.id == 410590963379994639:
# 		def evaluate(code):
# 			return exec(code)
# 		await ctx.send(evaluate())
		

# 	else:
# 		await ctx.send(f"{bot.errorEmoji} You do not have access to this command")

@bot.command()
@commands.cooldown(1, 15, BucketType.user) 
async def weather(ctx, *, city = None):
	await ctx.trigger_typing()
	message = await ctx.send(f"{bot.loadingEmoji} Loading...")
	if not city:
		city = "San Ramon"
	apiKey = "e83935ef7ce7823925eeb0bfd2db3f7f"
	apiURL = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + apiKey + "&q=" + city
	reply = requests.get(apiURL)
	weatherDatabase = reply.json()
	if weatherDatabase["cod"] == "404":
		await message.edit(content = f"{bot.errorEmoji} Invalid city")
	else:
		sunrise = datetime.fromtimestamp(int(weatherDatabase["sys"]["sunrise"])) - timedelta(hours = 8)
		sunset = datetime.fromtimestamp(int(weatherDatabase["sys"]["sunset"])) - timedelta(hours = 8)
		embed = discord.Embed(title = ":partly_sunny: Weather", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = f"https://openweathermap.org/img/wn/{weatherDatabase['weather'][0]['icon']}@4x.png")
		embed.add_field(name = "City", value = f"`{weatherDatabase['name']}`, `{weatherDatabase['sys']['country']}`", inline = True)
		embed.add_field(name = "Condition", value = f"`{(weatherDatabase['weather'][0]['description']).title()}`", inline = True)
		embed.add_field(name = "Cloudiness", value = f"`{weatherDatabase['clouds']['all']}`%", inline = True)
		embed.add_field(name = "Temperature", value = f"`{round((1.8 * ((weatherDatabase['main']['temp']) - 273.15)) + 32)}`°F", inline = True)
		embed.add_field(name = "Humidity", value = f"`{weatherDatabase['main']['humidity']}`%", inline = True)
		embed.add_field(name = "Wind", value = f"`{round((weatherDatabase['wind']['speed'] * 2.24), 1)}`mph `{portolan.abbr(degree = weatherDatabase['wind']['deg'])}`", inline = True)
		embed.add_field(name = "Sunrise", value = f"{sunrise.strftime('`%I`:`%M` `%p`')} PST", inline = True)
		embed.add_field(name = "Sunset", value = f"{sunset.strftime('`%I`:`%M` `%p`')} PST", inline = True)
		await message.edit(content = None, embed = embed)
		print(f"{bot.commandLabel} Weather")

@bot.command()
@commands.cooldown(1, 15, BucketType.user) 
async def joke(ctx):
	await ctx.trigger_typing()
	message = await ctx.send(f"{bot.loadingEmoji} Loading...")
	apiURL = "https://official-joke-api.appspot.com/jokes/random"
	reply = requests.get(apiURL)
	jokeDatabase = reply.json()
	embed = discord.Embed(title = ":book: A joke", description = f"**{jokeDatabase['setup']}**", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await message.edit(content = None, embed = embed)
	embed = discord.Embed(title = ":book: A joke", description = f"**{jokeDatabase['setup']}**\n{jokeDatabase['punchline']}", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await asyncio.sleep(2)
	await message.edit(content = None, embed = embed)
	print(f"{bot.commandLabel} Joke")

@bot.command()
@commands.cooldown(1, 15, BucketType.user) 
async def fact(ctx):
	await ctx.trigger_typing()
	message = await ctx.send(f"{bot.loadingEmoji} Loading...")
	apiURL = "https://uselessfacts.jsph.pl/random.json?language=en"
	reply = requests.get(apiURL)
	factDatabase = reply.json()
	embed = discord.Embed(title = ":book: A useless fact", description = f"{factDatabase['text']}", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await message.edit(content = None, embed = embed)
	print(f"{bot.commandLabel} Fact")


# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def shorten(ctx, *, URL: str):
# 	await ctx.trigger_typing()
# 	message = await ctx.send(f"{bot.loadingEmoji} Shortening URL...")
# 	tokensPool = "a9c21c045c5d62380a54a7d3a22b06d8e6396c1c"
# 	shortener = bitlyshortener.Shortener(token = tokensPool, max_cache = 256)
# 	URLs = [URL]
# 	shortenedURL = shortener.shorten_urls(URLs)
# 	print(shortenedURL)
# 	embed = discord.Embed(title = ":link: Shortened Link", description = shortenedURL[0], color = 0xFFFFFE, timestamp = datetime.utcnow())
# 	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = bot.user.avatar_url)
# 	embed.set_thumbnail(url = "https://i.imgur.com/YmjXC7s.png")
# 	await message.edit(content = None, embed = embed)

@tasks.loop(minutes = 1)
async def bellSchedule():
	timezone = pytz.timezone("America/Los_Angeles")
	time = datetime.now(timezone)
	stringTime = time.strftime("%I:%M %p")
	# adjust day if schedule is off
	day = time.isoweekday()
	if day in bot.daySchedule:
		if stringTime in bot.daySchedule[day]:
			output = ""
			ping = False
			if "Passing" in bot.daySchedule[day][stringTime]:
				output = ":dividers: "
			elif "Lunch" in bot.daySchedule[day][stringTime]:
				output = ":dividers: "
			elif "Student Support" in bot.daySchedule[day][stringTime]:
				output = ":jigsaw: "
				ping  = True
			else:
				output = "Period "
				ping = True
			embed = discord.Embed(title = "<a:rotatingHourglass:817538734597341235> Reminder", description = output + f"`{bot.daySchedule[day][stringTime]}` starts in 5 minutes!", color = 0xFFFFFE, timestamp = datetime.utcnow())
			embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
			embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
			if ping:
				await bot.generalChannel.send(bot.bellScheduleRole.mention, embed = embed)
				return
			await bot.generalChannel.send(embed = embed)

@bot.command(aliases = ["minsleft", "bruh"])
@commands.check(botOwner)
@commands.cooldown(1, 5, BucketType.user) 
async def left(ctx):
	# time.strftime("%I:%M %p")
	def timeInMinutes(datetimeObject):
		return (int(datetimeObject.strftime("%H")) * 60) + (int(datetimeObject.strftime("%M")))
	timezone = pytz.timezone("America/Los_Angeles")
	current = datetime.now(timezone)
	currentMinutes = timeInMinutes(current)
	# adjust day if schedule is off
	day = current.isoweekday()
	inSession = False
	minutesLeft = 0
	currentPeriod = ""
	if day in bot.daySchedule:
		if day == 1 and 495 <= currentMinutes <= 765:
			inSession = True
			for i in bot.monTimesMinutes:
				if i > currentMinutes:
					minutesLeft = timeInMinutes(i) - currentMinutes
					currentPeriod = bot.monTimesMinutes[i]
					break
		elif day != 1 and 495 <= currentMinutes <= 915:
			inSession = True
			for i in bot.dayScheduleMinutes[day]:
				if i > currentMinutes:
					minutesLeft = timeInMinutes(i) - currentMinutes
					currentPeriod = bot.dayScheduleMinutes[day][i]
					break
	if inSession:
		embed = discord.Embed(title = "<a:rotatingHourglass:817538734597341235> Time Left", description = f"{currentPeriod} has `{minutesLeft}` minutes left!", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
		await ctx.send(embed = embed)
	else:
		await ctx.send(f"{bot.errorEmoji} School is currently not in session")
		print(f"{bot.commandLabel} MLeft")

# reaction roles (add)
@bot.event
async def on_raw_reaction_add(payload):
	if payload.message_id == 759521601170833469:
		await payload.member.add_roles(bot.schoolRRDict[str(payload.emoji.name)], bot.dividerOneRole)
		await payload.member.send(f"{bot.plusEmoji} Added the **{bot.schoolRRDict[str(payload.emoji.name)].name}** role")
		print(f"{bot.eventLabel} Reaction Role (Added Role)")
	
	if payload.message_id == 759534246607585300:
		await payload.member.add_roles(bot.gameRRDict[payload.emoji.id], bot.dividerTwoRole)
		await payload.member.send(f"{bot.plusEmoji} Added the **{bot.gameRRDict[payload.emoji.id].name}** role")
		print(f"{bot.eventLabel} Reaction Role (Added Role)")

# reaction roles (remove)
@bot.event
async def on_raw_reaction_remove(payload):
	member = bot.server.get_member(payload.user_id)
	if payload.message_id == 759521601170833469:
		await member.remove_roles(bot.schoolRRDict[str(payload.emoji.name)])
		await member.send(f"{bot.minusEmoji} Removed the **{bot.schoolRRDict[str(payload.emoji.name)].name}** role")
		print(f"{bot.eventLabel} Reaction Role (Removed Role)")
	
	if payload.message_id == 759534246607585300:
		await member.remove_roles(bot.gameRRDict[payload.emoji.id])
		await member.send(f"{bot.minusEmoji} Removed the **{bot.gameRRDict[payload.emoji.id].name}** role")
		print(f"{bot.eventLabel} Reaction Role (Removed Role)")

# on member join event
@bot.event
async def on_member_join(member):
	if member.bot == False:
		await member.add_roles(bot.memberRole)
		await updateStatus()
		embed = discord.Embed(title = ":inbox_tray: Member Joined", description = f"You are the `{ordinal(userCount(1))}` member!", color = 0x00FF00, timestamp = datetime.utcnow())
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		embed.add_field(name = "Get Roles", value = f"Go to {bot.rolesChannel.mention}", inline = False)
		embed.add_field(name = "Main Info :loudspeaker:", value = f"Read the {bot.rulesChannel.mention}\nRead the {bot.channelsChannel.mention} info\nJoin the talk in {bot.generalChannel.mention}", inline = False)
		await bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
		await member.remove_roles(bot.mutedRole)

	else:
		await member.add_roles(bot.botRole)
		embed = discord.Embed(title = ":inbox_tray: Bot Joined", description = f"You are the `{ordinal(userCount(2))}` member!\n{bot.botRole.mention} role added", color = 0x00FF00, timestamp = datetime.utcnow())
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		await bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
		print(f"{bot.eventLabel} Bot Joined")
		await member.remove_roles(bot.mutedRole)

# on member exit event
@bot.event
async def on_member_remove(member):
	if member.bot == False:
		await updateStatus()
		embed = discord.Embed(title = f":outbox_tray: Member Left", description = "Either kicked/banned/left", color = 0xFF0000, timestamp = datetime.utcnow())
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		await bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)
		print(f"{bot.eventLabel} Member Left")

	else:
		embed = discord.Embed(title = f":outbox_tray: Bot Left", description = "Either kicked/banned/left", color = 0xFF0000, timestamp = datetime.utcnow())
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		await bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)
		print(f"{bot.eventLabel} Bot Left")

@bot.event
async def on_message_delete(message):
	if message.author.bot == False and bot.memberRole in message.author.roles and message.channel.id != 690647361139245136 and bot.allahRole not in message.author.roles:
		embed = discord.Embed(title = ":wastebasket: Message Deleted", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = message.author.avatar_url)
		embed.add_field(name = "Author", value = message.author.mention, inline = True)
		embed.add_field(name = "Channel", value = message.channel.mention, inline = True)
		embed.add_field(name = "Content", value = message.content, inline = True)
		# if (message.attachments[0].size > 0):
		# 	embed.set_image(url = message.attachments[0].proxy_url)
		await bot.logChannel.send(embed = embed)
		print(f"{bot.eventLabel} Message Deleted")

@bot.event
async def on_message_edit(before, after):
	if before.author.bot == False and before.content != after.content and bot.memberRole in before.author.roles and before.channel.id != 690647361139245136:
		embed = discord.Embed(title = ":pencil: Message Edited", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = before.author.avatar_url)
		embed.add_field(name = "Author", value = before.author.mention, inline = True)
		embed.add_field(name = "Channel", value = before.channel.mention, inline = True)
		embed.add_field(name = "Message", value = f"[Jump!]({before.jump_url})", inline = True)
		embed.add_field(name = "Before", value = before.content, inline = True)
		embed.add_field(name = "After", value = after.content, inline = True)
		# if (message.attachments[0].size > 0):
		# 	embed.set_image(url = message.attachments[0].proxy_url)
		await bot.logChannel.send(embed = embed)
		print(f"{bot.eventLabel} Message Edited")

# on message sent event
@bot.event
async def on_message(message):
	# if bot.user.mentioned_in(message):
	# 	await message.channel.send("https://tenor.com/view/hell-no-bollywood-indian-hell-no-gif-5616245")

	if message.guild is None and message.author.id == 410590963379994639:
		await bot.generalChannel.send(message.content)
	
	if message.author.id == 320369001005842435:
		if message.channel.id == 700074631935295532:
			if "ask" in message.content.lower() or "punz" in message.content.lower():
				await message.delete()
	
	await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
	if str(before.activity).lower() == "streaming":
		await after.remove_roles(bot.liveOnTwitchRole)
	if str(after.activity).lower() == "streaming":
		await after.add_roles(bot.liveOnTwitchRole)

@bot.event
async def on_voice_state_update(member, before, after):
	if after.self_stream:
		await bot.logChannel.send(f":red_circle: `{member}` went live in `{after.channel.name}` VC")

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CheckFailure):
		await ctx.trigger_typing()
		await ctx.send(f"{bot.errorEmoji} Missing permissions")
	elif not isinstance(error, CommandNotFound):
		if isinstance(error, CommandOnCooldown):
			await ctx.trigger_typing()
			await ctx.send(f"{bot.errorEmoji} You are on cooldown for `{round(error.retry_after, 1)}` seconds")
		else:
			await ctx.trigger_typing()
			await ctx.send(f"```{error}```")
			if ctx.command:
				ctx.command.reset_cooldown(ctx)
	else:
		if not any(x in str(error) for x in ["\"ban\"", "\"kick\"", "\"levels\"", "\"rank\"", "\"slowmode\"", "\"warn\"", "\"unban\""]):
			await ctx.send(f"```{error}```")

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def top(ctx):
# 	await ctx.trigger_typing()
# 	data = leaderboardTask()
# 	embed = discord.Embed(title = "Leaderboard", color = 0xFFFFFE, timestamp = datetime.utcnow())
# 	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
# 	for i in range(0, 10):
# 		embed.add_field(name = f"{i+1}) {data[0][i]}", value = f"Level {data[1][i]}", inline = False)
# 	await ctx.send(embed = embed)

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user)
# async def react(ctx, character):
# 	for message in ctx.channel.history(limit = 2):
# 		if message != ctx.message:
# 			await ctx.channel.last_message.add_reaction(character)
# 			return

@bot.command(aliases = ["f", "race", "r"])
@commands.cooldown(1, 10, BucketType.user)
async def fast(ctx):
	await ctx.trigger_typing()
	original = await ctx.send(f"{bot.loadingEmoji} Loading...")
	choice = random.choice(["math", "word", "find"])

	# math
	if choice == "math":
		operation = random.choice(["×", "/", "+", "-"])
		numbers = []
		answer = 0
		if operation == "×":
			numbers = [random.randint(0, 20), random.randint(0, 20)]
			answer = numbers[0] * numbers[1]
		elif operation == "/":
			denominator = random.randint(1, 20)
			answer = random.randint(1, 20)
			numbers = [denominator * answer, denominator]
		
		elif operation == "+":
			numbers = [random.randint(50, 100), random.randint(50, 100)]
			answer = numbers[0] + numbers[1]
		else:
			numbers = [random.randint(50, 100), random.randint(50, 100)]
			if numbers[0] < numbers[1]:
				numbers[0], numbers[1] = numbers[1], numbers[0]
			answer = numbers[0] - numbers[1]
		
		embed = discord.Embed(title = ":zap: Math Showdown", description = f"First to solve the following wins!\n```py\n{numbers[0]} {operation} {numbers[1]}```", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		await original.edit(content = None, embed = embed)
		
		def check(message):
			return message.content == str(int(answer)) and message.channel == ctx.channel
		try:
			message = await bot.wait_for("message", timeout = 15, check = check)
		except asyncio.TimeoutError:
			await original.edit(content = f"{bot.errorEmoji} Event has expired", embed = None)
		else:
			await message.add_reaction(bot.checkmarkEmoji)
			await ctx.send(f"{message.author.mention} wins!")
	
	# word
	elif choice == "word":
		apiURL = "https://random-word-api.herokuapp.com/word?number=1"
		reply = requests.get(apiURL)
		wordDB = reply.json()
		embed = discord.Embed(title = ":zap: Word Showdown", description = f"First to type the following backwards wins!\n```yaml\n{wordDB[0]}```", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		await original.edit(content = None, embed = embed)
		def check(message):
			return message.content == (wordDB[0])[::-1] and message.channel == ctx.channel
		try:
			message = await bot.wait_for("message", timeout = 15, check = check)
		except asyncio.TimeoutError:
			await original.edit(content = f"{bot.errorEmoji} Event has expired", embed = None)
		else:
			await message.add_reaction(bot.checkmarkEmoji)
			await ctx.send(f"{message.author.mention} wins!")
	
	# find
	else:
		wrong, right = random.choice(bot.emojis), random.choice(bot.emojis)
		table = [[wrong, wrong, wrong], [wrong, wrong, wrong], [wrong, wrong, wrong]]
		row, column = random.randint(0, 2), random.randint(0, 2)
		table[row][column] = right
		rowPH = ["A", "B", "C"]
		printedTable = "⠀⠀`1`⠀`2`⠀`3`\n"
		for i in range(0, 3):
			printedTable += f"`{rowPH[i]}` "
			for j in range(0, 3):
				printedTable += f"||{table[i][j]}|| "
			printedTable += "\n"
		answer = (rowPH[row] + str(column + 1)).lower()
		embed = discord.Embed(title = ":zap: Bubble Wrap", description = f"First to type the location to {right} wins!\n(ex: `B2` or `2B`)\n\n{printedTable}", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		await original.edit(content = None, embed = embed)
		def check(message):
			return message.content.lower() in [answer, answer[::-1]] and message.channel == ctx.channel
		try:
			message = await bot.wait_for("message", timeout = 15, check = check)
		except asyncio.TimeoutError:
			await original.edit(content = f"{bot.errorEmoji} Event has expired", embed = None)
		else:
			await message.add_reaction(bot.checkmarkEmoji)
			await ctx.send(f"{message.author.mention} wins!")


# @bot.command(aliases = ["cs"])
# @commands.cooldown(1, 5, BucketType.user)
# async def categories(ctx):
# 	output = ""
# 	for i in range (0, 24):
# 		output += f"`{bot.categoryDB['trivia_categories'][i]['id'] - 8}` {bot.categoryDB['trivia_categories'][i]['name']}\n"
# 	thinkList = ["<:thinkVivan:801531613082025995>", ":thinking:", "<:swaggerThink:809281292557746176>", "<:redThink:700463049013723136>", "<:breadThink:700463049852715048>"]
# 	embed = discord.Embed(title = f"{random.choice(thinkList)} Trivia Categories", description = f"These are all the category codes\nAn empty argument will generate a random category/difficulty\n`!trivia [category] [difficulty]`\n\n{output}", color = 0xFFFFFE, timestamp = datetime.utcnow())
# 	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
# 	await ctx.author.send(embed = embed)
# 	await ctx.send(f"{bot.checkmarkEmoji} Sent in direct messages")

# @bot.command()
# @commands.cooldown(1, 10, BucketType.user)
# async def rr(ctx):
# 	if ctx.author.id == 410590963379994639:
# 		message = await ctx.send("react to this message with anything to play russian roulette\none person is randomly muted\nneeds 4 ppl to activate")
# 		await message.add_reaction(bot.checkmarkEmoji)
# 		def check(reaction, user):
# 			return len(message.reactions) == 4
# 		try:
# 			reaction, user = await bot.wait_for("reaction_add", timeout = 15, check = check)
# 		except asyncio.TimeoutError:
# 			await message.edit(content = "not enough ppl reacted")
# 		else:
# 			allMembers = []
# 			for reaction in message.reactions:
# 				for user in reaction.users:
# 					allMembers.append(user.mention)
# 			mute(ctx, random.choice(random.choice(allMembers)), 1)

# 	else:
# 		await ctx.send("in testing")

@bot.command()
@commands.cooldown(1, 5, BucketType.user)
async def color(ctx, hexCode: discord.Color):
	embed = discord.Embed(title = ":trackball: Color Search", description = str(hexCode).lower(), color = hexCode, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = f"https://www.colorhexa.com/{str(hexCode).lower()[1:]}.png")
	await ctx.send(embed = embed)

@bot.command(aliases = ["roast", "insultme", "insult"])
@commands.cooldown(1, 10, BucketType.user)
async def roastme(ctx):
	await ctx.trigger_typing()
	message = await ctx.send(f"{bot.loadingEmoji} Loading...")
	apiURL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
	reply = requests.get(apiURL)
	roastDatabase = reply.json()
	embed = discord.Embed(title = ":pensive: An insult", description = roastDatabase["insult"], color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await message.edit(content = None, embed = embed)

@bot.command(aliases = [])
@commands.check(botOwner)
@commands.cooldown(1, 5, BucketType.user)
async def say(ctx, message):
	webhook = Webhook.partial(819665087929384990, "9xk511gc17f5c0-Ux9rhaY9P2C8VoQCGcJ4XYGGrKGQ-qzhE_s5vWxCEOkp8mRM28AKI", adapter = RequestsWebhookAdapter())
	webhook.send(message)

@bot.command(aliases = ["lb", "top", "^"])
@commands.cooldown(1, 10, BucketType.user)
async def leaderboard(ctx):
	with open("points.json", "r") as file:
		data = json.load(file)
		data = dict(sorted(data.items(), key = lambda item: item[1]))
		print
		data = dict(reversed(list(data.items())))
		outputArr = []
		for i in data:
			noun = "points"
			if data[i] == 1:
				noun = "point"
			if ctx.author.id == int(i):
				outputArr.append(f"<@{i}> (`{data[i]}` {noun}) :arrow_left::arrow_left::arrow_left:")
			else:
				outputArr.append(f"<@{i}> (`{data[i]}` {noun})")
		emoji = [":first_place:", ":second_place:", ":third_place:"]
		output = ""
		if len(outputArr) <= 15:
			for i in outputArr:
				if outputArr.index(i) <= 2:
					output += f"\n{emoji[outputArr.index(i)]}"
				else:
					output += f"\n**{ordinal(outputArr.index(i) + 1)}**"
				output += outputArr[outputArr.index(i)]
		else:
			for i in range(15):
				if outputArr.index(i) <= 2:
					output += f"\n{emoji[outputArr.index(i)]}"
				else:
					output += f"\n**{ordinal(i)}**"
				output += outputArr[outputArr.index(i)]
	
	embed = discord.Embed(title = ":trophy: Leaderboard", description = f"Top 15 of the `!trivia` command users\n{output}", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)


@bot.command(aliases = ["q", "question", "quiz", "t"])
@commands.cooldown(1, 20, BucketType.user)
async def trivia(ctx, difficulty: str = None):
	await ctx.trigger_typing()
	if ctx.channel.id != 636071901906731010:
		await ctx.send(f"{bot.errorEmoji} Man go to <#636071901906731010>")
		trivia.reset_cooldown(ctx)
		return

	message = await ctx.send(f"{bot.loadingEmoji} Loading...")
	if difficulty:
		if difficulty.startswith("e"):
			difficulty = "easy"
		elif difficulty.startswith("m"):
			difficulty = "medium"
		elif difficulty.startswith("h"):
			difficulty = "hard"
		else:
			await message.edit(content = f"{bot.errorEmoji} You can only choose an `easy`, `medium`, or `hard` question")
			trivia.reset_cooldown(ctx)
			return
	else:
		difficulty = random.choice(["easy", "medium", "hard"])
	
	apiURL = f"https://opentdb.com/api.php?amount=1&difficulty={difficulty}&type=multiple"
	reply = requests.get(apiURL)
	triviaDatabase = reply.json()
	category = html2text.html2text(triviaDatabase["results"][0]["category"]).replace("\n", "")
	question = html2text.html2text(triviaDatabase["results"][0]["question"]).replace("\n", "")		
	choices = [html2text.html2text(triviaDatabase["results"][0]["correct_answer"]).replace("\n", ""), 
	html2text.html2text(triviaDatabase["results"][0]["incorrect_answers"][0]).replace("\n", ""), 
	html2text.html2text(triviaDatabase["results"][0]["incorrect_answers"][1]).replace("\n", ""), 
	html2text.html2text(triviaDatabase["results"][0]["incorrect_answers"][2]).replace("\n", "")]
	# print(choices[0])
	random.shuffle(choices)
	correctIndex = choices.index(html2text.html2text(triviaDatabase["results"][0]["correct_answer"]).replace("\n", ""))
	reactionsList = ["🇦", "🇧", "🇨", "🇩"]

	embed = discord.Embed(title = "<a:lightbulb:819465502320623657> Trivia", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nreact with your answer within `10` seconds", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await message.edit(content = None, embed = embed)
	
	for i in reactionsList:
		await message.add_reaction(i)

	def check(reaction, user):
		return user == ctx.author and str(reaction.emoji) in reactionsList
	
	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = check)
	
	# question expired (10 seconds)
	except asyncio.TimeoutError:
		await message.clear_reactions()
		# points system
		diffPoints = {"easy": 1, "medium": 2, "hard": 3}
		with open("points.json", "r") as file:
			data = json.load(file)
			if str(ctx.author.id) in data:
				if data[str(ctx.author.id)] > diffPoints[difficulty]:
					data[str(ctx.author.id)] -= diffPoints[difficulty]
				else:
					data[str(ctx.author.id)] = 0
		with open("points.json", "w") as file:
			json.dump(data, file, indent = 2)
		
		reactionsList[correctIndex] = bot.checkmarkEmoji
		embed = discord.Embed(title = f":alarm_clock: Expired! (-{diffPoints[difficulty]} points)", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nview leaderboard with `!top`", color = 0xFF383E, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		await message.edit(content = None, embed = embed)
	
	else:
		await message.clear_reactions()
		# correct answer
		if reactionsList.index(str(reaction.emoji)) == correctIndex:
			# points system
			diffPoints = {"easy": 1, "medium": 2, "hard": 3}
			with open("points.json", "r") as file:
				data = json.load(file)
				if str(ctx.author.id) not in data:
					data[str(ctx.author.id)] = diffPoints[difficulty]
				else:
					data[str(ctx.author.id)] += diffPoints[difficulty]
			with open("points.json", "w") as file:
				json.dump(data, file, indent = 2)
			
			# embed
			reactionsList[correctIndex] = bot.checkmarkEmoji
			embed = discord.Embed(title = f"{bot.checkmarkEmoji} Correct! (+{diffPoints[difficulty]} points)", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nview leaderboard with `!top`", color = 0x3FB97C, timestamp = datetime.utcnow())
			embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
			await message.edit(content = None, embed = embed)
		
		# wrong answer
		else:
			# points system
			diffPoints = {"easy": 1, "medium": 2, "hard": 3}
			with open("points.json", "r") as file:
				data = json.load(file)
				if str(ctx.author.id) in data:
					if data[str(ctx.author.id)] > 0:
						data[str(ctx.author.id)] -= 1
					else:
						data[str(ctx.author.id)] = 0
					# if data[str(ctx.author.id)] > diffPoints[difficulty]:
					# 	data[str(ctx.author.id)] -= diffPoints[difficulty]
					# else:
					# 	data[str(ctx.author.id)] = 0
			with open("points.json", "w") as file:
				json.dump(data, file, indent = 2)
			
			# embed
			reactionsList[reactionsList.index(str(reaction.emoji))] = bot.errorEmoji
			reactionsList[correctIndex] = bot.checkmarkEmoji
			embed = discord.Embed(title = f"{bot.errorEmoji} Incorrect! (-1 point)", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nview leaderboard with `!top`", color = 0xFF383E, timestamp = datetime.utcnow())
			embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
			await message.edit(content = None, embed = embed)
		print(f"{bot.commandLabel} Trivia")


@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def test(ctx, username, password):
	if ctx.author.id == 410590963379994639:
		url = f"https://dvhs.schoolloop.com/mapi/login?version=3&devToken={uuid4()}&devOS=iPhone9,4&year={datetime.now().year}"
		result = requests.get(url, auth = HTTPBasicAuth(username, password))
		if result.status_code != 200:
			await ctx.send(result.text)
			return
		studentID = result.json().get("userID")
		url = f"https://dvhs.schoolloop.com/mapi/report_card?studentID={studentID}"
		result = requests.get(url, auth = HTTPBasicAuth(username, password))
		if result.status_code != 200:
			await ctx.send(result.text)
			return
		print(f"```json\n{result.json()}```")
	else:
		await ctx.send("no")

@bot.command(aliases = ["k"])
@commands.cooldown(1, 5, BucketType.user) 
async def krunker(ctx, link):
	if "krunker.io/?game=" in link:
		await ctx.message.delete()
		embed = discord.Embed(title = f"{bot.krunkerEmoji} Krunker Link", description = link, color = 0xFEB938, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Posted by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/699029209988726885.png?v=1")
		await bot.joinGameChannel.send(embed = embed)
		await ctx.send(f"{bot.checkmarkEmoji} Posted in {bot.joinGameChannel.mention}")
	else:
		await ctx.send(f"{bot.errorEmoji} Invalid link")
		print(f"{bot.commandLabel} Krunker")

# @bot.command()
# @commands.cooldown(1, 15, BucketType.user) 
# async def test(ctx):
# 	file  = discord.File(fp = "keepAlive.py", filename = "keepAlive.py")
# 	await ctx.send(file = file)

@bot.command(aliases = ["au"])
@commands.cooldown(1, 5, BucketType.user) 
async def amongus(ctx, code):
	if len(code) == 6 and not any(char.isdigit() for char in code):
		await ctx.message.delete()
		embed = discord.Embed(title = f"{bot.amongUsEmoji} Among Us Code", description = f"`{code}`", color = 0xF21717, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Posted by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/781258129329094666.png?v=1")
		await bot.joinGameChannel.send(embed = embed)
		await ctx.send(f"{bot.checkmarkEmoji} Posted in {bot.joinGameChannel.mention}")
	else:
		await ctx.send(f"{bot.errorEmoji} Invalid code")
		print(f"{bot.commandLabel} Among Us")

@bot.command(aliases = ["c"])
@commands.cooldown(1, 5, BucketType.user) 
async def chess(ctx, link):
	if "play.chess.com/" in link:
		await ctx.message.delete()
		embed = discord.Embed(title = f"{bot.chessEmoji} Among Us Code", description = link, color = 0xF21717, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Posted by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/781259278417395732.png?v=1")
		await bot.joinGameChannel.send(embed = embed)
		await ctx.send(f"{bot.checkmarkEmoji} Posted in {bot.joinGameChannel.mention}")
	else:
		await ctx.send(f"{bot.errorEmoji} Invalid link")
		print(f"{bot.commandLabel} Among Us")

# pfp command
@bot.command(aliases = ["avatar", "av"])
@commands.cooldown(1, 5, BucketType.user) 
async def pfp(ctx, member: discord.Member = None):
	await ctx.trigger_typing()
	member = ctx.author if not member else member
	embed = discord.Embed(title = ":frame_photo: Profile Picture", description = member.mention, color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = member.avatar_url)
	await ctx.send(embed = embed)

@bot.command()
@commands.cooldown(1, 15, BucketType.user) 
async def emojis(ctx):
	await ctx.trigger_typing()
	num = len(bot.server.emojis)/2
	firstHalf = ""
	for output in bot.server.emojis[:num]:
		firstHalf += str(output)
	embed = discord.Embed(title = ":small_red_triangle: Emojis (Page 1/2)", description = firstHalf, color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)
	await ctx.trigger_typing()
	secondHalf = ""
	for output in bot.server.emojis[num:]:
		firstHalf += str(output)
	embed = discord.Embed(title = ":small_red_triangle: Emojis (Page 2/2)", description = secondHalf, color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

@bot.command(aliases = ["s"])
@commands.cooldown(1, 5, BucketType.user) 
async def schedule(ctx):
	await ctx.trigger_typing()
	embed = discord.Embed(title = ":bell: DVHS Bell Schedule", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = "https://i.imgur.com/ES49tLo.jpg")
	await ctx.send(embed = embed)

@bot.command(aliases = ["nickname"])
@commands.cooldown(1, 5, BucketType.user) 
async def nick(ctx, *, nickname):
	await ctx.trigger_typing()
	if len(nickname) >= 1 and len(nickname) <= 32:
		await ctx.author.edit(nick = nickname)
		await ctx.send(f"{bot.checkmarkEmoji} Your nickname was set to `{nickname}`!")
	else:
		await ctx.send(f"{bot.errorEmoji} Nicknames can only be upto `32` characters long!")


# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def resetnicks(ctx):
# 	await ctx.trigger_typing()
# 	if bot.adminRole in ctx.author.roles:
# 		msg = await ctx.send(f"{bot.loadingEmoji} Hold up...")
# 		for member in bot.server.members:
# 			if member.bot is False and member.id != 410590963379994639:
# 				await member.edit(nick = member.name)
# 		await msg.edit(f"{bot.checkmarkEmoji} Done!")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")


@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def setstatus(ctx, *, argument):
	await ctx.trigger_typing()
	if ctx.author.id == 410590963379994639:
		if argument.lower() == "normal":
			await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{userCount(1)} Members • !help"))
			await ctx.send(f"{bot.checkmarkEmoji} Set!")
		else:
			await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = argument))
			await ctx.send(f"{bot.checkmarkEmoji} Set!")
		print(f"{bot.commandLabel} SetStatus")
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")


@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def kill(ctx):
	await ctx.trigger_typing()
	if ctx.author.id == 410590963379994639:
		await ctx.send(f"{bot.checkmarkEmoji} Ending process! (start manually in repl)")
		await bot.close()
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def randomperson(ctx):
	await ctx.trigger_typing()
	if ctx.author.id == 410590963379994639:
		await ctx.send(random.choice(bot.server.members).mention + " is the random person!")
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def pogga(ctx):
# 	await ctx.trigger_typing()
# 	if ctx.author.id == 410590963379994639:
# 		for member in bot.server.members:
# 			if member.bot == False:
# 				await member.send("<a:spinningToilet:775547013047648297> Happy New Years!")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def vc(ctx, argument):
# 	await ctx.trigger_typing()
# 	if bot.adminRole in ctx.author.roles or bot.moderatorRole in ctx.author.roles:
# 		channel = ctx.message.author.voice.channel
# 		if channel is not None:
# 			members = channel.members
# 			if argument.lower() == "mute":
# 				for member in members:
# 						await member.edit(mute = True)
# 				await ctx.send(f"{bot.checkmarkEmoji} Server Muted everyone in **{(channel.mention - "#")}**")
# 			if argument.lower() == "unmute":
# 				for member in members:
# 						await member.edit(mute = False)
# 						await ctx.send(f"{bot.checkmarkEmoji} Server Unmuted everyone in **{(channel.mention - "#")}**")
# 			else:
# 				await ctx.send(f"{bot.errorEmoji} Invalid Argument!")
# 		else:
# 			await ctx.send(f"{bot.errorEmoji} You have to be in a voice channel to use this command!")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

# dm command
@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def dm(ctx, member: discord.Member, *, message):
	await ctx.trigger_typing()
	if bot.vipRole in ctx.author.roles:
		await member.send(message + f"\n- from {ctx.author.mention}")
		await ctx.send(f"{bot.checkmarkEmoji} Sent!")
		print(f"{bot.commandLabel} DM")
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

@bot.command(aliases = ["servericon"])
@commands.cooldown(1, 5, BucketType.user) 
async def icon(ctx):
	embed = discord.Embed(title = ":frame_photo: Server Icon", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = bot.server.icon_url)
	await ctx.send(embed = embed)

@bot.command(aliases = ["hijab"])
@commands.cooldown(1, 5, BucketType.user) 
async def allah(ctx, member: discord.Member):
	await ctx.trigger_typing()
	allah = bot.server.get_role(736358205994696846)
	if (ctx.author.id == 320369001005842435 and allah in ctx.author.roles) or ctx.author.id == 410590963379994639:
		if len(allah.members) < 5:
			if allah not in member.roles:
				await member.add_roles(allah)
				await ctx.send(f"{member.mention} is now allah :pray:")
			else:
				await ctx.send("you retard they already allah :pray:")
		else:
			await ctx.send("there can only be 5 allahs at once :pray:")
	else:
		await ctx.send("shut up retard this is only for virajallah :pray:")

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def nomedia(ctx, member: discord.Member):
# 	if ctx.author.id == 410590963379994639:
# 		await ctx.channel.set_permissions(member, attach_files = False, embed_links = False, external_emojis = False)
# 		await ctx.send(f"{bot.checkmarkEmoji} Media perms gone, reduced to atoms")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} Missing permissions")

# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def media(ctx, member: discord.Member):
# 	if ctx.author.id == 410590963379994639:
# 		await ctx.channel.set_permissions(member, permissions = 0)
# 		await ctx.send(f"{bot.checkmarkEmoji} Media perms given bcak")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} Missing permissions")

@bot.command(aliases = ["unhijab"])
@commands.cooldown(1, 5, BucketType.user) 
async def unallah(ctx, member: discord.Member):
	await ctx.trigger_typing()
	allah = bot.server.get_role(736358205994696846)
	if (ctx.author.id == 320369001005842435 and allah in ctx.author.roles) or ctx.author.id == 410590963379994639:
		await member.remove_roles(allah)
		await ctx.send(f"{member.mention} is not allah anymore :angry:")
	else:
		await ctx.send("shut up retard this is only for virajallah :pray:")

@bot.command(aliases = ["hijabs"])
@commands.cooldown(1, 5, BucketType.user) 
async def allahs(ctx):
	await ctx.trigger_typing()
	allah = bot.server.get_role(736358205994696846)
	output = ""
	for member in allah.members:
		output += f"\n{member.mention}"
		if member.id == 320369001005842435:
			output += " :crown:"
	embed = discord.Embed(title = ":pray: Allahs", description = output, color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)
		

# profile command
@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def profile(ctx, member: discord.Member = None):
	await ctx.trigger_typing()
	member = ctx.author if not member else member
	roleCount = len([role for role in member.roles]) - 1
	# roleCount = len(roleCount) - 1
	joinPosition = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)

	if member.bot == False:
		# main role
		if bot.adminRole in member.roles:
			topRole = bot.adminRole.mention
			topColor = bot.adminRole.color
		elif bot.moderatorRole in member.roles:
			topRole = bot.moderatorRole.mention
			topColor = bot.moderatorRole.color
		elif bot.memberRole or bot.mutedRole in member.roles:
			topRole = bot.memberRole.mention
			topColor = bot.memberRole.color
		
		# divider roles
		if bot.dividerOneRole in member.roles:
			roleCount = roleCount - 1
		if bot.dividerTwoRole in member.roles:
			roleCount = roleCount - 1
		if bot.dividerThreeRole in member.roles:
			roleCount = roleCount - 1

		# counter roles
		if bot.counterRookieRole in member.roles:
			topCounterRole = bot.counterRookieRole.mention
		elif bot.counterBronzeRole in member.roles:
			topCounterRole = bot.counterBronzeRole.mention
		elif bot.counterSilverRole in member.roles:
			topCounterRole = bot.counterSilverRole.mention
		elif bot.counterGoldRole in member.roles:
			topCounterRole = bot.counterGoldRole.mention
		elif bot.counterPlatinumRole in member.roles:
			topCounterRole = bot.counterPlatinumRole.mention
		elif bot.counterDiamondRole in member.roles:
			topCounterRole = bot.counterDiamondRole.mention
		elif bot.counterEmeraldRole in member.roles:
			topCounterRole = bot.counterEmeraldRole.mention
		else:
			topCounterRole = "`None`"

		# gameRoles = [bot.krunkerRole, bot.minecraftRole, bot.valorantRole, bot.amongUsRole]
		
		# output = ""
		# for i in gameRoles:
		#		 if i in member.roles:
		#				 output += gameRoles[i].mention
		# gameRoles = ""
		
		# if bot.krunkerRole in member.roles:
		#		 gameRoles += f"\n{bot.krunkerRole.mention}"
		
		# if bot.minecraftRole in member.roles:
		#		 gameRoles += f"\n{bot.minecraftRole.mention}"

		# if bot.valorantRole in member.roles:
		#		 gameRoles += f"\n{bot.valorantRole.mention}"
		
		# if bot.amongUsRole in member.roles:
		#		 gameRoles += f"\n{bot.amongUsRole.mention}"

		# else:
		#		 gameRoles = "`None`"

		embed = discord.Embed(title=f":bust_in_silhouette: User Profile", description = f"`{member}`", color = topColor, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		embed.add_field(name = "Main Role", value = topRole, inline = True)
		embed.add_field(name = "Nickname", value = member.mention, inline = True)
		embed.add_field(name = "Role Count", value = f"`{roleCount}`", inline = True)
		embed.add_field(name = "Join Position", value = f"#`{joinPosition}`/`{len(bot.users)}`", inline = True)
		embed.add_field(name = "Top Countr Role", value = topCounterRole, inline = True)
		embed.add_field(name = "Game Roles", value = "Under Dev", inline = True)
		embed.add_field(name = "Account Creation", value = f"{member.created_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
		embed.add_field(name = "Server Joined", value = f"{member.joined_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
		await ctx.send(embed = embed)

		print(f"{bot.commandLabel} Member Profile")

	if member.bot == True:
		embed = discord.Embed(title=f":robot: Bot Profile", description = f"`{member}`", color = member.color, timestamp = datetime.utcnow())
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		embed.add_field(name = "Main Role", value = "<@&637083530555555846>", inline = True)
		embed.add_field(name = "Nickname", value = member.mention, inline = True)
		embed.add_field(name = "Role Count", value = f"`{roleCount}`", inline = True)
		embed.add_field(name = "Join Position", value = f"#`{joinPosition}` (out of `{len(bot.users)}`)", inline = True)
		embed.add_field(name = "Account Creation", value = f"{member.created_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
		embed.add_field(name = "Server Joined", value = f"{member.joined_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
		await ctx.send(embed = embed)
		print(f"{bot.commandLabel} Bot Profile")

@bot.command(aliases = ["silenced", "banished"])
@commands.cooldown(1, 5, BucketType.user) 
async def muted(ctx):
	output = ""
	if len(muteDatabase.all()) == 0:
		output = "None"
	else:
		for mute in muteDatabase.all():
			id = int(mute["id"].split()[0])
			output += bot.get_user(id).mention + "\n"
	
	embed = discord.Embed(title = ":mute: Muted", description = f"{output}", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} Muted")

# predict command
@bot.command(aliases = ["8ball"])
@commands.cooldown(1, 15, BucketType.user) 
async def predict(ctx, *, question: str):
	await ctx.trigger_typing()
	message = await ctx.send(f"{bot.loadingEmoji} Loading...")
	apiURL = "https://8ball.delegator.com/magic/JSON/" + question
	reply = requests.get(apiURL)
	rpDatabase = reply.json()
	embed = discord.Embed(title = ":8ball: The Mighty 8Ball", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.add_field(name = "Question", value = question, inline = False)
	embed.add_field(name = "Response", value = rpDatabase["magic"]["answer"], inline = False)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = "https://i.imgur.com/LkSBSuR.gif")
	await message.edit(content = None, embed = embed)
	print(f"{bot.commandLabel} 8Ball")



# flip command
@bot.command(aliases = ["coinflip"])
@commands.cooldown(1, 5, BucketType.user) 
async def flip(ctx):
	await ctx.trigger_typing()
	responses = {"Heads": "https://i.imgur.com/92xg7uR.png", "Tails": "https://i.imgur.com/TjqDdBI.png"}
	choice = random.choice(["Heads", "Tails"])
	embed = discord.Embed(title = "<:discord_coin:728695789316210860> Flip a Coin", description = f"It's `{choice}`", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = responses[choice])
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} Flip")

# mute command
@bot.command(aliases = ["stfu"])
@commands.cooldown(1, 5, BucketType.user) 
async def mute(ctx, user: str, mtime = None):
	await ctx.trigger_typing()
	if mtime == None:
			mtime = -1

	member = ctx.message.mentions[0]
	vipStat = bot.vipRole in member.roles

	if float(mtime) > 0:
		mtime = float(mtime)

	if (bot.adminRole in ctx.message.author.roles) or (bot.moderatorRole in ctx.message.author.roles):
		if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) == [] and (not ((bot.adminRole in member.roles) or (bot.moderatorRole in member.roles) or (bot.botRole in member.roles) or (bot.devBotRole in member.roles))):
				if mtime > 0:
					if mtime < 1:
						stime = round(mtime * 60)
						sunit = "seconds"										

						if stime == 1:
							sunit = "second"
						
						embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{stime}` {sunit}", color = 0x00FF00, timestamp = datetime.utcnow())
						embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
						embed.set_thumbnail(url = member.avatar_url)
						await ctx.send(embed = embed)

						print(f"{bot.commandLabel} Mute ({stime} {sunit.capitalize()})")
					
					if mtime >= 60:
						htime = mtime / 60
						hunit = "hours"

						if htime == 1:
								hunit = "hour"
						
						embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{htime}` {hunit}", color = 0x00FF00, timestamp = datetime.utcnow())
						embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
						embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
						embed.set_thumbnail(url = member.avatar_url)
						await ctx.send(embed = embed)

						print(f"{bot.commandLabel} Mute ({htime} {hunit.capitalize()})")
					
					if (mtime >= 1) and (mtime < 60):
						munit = "minutes"
						
						if mtime == 1:
								munit = "minute"
						
						embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{mtime}` {munit}", color = 0x00FF00, timestamp = datetime.utcnow())
						embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
						embed.set_thumbnail(url = member.avatar_url)
						await ctx.send(embed = embed)

						print(f"{bot.commandLabel} Mute ({mtime} {munit.capitalize()})")
				
				else:
					embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `infinity` (`∞`)", color = 0x00FF00, timestamp = datetime.utcnow())
					embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
					embed.set_thumbnail(url = member.avatar_url)
					await ctx.send(embed = embed)

					print(f"{bot.commandLabel} Mute (Infinity ∞)")
				
				muteDatabase.insert({"id":(str(member.id) + " " + str(member.guild.id)), "expires":(mtime * 60)})
				await member.add_roles(bot.mutedRole)
				await member.remove_roles(bot.memberRole)
				if vipStat:
					await member.remove_roles(bot.vipRole)

				if mtime > 0:
					await asyncio.sleep(mtime*60)
					
					await member.remove_roles(bot.mutedRole)
					await member.add_roles(bot.memberRole)
					if vipStat:
						await member.add_roles(bot.vipRole)
					
					print(f"{bot.eventLabel} Unmute")
						
					if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) != []:
						embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention}'s mute expired", color = 0x00FF00, timestamp = datetime.utcnow())
						embed.set_footer(text = f"Originally muted by {ctx.author}", icon_url = ctx.author.avatar_url)
						embed.set_thumbnail(url = member.avatar_url)
						await ctx.send(embed = embed)
						muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
		
		else:
			if (bot.adminRole in member.roles) or (bot.moderatorRole in member.roles) or (bot.botRole in member.roles) or (bot.devBotRole in member.roles):
				await ctx.send(f"{bot.errorEmoji} This user cannot be muted")
		
			else:
				await ctx.send(f"{bot.errorEmoji} This user is already muted")
	else:
		await ctx.send(f"{bot.errorEmoji} Missing permissions")

# players = {}
# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def play(ctx, url):
# 	await ctx.trigger_typing()
#	 if ctx.author.id == 410590963379994639:
#	 	voice_client = bot.voice_client_in(bot.server)
#	 	player = await voice_client.create_ytdl_player(url)
#	 	players[server.id] = player
#	 	player.start()
#	 else:
#	 	await ctx.send("nah")

# unmute command
@bot.command()
@commands.cooldown(1, 5, BucketType.user) 
async def disable(ctx, command):
	if ctx.author.id == 410590963379994639:
		bot.remove_command(command)
		await ctx.send(f"{bot.checkmarkEmoji} Disabled the `{command}` command")
	else:
		await ctx.send(f"{bot.errorEmoji} Missing permissions")

# # unmute command
# @bot.command()
# @commands.cooldown(1, 5, BucketType.user) 
# async def enable(ctx, command):
# 	if ctx.author.id == 410590963379994639:
# 		bot.add_command(command)
# 		await ctx.send(f"{bot.checkmarkEmoji} Enabled the `{command}` command")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} Missing permissions")


# unmute command
@bot.command(aliases = ["unstfu"])
@commands.cooldown(1, 5, BucketType.user) 
async def unmute(ctx, user: str):
	await ctx.trigger_typing()
	member = ctx.message.mentions[0]
	if (bot.adminRole in ctx.message.author.roles) or (bot.moderatorRole in ctx.message.author.roles):
		if bot.mutedRole in member.roles:
			await member.remove_roles(bot.mutedRole)
			if not bot.memberRole in member.roles:
				await member.add_roles(bot.memberRole)
			embed = discord.Embed(title = f":loud_sound: Unmuted", description = f"{member.mention} was unmuted", color = 0x00FF00, timestamp = datetime.utcnow())
			embed.set_footer(text = f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar_url)
			embed.set_thumbnail(url = member.avatar_url)
			await ctx.send(embed = embed)
		
		else:
			embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Unmute", description = f"{member.mention} isn't even muted", color = 0xFF0000, timestamp = datetime.utcnow())
			embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
			embed.set_thumbnail(url = member.avatar_url)
			await ctx.send(embed = embed)
		
		if not bot.memberRole in member.roles:
			await member.add_roles(bot.memberRole)
		
		muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
		print(f"{bot.commandLabel} Unmute")
	
	else:
		embed = discord.Embed(title = f"{bot.errorEmoji} Missing Permissions", description = f"Required Roles: \n• {bot.adminRole.mention} \n• {bot.moderatorRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())	 
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

# pp command
@bot.command(aliases = ["dong"])
@commands.cooldown(1, 5, BucketType.user) 
async def pp(ctx):
	await ctx.trigger_typing()
	length = float(random.randint(0, 400)) / 10
	output = ""
	i = 0

	while i != round(length):
		output += "="
		i += 1

	if length <= 8:
		rating = "Atomlike"

	elif length <= 16:
		rating = "Smol"

	elif length <= 24:
		rating = "Average"

	elif length <= 32:
		rating = "Large"

	elif length <= 40:
		rating = "BBC"

	embed = discord.Embed(title = ":eggplant: PP Rater", description = f"8{output}D \n**Length:** `{round(length, 2)}` inches \n**Rating:** `{rating}`", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

	print(f"{bot.commandLabel} PP")

# ip command
@bot.command(aliases = ["mcip"])
@commands.cooldown(1, 5, BucketType.user) 
async def ip(ctx):
	await ctx.trigger_typing()
	embed = discord.Embed(title = f"{bot.minecraftEmoji} Minecraft Server IPs", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

	a = "<a:dndGIF:791185650996346891>"
	b = "<a:dndGIF:791185650996346891>"

	if bot.survivalServerBot.status is discord.Status.online:
		a = "<a:onlineGIF:791185651311575051>"

	# private server 2 bot status
	if bot.creativeServerBot.status is discord.Status.online:
		b = "<a:onlineGIF:791185651311575051>"

	embed.add_field(name = f"{a} Survival Server", value = "Version: `1.16.5`\nIP Address: `ballin-survival.ddns.net`\nBridged Chat: <#693321555366903851>", inline = False)
	embed.add_field(name = f"{b} Creative Server", value = "Version: `1.16.5`\nIP Address: `swiftspirit1408.aternos.me`\nBridged Chat: <#659885014603005953>", inline = False)

	embed.add_field(name = f"{bot.plusEmoji} How to Join", value = "• join the IP\n• DM the code you get to <@693313699779313734>\n• once you're in, do `/register <password>`", inline = False)

	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} IP")

# demote command
@bot.command(aliases = ["promote"])
@commands.cooldown(1, 5, BucketType.user) 
async def mod(ctx, member: discord.Member):
	await ctx.trigger_typing()
	permitted = [410590963379994639, 533167218838470666]
	if ctx.author.id in permitted:
		if bot.memberRole in member.roles:
			await member.remove_roles(bot.memberRole)
			await member.add_roles(bot.moderatorRole)
			embed = discord.Embed(title = "<:upvote:732640878145044623> Demoted", description = f"{member.mention} is now a {bot.moderatorRole.mention}", color = 0xFFFFFE, timestamp = datetime.utcnow())			 
			embed.set_footer(text = f"Demoted by {ctx.author}", icon_url = ctx.author.avatar_url)
			embed.set_thumbnail(url = member.avatar_url)
			await ctx.send(embed = embed)
			await bot.staffOnlyChannel.send(f"<:upvote:732640878145044623> {member.mention} was demoted")
			print(f"{bot.commandLabel} Demote")
		else:
			await ctx.send(f"{bot.errorEmoji} They are already a moderator")
	else:
		await ctx.send(f"{bot.errorEmoji} Missing permissions")

# demote command
@bot.command(aliases = ["demod", "demote"])
@commands.cooldown(1, 5, BucketType.user) 
async def unmod(ctx, member: discord.Member):
	await ctx.trigger_typing()
	permitted = [410590963379994639, 533167218838470666]
	if ctx.author.id in permitted:
		if bot.moderatorRole in member.roles:
			await member.remove_roles(bot.moderatorRole)
			await member.add_roles(bot.memberRole)
			embed = discord.Embed(title = "<:downvote:732640878249902161> Demoted", description = f"{member.mention} is now a {bot.memberRole.mention}", color = 0xFFFFFE, timestamp = datetime.utcnow())			 
			embed.set_footer(text = f"Demoted by {ctx.author}", icon_url = ctx.author.avatar_url)
			embed.set_thumbnail(url = member.avatar_url)
			await ctx.send(embed = embed)
			await bot.staffOnlyChannel.send(f"<:downvote:732640878249902161> {member.mention} was demoted")
			print(f"{bot.commandLabel} Demote")
		else:
			await ctx.send(f"{bot.errorEmoji} They aren't even a moderator")
	else:
		await ctx.send(f"{bot.errorEmoji} Missing permissions")

# invite command
@bot.command(aliases = ["inv"])
@commands.cooldown(1, 5, BucketType.user) 
async def invite(ctx):
	await ctx.trigger_typing()
	await ctx.send("discord.gg/fG8vTrj")
	# embed = discord.Embed(title = ":inbox_tray: Server Invite Link", description = bot.serverInviteURL, color = 0xFFFFFE, timestamp = datetime.utcnow())
	# embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	# embed.set_thumbnail(url = bot.server.icon_url)
	# await ctx.send(embed = embed)
	# print(f"{bot.commandLabel} Invite")

# ping command
@bot.command(aliases = ["latency"])
@commands.cooldown(1, 5, BucketType.user) 
async def ping(ctx):
	await ctx.trigger_typing()
	time = datetime.now() - bot.startTime
	days = time.days
	hours, remainder = divmod(time.seconds, 3600)
	minutes, seconds = divmod(remainder, 60)

	dunit = "day"
	hunit = "hour"
	munit = "minute"
	sunit = "second"

	if days > 1 or days == 0:
		dunit += "s"
	
	if hours > 1 or hours == 0:
		hunit += "s"
	
	if minutes > 1 or minutes == 0:
		munit += "s"
	
	if seconds > 1 or seconds == 0:
		sunit += "s"

	e = discord.Embed(title = "🏓 Pong!", color = 0xFFFFFE, timestamp = datetime.utcnow())
	e.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	e.add_field(name = ":signal_strength: Latency", value = f"`{round(bot.latency * 1000)}`ms", inline = True)
	e.add_field(name = ":robot: Hardware", value = f"`{psutil.cpu_count()}` Cores \n`{round(psutil.cpu_percent())}`% CPU Usage \n`{round(psutil.virtual_memory().percent)}`% RAM Usage", inline = True)
	e.add_field(name = ":chart_with_upwards_trend: Uptime", value = f"`{days}` {dunit} \n`{hours}` {hunit} \n`{minutes}` {munit} \n`{seconds}` {sunit}", inline = True)
	await ctx.send(embed = e)
	print(f"{bot.commandLabel} Ping")

# # help command
# @bot.command(aliases = ["info"])
# @commands.cooldown(1, 5, BucketType.user) 
# async def help(ctx):
# 	await ctx.trigger_typing()
# 	embed = discord.Embed(title = "Help Section", color = 0xFFFFFE, timestamp = datetime.utcnow())
# 	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
# 	embed.set_thumbnail(url = bot.server.icon_url)
# 	embed.add_field(name = ":bust_in_silhouette: User Profile", value = "`!profile` \n`!profile @user`", inline = True)
# 	embed.add_field(name = ":8ball: The Magic 8Ball", value = "`!8ball <question>` \n`!predict <question>`", inline = True)
# 	embed.add_field(name = "<:coin_discord:728695789316210860> Flip a Coin", value = "`!flip` \n`!coinflip`", inline = True)
# 	embed.add_field(name = ":mute: Mute User", value = "`!mute @user <minutes>` \n`!stfu @user <minutes>`", inline = True)
# 	embed.add_field(name = ":loud_sound: Unmute User", value = "`!unmute @user` \n`!unstfu @user`", inline = True)
# 	embed.add_field(name = ":eggplant: PP Rater", value = "`!pp` \n`!dong`", inline = True)
# 	embed.add_field(name = ":medal: Server Roles", value = "`!roles` \n`!ranks`", inline = True)
# 	embed.add_field(name = "<:minecraft_icon:699029490332074015> Start Server(s)", value = "`!start 1` ([Server 1](https://swiftspirit1408.aternos.me/)) \n`!start 2` ([Server 2](https://poopyucky.aternos.me/))", inline = True)
# 	embed.add_field(name = "<:minecraft_icon:699029490332074015> Server IP's", value = "`!ip` \n`!mcip`", inline = True)
# 	embed.add_field(name = "<:krunker_icon:699029209988726885> Krunker Link", value = "`!krunker <link> <title>` \n`!k <link> <title>`", inline = True)
# 	embed.add_field(name = "<:upvote:732640878145044623> Promote", value = "`!promote @user` \n`!mod @user`", inline = True)
# 	embed.add_field(name = "<:downvote:732640878249902161> Demote", value = "`!demote @user` \n`!unmod @user`", inline = True)
# 	embed.add_field(name = ":inbox_tray: Server Invite", value = "`!invite` \n`!inv`", inline = True)
# 	embed.add_field(name = ":ping_pong: Bot Latency", value = "`!ping` \n`!latency`", inline = True)
# 	embed.add_field(name = ":desktop: Help Page", value = "`!help` \n`!info`", inline = True)
# 	embed.add_field(name = ":robot: Bot Info", value = "**Developer:** <@410590963379994639> \n**Language:** [`Python`](https://discordpy.readthedocs.io/en/latest/) \n**Hosting:** [`Dell Inspiron 15 Laptop`](https://g.co/kgs/CKznxn) \n**Github Repo:** [`Link`](https://github.com/hdadhich01/The-Butler-Discord-Bot)", inline = False)
# 	await ctx.send(embed = embed)
# 	print(f"{bot.commandLabel} Help")

# import token and run bot
keepAlive()
bot.run(os.environ.get("token"), bot = True, reconnect = True)