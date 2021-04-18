import art
from datetime import datetime
import discord
from discord.ext import commands
import json
from keepAlive import keepAlive
import os
# import tinydb
import variables
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents, case_insensitive = True)
# mutes = {}
# muteDatabase = tinydb.TinyDB("muteDatabase.json")
# query = tinydb.Query()

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
  bot.vcRole = s.get_role(variables.vcRoleID)

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
  bot.vcEmoji = bot.get_emoji(variables.vcEmojiID)
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

  bot.gameRRDict = {variables.amongUsEmojiID: bot.amongUsRole, variables.chessEmojiID: bot.chessRole, variables.krunkerEmojiID: bot.krunkerRole, variables.minecraftEmojiID: bot.minecraftRole, variables.skribblEmojiID: bot.skribblRole, variables.valorantEmojiID: bot.valorantRole, variables.vcEmojiID: bot.vcRole}
  # bot.categoryDB = requests.get("https://opentdb.com/api_category.php").json()

  bot.monTimes = {"08:10 AM": "A", "08:40 AM": "Passing", "08:45 AM": "1", "09:15 AM": "Passing","09:20 AM": "2", "09:50 AM": "Passing", "09:55 AM": "3", "10:25 AM": "Passing", "10:30 AM": "4", "11:00 AM": "Lunch", "11:30 AM": "Passing", "11:35 AM": "5", "12:05 PM": "Passing", "12:10 PM": "6"}
  bot.tuesThursTimes = {"08:10 AM": "A", "09:25 AM": "Passing", "09:35 AM": "1", "10:50 AM": "Passing", "11:05 AM": "3", "12:20 PM": "Lunch", "12:55 PM": "Passing", "01:05 PM": "5", "02:20 PM": "Passing", "02:30 PM": "Student Support"}
  bot.wedFriTimes = {"08:10 AM": "A", "09:25 AM": "Passing", "09:35 AM": "2", "10:50 AM": "Passing", "11:05 AM": "4", "12:20 PM": "Lunch", "12:55 PM": "Passing", "01:05 PM": "6", "02:20 PM": "Passing", "02:30 PM": "Student Support"}
  bot.daySchedule = {1: bot.monTimes, 2: bot.tuesThursTimes, 3: bot.wedFriTimes, 4: bot.tuesThursTimes, 5: bot.wedFriTimes}

  bot.monTimesMinutes = {}
  bot.tuesThursTimesMinutes = {}
  bot.wedFriTimesMinutes = {}

  def timeInMinutes(datetimeObject):
    return (int(datetimeObject.strftime("%H")) * 60) + (int(datetimeObject.strftime("%M"))) + 5

  # stringTime = time.strftime("%I:%M %p")
  for i in bot.monTimes:
    bot.monTimesMinutes[timeInMinutes(datetime.strptime(i, "%I:%M %p"))] = bot.monTimes[i]
  for i in bot.tuesThursTimes:
    bot.tuesThursTimesMinutes[timeInMinutes(datetime.strptime(i, "%I:%M %p"))] = bot.tuesThursTimes[i]
  for i in bot.wedFriTimes:
    bot.wedFriTimesMinutes[timeInMinutes(datetime.strptime(i, "%I:%M %p"))] = bot.wedFriTimes[i]
  bot.dayScheduleMinutes = {1: bot.monTimesMinutes, 2: bot.tuesThursTimesMinutes, 3: bot.wedFriTimesMinutes, 4: bot.tuesThursTimesMinutes, 5: bot.wedFriTimesMinutes}

  with open("cogs/afks.json", "r") as file:
    data = json.load(file)
    for id in list(data):
      if not bot.server.get_member(int(id)).display_name.startswith("[AFK] "):
        del data[str(id)]
    for member in s.members:
      if str(member.id) not in data and member.display_name.startswith("[AFK] "):
        data[str(member.id)] = [str(datetime.now()), None]
  with open("cogs/afks.json", "w") as file:
    json.dump(data, file, indent = 2)

  def botOwner(ctx):
    return ctx.author.id == 410590963379994639
  bot.botOwner = botOwner
  
  def altCheck(ctx):
    return ctx.author.id == 582313253208850433
  bot.altCheck = altCheck

  def staffCheck(ctx):
    staff = [bot.adminRole, bot.moderatorRole]
    return any(role in ctx.author.roles for role in staff)
  bot.staffCheck = staffCheck

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
  bot.userCount = userCount

  async def updateStatus():
    await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{userCount(1)} Members • !help"))
  bot.updateStatus = updateStatus

# bot startup event
@bot.event
async def on_ready():
  print(f"Loading Cogs:")
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      bot.load_extension(f"cogs.{filename[:-3]}")
      print(f"- {filename}")
  await assignments()
  bot.startTime = datetime.now()
  await bot.updateStatus()
  print(f" DPY Version: {discord.__version__}")
  art.tprint(bot.user.name)
  # for i in muteDatabase:
  #   ids = i["id"].split(" ")
  #   server = bot.get_guild(int(ids[1]))
  #   member = bot.server.get_member(int(ids[0]))
  #   if bot.mutedRole in member.roles:
  #     await member.remove_roles(bot.mutedRole)
  #     await member.add_roles(bot.memberRole)
  #   muteDatabase.remove(query.id == (str(member.id) + " " + str(server.id)))
  #   generalChannel = bot.get_channel(variables.generalChannelID)
  #   embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention} was unmuted on bot startup", color = 0x00FF00, timestamp = datetime.utcnow())
  #   embed.set_footer(text = f"Unmuted  by {bot.user}", icon_url = bot.user.avatar_url)
  #   embed.set_thumbnail(url = member.avatar_url)
  #   await generalChannel.send(embed = embed)
  #   print(f"{bot.eventLabel} Unmuted (Automatic)")
  
  rulesMessage = await bot.rulesChannel.fetch_message(790036264648441897)
  embed = discord.Embed(title = "Rules :scroll:", color = 0xe67e22)
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
  • no nsfw or crazy spamming (except in <#612384531999096832>)
  • arguing is allowed, but if it gets too spicy, go to <#744374005280276522>""", inline = False)
  embed.add_field(name = "More Info", value = f"""
  • run `!help` to see server commands
  • staff can mute you at their discretion
  • ignorance of the rules above is not a valid excuse
  • bans and kicks generally happen after discussion in {bot.generalChannel.mention}
  • rules for the **minecraft servers** are pinned (<#659885014603005953> & <#693321555366903851>)""", inline = False)
  await rulesMessage.edit(embed = embed)

  subjectRolesMessage = await bot.rolesChannel.fetch_message(759521601170833469)
  embed = discord.Embed(title = "School Roles :books:", description = f"Pick up some roles for any subjects you take! \n\n:brain: {bot.helpRole.mention} \nto help anyone in immediate need \n:bell: {bot.bellScheduleRole.mention} \nto receive bell schedule pings \n\n:one: {bot.precalculusRole.mention} \n:two: {bot.apCalcABRole.mention} \n:three: {bot.apCalcBCRole.mention} \n:four: {bot.hPhysicsRole.mention} \n:five: {bot.apPhysicsRole.mention} \n:six: {bot.apBiologyRole.mention} \n:seven: {bot.rushRole.mention} \n:eight: {bot.apushRole.mention} \n:nine: {bot.vsNetRole.mention} \n:keycap_ten: {bot.apcsRole.mention}", color = 0xe67e22)
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
  {bot.valorantEmoji} {bot.valorantRole.mention}
  {bot.vcEmoji} {bot.vcRole.mention}""", color = 0xe67e22)
  embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
  embed.set_thumbnail(url = bot.server.icon_url)
  await gameRolesMessage.edit(embed = embed)

keepAlive()
bot.run(os.environ["token"], bot = True, reconnect = True)

# junk shit for on_ready
# subjectRolesMessage = await bot.rolesChannel.fetch_message(759521601170833469)
# embed = discord.Embed(title = "School Roles :books:", description = f"Pick up some roles for any subjects you take! \n\n:brain: {bot.helpRole.mention} \nto help anyone in immediate need \n:bell: {bot.bellScheduleRole.mention} \nto receive bell schedule pings \n\n:one: {bot.precalculusRole.mention} \n:two: {bot.apCalcABRole.mention} \n:three: {bot.apCalcBCRole.mention} \n:four: {bot.hPhysicsRole.mention} \n:five: {bot.apPhysicsRole.mention} \n:six: {bot.apBiologyRole.mention} \n:seven: {bot.rushRole.mention} \n:eight: {bot.apushRole.mention} \n:nine: {bot.vsNetRole.mention} \n:keycap_ten: {bot.apcsRole.mention}", color = 0xe67e22)
# embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
# embed.set_thumbnail(url = bot.server.icon_url)
# await subjectRolesMessage.edit(embed = embed)

# gameRolesMessage = await bot.rolesChannel.fetch_message(759534246607585300)
# embed = discord.Embed(title = "Game Roles :video_game:", description = f"""Pick up some roles for any games you play! 

# {bot.amongUsEmoji} {bot.amongUsRole.mention} 
# {bot.chessEmoji} {bot.chessRole.mention} 
# {bot.krunkerEmoji} {bot.krunkerRole.mention} 
# {bot.minecraftEmoji} {bot.minecraftRole.mention} 
# {bot.skribblEmoji} {bot.skribblRole.mention} 
# {bot.valorantEmoji} {bot.valorantRole.mention}
# {bot.vcEmoji} {bot.vcRole.mention}""", color = 0xe67e22)
# embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
# embed.set_thumbnail(url = bot.server.icon_url)
# await gameRolesMessage.edit(embed = embed)

# rulesMessage = await bot.rulesChannel.fetch_message(790036264648441897)
# embed = discord.Embed(title = "Rules :scroll:", color = 0xe67e22)
# embed.set_footer(text = "Server Rules", icon_url = bot.server.icon_url)
# embed.set_thumbnail(url = bot.server.icon_url)
# embed.add_field(name = "Common Sense", value = f"""
# • no self promo
# • follow [Discord TOS](https://discord.com/terms)
# • do not diss <@533153734373539840>
# • have some [common sense](https://youtu.be/YSDTPPM9qsc)
# • avoid being blatantly offensive
# • no annoying/unnecessary pinging
# • respect da staff cuz they're kinda hot
# • don't be an asshole/annoying person
# • use the right channel for your topic of discussion
# • no nsfw or crazy spamming (except in <#777040210005065739>)
# • arguing is allowed, but if it gets too spicy, go to <#744374005280276522>""", inline = False)
# embed.add_field(name = "More Info", value = f"""
# • run `!help` to see server commands
# • staff can mute you at their discretion
# • ignorance of the rules above is not a valid excuse
# • bans and kicks generally happen after discussion in {bot.generalChannel.mention}
# • rules for the **minecraft servers** are pinned (<#659885014603005953> & <#693321555366903851>)""", inline = False)
# await rulesMessage.edit(embed = embed)

# channelsMessage1 = await bot.channelsChannel.fetch_message(790467696860594207)
# embed = discord.Embed(title = "Channels :computer:", description = "ayo wtf are these channels for??", color = 0xe67e22)
# embed.set_footer(text = "Server Channels", icon_url = bot.server.icon_url)
# embed.set_thumbnail(url = bot.server.icon_url)
# embed.add_field(name = "Text Channels", value = f"""
# • {bot.welcomeChannel.mention} user welcome and adios messages
# • {bot.rolesChannel.mention} reaction roles 
# • {bot.rulesChannel.mention} the constitution
# • {bot.channelsChannel.mention} info on all channels
# • <#635302492132999168> announcements and updates
# • <#732997653394227220> suggestions posted with `s!suggest <suggestion>`
# • <#745337266943164446> messages with four or more :star: reactions
# • {bot.generalChannel.mention} communicate with other idiots
# • <#612384531999096832> play some bangers with <@630199558294470676>""", inline = False)
# await channelsMessage1.edit(embed = embed)

# channelsMessage2 = await bot.channelsChannel.fetch_message(790467697841274890)
# embed = discord.Embed(title = "Channels :computer:", color = 0xe67e22)
# embed.set_footer(text = "Server Channels", icon_url = bot.server.icon_url)
# embed.set_thumbnail(url = bot.server.icon_url)
# embed.add_field(name = "Text Channels Continued...", value = f"""
# • <#744374005280276522> verbally duel with another person
# • <#744374515328614421> weeb territory
# • <#777040210005065739> in the name, just don't be mad weird when it comes to nsfw
# • <#700074631935295532> academic related discussion
# • <#690647361139245136> count till the end of time and space
# • <#746951407546007643> auto-posted {bot.amongUsEmoji}, {bot.chessEmoji}, and {bot.krunkerEmoji} join codes/links
# • <#636071901906731010> use all bots
# • <#659885014603005953> minecraft creative world chat
# • <#693321555366903851> minecraft survival world chat""", inline = False)
# await channelsMessage2.edit(embed = embed)

# # await gameRolesMessage.add_reaction(bot.amongUsEmoji)
# # await gameRolesMessage.add_reaction(bot.chessEmoji)
# # await gameRolesMessage.add_reaction(bot.krunkerEmoji)
# # await gameRolesMessage.add_reaction(bot.minecraftEmoji)
# # await gameRolesMessage.add_reaction(bot.skribblEmoji)
# # await gameRolesMessage.add_reaction(bot.valorantEmoji)

# # await subjectRolesMessage.add_reaction("\U0001f9e0")
# # await subjectRolesMessage.add_reaction("\U0001f514")
# # await subjectRolesMessage.add_reaction("\U00000031\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000032\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000033\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000034\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000035\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000036\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000037\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000038\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U00000039\U0000fe0f\U000020e3")
# # await subjectRolesMessage.add_reaction("\U0001f51f")