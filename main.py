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

  bot.birthdayRole = s.get_role(references.birthdayRoleID)
  bot.adminRole = s.get_role(references.adminRoleID)
  bot.moderatorRole = s.get_role(references.moderatorRoleID)
  bot.mutedRole = s.get_role(references.mutedRoleID)
  bot.vipRole = s.get_role(references.vipRoleID)
  bot.potatoRole = s.get_role(references.potatoRoleID)
  bot.juiceRole = s.get_role(references.juiceRoleID)
  bot.memberRole = s.get_role(references.memberRoleID)
  bot.botRole = s.get_role(references.botRoleID)
  
  bot.dividerOneRole = s.get_role(references.dividerOneRoleID)
  
  
  bot.dividerTwoRole = s.get_role(references.dividerTwoRoleID)
  bot.chessRole = s.get_role(references.chessRoleID)
  bot.contentRole = s.get_role(references.contentRoleID)
  bot.krunkerRole = s.get_role(references.krunkerRoleID)
  bot.minecraftRole = s.get_role(references.minecraftRoleID)
  bot.politicsRole = s.get_role(references.politicsRoleID)
  bot.skribblRole = s.get_role(references.skribblRoleID)
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
  bot.plusEmoji = bot.get_emoji(references.plusEmojiID)
  bot.minusEmoji = bot.get_emoji(references.minusEmojiID)

  bot.gameRR = {"\U0000265f\U0000fe0f": bot.chessRole, "\U0001f37f": bot.contentRole, "\U0001f52b": bot.krunkerRole, "\U000026cf\U0000fe0f": bot.minecraftRole, "\U0001f453": bot.politicsRole, "🖍️": bot.skribblRole, "\U0001f399\U0000fe0f": bot.vcRole}

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
  print(f"Discord.py {discord.__version__}")
  print(f"Loading Cogs:")
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      bot.load_extension(f"cogs.{filename[:-3]}")
      print(f"- {filename}")
  await assignments()
  
  # afk reapplication
  for server in bot.guilds:
    for member in server.members:
      if str(member.id) in db:
        if not member.display_name.startswith("[AFK] "):
          del db[str(member.id)]
      else:
        if member.display_name.startswith("[AFK] "):
          db[str(member.id)] = [str(datetime.now()), None]
  
  tprint(bot.user.name)
  await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{bot.memberCount()} Members • !help"))
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

  # subjectRolesMessage = await bot.rolesChannel.fetch_message(759521601170833469)
  # embed = discord.Embed(title = "School Roles :books:", description = f"Pick up some roles for any subjects you take! \n\n:brain: {bot.helperRole.mention} \nto help anyone in immediate need \n:bell: {bot.bellScheduleRole.mention} \nto receive bell schedule pings \n\n:one: {bot.precalculusRole.mention} \n:two: {bot.apCalcABRole.mention} \n:three: {bot.apCalcBCRole.mention} \n:four: {bot.hPhysicsRole.mention} \n:five: {bot.apPhysicsRole.mention} \n:six: {bot.apBiologyRole.mention} \n:seven: {bot.rushRole.mention} \n:eight: {bot.apushRole.mention} \n:nine: {bot.vsNetRole.mention} \n:keycap_ten: {bot.apcsRole.mention}", color = 0xe67e22)
  # embed.set_footer(text = "Server Reaction Roles", icon_url = bot.server.icon_url)
  # embed.set_thumbnail(url = bot.server.icon_url)
  subjectRolesMessage = await bot.rolesChannel.fetch_message(759521601170833469)
  embed = discord.Embed(title = "School :books:", description = "Will be returning in August!", color = 0xe67e22)
  embed.set_thumbnail(url = bot.server.icon_url)
  await subjectRolesMessage.edit(embed = embed)

  gameRolesMessage = await bot.rolesChannel.fetch_message(759534246607585300)
  embed = discord.Embed(title = "Entertainment :video_game:", description = f"""Pick up some roles below!
  ♟️ {bot.chessRole.mention}
  🍿 {bot.contentRole.mention}
  🔫 {bot.krunkerRole.mention}
  ⛏️ {bot.minecraftRole.mention}
  👓 {bot.politicsRole.mention}
  🖍️ {bot.skribblRole.mention}
  🎙️ {bot.vcRole.mention}""", color = 0xe67e22)
  embed.set_thumbnail(url = bot.server.icon_url)
  await gameRolesMessage.edit(embed = embed)

  # for i in list(bot.gameRRDict.keys()):
  #   await gameRolesMessage.add_reaction(i)

keepAlive()
bot.run(os.environ["token"], bot = True, reconnect = True)