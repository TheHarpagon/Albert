from art import tprint
from datetime import datetime
import discord
from discord.ext import commands
from HelpCommand import HelpCommand
from keepAlive import keepAlive
import os
import references
from replit import db

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all(), case_insensitive = True)

bot.help_command = HelpCommand(command_attrs = {
   "name": "help",
   "help": "Displays this message",
   "aliases": ["info"],
   "cooldown": commands.Cooldown(1, 5, commands.BucketType.user)
})

async def assignments():
  s = bot.get_guild(references.serverID)
  bot.server = bot.get_guild(references.serverID)
  bot.welcomeChannel = bot.get_channel(references.welcomeChannelID)
  bot.rolesChannel = bot.get_channel(references.rolesChannelID)
  bot.rulesChannel = bot.get_channel(references.rulesChannelID)
  bot.logChannel = bot.get_channel(references.logChannelID)
  bot.generalChannel = bot.get_channel(references.generalChannelID)
  bot.vipChannel = bot.get_channel(references.vipChannelID)
  bot.botProfile = s.get_member(references.rolesChannelID)

  bot.adminRole = s.get_role(references.adminRoleID)
  bot.moderatorRole = s.get_role(references.moderatorRoleID)
  bot.mutedRole = s.get_role(references.mutedRoleID)
  bot.potatoRole = s.get_role(references.potatoRoleID)
  bot.juiceRole = s.get_role(references.juiceRoleID)
  bot.vipRole = s.get_role(references.vipRoleID)
  bot.memberRole = s.get_role(references.memberRoleID)
  bot.botRole = s.get_role(references.botRoleID)
  
  bot.dividerOneRole = s.get_role(references.dividerOneRoleID)
  
  bot.dividerTwoRole = s.get_role(references.dividerTwoRoleID)
  bot.csgoRole = s.get_role(references.csgoRoleID)
  bot.chessRole = s.get_role(references.chessRoleID)
  bot.fofRole = s.get_role(references.fofRoleID)
  bot.krunkerRole = s.get_role(references.krunkerRoleID)
  bot.minecraftRole = s.get_role(references.minecraftRoleID)
  bot.skribblRole = s.get_role(references.skribblRoleID)
  bot.tf2Role = s.get_role(references.tf2RoleID)
  bot.vcRole = s.get_role(references.vcRoleID)

  bot.dividerThreeRole = s.get_role(references.dividerThreeRoleID)
  bot.counterBronzeRole = s.get_role(references.counterBronzeRoleID)
  bot.counterSilverRole = s.get_role(references.counterSilverRoleID)
  bot.counterGoldRole = s.get_role(references.counterGoldRoleID)
  bot.counterDiamondRole = s.get_role(references.counterDiamondRoleID)
  bot.counterPlatinumRole = s.get_role(references.counterPlatinumRoleID)
  bot.counterBossRole = s.get_role(references.counterBossRoleID)

  bot.loadingEmoji = bot.get_emoji(references.loadingEmojiID)
  bot.errorEmoji = bot.get_emoji(references.errorEmojiID)
  bot.checkmarkEmoji = bot.get_emoji(references.checkmarkEmojiID)
  bot.minusEmoji = bot.get_emoji(references.minusEmojiID)
  bot.plusEmoji = bot.get_emoji(references.plusEmojiID)

  bot.gameRR = {"\U0001f4b8": bot.csgoRole, "\U0000265f\U0000fe0f": bot.chessRole, "\U0001f920": bot.fofRole, "\U0001f52b": bot.krunkerRole, "\U000026cf\U0000fe0f": bot.minecraftRole, "\U0001f58d\U0000fe0f": bot.skribblRole, "\U0001f3ed": bot.tf2Role, "\U0001f399\U0000fe0f": bot.vcRole}

  output = ""
  for i in bot.gameRR:
    output += f"{i} {bot.gameRR[i].mention}\n"

  gameRoles = await bot.rolesChannel.fetch_message(759534246607585300)
  embed = discord.Embed(title = "Entertainment :video_game:", description = output, color = 0xe67e22)
  embed.set_thumbnail(url = bot.server.icon_url)
  await gameRoles.edit(embed = embed)

  # alphabet = ["\U0001f1e6", "\U0001f1e7", "\U0001f1e8", "\U0001f1e9", "\U0001f1ea", "\U0001f1eb", "\U0001f1ec", "\U0001f1ed", "\U0001f1ee", "\U0001f1ef", "\U0001f1f0", "\U0001f1f1", "\U0001f1f2", "\U0001f1f3", "\U0001f1f4", "\U0001f1f5", "\U0001f1f6", "\U0001f1f7", "\U0001f1f8", "\U0001f1f9", "\U0001f1fa", "\U0001f1fb", "\U0001f1fc", "\U0001f1fd", "\U0001f1fe", "\U0001f1ff"]
  bot.schoolRR = {"\U0001f1e6": bot.server.get_role(875898934332112906), "\U0001f1e7": bot.server.get_role(875898978875613215), "\U0001f1e8": bot.server.get_role(875899842914824223), "\U0001f1e9": bot.server.get_role(875899034127200306), "\U0001f1ea": bot.server.get_role(875899716544655390), "\U0001f1eb": bot.server.get_role(875899805098983474), "\U0001f1ec": bot.server.get_role(876998184990285874), "\U0001f1ed": bot.server.get_role(879055606487601172), "\U0001f1ee": bot.server.get_role(875182522684813382), "\U0001f1ef": bot.server.get_role(875899099994525736), "\U0001f1f0": bot.server.get_role(875899618209202177), "\U0001f1f1": bot.server.get_role(875899569534296074), "\U0001f1f2": bot.server.get_role(875899898430619728), "\U0001f1f3": bot.server.get_role(875900086402560051), "\U0001f1f4": bot.server.get_role(875900126231683082), "\U0001f1f5": bot.server.get_role(875899957029253170), "\U0001f1f6": bot.server.get_role(875899675746631760), "\U0001f1f7": bot.server.get_role(877388019513061446)}
  
  output = ""
  for i in bot.schoolRR:
    output += f"{i} {bot.schoolRR[i].mention}\n"

  subjectRoles = await bot.rolesChannel.fetch_message(759521601170833469)
  embed = discord.Embed(title = "School Roles :books:", description = output, color = 0xe67e22)
  embed.set_thumbnail(url = bot.server.icon_url)
  await subjectRoles.edit(embed = embed)

  for i in list(bot.gameRR.keys()):
    await gameRoles.add_reaction(i)
  for i in list(bot.schoolRR.keys()):
    await subjectRoles.add_reaction(i)

  def memberCount():
    return len([member for member in bot.get_all_members() if not member.bot])
  bot.memberCount = memberCount

  def botCount():
    return len([member for member in bot.get_all_members() if member.bot])
  bot.botCount = botCount

  async def updateStatus():
    await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{bot.memberCount()} Members • !help"))
  bot.updateStatus = updateStatus


# bot startup event
@bot.event
async def on_ready():
  print(f"DPY Version: {discord.__version__}")
  print("Loading Assignments:")
  await assignments()
  print(f"✅ Loaded\nLoading Cogs:")
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      bot.load_extension(f"cogs.{filename[:-3]}")
      print(f"✅ {filename}")
  
  # afk reapplication
  for member in bot.server.members:
    if str(member.id) in db:
      if not member.display_name.startswith("[AFK] "):
        del db[str(member.id)]
    else:
      if member.display_name.startswith("[AFK] "):
        db[str(member.id)] = [str(datetime.now()), None]
  
  tprint(bot.user.name)
  bot.updateStatus
  bot.startTime = datetime.now()
  
  rulesMessage = await bot.rulesChannel.fetch_message(790036264648441897)
  embed = discord.Embed(title = "Rules :scroll:", color = 0xe67e22)
  embed.set_thumbnail(url = bot.server.icon_url)
  embed.add_field(name = "Common Sense", value = f"""
  • no nsfw
  • no self promo
  • follow [Discord TOS](https://discord.com/terms)
  • do not diss <@533153734373539840>
  • have some [common sense](https://youtu.be/YSDTPPM9qsc)
  • avoid being blatantly offensive
  • no annoying/unnecessary pinging
  • don't be an asshole/annoying person
  • use the right channel for your topic of discussion""", inline = False)
  embed.add_field(name = "More Info", value = f"""
  • run `!help` to see server commands
  • staff can mute at their own discretion
  • ignorance of the rules above is not a valid excuse
  • rules for the Minecraft SMP pinned in <#693321555366903851>""", inline = False)
  await rulesMessage.edit(embed = embed)

keepAlive()
bot.run(os.environ["token"], bot = True, reconnect = True)