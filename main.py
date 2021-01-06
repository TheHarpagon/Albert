# importing libraries
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import discord
from discord.ext import commands
from discord.ext import tasks
from keepAlive import keepAlive
import os
import psutil
import pytz
import random
import requests
import tinydb
import variables

# set prefix and remove default help command
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents, case_insensitive = True)
bot.remove_command("help")

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
	bot.krunkerLinksChannel = bot.get_channel(variables.krunkerLinksChannelID)
	bot.botProfile = s.get_member(variables.rolesChannelID)
	bot.privateServer1Bot = bot.get_channel(variables.privateServer1BotID)
	bot.privateServer2Bot = bot.get_channel(variables.privateServer2BotID)
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
	bot.memberRole = s.get_role(variables.memberRoleID)
	bot.botRole = s.get_role(variables.botRoleID)
	
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
	await assignments()
	bellSchedule.start()
	bot.startTime = datetime.now()
	await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{userCount(1)} Members • !help"))
	# await bot.change_presence(activity = discord.Streaming(name = "Onlyfanz", url = "https://bit.ly/3lH4oSp"))
	print(f"""
  _____ _            ____        _   _           
 |_   _| |__   ___  | __ ) _   _| |_| | ___ _ __ 
   | | | '_ \ / _ \ |  _ \| | | | __| |/ _ \ '__|
   | | | | | |  __/ | |_) | |_| | |_| |  __/ |   
   |_| |_| |_|\___| |____/ \__,_|\__|_|\___|_|   
                                                 """)

	subjectRolesMessage = await bot.rolesChannel.fetch_message(759521601170833469)
	embed = discord.Embed(title = "School Roles :books:", description = f"Pick up some roles for any subjects you take! \n\n:brain: {bot.helpRole.mention} \nto help anyone in immediate need \n:bell: {bot.bellScheduleRole.mention} \nto receive bell schedule pings \n\n:one: {bot.precalculusRole.mention} \n:two: {bot.apCalcABRole.mention} \n:three: {bot.apCalcBCRole.mention} \n:four: {bot.hPhysicsRole.mention} \n:five: {bot.apPhysicsRole.mention} \n:six: {bot.apBiologyRole.mention} \n:seven: {bot.rushRole.mention} \n:eight: {bot.apushRole.mention} \n:nine: {bot.vsNetRole.mention} \n:keycap_ten: {bot.apcsRole.mention}", color = 0xFFFFFE)
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	await gameRolesMessage.edit(embed = embed)

	rulesMessage = await bot.rulesChannel.fetch_message(790036264648441897)
	embed = discord.Embed(title = "Rules :scroll:", color = 0xFFFFFE)
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = "Server Rules", icon_url = bot.server.icon_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	embed.add_field(name = "Common Sense", value = f"""
• no self promo
• follow [Discord TOS](https://discord.com/terms)
• do not diss <@533153734373539840>
• have some [common sense](https://youtu.be/YSDTPPM9qsc)
• [try not](https://youtu.be/uJHU6CICPGk) to be unfunny as hell
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
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
		embed = discord.Embed(title = f":loud_sound: Unmuted", description = f"{member.mention} was unmuted on bot startup", color = 0x00FF00, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Unmuted by {bot.user}", icon_url = bot.user.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await generalChannel.send(embed = embed)

		print(f"{bot.eventLabel} Unmuted (Automatic)")

@tasks.loop(minutes = 1.0)
async def bellSchedule():
	# tz = timezone(timedelta(hours = -8))
	today = datetime.now() - timedelta(hours = 8)
	currTime = today.time().strftime("%H:%M")
	monTimes = {"08:10": ":books: Period `A`", "08:45": ":books: Period `1`", "09:20": ":books: Period `2`", "09:55": ":books: Period `3`", "10:30": ":books: Period `4`", "11:00": ":sandwich: `Lunch`", "11:35": ":books: Period `5`", "12:10": ":books: Period `6`"}
	tuesThursTimes = {"08:10": ":books: Period `A` (Async)", "09:35": ":books: Period `1`", "11:05": ":books: Period `3`", "12:20": ":sandwich: `Lunch`", "13:05": ":books: Period `5`", "14:30": ":game_die: `Student Support`"}
	wedFriTimes = {"08:10": ":books: Period `A`", "09:35": ":books: Period `2`", "11:05": ":books: Period `4`", "12:20": ":sandwich: `Lunch`", "13:05": ":books: Period `6`", "14:30": ":game_die: `Student Support`"}
	
	if today.isoweekday() == 1:
		if currTime in monTimes:
			embed = discord.Embed(title = f":bell: Reminder", description = f"{monTimes[currTime]} starts in `5` minutes!", color = 0xFFFFFE, timestamp = datetime.utcnow())
			embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
			embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
			embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
			await bot.generalChannel.send(bot.bellScheduleRole.mention, embed = embed)
	elif today.isoweekday() in [2, 4]:
		if currTime in tuesThursTimes:
			embed = discord.Embed(title = f":bell: Reminder", description = f"{tuesThursTimes[currTime]} starts in `5` minutes!", color = 0xFFFFFE, timestamp = datetime.utcnow())
			embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
			embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
			embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
			await bot.generalChannel.send(bot.bellScheduleRole.mention, embed = embed)
	elif today.isoweekday() in [3, 5]:
		if currTime in wedFriTimes:
			embed = discord.Embed(title = f":bell: Reminder", description = f"{wedFriTimes[currTime]} starts in `5` minutes!", color = 0xFFFFFE, timestamp = datetime.utcnow())
			embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
			embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
			embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
			await bot.generalChannel.send(bot.bellScheduleRole.mention, embed = embed)

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
		embed = discord.Embed(title = ":inbox_tray: Member Joined", description = f"You are Member #`{userCount(1)}`", color = 0x00FF00, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		embed.add_field(name = "Get Roles", value = f"Go to {bot.rolesChannel.mention}", inline = False)
		embed.add_field(name = "Main Info :loudspeaker:", value = f"Read the {bot.rulesChannel.mention}\nRead the {bot.channelsChannel.mention} info\nJoin the talk in {bot.generalChannel.mention}", inline = False)
		await bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
		await member.remove_roles(bot.mutedRole)

	else:
		await member.add_roles(bot.botRole)
		embed = discord.Embed(title = ":inbox_tray: Bot Joined", description = f"You are Bot #`{userCount(1)}`\n{bot.botRole.mention} role added", color = 0x00FF00, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		await bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)
		print(f"{bot.eventLabel} Member Left")

	else:
		embed = discord.Embed(title = f":outbox_tray: Bot Left", description = "Either kicked/banned/left", color = 0xFF0000, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = bot.server.name, icon_url = bot.server.icon_url)
		embed.set_thumbnail(url = member.avatar_url)
		await bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)
		print(f"{bot.eventLabel} Bot Left")

@bot.event
async def on_message_delete(message):
	if message.author.bot == False and bot.memberRole in message.author.roles and message.channel.id != 690647361139245136:
		embed = discord.Embed(title = ":wastebasket: Message Deleted", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
	if bot.user.mentioned_in(message):
		await message.channel.send("https://tenor.com/view/hell-no-bollywood-indian-hell-no-gif-5616245")
	
	# checking if message is a valid krunker link
	if ((message.content.startswith("https://krunker.io/?game=")) or (message.content.startswith("https://www.krunker.io/?game=")) or (message.content.startswith("krunker.io/?game=")) or (message.content.startswith("www.krunker.io/?game="))) and (message.content[-6] == ":"):
		await message.delete()
		embed = discord.Embed(title = "<:krunker_icon:699029209988726885> Krunker Link", description = message.content, color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Link posted by {message.author}", icon_url = message.author.avatar_url)
		embed.set_thumbnail(url = "https://i.imgur.com/SIIjfcd.png")
		linkPost = await bot.krunkerLinksChannel.send(embed = embed)

		embed = discord.Embed(title = "<:krunker_icon:699029209988726885> Krunker Link", description = f":white_check_mark: Posted [here]({linkPost.jump_url})", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Link posted by {message.author}", icon_url = message.author.avatar_url)
		embed.set_thumbnail(url = "https://i.imgur.com/SIIjfcd.png")
		await message.channel.send(embed = embed)
		print(f"{bot.eventLabel} Krunker Link Posted")
	
	if message.guild is None and message.author.id == 410590963379994639:
		await bot.generalChannel.send(message.content)
	
	await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
	if str(before.activity).lower() == "streaming":
		await after.remove_roles(bot.liveOnTwitchRole)
	if str(after.activity).lower() == "streaming":
		await after.add_roles(bot.liveOnTwitchRole)

@bot.event
async def on_voice_state_update(member, before, after):
	if after.channel:
		await bot.logChannel.send(f"{bot.plusEmoji} `{member}` has joined `{after.channel.name}` VC")
	if not before.self_stream and after.self_stream:
		await bot.logChannel.send(f":red_circle: `{member}` went live in `{after.channel.name}` VC")

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send(f"{bot.errorEmoji} {error}")
#     elif isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send(f"{bot.errorEmoji} {error}")
#     else:
#         await ctx.send(bot.errorEmoji)

# @bot.command()
# async def top(ctx):
# 	data = leaderboardTask()
# 	embed = discord.Embed(title = "Leaderboard", color = 0xFFFFFE, timestamp = datetime.utcnow())
# 	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
# 	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
# 	for i in range(0, 10):
# 		embed.add_field(name = f"{i+1}) {data[0][i]}", value = f"Level {data[1][i]}", inline = False)
# 	await ctx.send(embed = embed)

# pfp command
@bot.command(aliases = ["avatar", "av"])
async def pfp(ctx, member: discord.Member = None):
	member = ctx.author if not member else member
	embed = discord.Embed(title = ":frame_photo: Profile Picture", description = member.mention, color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = member.avatar_url)
	await ctx.send(embed = embed)

@bot.command()
async def emojis(ctx):
	message = ""
	for emoji in bot.server.emojis:
		message += str(emoji)
	await ctx.send(f"`{len(bot.server.emojis)}` Emojis")
	await ctx.send(message)

@bot.command(aliases = ["s"])
async def schedule(ctx):
	embed = discord.Embed(title = ":bell: DVHS Bell Schedule", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = "https://i.imgur.com/ES49tLo.jpg")
	await ctx.send(embed = embed)

@bot.command(aliases = ["nickname"])
async def nick(ctx, *, nickname):
	if len(nickname) >= 1 and len(nickname) <= 32:
		await ctx.author.edit(nick = nickname)
		await ctx.send(f"{bot.checkmarkEmoji} Your nickname was set to `{nickname}`!")
	else:
		await ctx.send(f"{bot.errorEmoji} Nicknames can only be upto `32` characters long!")


# @bot.command()
# async def resetnicks(ctx):
# 	if bot.adminRole in ctx.author.roles:
# 		msg = await ctx.send("<a:loadingColorful:765034824926232606> Hold up...")
# 		for member in bot.server.members:
# 			if member.bot is False and member.id != 410590963379994639:
# 				await member.edit(nick = member.name)
# 		await msg.edit(f"{bot.checkmarkEmoji} Done!")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")


@bot.command()
async def setstatus(ctx, *, argument):
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
async def kill(ctx):
	if ctx.author.id == 410590963379994639:
		await ctx.send(f"{bot.checkmarkEmoji} Ending process! (start manually in repl)")
		await bot.close()
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

@bot.command()
async def randomperson(ctx):
	if ctx.author.id == 410590963379994639:
		await ctx.send(random.choice(bot.server.members).mention + " is the random person!")
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

# @bot.command()
# async def pogga(ctx):
# 	if ctx.author.id == 410590963379994639:
# 		for member in bot.server.members:
# 			if member.bot == False:
# 				await member.send("<a:spinningToilet:775547013047648297> Happy New Years!")
# 	else:
# 		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

# @bot.command()
# async def vc(ctx, argument):
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
async def dm(ctx, member: discord.Member, *, message):
	if bot.vipRole in ctx.author.roles:
		await member.send(message + f"\n- from {ctx.author.mention}")
		await ctx.send(f"{bot.checkmarkEmoji} Sent!")
		print(f"{bot.commandLabel} DM")
	else:
		await ctx.send(f"{bot.errorEmoji} You do not have access to use this command!")

@bot.command(aliases = ["servericon"])
async def icon(ctx):
	embed = discord.Embed(title = ":frame_photo: Server Icon", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = bot.server.icon_url)
	await ctx.send(embed = embed)

# profile command
@bot.command()
async def profile(ctx, member: discord.Member = None):
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
		#     if i in member.roles:
		#         output += gameRoles[i].mention
		# gameRoles = ""
		
		# if bot.krunkerRole in member.roles:
		#     gameRoles += f"\n{bot.krunkerRole.mention}"
		
		# if bot.minecraftRole in member.roles:
		#     gameRoles += f"\n{bot.minecraftRole.mention}"

		# if bot.valorantRole in member.roles:
		#     gameRoles += f"\n{bot.valorantRole.mention}"
		
		# if bot.amongUsRole in member.roles:
		#     gameRoles += f"\n{bot.amongUsRole.mention}"

		# else:
		#     gameRoles = "`None`"

		embed = discord.Embed(title=f":bust_in_silhouette: User Profile", description = f"`{member}`", color = topColor, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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

# predict command
@bot.command(aliases = ["8ball"])
async def predict(ctx, *, question: str):
	responses = [   f"shut the fuck up {ctx.author.nick.lower()}",
									"Yeah I can picture that ngl",
									"Yeah fs dude",
									"Yeah no doubt dude",
									"Absolutely, not even a question",
									"Si obviamente (yes in spanish)",
									"According to my super senses, yes",
									"99% chance that's happening",
									"Seems to be that way",
									"Oui (yes in french)",
									"Hai, shitsumon sae arimasen (yes in japanese)",
									"I just puffed a joint gimme a sec bruh",
									"Ask me later, busy clapping your mom's cheeks",
									"Well you jinxed it so can't say man",
									"I just lost brain cells from that question and therefore cannot answer",
									"Recite the entire Quran and ask again",
									"Hippity hop, I don't give a fuck, stop annoying me now",
									"Nah that shit false fam",
									"After shaking me hella hard like that, imma obviously say no",
									"Nah chief",
									"Bruh I'm a fucking Discord Bot made by a human, why tf you asking me",
									"My sources say no, but they also said Hillary would win",
									"How the hell is applebee's still in business, crazy shit man",
									"Does it look like I give a shit bruh",
									"Go ask your mom buddy",
									"My sources say no, but then again, they also say they hate you",
									"My answer to your question lies [here](https://www.youtube.com/watch?v=ub82Xb1C8os)",
									"The chance of that is lower than your penis size my dude"   ]

	embed = discord.Embed(title = ":8ball: The Mighty 8Ball", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.add_field(name = "Question", value = question, inline = False)
	embed.add_field(name = "Response", value = random.choice(responses), inline = False)
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = "https://i.imgur.com/LkSBSuR.gif")
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} 8Ball")

# flip command
@bot.command(aliases = ["coinflip"])
async def flip(ctx):

	responses = ["Heads", "Tails"]

	response = random.choice(responses)

	if response == responses[0]:
		embed = discord.Embed(title = "<:discord_coin:728695789316210860> Flip a Coin", description = f"It's `{response}`", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = "https://i.imgur.com/92xg7uR.png")
		await ctx.send(embed = embed)
	
	else:
		embed = discord.Embed(title = "<:discord_coin:728695789316210860> Flip a Coin", description = f"It's `{response}`", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = "https://i.imgur.com/TjqDdBI.png")
		await ctx.send(embed = embed)
	
	print(f"{bot.commandLabel} Flip")

# mute command
@bot.command(aliases = ["stfu"])
async def mute(ctx, user: str, mtime = None):
	if mtime == None:
			mtime = -1

	member = ctx.message.mentions[0]

	if float(mtime) > 0:
		mtime = float(mtime)

	if (bot.adminRole in ctx.message.author.roles) or (bot.moderatorRole in ctx.message.author.roles):
		if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) == [] and (not ((bot.adminRole in member.roles) or (bot.moderatorRole in member.roles) or (bot.botRole in member.roles))):
				if mtime > 0:
					if mtime < 1:
						stime = round(mtime * 60)
						sunit = "seconds"                    

						if stime == 1:
							sunit = "second"
						
						embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{stime}` {sunit}", color = 0x00FF00, timestamp = datetime.utcnow())
						embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
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
						embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
						embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
						embed.set_thumbnail(url = member.avatar_url)
						await ctx.send(embed = embed)

						print(f"{bot.commandLabel} Mute ({mtime} {munit.capitalize()})")
				
				else:
					embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `infinity` (`∞`)", color = 0x00FF00, timestamp = datetime.utcnow())
					embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
					embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
					embed.set_thumbnail(url = member.avatar_url)
					await ctx.send(embed = embed)

					print(f"{bot.commandLabel} Mute (Infinity ∞)")
				
				muteDatabase.insert({"id":(str(member.id) + " " + str(member.guild.id)), "expires":(mtime * 60)})
				await member.add_roles(bot.mutedRole)
				await member.remove_roles(bot.memberRole)

				if mtime > 0:
					await asyncio.sleep(mtime*60)
					
					await member.remove_roles(bot.mutedRole)
					await member.add_roles(bot.memberRole)
					
					print(f"{bot.eventLabel} Unmute")
						
					if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) != []:
						embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention}'s mute expired", color = 0x00FF00, timestamp = datetime.utcnow())
						embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
						embed.set_footer(text = f"Originally muted by {ctx.author}", icon_url = ctx.author.avatar_url)
						embed.set_thumbnail(url = member.avatar_url)
						await ctx.send(embed = embed)
						muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
		
		else:
			if (bot.adminRole in member.roles) or (bot.moderatorRole in member.roles) or (bot.botRole in member.roles):
				embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Mute", description = f"Exempt Roles: \n• {bot.adminRole.mention} \n• {bot.moderatorRole.mention} \n• {bot.botRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow()) 
				embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
				embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
				embed.set_thumbnail(url = member.avatar_url)
				await ctx.send(embed = embed)
		
			else:
				embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Mute", description = f"{member.mention} is already muted", color = 0xFF0000, timestamp = datetime.utcnow())
				embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
				embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
				embed.set_thumbnail(url = member.avatar_url)
				await ctx.send(embed = embed)
	else:
		embed = discord.Embed(title = f"{bot.errorEmoji} Missing Permissions", description = f"Required Roles: \n• {bot.adminRole.mention} \n• {bot.moderatorRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())   
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

@bot.command()
async def vcjoin(ctx):
	if ctx.author.id == 410590963379994639:
		channel = ctx.message.author.voice.channel
		await channel.connect()
		await ctx.send("i mean ok if you're that lonely ill join ig")
	else:
		await ctx.send("nah bro only for my owner")

# players = {}
# @bot.command()
# async def play(ctx, url):
#     if ctx.author.id == 410590963379994639:
#         voice_client = bot.voice_client_in(bot.server)
#         player = await voice_client.create_ytdl_player(url)
#         players[server.id] = player
#         player.start()
#     else:
#         await ctx.send("nah")


# unmute command
@bot.command(aliases = ["unstfu"])
async def unmute(ctx, user: str):
	member = ctx.message.mentions[0]
	if (bot.adminRole in ctx.message.author.roles) or (bot.moderatorRole in ctx.message.author.roles):
		if bot.mutedRole in member.roles:
			await member.remove_roles(bot.mutedRole)
			if not bot.memberRole in member.roles:
				await member.add_roles(bot.memberRole)
			embed = discord.Embed(title = f":loud_sound: Unmuted", description = f"{member.mention} was unmuted", color = 0x00FF00, timestamp = datetime.utcnow())
			embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
			embed.set_footer(text = f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar_url)
			embed.set_thumbnail(url = member.avatar_url)
			await ctx.send(embed = embed)
		
		else:
			embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Unmute", description = f"{member.mention} isn't even muted", color = 0xFF0000, timestamp = datetime.utcnow())
			embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
			embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
			embed.set_thumbnail(url = member.avatar_url)
			await ctx.send(embed = embed)
		
		if not bot.memberRole in member.roles:
			await member.add_roles(bot.memberRole)
		
		muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
		print(f"{bot.commandLabel} Unmute")
	
	else:
		embed = discord.Embed(title = f"{bot.errorEmoji} Missing Permissions", description = f"Required Roles: \n• {bot.adminRole.mention} \n• {bot.moderatorRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())   
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

# pp command
@bot.command(aliases = ["dong"])
async def pp(ctx):
	length = float(random.randint(0, 400)) / 10
	output = ""
	i = 0

	while i != round(length):
		output += "="
		i += 1

	if length > 0 and length <= 8:
		rating = "Atomlike"

	if length > 2 and length <= 16:
		rating = "Smol"

	if length > 6 and length <= 24:
		rating = "Average"

	if length > 10 and length <= 32:
		rating = "Large"

	if length > 15 and length <= 40:
		rating = "BBC"

	embed = discord.Embed(title = ":eggplant: PP Rater", description = f"8{output}D \n**Length:** `{round(length, 2)}` inches \n**Rating:** `{rating}`", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = ctx.author.avatar_url)
	await ctx.send(embed = embed)

	print(f"{bot.commandLabel} PP")

# roles command
@bot.command(aliases = ["ranks"])
async def roles(ctx):
	embed = discord.Embed(title = ":medal: Server Roles", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_image(url = "https://i.gyazo.com/5d858524628ea71faaa9c7b922ec093d.png")
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} Roles")

# ip command
@bot.command(aliases = ["mcip"])
async def ip(ctx):
	embed = discord.Embed(title = "<:minecraft_icon:699029490332074015> Minecraft Server IPs", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

	# privateServer1BotStatus = "<:offline:736832948913045588>"
	# privateServer2BotStatus = "<:offline:736832948913045588>"

	# # private server 1 bot status
	# if bot.privateServer1Bot.status == discord.Status.online:
	#     privServer1BotStatus = "<:online:736832948980154379>"

	# private server 2 bot status
	# if bot.privateServer1Bot.status == discord.Status.online:
	#     privServer2BotStatus = "<:online:736832948980154379>"

	embed.add_field(name = f"Server 1 [1.16.3]", value = "[`swiftspirit1408.aternos.me`](https://swiftspirit1408.aternos.me) \nChat available [here](https://discordapp.com/channels/612059384721440789/659885014603005953)", inline = False)
	embed.add_field(name = f"Server 2 [1.16.3]", value = "[`poopyucky.aternos.me`](https://poopyucky.aternos.me) \nChat available [here](https://discordapp.com/channels/612059384721440789/693321555366903851)", inline = False)
	embed.add_field(name = "Other Servers [1.8+]", value = "BlocksMC: `blocksmc.com` \nPikaNetwork: `play.pika-network.net` \nMineBerry: `mc.mineberry.net`", inline = False)
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} IP")

# promote command
@bot.command(aliases = ["mod"])
async def promote(ctx, member: discord.Member):
	if (bot.adminRole in ctx.message.author.roles) and (bot.memberRole in member.roles):
		await member.add_roles(bot.moderatorRole)
		await member.remove_roles(bot.memberRole)

		embed = discord.Embed(title = f"<:upvote:732640878145044623> Promoted", description = f"{member.mention} is now a {bot.moderatorRole.mention}", color = 0x00FF00, timestamp = datetime.utcnow())       
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Promoted by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

		await bot.staffOnlyChannel.send(f"<:upvote:732640878145044623> {member.mention} was promoted")
		embed = discord.Embed(title = "Staff Guidelines", description = f"Below are some guidelines/rules for a {bot.moderatorRole.mention}! \nPlease **do not** abuse your powers, or you will be demoted", color = 0xFFFFFE, timestamp = datetime.utcnow())
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		embed.add_field(name = "Warning", value = "warn when user violate rules lightly \n`!warn @user reason` \n`!infractions @user`", inline = False)
		embed.add_field(name = "Muting & Unmting", value = "mute when user violates rules \n`!mute @user` (∞)\n`!mute @user 15` (15 minutes)\nUnmute → `!unmute @user`", inline = False)
		embed.add_field(name = "Kicking/Banning/Unbanning", value = "do not kick or ban without asking <@410590963379994639> \n`!kick @user reason` \n`!ban @user reason` \n`!unban @user`", inline = False)
		embed.add_field(name = "Pins & Announcements", value = "pin and announce only important stuff", inline = False)
		embed.add_field(name = "Permissions", value = "• delete any user's messages \n• view and type in <#701630600347516999> and <#690072751628877865> \n• type in <#635302492132999168> and <#659885490790727716> \n• Operator in `Server 1`\* \n\n*run OP commands from <#659885490790727716> **without** the slash \n`time set day` :white_check_mark: \n`/time set day` :x:", inline = False)
		await bot.staffOnlyChannel.send(embed = embed)
		print(f"{bot.commandLabel} Promote")

	elif (bot.adminRole in ctx.message.author.roles) and (bot.moderatorRole in member.roles):
		embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Promote", description = f"{member.mention} is already a {bot.moderatorRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())       
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

	elif (bot.adminRole in ctx.message.author.roles) and (bot.adminRole in member.roles):
		embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Promote", description = f"You fool, you are literally the {bot.adminRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())       
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(title = f"{bot.errorEmoji} Missing Permissions", description = f"Required Role: \n• {bot.adminRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())  
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

# demote command
@bot.command(aliases = ["unmod"])
async def demote(ctx, member: discord.Member):
	if (bot.adminRole in ctx.message.author.roles) and (bot.moderatorRole in member.roles):
		await member.add_roles(bot.memberRole)
		await member.remove_roles(bot.moderatorRole)

		embed = discord.Embed(title = f"<:downvote:732640878249902161> Demoted", description = f"{member.mention} is now a {bot.memberRole.mention}", color = 0x00FF00, timestamp = datetime.utcnow())       
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Demoted by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

		await bot.staffOnlyChannel.send(f"<:downvote:732640878249902161> {member.mention} was demoted")
		print(f"{bot.commandLabel} Demote")

	elif (bot.adminRole in ctx.message.author.roles) and (bot.memberRole in member.roles):
		embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Demote", description = f"{member.mention} is already a {bot.memberRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())    
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

	elif (bot.adminRole in ctx.message.author.roles) and (bot.adminRole in member.roles):
		embed = discord.Embed(title = f"{bot.errorEmoji} Unable to Promote", description = f"You fool, you literally are the {bot.adminRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())       
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

	else:
		embed = discord.Embed(title = f"{bot.errorEmoji} Missing Permissions", description = f"Required Role: {bot.adminRole.mention}", color = 0xFF0000, timestamp = datetime.utcnow())    
		embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
		embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
		embed.set_thumbnail(url = member.avatar_url)
		await ctx.send(embed = embed)

# invite command
@bot.command(aliases = ["inv"])
async def invite(ctx):
	embed = discord.Embed(title = ":inbox_tray: Server Invite Link", description = bot.serverInviteURL, color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} Invite")

# ping command
@bot.command(aliases = ["latency"])
async def ping(ctx):
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
	e.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	e.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	e.add_field(name = ":signal_strength: Latency", value = f"`{round(bot.latency * 1000)}`ms", inline = True)
	e.add_field(name = ":robot: Hardware", value = f"`{psutil.cpu_count()}` Cores \n`{round(psutil.cpu_percent())}`% CPU Usage \n`{round(psutil.virtual_memory().percent)}`% RAM Usage", inline = True)
	e.add_field(name = ":chart_with_upwards_trend: Uptime", value = f"`{days}` {dunit} \n`{hours}` {hunit} \n`{minutes}` {munit} \n`{seconds}` {sunit}", inline = True)
	await ctx.send(embed = e)
	print(f"{bot.commandLabel} Ping")

# help command
@bot.command(aliases = ["info"])
async def help(ctx):
	embed = discord.Embed(title = "Help Section", color = 0xFFFFFE, timestamp = datetime.utcnow())
	embed.set_author(name = bot.user.name, url = bot.statusPageURL, icon_url = bot.user.avatar_url)
	embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
	embed.set_thumbnail(url = bot.server.icon_url)
	embed.add_field(name = ":bust_in_silhouette: User Profile", value = "`!profile` \n`!profile @user`", inline = True)
	embed.add_field(name = ":8ball: The Magic 8Ball", value = "`!8ball <question>` \n`!predict <question>`", inline = True)
	embed.add_field(name = "<:coin_discord:728695789316210860> Flip a Coin", value = "`!flip` \n`!coinflip`", inline = True)
	embed.add_field(name = ":mute: Mute User", value = "`!mute @user <minutes>` \n`!stfu @user <minutes>`", inline = True)
	embed.add_field(name = ":loud_sound: Unmute User", value = "`!unmute @user` \n`!unstfu @user`", inline = True)
	embed.add_field(name = ":eggplant: PP Rater", value = "`!pp` \n`!dong`", inline = True)
	embed.add_field(name = ":medal: Server Roles", value = "`!roles` \n`!ranks`", inline = True)
	embed.add_field(name = "<:minecraft_icon:699029490332074015> Start Server(s)", value = "`!start 1` ([Server 1](https://swiftspirit1408.aternos.me/)) \n`!start 2` ([Server 2](https://poopyucky.aternos.me/))", inline = True)
	embed.add_field(name = "<:minecraft_icon:699029490332074015> Server IP's", value = "`!ip` \n`!mcip`", inline = True)
	embed.add_field(name = "<:krunker_icon:699029209988726885> Krunker Link", value = "`!krunker <link> <title>` \n`!k <link> <title>`", inline = True)
	embed.add_field(name = "<:upvote:732640878145044623> Promote", value = "`!promote @user` \n`!mod @user`", inline = True)
	embed.add_field(name = "<:downvote:732640878249902161> Demote", value = "`!demote @user` \n`!unmod @user`", inline = True)
	embed.add_field(name = ":inbox_tray: Server Invite", value = "`!invite` \n`!inv`", inline = True)
	embed.add_field(name = ":ping_pong: Bot Latency", value = "`!ping` \n`!latency`", inline = True)
	embed.add_field(name = ":desktop: Help Page", value = "`!help` \n`!info`", inline = True)
	embed.add_field(name = ":robot: Bot Info", value = "**Developer:** <@410590963379994639> \n**Language:** [`Python`](https://discordpy.readthedocs.io/en/latest/) \n**Hosting:** [`Dell Inspiron 15 Laptop`](https://g.co/kgs/CKznxn) \n**Github Repo:** [`Link`](https://github.com/hdadhich01/The-Butler-Discord-Bot)", inline = False)
	await ctx.send(embed = embed)
	print(f"{bot.commandLabel} Help")

# import token and run bot
keepAlive()
bot.run(os.environ.get("token"), bot = True, reconnect = True)