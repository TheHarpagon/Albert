import aiohttp
import asyncio
from datetime import datetime, timedelta
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import html2text
import humanize
import io
import json
from ordinal import ordinal
import portolan
import random
from replit import db
import tinydb
import uuid

async def isStaff(ctx):
  return True if ctx.author.id == 410590963379994639 or ctx.bot.moderatorRole in ctx.author.roles else False

class DatabaseCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(help = "Sets your AFK status", aliases = ["busy", "bye", "gn"])
  async def afk(self, ctx, *, message = None):
    if ctx.author.display_name.startswith("[AFK] "):
      return
    if not ctx.author.guild_permissions.administrator:
      if len(ctx.author.display_name) <= 26:
        await ctx.author.edit(nick = f"[AFK] {ctx.author.display_name}")
      else:
        await ctx.author.edit(nick = f"[AFK] {ctx.author.display_name[:-6]}")
    db[str(ctx.author.id)] = [str(ctx.message.created_at), message]
    text = f"{self.bot.checkmarkEmoji} Set your AFK"
    text += f"\n```{message}```" if message else ""
    await ctx.send(text)
  
  @commands.command(help = "Displays all AFKs")
  async def afks(self, ctx):
    output = ""
    for i in db:
      output += f"<@{i}>"
    embed = discord.Embed(title = ":spy: AFKs", description = output, color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  # migrated scan command to https://github.com/TheHarpagon/Holmes
  
  @commands.command(help = "Displays a ranodom fact", aliases = ["randomfact"])
  @commands.cooldown(1, 10, BucketType.user) 
  async def fact(self, ctx):
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    async with aiohttp.ClientSession() as session:
      async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as reply:
        data = await reply.json()
    embed = discord.Embed(title = ":book: Fact", description = f"{data['text']}", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await message.edit(content = None, embed = embed)
  
  @commands.command(help = "Sends a multiplayer quiz", aliases = ["f", "race", "r"])
  @commands.guild_only()
  @commands.cooldown(1, 5, BucketType.channel)
  async def fast(self, ctx):
    original = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    choice = random.randint(0, 2)

    def math():
      operation, numbers, answer = random.choice(["×", "/", "+", "-"]), [], 0
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
        while numbers[0] < numbers[1]:
          numbers = [random.randint(50, 100), random.randint(50, 100)]
        answer = numbers[0] - numbers[1]
      
      embed = discord.Embed(title = ":zap: Math Showdown", description = f"First to solve the following wins!\n```py\n{numbers[0]} {operation} {numbers[1]}```", color = 0xe67e22)
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      return [embed, answer]
    
    async def word():
      async with aiohttp.ClientSession() as session:
        async with session.get("https://random-word-api.herokuapp.com/word?number=1") as reply:
          data = await reply.json()
      answer = data[0][::-1]
      embed = discord.Embed(title = ":zap: Word Showdown", description = f"First to type the following backwards wins!\n```yaml\n{data[0]}```", color = 0xe67e22)
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      return [embed, answer]
    
    def find():
      wrong, correct = ":white_large_square:", ":brown_square:"
      table = [[wrong, wrong, wrong], [wrong, wrong, wrong], [wrong, wrong, wrong]]
      answerTable = [["1a", "1b", "1c"], ["2a", "2b", "2c"], ["3a", "3b", "3c"]]
      randChoice = [random.randint(0, 2), random.randint(0, 2)]
      row, column, answer = randChoice[0], randChoice[1], answerTable[randChoice[0]][randChoice[1]]
      table[row][column] = correct
      rowPH = ["`1`", "`2`", "`3`"]
      printedTable = "⠀⠀`A`⠀`B`⠀`C`\n"
      for i in range(0, 3):
        printedTable += f"`{rowPH[i]}` "
        for j in range(0, 3):
          printedTable += f"||{table[i][j]}|| "
        printedTable += "\n"
      embed = discord.Embed(title = ":zap: Bubble Wrap", description = f"First to type the location to the :brown_square: wins!\n(ex: `B2` or `2B`)\n\n{printedTable}", color = 0xe67e22)
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      return [embed, answer]
    
    pack = await [math, word, find][choice]() if choice == 1 else [math, word, find][choice]()
    await original.edit(content = None, embed = pack[0])
    
    def check(message):
      if choice == 2:
        return message.content.lower() in [pack[1], pack[1][::-1]] and message.channel == ctx.channel
      else:
        return message.content.lower() == str(pack[1]) and message.channel == ctx.channel
    try:
      message = await self.bot.wait_for("message", timeout = 15, check = check)
    except asyncio.TimeoutError:
      await original.edit(content = f"{self.bot.errorEmoji} Event has expired", embed = None)
    else:
      await message.add_reaction(self.bot.checkmarkEmoji)
      await ctx.send(f"{message.author.mention} wins!")
  
  @commands.command(help = "Displays your grades (read [here](https://pastebin.com/30DtnU4p))")
  @commands.cooldown(1, 20, BucketType.user) 
  async def grades(self, ctx, username, password):
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    if ctx.message.guild:
      await ctx.message.delete()
      embed = discord.Embed(title = ":books: Grades", description = f"You can't use this command here, please DM me and try again", color = 0xe67e22)
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      await message.edit(content = None, embed = embed)
      ctx.command.reset_cooldown(ctx)
      return
    async with aiohttp.ClientSession(auth = aiohttp.BasicAuth(username, password)) as session:
      async with session.get(f"https://dvhs.schoolloop.com/mapi/login?version=3&devToken={uuid.uuid4()}&devOS=iPhone9,4&year={datetime.now().year}") as reply:
        if reply.status != 200:
          if "user" in await reply.text():
            await message.edit(content = f"{self.bot.errorEmoji} Username not found")
          else:
            await message.edit(content = f"{self.bot.errorEmoji} Incorrect password")
          return
        studentDB = await reply.json(content_type = None)
      async with session.get(f"https://dvhs.schoolloop.com/mapi/report_card?studentID={studentDB['userID']}") as reply:
        resultDB = await reply.json(content_type = None)
    
    embed = discord.Embed(title = ":scroll: Grades", description = "Your grades/credentials are **never** saved (read [here](https://www.google.com/))", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    for i in resultDB:
      if i["courseName"] != "Access":
        period = "A" if i["period"] == "0" else i["period"]
        lastUpdated = "null" if i["lastUpdated"] == "null" else humanize.naturaltime(datetime.now() - datetime.strptime(i["lastUpdated"], "%m/%d/%y %I:%M %p"))
        embed.add_field(name = f"{period} - {i['courseName']}", value = f"Teacher: `{i['teacherName']}`\nGrade: `{i['grade']}` (`{i['score']}`)\nLast Updated: {lastUpdated}", inline = False)
    await message.edit(content = None, embed = embed)
  
  @commands.command(help = "Displays a random joke")
  @commands.cooldown(1, 10, BucketType.user) 
  async def joke(self, ctx):
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    async with aiohttp.ClientSession() as session:
      async with session.get("https://official-joke-api.appspot.com/jokes/random") as reply:
        data = await reply.json()
    embed = discord.Embed(title = ":book: A joke", description = f"**{data['setup']}**", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await message.edit(content = None, embed = embed)
    embed = discord.Embed(title = ":book: A joke", description = f"**{data['setup']}**\n{data['punchline']}", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await asyncio.sleep(2)
    await message.edit(content = None, embed = embed)

  @commands.command(help = "Mutes a user", aliases = ["stfu"])
  async def mute(self, ctx, user: str, mtime = None):
    mutes = {}
    muteDatabase = tinydb.TinyDB("cogs/muteDatabase.json")
    query = tinydb.Query()
    if mtime == None:
        mtime = -1

    member = ctx.message.mentions[0]
    vipStat = self.bot.vipRole in member.roles

    if float(mtime) > 0:
      mtime = float(mtime)

    if ((ctx.message.author.id == 410590963379994639) or (self.bot.moderatorRole in ctx.message.author.roles)) and (self.bot.memberRole not in ctx.message.author.roles):
      if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) == [] and (not ((self.bot.adminRole in member.roles) or (self.bot.moderatorRole in member.roles) or (self.bot.botRole in member.roles))):
          if mtime > 0:
            if mtime < 1:
              stime = round(mtime * 60)
              sunit = "seconds"                    

              if stime == 1:
                sunit = "second"
              
              embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{stime}` {sunit}", color = 0x00FF00)
              embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
              embed.set_thumbnail(url = member.avatar_url)
              await ctx.send(embed = embed)
            
            if mtime >= 60:
              htime = mtime / 60
              hunit = "hours"

              if htime == 1:
                hunit = "hour"
              
              embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{htime}` {hunit}", color = 0x00FF00)
              embed.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url)
              embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
              embed.set_thumbnail(url = member.avatar_url)
              await ctx.send(embed = embed)
            
            if (mtime >= 1) and (mtime < 60):
              munit = "minutes"
              
              if mtime == 1:
                munit = "minute"
              
              embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{mtime}` {munit}", color = 0x00FF00)
              embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
              embed.set_thumbnail(url = member.avatar_url)
              await ctx.send(embed = embed)
          
          else:
            embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `infinity` (`∞`)", color = 0x00FF00)
            embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
            embed.set_thumbnail(url = member.avatar_url)
            await ctx.send(embed = embed)
          
          muteDatabase.insert({"id":(str(member.id) + " " + str(member.guild.id)), "expires":(mtime * 60)})
          await member.add_roles(self.bot.mutedRole)
          await member.remove_roles(self.bot.memberRole)
          if vipStat:
            await member.remove_roles(self.bot.vipRole)

          if mtime > 0:
            await asyncio.sleep(mtime*60)
            
            await member.remove_roles(self.bot.mutedRole)
            await member.add_roles(self.bot.memberRole)
            if vipStat:
              await member.add_roles(self.bot.vipRole)
              
            if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) != []:
              embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention}'s mute expired", color = 0x00FF00)
              embed.set_footer(text = f"Originally muted by {ctx.author}", icon_url = ctx.author.avatar_url)
              embed.set_thumbnail(url = member.avatar_url)
              await ctx.send(embed = embed)
              muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
      
      else:
        if (self.bot.adminRole in member.roles) or (self.bot.moderatorRole in member.roles) or (self.bot.botRole in member.roles):
          await ctx.send(f"{self.bot.errorEmoji} This user cannot be muted")
      
        else:
          await ctx.send(f"{self.bot.errorEmoji} This user is already muted")
    else:
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
  
  @commands.command()
  async def test(self, ctx):
    print()
  
  @commands.command(help = "Strips off text from an attachment", aliases = ["read", "scan"])
  @commands.cooldown(1, 20, BucketType.user)
  async def ocr(self, ctx, engine = 2):
    message = await ctx.send(f"{self.bot.loadingEmoji} Scanning... (this will take a moment)")
    attachments = []
    if ctx.message.reference:
      reference = await ctx.fetch_message(ctx.message.reference.message_id)
      attachments.extend(reference.attachments)
    attachments.extend(ctx.message.attachments)

    if attachments:
      if engine not in [1, 2]:
        await message.edit(content = f"{self.bot.errorEmoji} Invalid engine, choose `1` or `2` (more info at https://ocr.space/ocrapi#ocrengine)")
        return
      
      for i in attachments:
        if i.size / 1000 <= 1024:
          async def process(url, apiKey, engine):
            payload = {"url": url, "apikey": apiKey, "OCREngine": engine}
            async with aiohttp.ClientSession() as session:
              async with session.post("https://api.ocr.space/parse/image", data = payload) as reply:
                return await reply.json()
          data = await process(i.url, "8031c0b2f488957", engine)
          if data["IsErroredOnProcessing"]:
            await message.edit(content = f"{self.bot.errorEmoji} An error occured (maybe try again with `!ocr {1 if engine == 2 else 2}`)\n```\n{data['ErrorMessage'][0]}```")
            return
          if not data["ParsedResults"][0]["ParsedText"]:
            await message.edit(content = f"{self.bot.errorEmoji} No text found (if this is an error, try again with `!ocr {1 if engine == 2 else 2}`)")
            return
          embed = discord.Embed(title = ":newspaper: Text Scanner", color = 0xe67e22)
          embed.add_field(name = "Details", value = f"Name: [{i.filename}]({i.url})\nSize: `{round(i.size / 1000, 2)}` kilobytes\nProcess: `{round(int(data['ProcessingTimeInMilliseconds']) / 1000, 2)}` seconds\nEngine: `{engine}` (see more [here](https://ocr.space/ocrapi#ocrengine))", inline = False)
          embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
          if len(data["ParsedResults"][0]["ParsedText"]) > 1024:
            await ctx.send(embed = embed, file = discord.File(io.StringIO(data["ParsedResults"][0]["ParsedText"]), filename = "results.txt"))
          else:
            embed.add_field(name = "Results", value = f"```\n{data['ParsedResults'][0]['ParsedText']}```", inline = False)
            await ctx.send(embed = embed)
        else:
          await ctx.send(content = f"{self.bot.errorEmoji} `{i.filename}` exceeds the `1024` kilobyte limit")
      await message.delete()
    else:
      await message.edit(content = f"{self.bot.errorEmoji} Try attaching/referencing something")
      ctx.command.reset_cooldown(ctx)
  
  # @commands.command(help = "Modifies a user's points for trivia", aliases = ["p"])
  # @commands.check(botOwner)
  # @commands.cooldown(1, 5, BucketType.user)
  # async def points(self, ctx, action, member: discord.Member, amount):
  #   if action.lower() == "add":
  #     if int(amount) > 0:
  #       with open("cogs/points.json", "r") as file:
  #           data = json.load(file)
  #           if str(member.id) not in data:
  #             data[str(member.id)] = int(amount)
  #           else:
  #             data[str(member.id)] += int(amount)
  #       with open("cogs/points.json", "w") as file:
  #         json.dump(data, file, indent = 2)
  #       await ctx.send(f"{self.bot.checkmarkEmoji} Added `{amount}` points to {member.mention}!")
  #     else:
  #       await ctx.send(f"{self.bot.errorEmoji} Enter an amount greater than `0`")
  #   elif action.lower() == "remove":
  #     if int(amount) > 0:
  #       with open("cogs/points.json", "r") as file:
  #         data = json.load(file)
  #         if str(member.id) in data:
  #           if data[str(member.id)] > 0:
  #             data[str(member.id)] -= int(amount)
  #           else:
  #             data[str(member.id)] = 0
  #       with open("cogs/points.json", "w") as file:
  #         json.dump(data, file, indent = 2)
  #       await ctx.send(f"{self.bot.checkmarkEmoji} Removed `{amount}` points from {member.mention}!")
  #     else:
  #       await ctx.send(f"{self.bot.errorEmoji} Enter an amount greater than `0`")
  #   else:
  #     await ctx.send(f"{self.bot.errorEmoji} Invalid argument")

  @commands.command(help = "Predicts your fortune", aliases = ["8ball"])
  @commands.cooldown(1, 10, BucketType.user)
  async def predict(self, ctx, *, question: str):
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    async with aiohttp.ClientSession() as session:
      async with session.get(f"https://8ball.delegator.com/magic/JSON/{question}") as reply:
        data = await reply.json()
    embed = discord.Embed(title = ":8ball: The Mighty 8Ball", color = 0xe67e22)
    embed.add_field(name = "Question", value = question, inline = False)
    embed.add_field(name = "Response", value = data["magic"]["answer"], inline = False)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = "https://i.imgur.com/LkSBSuR.gif")
    await message.edit(content = None, embed = embed)
  
  # @commands.command(help = "Displays the raw json for afk users")
  # async def rawafks(self, ctx):
  #   await ctx.send(f"```json\n{str(db)}```")
  
  @commands.command(help = "Roasts a user", aliases = ["burn", "insult"])
  @commands.cooldown(1, 10, BucketType.user)
  async def roast(self, ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member
    content = None if not member else member.mention
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    async with aiohttp.ClientSession() as session:
      async with session.get("https://evilinsult.com/generate_insult.php?lang=en&type=json") as reply:
        data = await reply.json()
    embed = discord.Embed(title = "<:pepeLaugh:812786514911428608> Insult", description = data["insult"], color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await message.edit(content = content, embed = embed)
  
  # @commands.command(help = "Shortens a URL", aliases = ["link", "short", "tiny"])
  # @commands.cooldown(1, 5, BucketType.user) 
  # async def shorten(self, ctx, *, URL: str):
  #   message = await ctx.send(f"{self.bot.loadingEmoji} Shortening URL...")
  #   tokensPool = "a9c21c045c5d62380a54a7d3a22b06d8e6396c1c"
  #   shortener = bitlyshortener.Shortener(token = tokensPool, max_cache = 256)
  #   URLs = [URL]
  #   shortenedURL = shortener.shorten_urls(URLs)
  #   print(shortenedURL)
  #   embed = discord.Embed(title = ":link: Shortened Link", description = shortenedURL[0], color = 0xe67e22)
  #   embed.set_footer(text = f"Requested by {ctx.author}", icon_url = self.bot.user.avatar_url)
  #   embed.set_thumbnail(url = "https://i.imgur.com/YmjXC7s.png")
  #   await message.edit(content = None, embed = embed)
  
  @commands.command(help = "Beta mute command", aliases = ["testmute"])
  @commands.is_owner()
  async def tmute(self, ctx, member: discord.Member, duration = None):
    if ctx.author.id == 410590963379994639 or self.bot.moderatorRole not in member.roles:
      if self.bot.mutedRole in member.roles:
        await ctx.send(f"{self.bot.errorEmoji} They are already muted")
        return
      with open("cogs/mutes.json", "r") as file:
        data = json.load(file)
      if str(member.id) in data:
        await ctx.send(f"{self.bot.errorEmoji} They are already muted")
      else:
        if duration:
          if duration[-1] in ["m", "h"]:
            seconds = 0
            time = {"m": 60, "h": 3600}
            if duration[-1] == "m":
              seconds = int(duration[:-1]) * 60
            elif duration[-1] == "h":
              seconds = int(duration[:-1]) * 3600
            await member.remove_roles(self.bot.vipRole, self.bot.memberRole)
            await member.add_roles(self.bot.mutedRole)
            await ctx.send(f"{self.bot.checkmarkEmoji} Muted for `{duration}`")
            data[str(ctx.author.id)] = (time[duration.lower()[-1]])
            with open("cogs/mutes.json", "w") as file:
              json.dump(data, file, indent = 2)
            await asyncio.sleep(seconds)
            with open("cogs/mutes.json", "r") as file:
              data = json.load(file)
            del data[str(ctx.author.id)]
            with open("cogs/mutes.json", "w") as file:
              json.dump(data, file, indent = 2)
          else:
            await ctx.send(f"{self.bot.errorEmoji} Invalid duration, use it as such\nex: `13m` or `0.75h`")
            return
        else:
          await member.remove_roles(self.bot.vipRole, self.bot.memberRole)
          await member.add_roles(self.bot.mutedRole)
          data[str(member.id)] = "infiniy"
          with open("cogs/mutes.json", "w") as file:
            json.dump(data, file, indent = 2)
          await ctx.send(f"{self.bot.checkmarkEmoji} Muted")
    else:
      await ctx.send(f"{self.bot.errorEmoji} You can't mute staff")
  
  @commands.command(help = "Displays the trivia leaderboard", aliases = ["lb", "leaderboard", "^"])
  @commands.cooldown(1, 10, BucketType.user)
  async def top(self, ctx):
    with open("cogs/points.json", "r") as file:
      data = json.load(file)
    data = dict(sorted(data.items(), key = lambda item: item[1]))
    data = dict(reversed(list(data.items())))
    lb = []
    for i in data:
      if ctx.author.id == int(i):
        lb.append(f"<@{i}> `{data[i]}` :arrow_left:")
      else:
        lb.append(f"<@{i}> `{data[i]}`")
    emojis = [":first_place:", ":second_place:", ":third_place:"]
    output = ""
    if len(lb) <= 15:
      for i in lb:
        if lb.index(i) <= 2:
          output += f"\n{emojis[lb.index(i)]} "
        else:
          output += f"\n**{ordinal(lb.index(i) + 1)} **"
        output += lb[lb.index(i)]
    else:
      for i in range(15):
        if i <= 2:
          output += f"\n{emojis[i]} "
        else:
          output += f"\n**{ordinal(i + 1)}** "
        output += lb[i]

    embed = discord.Embed(title = ":trophy: Leaderboard", description = f"Top 15 Trivia Command Users\nLevel up with `!trivia`\n{output}", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
  
  @commands.command(help = "Sends a singleplayer quiz", aliases = ["q", "question", "quiz", "t"])
  @commands.cooldown(1, 20, BucketType.user)
  async def trivia(self, ctx, difficulty: str = None):
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    difficulties = {"e": "easy", "m": "medium", "h": "hard"}
    points = {"easy": 1, "medium": 2, "hard": 3}

    if ctx.channel.id == 612059384721440791:
      await message.edit(content = f"{self.bot.errorEmoji} Not in general")
      return
    
    if difficulty:
      if difficulty[0].lower() in difficulties:
        difficulty = difficulties[difficulty[0].lower()]
      else:
        await message.edit(content = f"{self.bot.errorEmoji} You can only choose an `easy`, `medium`, or `hard` question")
        ctx.command.reset_cooldown(ctx)
        return
    else:
      difficulty = random.choice(list(difficulties.values()))
    
    async with aiohttp.ClientSession() as session:
      async with session.get(f"https://opentdb.com/api.php?amount=1&difficulty={difficulty}&type=multiple") as reply:
        data = await reply.json()

    category = html2text.html2text(data["results"][0]["category"]).replace("\n", "")
    question = html2text.html2text(data["results"][0]["question"]).replace("\n", "")
    choices = [html2text.html2text(data["results"][0]["correct_answer"]).replace("\n", "")]
    for i in data["results"][0]["incorrect_answers"]:
      choices.append(html2text.html2text(i).replace("\n", ""))
    random.shuffle(choices)
    correctIndex = choices.index(html2text.html2text(data["results"][0]["correct_answer"]).replace("\n", ""))
    reactionsList = ["🇦", "🇧", "🇨", "🇩"]
    embed = discord.Embed(title = ":student: Trivia", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nreact with your answer within `10` seconds", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    await message.edit(content = None, embed = embed)
    for i in reactionsList:
      await message.add_reaction(i)
    
    def check(reaction, user):
      return user == ctx.author and str(reaction.emoji) in reactionsList
    try:
      reaction, user = await self.bot.wait_for("reaction_add", timeout = 10, check = check)
    
    # expired
    except asyncio.TimeoutError:
      await message.clear_reactions()
      # points system
      with open("cogs/points.json", "r") as file:
        data = json.load(file)
      if str(ctx.author.id) in data:
        if data[str(ctx.author.id)] > 0:
          data[str(ctx.author.id)] -= 1
      with open("cogs/points.json", "w") as file:
        json.dump(data, file, indent = 2)
      
      reactionsList[correctIndex] = self.bot.checkmarkEmoji
      embed = discord.Embed(title = f":alarm_clock: Expired! (-{points[difficulty]} points)", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nview the global leaderboard with `!top`", color = 0xFF383E)
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      await message.edit(content = None, embed = embed)
    
    # responded
    else:
      await message.clear_reactions()
      # correct answer
      if reactionsList.index(str(reaction.emoji)) == correctIndex:
        # points system
        with open("cogs/points.json", "r") as file:
          data = json.load(file)
        if str(ctx.author.id) not in data:
          data[str(ctx.author.id)] = points[difficulty]
        else:
          data[str(ctx.author.id)] += points[difficulty]
        with open("cogs/points.json", "w") as file:
          json.dump(data, file, indent = 2)
        
        reactionsList[correctIndex] = self.bot.checkmarkEmoji
        embed = discord.Embed(title = f"{self.bot.checkmarkEmoji} Correct! (+{points[difficulty]} points)", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nview the global leaderboard with `!top`", color = 0x3FB97C)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await message.edit(content = None, embed = embed)
      
      # wrong answer
      else:
        # # points system
        # with open("cogs/points.json", "r") as file:
        #   data = json.load(file)
        # if str(ctx.author.id) in data:
        #   if data[str(ctx.author.id)] > points[difficulty]:
        #     data[str(ctx.author.id)] -= points[difficulty]
        #   else:
        #     data[str(ctx.author.id)] = 0
        #   with open("cogs/points.json", "w") as file:
        #     json.dump(data, file, indent = 2)
        # (-{points[difficulty]} points)
        
        reactionsList[reactionsList.index(str(reaction.emoji))] = self.bot.errorEmoji
        reactionsList[correctIndex] = self.bot.checkmarkEmoji
        embed = discord.Embed(title = f"{self.bot.errorEmoji} Incorrect!", description = f"**Category**: {category}\n**Difficulty**: {difficulty.capitalize()}\n**Question**: {question}\n\n{reactionsList[0]} {choices[0]}\n{reactionsList[1]} {choices[1]}\n{reactionsList[2]} {choices[2]}\n{reactionsList[3]} {choices[3]}\n\nview the global leaderboard with `!top`", color = 0xFF383E)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await message.edit(content = None, embed = embed)
  
  @commands.command(help = "Unmutes a user", aliases = ["unstfu"])
  async def unmute(self, ctx, user: str):
    mutes = {}
    muteDatabase = tinydb.TinyDB("cogs/muteDatabase.json")
    query = tinydb.Query()
    member = ctx.message.mentions[0]
    if (self.bot.adminRole in ctx.message.author.roles) or (self.bot.moderatorRole in ctx.message.author.roles):
      if self.bot.mutedRole in member.roles:
        await member.remove_roles(self.bot.mutedRole)
        if not self.bot.memberRole in member.roles:
          await member.add_roles(self.bot.memberRole)
        embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention} was unmuted", color = 0x00FF00)
        embed.set_footer(text = f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
      
      else:
        embed = discord.Embed(title = f"{self.bot.errorEmoji} Unable to Unmute", description = f"{member.mention} isn't even muted", color = 0xFF0000)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = member.avatar_url)
        await ctx.send(embed = embed)
      
      if not self.bot.memberRole in member.roles:
        await member.add_roles(self.bot.memberRole)
      
      muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
    
    else:
      embed = discord.Embed(title = f"{self.bot.errorEmoji} Missing Permissions", description = f"Required Roles: \n• {self.bot.adminRole.mention} \n• {self.bot.moderatorRole.mention}", color = 0xFF0000)   
      embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
      embed.set_thumbnail(url = member.avatar_url)
      await ctx.send(embed = embed)
  
  @commands.command(help = "Displays the weather for a city")
  @commands.cooldown(1, 20, BucketType.user) 
  async def weather(self, ctx, *, city = None):
    message = await ctx.send(f"{self.bot.loadingEmoji} Loading...")
    if not city: city = "San Ramon"
    async with aiohttp.ClientSession() as session:
      async with session.get(f"http://api.openweathermap.org/data/2.5/weather?appid=e83935ef7ce7823925eeb0bfd2db3f7f&q={city}") as reply:
        data = await reply.json()
    
    if data["cod"] == "404":
      await message.edit(content = f"{self.bot.errorEmoji} Invalid city")
      return
    
    sunrise = datetime.fromtimestamp(int(data["sys"]["sunrise"])) - timedelta(hours = 7)
    sunset = datetime.fromtimestamp(int(data["sys"]["sunset"])) - timedelta(hours = 7)
    embed = discord.Embed(title = ":partly_sunny: Weather", color = 0xe67e22)
    embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
    embed.set_thumbnail(url = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png")
    embed.add_field(name = "City", value = f"`{data['name']}`, `{data['sys']['country']}`", inline = True)
    embed.add_field(name = "Condition", value = f"`{(data['weather'][0]['description']).title()}`", inline = True)
    embed.add_field(name = "Cloudiness", value = f"`{data['clouds']['all']}`%", inline = True)
    embed.add_field(name = "Temperature", value = f"`{round((1.8 * ((data['main']['temp']) - 273.15)) + 32)}`°F", inline = True)
    embed.add_field(name = "Humidity", value = f"`{data['main']['humidity']}`%", inline = True)
    embed.add_field(name = "Wind", value = f"`{round((data['wind']['speed'] * 2.24), 1)}`mph `{portolan.abbr(degree = data['wind']['deg'])}`", inline = True)
    embed.add_field(name = "Sunrise", value = f"{sunrise.strftime('`%I`:`%M` `%p`')} PST", inline = True)
    embed.add_field(name = "Sunset", value = f"{sunset.strftime('`%I`:`%M` `%p`')} PST", inline = True)
    await message.edit(content = None, embed = embed)
  
  # @commands.command(help = "Produces a URL for an attachment")
  # @commands.cooldown(1, 15, BucketType.user) 
  # async def upload(self, ctx):
  #   message = await ctx.send(f"{self.bot.loadingEmoji} Loading... (this will take a bit)")
  #   if ctx.message.attachments:
  #     for i in ctx.message.attachments:
  #       # 71cc188d6f0ff7d6ba026bccb2a9b585

  #       embed = discord.Embed(title = ":desktop: Uploaded File", description = "", color = 0xe67e22)
  #       embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  #       await message.edit(content = None, embed = embed)
  #   else:
  #     await message.edit(content = f"{self.bot.errorEmoji} Try attaching something")

def setup(bot):
  bot.add_cog(DatabaseCommands(bot))