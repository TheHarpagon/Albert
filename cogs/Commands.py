import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import humanize
import psutil
import pytz
import random

async def isStaff(ctx):
  return any(role in ctx.author.roles for role in [ctx.bot.adminRole, ctx.bot.moderatorRole])

async def isJuiceStaff(ctx):
  return ctx.bot.juiceRole in ctx.author.roles

class Commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(help = "Allahs a user", aliases = ["hijab"])
  async def allah(self, ctx, member: discord.Member):
    allah = self.bot.server.get_role(736358205994696846)
    if ctx.author.id == 320369001005842435 or ctx.author.id == 410590963379994639:
      if allah not in member.roles:
        if len(allah.members) < 10:
          await member.add_roles(allah)
          await ctx.send(f"{self.bot.checkmarkEmoji} {member.mention} is now allah :pray:")
        else:
          await ctx.send(f"{self.bot.errorEmoji} There can only be 10 hijabs at once")
      else:
        await ctx.send(f"{self.bot.errorEmoji} They already allah :face_with_raised_eyebrow:")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Shut the fuck up haram ass, this is only for virajallah")
  
  @commands.command(help = "Displays all users with the allah role", aliases = ["hijabs"])
  async def allahs(self, ctx):
    allah = self.bot.server.get_role(736358205994696846)
    output = ""
    for member in allah.members:
      output += f"\n{member.mention}"
      if member.id == 320369001005842435:
        output += " :crown:"
    embed = discord.Embed(title = f":pray: Allahs ({len(allah.members)}/10)", description = output, color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Displays all aso emotes")
  @commands.cooldown(1, 20, BucketType.default) 
  async def aso(self, ctx):
    output = ""
    for i in self.bot.emojis:
      if len(i.name) >= 4:
        if "so" in i.name[-2:]:
          output += f"{i}"
    await ctx.send(output)
  
  @commands.command(help = "Posts an Among Us code", aliases = ["au"])
  async def amongus(self, ctx, code):
    if len(code) == 6 and not any(char.isdigit() for char in code):
      await ctx.message.delete()
      embed = discord.Embed(title = f"{self.bot.amongUsEmoji} Among Us Code", description = f"`{code}`", color = 0xF21717, timestamp = datetime.utcnow())
      embed.set_footer(text = f"Posted by {ctx.author}", icon_url = ctx.author.avatar_url)
      embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/781258129329094666.png?v=1")
      await self.bot.joinGameChannel.send(embed = embed)
      await ctx.send(f"{self.bot.checkmarkEmoji} Posted in {self.bot.joinGameChannel.mention}")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Invalid code")
    
  @commands.command(help = "Bans a user")
  @commands.check(isStaff)
  async def ban(self, ctx, member: discord.Member, *, reason = None):
    if self.bot.adminRole in member.roles or self.bot.moderatorRole in member.roles:
      await ctx.send(f"{self.bot.errorEmoji} You can't do that")
      return
    await member.ban(reason = reason)
    embed = discord.Embed(title = ":lock: Ban", description = f"User: {member.mention}\nReason: {reason}", color = 0xFF0000, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Posts a Chess link", aliases = ["c"])
  async def chess(self, ctx, link):
    if "play.chess.com/" in link:
      await ctx.message.delete()
      embed = discord.Embed(title = f"{self.bot.chessEmoji} Among Us Code", description = link, color = 0xF21717, timestamp = datetime.utcnow())
      embed.set_footer(text = f"Posted by {ctx.author}", icon_url = ctx.author.avatar_url)
      embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/781259278417395732.png?v=1")
      await self.bot.joinGameChannel.send(embed = embed)
      await ctx.send(f"{self.bot.checkmarkEmoji} Posted in {self.bot.joinGameChannel.mention}")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Invalid link")
  
  @commands.command(help = "Displays a hex code", aliases = ["colour"])
  @commands.cooldown(1, 5, BucketType.user)
  async def color(self, ctx, hexCode: discord.Color):
    embed = discord.Embed(title = ":trackball: Color", description = str(hexCode).lower(), color = hexCode, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = f"https://www.colorhexa.com/{str(hexCode).lower()[1:]}.png")
    await ctx.send(embed = embed)
  
  @commands.command(help = "Disables a command")
  @commands.is_owner()
  async def disable(self, ctx, command):
    self.bot.remove_command(command)
    await ctx.send(f"{self.bot.checkmarkEmoji} Disabled the `{command}` command")
  
  @commands.command(help = "DMs a user")
  @commands.cooldown(1, 10, BucketType.user)
  async def dm(self, ctx, member: discord.Member, *, message):
    if ctx.author.id == member.id:
      await ctx.send(f"{self.bot.errorEmoji} You can't DM yourself")
      return
    if member.bot == True:
      await ctx.send(f"{self.bot.errorEmoji} You can't DM a bot")
      return
    try:
      await member.send(f"{message}\n- from {ctx.author.mention}")
      await ctx.send(f"{self.bot.checkmarkEmoji} Sent!")
    except:
      await ctx.send(f"{self.bot.errorEmoji} That person has blocked me")
  
  @commands.command(help = "Enables a command")
  @commands.cooldown(1, 5, BucketType.user)
  async def enable(self, ctx, command):
    if ctx.author.id == 410590963379994639:
      self.bot.add_command(command)
      await ctx.send(f"{self.bot.checkmarkEmoji} Enabled the `{command}` command")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  @commands.command(help = "Flips a coin", aliases = ["coin", "coinflip", "flipcoin"])
  @commands.cooldown(1, 5, BucketType.user)
  async def flip(self, ctx):
    responses = {"Heads": "https://i.imgur.com/92xg7uR.png", "Tails": "https://i.imgur.com/TjqDdBI.png"}
    choice = random.choice(["Heads", "Tails"])
    embed = discord.Embed(title = ":coin: Flip a Coin", description = f"It's `{choice}`", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = responses[choice])
    await ctx.send(embed = embed)
  
  @commands.command(help = "Displays the server icon", aliases = ["servericon"])
  @commands.guild_only()
  @commands.cooldown(1, 5, BucketType.user)
  async def icon(self, ctx):
    embed = discord.Embed(title = ":frame_photo: Server Icon", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = ctx.guild.icon_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Displays invite links", aliases = ["inv"])
  @commands.cooldown(1, 5, BucketType.user)
  async def invite(self, ctx):
    embed = discord.Embed(title = ":inbox_tray: Invite Link", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_thumbnail(url = self.bot.user.avatar_url)
    embed.add_field(name = "Bot", value = "[Link](https://discord.com/api/oauth2/authorize?client_id=851538022356615208&permissions=134605888&scope=bot)", inline = False)
    embed.add_field(name = "Server", value = "discord.gg/uncle", inline = False)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  # todo
  @commands.command(help = "Displays the Minecraft server's info", aliases = ["mc", "mcip", "minecraft"])
  @commands.cooldown(1, 5, BucketType.user)
  async def ip(self, ctx):
    embed = discord.Embed(title = f"{self.bot.minecraftEmoji} Minecraft Server IPs", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    a = "<a:dndGIF:791185650996346891>"
    b = "<a:dndGIF:791185650996346891>"
    if self.bot.survivalServerBot.status is discord.Status.online:
      a = "<a:onlineGIF:791185651311575051>"
    # private server 2 bot status
    if self.bot.creativeServerBot.status is discord.Status.online:
      b = "<a:onlineGIF:791185651311575051>"
    embed.add_field(name = f"{a} Survival Server", value = "Version: `1.16.5`\nIP Address: `ballin-survival.ddns.net`\nBridged Chat: <#693321555366903851>", inline = False)
    embed.add_field(name = f"{b} Creative Server", value = "Version: `1.16.5`\nIP Address: `swiftspirit1408.aternos.me`\nBridged Chat: <#659885014603005953>", inline = False)
    embed.add_field(name = f"{self.bot.plusEmoji} How to Join", value = "• join the IP\n• DM the code you get to <@693313699779313734>\n• once you're in, do `/register <password>`", inline = False)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Juices a user", aliases = ["joose"])
  async def juice(self, ctx, member: discord.Member):
    juicer = self.bot.server.get_role(835703896713330699)
    if ctx.author.id in [410590963379994639, 335083840001540119, 394731512068702209, 612056767551111168]:
      if member.id == 639668920835375104:
        await ctx.send(f"{self.bot.errorEmoji} {member.mention} is haram as hell :face_with_raised_eyebrow:")
        return
      if juicer not in member.roles:
        await member.add_roles(juicer)
        await ctx.send(f"{self.bot.checkmarkEmoji} {member.mention} is now juicer :beverage_box:")
      else:
        await ctx.send(f"{self.bot.errorEmoji} They already juicer :face_with_raised_eyebrow:")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Man only owner and akshay ani uncles can do this")
  
  @commands.command(help = "Displays all juiced users", aliases = ["joosers"])
  async def juicers(self, ctx):
    juicer = self.bot.server.get_role(835703896713330699)
    output = ""
    for member in juicer.members:
      output += f"\n{member.mention}"
      if member.id in [410590963379994639, 335083840001540119, 394731512068702209]:
        output += " :crown:"
    embed = discord.Embed(title = f":beverage_box: Juicers ({len(juicer.members)})", description = output, color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Kicks a user")
  @commands.check(isStaff)
  async def kick(self, ctx, member: discord.Member, *, reason = None):
    if self.bot.adminRole in member.roles or self.bot.moderatorRole in member.roles:
      await ctx.send(f"{self.bot.errorEmoji} You can't do that")
      return
    await member.kick(reason = reason)
    embed = discord.Embed(title = ":soccer: Kick", description = f"User: {member.mention}\nReason: {reason}", color = 0xFF0000, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Shuts me down", aliases = ["die", "dropdead"])
  @commands.is_owner()
  async def kill(self, ctx):
    await ctx.send(f"{self.bot.checkmarkEmoji} Jumping off a cliff!")
    await self.bot.close()
  
  @commands.command(help = "Posts a Krunker link", aliases = ["k"])
  @commands.cooldown(1, 5, BucketType.user)
  async def krunker(self, ctx, link):
    if "krunker.io/?game=" in link:
      await ctx.message.delete()
      embed = discord.Embed(title = f"{self.bot.krunkerEmoji} Krunker Link", description = link, color = 0xFEB938, timestamp = datetime.utcnow())
      embed.set_footer(text = f"Posted by {ctx.author}", icon_url = ctx.author.avatar_url)
      embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/699029209988726885.png?v=1")
      await self.bot.joinGameChannel.send(embed = embed)
      await ctx.send(f"{self.bot.checkmarkEmoji} Posted in {self.bot.joinGameChannel.mention}")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Invalid link")
  
  @commands.command(help = "Gives a user mod", aliases = ["promote"])
  @commands.cooldown(1, 5, BucketType.user)
  async def mod(self, ctx, member: discord.Member):
    permitted = [410590963379994639, 533167218838470666]
    if ctx.author.id in permitted:
      if self.bot.memberRole in member.roles:
        await member.remove_roles(self.bot.memberRole)
        await member.add_roles(self.bot.moderatorRole)
        embed = discord.Embed(title = "<:upvote:732640878145044623> Demoted", description = f"{member.mention} is now a {self.bot.moderatorRole.mention}", color = 0xe67e22, timestamp = datetime.utcnow())       
        embed.set_footer(text = f"Demoted by {ctx.author}", icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
        await self.bot.staffOnlyChannel.send(f"<:upvote:732640878145044623> {member.mention} was promoted")
      else:
        await ctx.send(f"{self.bot.errorEmoji} They are already a moderator")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  @commands.command(help = "Displays muted users", aliases = ["silenced", "banished"])
  @commands.cooldown(1, 5, BucketType.user)
  async def muted(self, ctx):
    output = ""
    for member in self.bot.mutedRole.members:
      output += f"{member.mention}\n"
    embed = discord.Embed(title = ":mute: Muted", description = f"{output}", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)

  @commands.command(help = "Sets your nickname", aliases = ["nickname", "setnick", "setnickname"])
  @commands.guild_only()
  @commands.cooldown(1, 5, BucketType.user)
  async def nick(self, ctx, *, nickname):
    if len(nickname) >= 1 and len(nickname) <= 32:
      await ctx.author.edit(nick = nickname)
      await ctx.send(f"{self.bot.checkmarkEmoji} Set your nickname to `{nickname}`")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Nicknames can only be up to `32` characters long!")
  
  @commands.command(help = "Displays a user's profile picture", aliases = ["avatar", "av", "pic", "picture"])
  @commands.cooldown(1, 5, BucketType.user)
  async def pfp(self, ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(title = ":frame_photo: Profile Picture", description = member.mention, color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Displays my latency among other statistics", aliases = ["latency", "statistics", "stats"])
  @commands.cooldown(1, 5, BucketType.user)
  async def ping(self, ctx):
    embed = discord.Embed(title = "🏓 Pong!", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.add_field(name = "Latency", value = f"`{round(self.bot.latency * 1000)}`ms", inline = True)
    embed.add_field(name = "Hardware", value = f"`{psutil.cpu_count()}` Cores \n`{round(psutil.cpu_percent())}`% CPU Usage \n`{round(psutil.virtual_memory().percent)}`% RAM Usage", inline = True)
    embed.add_field(name = "Last Restart", value = humanize.naturaltime(datetime.now() - self.bot.startTime), inline = True)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Displays your dong size", aliases = ["dong"])
  @commands.cooldown(1, 5, BucketType.user)
  async def pp(self, ctx):
    length = float(random.randint(0, 400)) / 10
    output = ""
    i = 0
    ratings = {8: "Atomlike", 16: "Smol", 24: "Average", 32: "Large", 40: "BBC"}
    index = 0
    
    for i in ratings:
      if length > i:
        index += 1
      else:
        break
    for i in range(round(length)):
     output += "="
    
    embed = discord.Embed(title = ":eggplant: PP Rater", description = f"8{output}D \n**Length:** `{round(length, 2)}` inches \n**Rating:** `{ratings[list(ratings.keys())[index]]}`", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Prays to allah", aliases = ["goatsacrifice"])
  @commands.cooldown(1, 15, BucketType.guild)
  async def pray(self, ctx):
    allah = self.bot.server.get_role(736358205994696846)
    if allah in ctx.author.roles:
      await ctx.send(":goat:")
      await asyncio.sleep(1)
      await ctx.send(":pray:")
      await asyncio.sleep(1)
      await ctx.send(":goat: :knife: :drop_of_blood:")
      await asyncio.sleep(1)
      await ctx.send(":weary: ALLAH THE ALMIGHTY")
    else:
      await ctx.send("haram ass you cant use this bs")
  
  # @commands.command()
  # @commands.cooldown(1, 5, BucketType.user)
  # async def profile(self, ctx, member: discord.Member = None):
  #   member = ctx.author if not member else member
  #   roleCount = len([role for role in member.roles]) - 1
  #   # roleCount = len(roleCount) - 1
  #   joinPosition = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)

  #   if member.bot == False:
  #     # main role
  #     if self.bot.adminRole in member.roles:
  #       topRole = self.bot.adminRole.mention
  #       topColor = self.bot.adminRole.color
  #     elif self.bot.moderatorRole in member.roles:
  #       topRole = self.bot.moderatorRole.mention
  #       topColor = self.bot.moderatorRole.color
  #     elif self.bot.memberRole or self.bot.mutedRole in member.roles:
  #       topRole = self.bot.memberRole.mention
  #       topColor = self.bot.memberRole.color
      
  #     # divider roles
  #     if self.bot.dividerOneRole in member.roles:
  #       roleCount = roleCount - 1
  #     if self.bot.dividerTwoRole in member.roles:
  #       roleCount = roleCount - 1
  #     if self.bot.dividerThreeRole in member.roles:
  #       roleCount = roleCount - 1

  #     # counter roles
  #     if self.bot.counterRookieRole in member.roles:
  #       topCounterRole = self.bot.counterRookieRole.mention
  #     elif self.bot.counterBronzeRole in member.roles:
  #       topCounterRole = self.bot.counterBronzeRole.mention
  #     elif self.bot.counterSilverRole in member.roles:
  #       topCounterRole = self.bot.counterSilverRole.mention
  #     elif self.bot.counterGoldRole in member.roles:
  #       topCounterRole = self.bot.counterGoldRole.mention
  #     elif self.bot.counterPlatinumRole in member.roles:
  #       topCounterRole = self.bot.counterPlatinumRole.mention
  #     elif self.bot.counterDiamondRole in member.roles:
  #       topCounterRole = self.bot.counterDiamondRole.mention
  #     elif self.bot.counterEmeraldRole in member.roles:
  #       topCounterRole = self.bot.counterEmeraldRole.mention
  #     else:
  #       topCounterRole = "`None`"

  #     # gameRoles = [bot.krunkerRole, bot.minecraftRole, bot.valorantRole, bot.amongUsRole]
      
  #     # output = ""
  #     # for i in gameRoles:
  #     #     if i in member.roles:
  #     #         output += gameRoles[i].mention
  #     # gameRoles = ""
      
  #     # if bot.krunkerRole in member.roles:
  #     #     gameRoles += f"\n{bot.krunkerRole.mention}"
      
  #     # if bot.minecraftRole in member.roles:
  #     #     gameRoles += f"\n{bot.minecraftRole.mention}"

  #     # if bot.valorantRole in member.roles:
  #     #     gameRoles += f"\n{bot.valorantRole.mention}"
      
  #     # if bot.amongUsRole in member.roles:
  #     #     gameRoles += f"\n{bot.amongUsRole.mention}"

  #     # else:
  #     #     gameRoles = "`None`"

  #     embed = discord.Embed(title=f":bust_in_silhouette: User Profile", description = f"`{member}`", color = topColor, timestamp = datetime.utcnow())
  #     embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  #     embed.set_thumbnail(url = member.avatar_url)
  #     embed.add_field(name = "Main Role", value = topRole, inline = True)
  #     embed.add_field(name = "Nickname", value = member.mention, inline = True)
  #     embed.add_field(name = "Role Count", value = f"`{roleCount}`", inline = True)
  #     embed.add_field(name = "Join Position", value = f"#`{joinPosition}`/`{len(self.bot.users)}`", inline = True)
  #     embed.add_field(name = "Top Countr Role", value = topCounterRole, inline = True)
  #     embed.add_field(name = "Game Roles", value = "Under Dev", inline = True)
  #     embed.add_field(name = "Account Creation", value = f"{member.created_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
  #     embed.add_field(name = "Server Joined", value = f"{member.joined_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
  #     await ctx.send(embed = embed)

  @commands.command(help = "Displays a user's profile", aliases = ["activity", "status", "user", "userinfo"])
  @commands.guild_only()
  @commands.cooldown(1, 5, BucketType.user)
  async def profile(self, ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(title = ":busts_in_silhouette: Profile", description = member.mention, color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    joinPos = sum(m.joined_at < member.joined_at for m in self.bot.server.members if m.joined_at is not None) + 1
    embed.add_field(name = f"Join", value = f"`{joinPos}` / `{len(self.bot.server.members)}`\n{humanize.naturaltime(datetime.now() - member.joined_at)}", inline = True)
    embed.add_field(name = f"Status", value = str(member.status).capitalize(), inline = True)
    if member.activities:
      activity = ""
      j = 1
      for i in member.activities:
        try:
          name = f"Spotify\nView more with `!spotify @{member.name}`" if i.type == discord.ActivityType.listening else f"{i.emoji} {i.name}" if i.emoji else i.name
          activity += f"Name: {name}"
          activity += f"\nDetails: {i.details}" if i.details else ""
          activity += f"\nState: {i.state}" if i.state else ""
          elapsed = int((datetime.now() - i.start).total_seconds())
          activity += f"\nElapsed: `{int(elapsed / 3600):02d}`:`{int((elapsed % 3600) / 60):02d}`:`{(elapsed % 60):02d}`"
        except:
          pass
        activity = "Error during retrieval" if not activity else activity
        embed.add_field(name = f"Activity ({j})", value = activity, inline = False)
        j += 1
        activity = ""
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Reacts with aso to a message")
  @commands.cooldown(1, 20, BucketType.default) 
  async def reactaso(self, ctx, msgID):
    try:
      message = await ctx.fetch_message(msgID)
    except:
      await ctx.send(f"{self.bot.errorEmoji} Invalid message ID")
    await ctx.message.clear_reactions()
    output = []
    for i in self.bot.emojis:
      if len(i.name) >= 4:
        if "so" in i.name[-2:]:
          output.append(i)
    for i in output:
      await message.add_reaction(i)
    await ctx.send(":neutral_face:")
  
  @commands.command(help = "Reloads an extension")
  @commands.is_owner()
  async def reload(self, ctx, *, module):
    try:
      self.bot.unload_extension(f"cogs.{module}")
      self.bot.load_extension(f"cogs.{module}")
    except Exception as e:
      await ctx.send(f"{self.bot.errorEmoji} An error occurred\n```{e}```")
    else:
      await ctx.send(f"{self.bot.checkmarkEmoji} Reloaded")
  
  @commands.command(help = "Sets my status")
  @commands.is_owner()
  async def setstatus(self, ctx, *, argument = None):
    if not argument:
      await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{self.bot.memberCount()} Members • !help"))
      await ctx.send(f"{self.bot.checkmarkEmoji} Set!")
    else:
      await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = argument))
      await ctx.send(f"{self.bot.checkmarkEmoji} Set!")
  
  @commands.command(help = "Displays a user's spotify status", aliases = ["music"])
  @commands.guild_only()
  @commands.cooldown(1, 5, BucketType.user)
  async def spotify(self, ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    listening = False
    if member.activities:
      for i in member.activities:
        if i.type == discord.ActivityType.listening:
          listening = True
          activity = i
          break
    if not listening:
      await ctx.send(f"{self.bot.errorEmoji} Can't detect {'your' if member == ctx.author else 'their'} listening status")
      return
    passed = int((datetime.now() - activity.start).total_seconds())
    total = int((activity.end - activity.start).total_seconds())
    duration = list("▱▱▱▱▱▱▱▱")
    for i in range(int((passed / total) * len(duration))):
      duration[i] = "▰"
    embed = discord.Embed(title = "<:spotify:841831747867377684> Spotify", description = member.mention, color = activity.color, timestamp = datetime.utcnow())
    embed.add_field(name = "Title", value = f"[{activity.title}](https://open.spotify.com/track/{activity.track_id})", inline = True)
    embed.add_field(name = f"Artist{'s' if len(activity.artists) > 1 else ''}", value = ", ".join(activity.artists), inline = True)
    embed.add_field(name = "Album", value = activity.album, inline = True)
    embed.add_field(name = "Timestamp", value = f"```yaml\n{int(passed / 60)}:{(passed % 60):02d} / {int(total / 60)}:{(total % 60):02d}```", inline = True)
    embed.add_field(name = "Duration", value = f"```yaml\n{''.join(duration)}```", inline = True)
    embed.set_image(url = activity.album_cover_url)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Unallahs a user", aliases = ["unhijab"])
  async def unallah(self, ctx, member: discord.Member):
    allah = self.bot.server.get_role(736358205994696846)
    if (ctx.author.id == 320369001005842435 and allah in ctx.author.roles) or ctx.author.id == 410590963379994639:
      if allah in member.roles:
        await member.remove_roles(allah)
        await ctx.send(f"{self.bot.checkmarkEmoji} {member.mention} is not allah anymore :angry:")
      else:
        await ctx.send(f"{self.bot.errorEmoji} {member.mention} is not even allah you dumd :face_with_raised_eyebrow:")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Shut the fuck up haram ass, this is only for virajallah")
  
  @commands.command(help = "Unjuices a user", aliases = ["unjoose"])
  async def unjuice(self, ctx, member: discord.Member):
    juicer = self.bot.server.get_role(835703896713330699)
    if ctx.author.id in [410590963379994639, 335083840001540119, 394731512068702209, 612056767551111168]:
      if juicer in member.roles:
        await member.remove_roles(juicer)
        await ctx.send(f"{self.bot.checkmarkEmoji} {member.mention} is not juicer anymore :angry:")
      else:
        await ctx.send(f"{self.bot.errorEmoji} They ain't even juicer :face_with_raised_eyebrow:")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Man only owner and akshay ani uncles can do this")
  
  @commands.command(help = "Removes mod from a user", aliases = ["demod", "demote"])
  async def unmod(self, ctx, member: discord.Member):
    permitted = [410590963379994639, 533167218838470666]
    if ctx.author.id in permitted:
      if self.bot.moderatorRole in member.roles:
        await member.remove_roles(self.bot.moderatorRole)
        await member.add_roles(self.bot.memberRole)
        embed = discord.Embed(title = "<:downvote:732640878249902161> Demoted", description = f"{member.mention} is now a {self.bot.memberRole.mention}", color = 0xe67e22, timestamp = datetime.utcnow())       
        embed.set_footer(text = f"Demoted by {ctx.author}", icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
        await self.bot.staffOnlyChannel.send(f"<:downvote:732640878249902161> {member.mention} was demoted")
      else:
        await ctx.send(f"{self.bot.errorEmoji} They aren't even a moderator")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  # @command.command()
  # @commands.cooldown(1, 5, BucketType.user)
  # async def vc(ctx, argument):
  #   if self.bot.adminRole in ctx.author.roles or self.bot.moderatorRole in ctx.author.roles:
  #     channel = ctx.message.author.voice.channel
  #     if channel is not None:
  #       members = channel.members
  #       if argument.lower() == "mute":
  #         for member in members:
  #             await member.edit(mute = True)
  #         await ctx.send(f"{self.bot.checkmarkEmoji} Server Muted everyone in **{(channel.mention - "#")}**")
  #       if argument.lower() == "unmute":
  #         for member in members:
  #             await member.edit(mute = False)
  #             await ctx.send(f"{self.bot.checkmarkEmoji} Server Unmuted everyone in **{(channel.mention - "#")}**")
  #       else:
  #         await ctx.send(f"{self.bot.errorEmoji} Invalid Argument!")
  #     else:
  #       await ctx.send(f"{self.bot.errorEmoji} You have to be in a voice channel to use this command!")
  #   else:
  #     await ctx.send(f"{self.bot.errorEmoji} You do not have access to use this command!")

def setup(bot):
  bot.add_cog(Commands(bot))