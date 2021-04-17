from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import psutil
import pytz
import random

class Commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(aliases = ["hijab"])
  async def allah(self, ctx, member: discord.Member):
    await ctx.trigger_typing()
    allah = self.bot.server.get_role(736358205994696846)
    if (ctx.author.id == 320369001005842435 and allah in ctx.author.roles) or ctx.author.id == 410590963379994639:
      if len(allah.members) < 10:
        if allah not in member.roles:
          await member.add_roles(allah)
          await ctx.send(f"{member.mention} is now allah :pray:")
        else:
          await ctx.send("you retard they already allah :pray:")
      else:
        await ctx.send("there can only be 10 allahs at once :pray:")
    else:
      await ctx.send("shut up retard this is only for virajallah :pray:")
  
  @commands.command(aliases = ["hijabs"])
  async def allahs(self, ctx):
    await ctx.trigger_typing()
    allah = self.bot.server.get_role(736358205994696846)
    output = ""
    for member in allah.members:
      output += f"\n{member.mention}"
      if member.id == 320369001005842435:
        output += " :crown:"
    embed = discord.Embed(title = f":pray: Allahs {len(allah.members)}/10", description = output, color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(aliases = ["au"])
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
  
  @commands.command(aliases = ["c"])
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
  
  @commands.command()
  async def color(self, ctx, hexCode: discord.Color):
    embed = discord.Embed(title = ":trackball: Color Search", description = str(hexCode).lower(), color = hexCode, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = f"https://www.colorhexa.com/{str(hexCode).lower()[1:]}.png")
    await ctx.send(embed = embed)
  
  @commands.command()
  @commands.is_owner()
  async def disable(self, ctx, command):
    if ctx.author.id == 410590963379994639:
      self.bot.remove_command(command)
      await ctx.send(f"{self.bot.checkmarkEmoji} Disabled the `{command}` command")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  @commands.command()
  @commands.cooldown(1, 10, BucketType.user) 
  async def dm(self, ctx, member: discord.Member, *, message):
    await ctx.trigger_typing()
    if self.bot.vipRole in ctx.author.roles:
      await member.send(message + f"\n- from {ctx.author.mention}")
      await ctx.send(f"{self.bot.checkmarkEmoji} Sent!")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  @commands.command()
  @commands.cooldown(1, 5, BucketType.user) 
  async def enable(self, ctx, command):
    if ctx.author.id == 410590963379994639:
      self.bot.add_command(command)
      await ctx.send(f"{self.bot.checkmarkEmoji} Enabled the `{command}` command")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  @commands.command(aliases = ["coinflip"])
  async def flip(self, ctx):
    await ctx.trigger_typing()
    responses = {"Heads": "https://i.imgur.com/92xg7uR.png", "Tails": "https://i.imgur.com/TjqDdBI.png"}
    choice = random.choice(["Heads", "Tails"])
    embed = discord.Embed(title = "<:discord_coin:728695789316210860> Flip a Coin", description = f"It's `{choice}`", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = responses[choice])
    await ctx.send(embed = embed)
  
  # @commands.command()
  # async def help(self, ctx):
  #   await ctx.trigger_typing()

  
  @commands.command(aliases = ["servericon"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def icon(self, ctx):
    embed = discord.Embed(title = ":frame_photo: Server Icon", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = self.bot.server.icon_url)
    await ctx.send(embed = embed)
  
  # invite command
  @commands.command(aliases = ["inv"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def invite(self, ctx):
    await ctx.trigger_typing()
    await ctx.send("discord.gg/fG8vTrj")
  
  @commands.command(aliases = ["mcip"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def ip(self, ctx):
    await ctx.trigger_typing()
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
  
  @commands.command()
  @commands.cooldown(1, 5, BucketType.user) 
  async def kill(self, ctx):
    await ctx.trigger_typing()
    if ctx.author.id == 410590963379994639:
      await ctx.send(f"{self.bot.checkmarkEmoji} Ending process! (start manually in repl)")
      await self.bot.close()
    else:
      await ctx.send(f"{self.bot.errorEmoji} You do not have access to use this command!")
  
  @commands.command(aliases = ["k"])
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
  
  @commands.command(aliases = ["minsleft", "bruh"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def left(self, ctx):
    # time.strftime("%I:%M %p")
    timezone = pytz.timezone("America/Los_Angeles")
    current = datetime.now(timezone)
    currentMinutes = (int(current.strftime("%H")) * 60) + (int(current.strftime("%M")))
    # adjust day if schedule is off
    day = current.isoweekday()
    inSession = False
    emoji = ""
    currentPeriod = ""
    minutesLeft = 0
    output = ""
    if day in self.bot.daySchedule:
      if day == 1 and 495 <= currentMinutes <= 765:
        inSession = True
        for i in self.bot.monTimesMinutes:
          if i > currentMinutes:
            minutesLeft = i - currentMinutes
            currentPeriod = list(self.bot.monTimesMinutes.values())[list(self.bot.monTimesMinutes.keys()).index(i) - 1]
            break
      elif day != 1 and 495 <= currentMinutes <= 915:
        inSession = True
        for i in self.bot.dayScheduleMinutes[day]:
          if i > currentMinutes:
            minutesLeft = i - currentMinutes
            currentPeriod = list(self.bot.dayScheduleMinutes[day].values())[list(self.bot.dayScheduleMinutes[day].keys()).index(i) - 1]
            break
      else:
        if currentMinutes <= 495:
          output = "School hasn't started yet"
        else:
          output = "School isn't in session"
    else:
      output = "My guy, it's the weekend :neutral_face:"

    if inSession:
      if "Passing" in currentPeriod:
        emoji = ":dividers:"
      elif "Lunch" in currentPeriod:
        emoji = ":dividers:"
      elif "Student Support" in currentPeriod:
        emoji = ":jigsaw:"
      else:
        emoji = ":books: Period"
      output = f"{emoji} `{currentPeriod}` has `{minutesLeft}` minutes left!"
      embed = discord.Embed(title = "<a:rotatingHourglass:817538734597341235> Time Left", description = output, color = 0xe67e22, timestamp = datetime.utcnow())
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
      await ctx.send(embed = embed)
    else:
      await ctx.send(f"{self.bot.errorEmoji} {output}")
  
  @commands.command(aliases = ["promote"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def mod(self, ctx, member: discord.Member):
    await ctx.trigger_typing()
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
  
  @commands.command(aliases = ["silenced", "banished"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def muted(self, ctx):
    output = ""
    for member in self.bot.mutedRole.members:
      output += f"{member.mention}\n"
    embed = discord.Embed(title = ":mute: Muted", description = f"{output}", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)

  @commands.command(aliases = ["nickname"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def nick(self, ctx, *, nickname):
    await ctx.trigger_typing()
    if len(nickname) >= 1 and len(nickname) <= 32:
      await ctx.author.edit(nick = nickname)
      await ctx.send(f"{self.bot.checkmarkEmoji} Your nickname was set to `{nickname}`!")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Nicknames can only be upto `32` characters long!")
  
  @commands.command(aliases = ["avatar", "av"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def pfp(self, ctx, member: discord.Member = None):
    await ctx.trigger_typing()
    member = ctx.author if not member else member
    embed = discord.Embed(title = ":frame_photo: Profile Picture", description = member.mention, color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(aliases = ["latency"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def ping(self, ctx):
    await ctx.trigger_typing()
    time = datetime.now() - self.bot.startTime
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

    embed = discord.Embed(title = "🏓 Pong!", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.add_field(name = ":signal_strength: Latency", value = f"`{round(self.bot.latency * 1000)}`ms", inline = True)
    embed.add_field(name = ":robot: Hardware", value = f"`{psutil.cpu_count()}` Cores \n`{round(psutil.cpu_percent())}`% CPU Usage \n`{round(psutil.virtual_memory().percent)}`% RAM Usage", inline = True)
    embed.add_field(name = ":chart_with_upwards_trend: Uptime", value = f"`{days}` {dunit} \n`{hours}` {hunit} \n`{minutes}` {munit} \n`{seconds}` {sunit}", inline = True)
    await ctx.send(embed = embed)
  
  @commands.command(aliases = ["dong"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def pp(self, ctx):
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

    embed = discord.Embed(title = ":eggplant: PP Rater", description = f"8{output}D \n**Length:** `{round(length, 2)}` inches \n**Rating:** `{rating}`", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command()
  @commands.cooldown(1, 5, BucketType.user) 
  async def profile(self, ctx, member: discord.Member = None):
    await ctx.trigger_typing()
    member = ctx.author if not member else member
    roleCount = len([role for role in member.roles]) - 1
    # roleCount = len(roleCount) - 1
    joinPosition = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)

    if member.bot == False:
      # main role
      if self.bot.adminRole in member.roles:
        topRole = self.bot.adminRole.mention
        topColor = self.bot.adminRole.color
      elif self.bot.moderatorRole in member.roles:
        topRole = self.bot.moderatorRole.mention
        topColor = self.bot.moderatorRole.color
      elif self.bot.memberRole or self.bot.mutedRole in member.roles:
        topRole = self.bot.memberRole.mention
        topColor = self.bot.memberRole.color
      
      # divider roles
      if self.bot.dividerOneRole in member.roles:
        roleCount = roleCount - 1
      if self.bot.dividerTwoRole in member.roles:
        roleCount = roleCount - 1
      if self.bot.dividerThreeRole in member.roles:
        roleCount = roleCount - 1

      # counter roles
      if self.bot.counterRookieRole in member.roles:
        topCounterRole = self.bot.counterRookieRole.mention
      elif self.bot.counterBronzeRole in member.roles:
        topCounterRole = self.bot.counterBronzeRole.mention
      elif self.bot.counterSilverRole in member.roles:
        topCounterRole = self.bot.counterSilverRole.mention
      elif self.bot.counterGoldRole in member.roles:
        topCounterRole = self.bot.counterGoldRole.mention
      elif self.bot.counterPlatinumRole in member.roles:
        topCounterRole = self.bot.counterPlatinumRole.mention
      elif self.bot.counterDiamondRole in member.roles:
        topCounterRole = self.bot.counterDiamondRole.mention
      elif self.bot.counterEmeraldRole in member.roles:
        topCounterRole = self.bot.counterEmeraldRole.mention
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
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      embed.set_thumbnail(url = member.avatar_url)
      embed.add_field(name = "Main Role", value = topRole, inline = True)
      embed.add_field(name = "Nickname", value = member.mention, inline = True)
      embed.add_field(name = "Role Count", value = f"`{roleCount}`", inline = True)
      embed.add_field(name = "Join Position", value = f"#`{joinPosition}`/`{len(self.bot.users)}`", inline = True)
      embed.add_field(name = "Top Countr Role", value = topCounterRole, inline = True)
      embed.add_field(name = "Game Roles", value = "Under Dev", inline = True)
      embed.add_field(name = "Account Creation", value = f"{member.created_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
      embed.add_field(name = "Server Joined", value = f"{member.joined_at.strftime('`%a`, `%B` `%#d`, `%Y`')}", inline = True)
      await ctx.send(embed = embed)
  
  @commands.command()
  @commands.is_owner()
  @commands.cooldown(1, 5, BucketType.user) 
  async def randomperson(self, ctx):
    await ctx.trigger_typing()
    await ctx.send(f"{random.choice(self.bot.sever.members).mention} is the random person!")
  
  # @commands.command()
  # @commands.cooldown(1, 10, BucketType.user)
  # async def rr(ctx):
  #   if ctx.author.id == 410590963379994639:
  #     message = await ctx.send("react to this message with anything to play russian roulette\none person is randomly muted\nneeds 4 ppl to activate")
  #     await message.add_reaction(self.bot.checkmarkEmoji)
  #     def check(reaction, user):
  #       return len(message.reactions) == 4
  #     try:
  #       reaction, user = await self.bot.wait_for("reaction_add", timeout = 15, check = check)
  #     except asyncio.TimeoutError:
  #       await message.edit(content = "not enough ppl reacted")
  #     else:
  #       allMembers = []
  #       for reaction in message.reactions:
  #         for user in reaction.users:
  #           allMembers.append(user.mention)
  #       mute(ctx, random.choice(random.choice(allMembers)), 1)

  #   else:
  #     await ctx.send("in testing")
  
  @commands.command(aliases = ["s"])
  @commands.cooldown(1, 5, BucketType.user) 
  async def schedule(self, ctx):
    await ctx.trigger_typing()
    embed = discord.Embed(title = ":bell: DVHS Bell Schedule", color = 0xe67e22, timestamp = datetime.utcnow())
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_image(url = "https://i.imgur.com/ES49tLo.jpg")
    await ctx.send(embed = embed)
  
  @commands.command()
  @commands.is_owner()
  async def setstatus(self, ctx, *, argument):
    await ctx.trigger_typing()
    if argument.lower() == "normal":
      await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{self.bot.userCount(1)} Members • !help"))
      await ctx.send(f"{self.bot.checkmarkEmoji} Set!")
    else:
      await self.bot.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = argument))
      await ctx.send(f"{self.bot.checkmarkEmoji} Set!")
  
  # @commands.command()
  # @commands.cooldown(1, 5, BucketType.user) 
  # async def test(ctx, username, password):
  #   if ctx.author.id == 410590963379994639:
  #     url = f"https://dvhs.schoolloop.com/mapi/login?version=3&devToken={uuid4()}&devOS=iPhone9,4&year={datetime.now().year}"
  #     result = requests.get(url, auth = HTTPBasicAuth(username, password))
  #     if result.status_code != 200:
  #       await ctx.send(result.text)
  #       return
  #     studentID = result.json().get("userID")
  #     url = f"https://dvhs.schoolloop.com/mapi/report_card?studentID={studentID}"
  #     result = requests.get(url, auth = HTTPBasicAuth(username, password))
  #     if result.status_code != 200:
  #       await ctx.send(result.text)
  #       return
  #     print(f"```json\n{result.json()}```")
  #   else:
  #     await ctx.send("no")
  
  @commands.command(aliases = ["unhijab"])
  async def unallah(self, ctx, member: discord.Member):
    await ctx.trigger_typing()
    allah = self.bot.server.get_role(736358205994696846)
    if (ctx.author.id == 320369001005842435 and allah in ctx.author.roles) or ctx.author.id == 410590963379994639:
      await member.remove_roles(allah)
      await ctx.send(f"{member.mention} is not allah anymore :angry:")
    else:
      await ctx.send("shut up retard this is only for virajallah :pray:")
  
  @commands.command(aliases = ["demod", "demote"])
  async def unmod(self, ctx, member: discord.Member):
    await ctx.trigger_typing()
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
  #   await ctx.trigger_typing()
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