# # main.py assignments()
# bot.monTimes = {"08:10 AM": "A", "08:40 AM": "Passing", "08:45 AM": "1", "09:15 AM": "Passing","09:20 AM": "2", "09:50 AM": "Passing", "09:55 AM": "3", "10:25 AM": "Passing", "10:30 AM": "4", "11:00 AM": "Lunch", "11:30 AM": "Passing", "11:35 AM": "5", "12:05 PM": "Passing", "12:10 PM": "6"}
# bot.tuesThursTimes = {"09:35 AM": "1", "10:50 AM": "Passing", "11:05 AM": "3", "12:20 PM": "Lunch", "12:55 PM": "Passing", "01:05 PM": "5", "02:20 PM": "Passing", "02:30 PM": "Student Support"}
# bot.wedFriTimes = {"08:10 AM": "A", "09:25 AM": "Passing", "09:35 AM": "2", "10:50 AM": "Passing", "11:05 AM": "4", "12:20 PM": "Lunch", "12:55 PM": "Passing", "01:05 PM": "6", "02:20 PM": "Passing", "02:30 PM": "Student Support"}
# bot.daySchedule = {1: bot.monTimes, 2: bot.tuesThursTimes, 3: bot.wedFriTimes, 4: bot.tuesThursTimes, 5: bot.wedFriTimes}

# bot.monTimesMinutes = {495: "A", 525: "Passing", 530: "1", 560: "Passing", 565: "2", 595: "Passing", 600: "3", 630: "Passing", 635: "4", 665: "Lunch", 695: "Passing", 700: "5", 730: "Passing", 735: "6"}
# bot.tuesThursTimesMinutes = {580: "1", 655: "Passing", 670: "3", 745: "Lunch", 780: "Passing", 790: "5", 865: "Passing", 875: "Student Support"}
# bot.wedFriTimesMinutes = {495: "A", 570: "Passing", 580: "2", 655: "Passing", 670: "4", 745: "Lunch", 780: "Passing", 790: "6", 865: "Passing", 875: "Student Support"}
# bot.dayScheduleMinutes = {1: bot.monTimesMinutes, 2: bot.tuesThursTimesMinutes, 3: bot.wedFriTimesMinutes, 4: bot.tuesThursTimesMinutes, 5: bot.wedFriTimesMinutes}

# # cogs/Commands.py
# @commands.command(aliases = ["bruh"])
# @commands.cooldown(1, 5, BucketType.user) 
# async def left(self, ctx):
#   # time.strftime("%I:%M %p")
#   timezone = pytz.timezone("America/Los_Angeles")
#   current = datetime.now(timezone)
#   currentMinutes = (int(current.strftime("%H")) * 60) + (int(current.strftime("%M")))
#   print(currentMinutes)
#   # adjust day if schedule is off
#   day = 1
#   inSession = False
#   emoji = ""
#   currentPeriod = ""
#   minutesLeft = 0
#   output = ""
#   if day in self.bot.daySchedule:
#     if day == 1 and 495 <= currentMinutes <= 765:
#       inSession = True
#       for i in self.bot.monTimesMinutes:
#         if i > currentMinutes:
#           minutesLeft = i - currentMinutes
#           currentPeriod = list(self.bot.monTimesMinutes.values())[list(self.bot.monTimesMinutes.keys()).index(i) - 1]
#           break
#     elif day in [2, 4] and 580 <= currentMinutes <= 915:
#       inSession = True
#       for i in self.bot.dayScheduleMinutes[day]:
#         if i > currentMinutes:
#           minutesLeft = i - currentMinutes
#           currentPeriod = list(self.bot.dayScheduleMinutes[day].values())[list(self.bot.dayScheduleMinutes[day].keys()).index(i) - 1]
#           break
#     elif day in [3, 5] and 495 <= currentMinutes <= 915:
#       inSession = True
#       for i in self.bot.dayScheduleMinutes[day]:
#         if i > currentMinutes:
#           minutesLeft = i - currentMinutes
#           currentPeriod = list(self.bot.dayScheduleMinutes[day].values())[list(self.bot.dayScheduleMinutes[day].keys()).index(i) - 1]
#           break
#     else:
#       # change this
#       if currentMinutes <= 495:
#         output = "School hasn't started yet"
#       else:
#         output = "School isn't in session"
#   else:
#     output = "My guy, it's the weekend :neutral_face:"

#   if inSession:
#     if "Passing" in currentPeriod:
#       emoji = ":dividers:"
#     elif "Lunch" in currentPeriod:
#       emoji = ":dividers:"
#     elif "Student Support" in currentPeriod:
#       emoji = ":jigsaw:"
#     else:
#       emoji = ":books: Period"
#     output = f"{emoji} `{currentPeriod}` has `{minutesLeft}` minutes left!"
#     embed = discord.Embed(title = "<a:rotatingHourglass:817538734597341235> Time Left", description = output, color = 0xe67e22, timestamp = datetime.utcnow())
#     embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
#     embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
#     await ctx.send(embed = embed)
#   else:
#     await ctx.send(f"{self.bot.errorEmoji} {output}")

# @commands.command(aliases = ["s"])
# @commands.cooldown(1, 5, BucketType.user) 
# async def schedule(self, ctx):
#   embed = discord.Embed(title = ":bell: DVHS Bell Schedule", color = 0xe67e22, timestamp = datetime.utcnow())
#   embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
#   embed.set_image(url = "https://i.imgur.com/ES49tLo.jpg")
#   await ctx.send(embed = embed)

# # cogs/Tasks.py
# @tasks.loop(minutes = 1)
# async def bellSchedule(self):
#   timezone = pytz.timezone("America/Los_Angeles")
#   time = datetime.now(timezone)
#   stringTime = time.strftime("%I:%M %p")
#   # adjust day if schedule is off
#   day = 1
#   if day in self.bot.daySchedule:
#     if stringTime in self.bot.daySchedule[day]:
#       output = ""
#       ping = False
#       if "Passing" in self.bot.daySchedule[day][stringTime]:
#         output = ":dividers: "
#       elif "Lunch" in self.bot.daySchedule[day][stringTime]:
#         output = ":dividers: "
#       elif "Student Support" in self.bot.daySchedule[day][stringTime]:
#         output = ":jigsaw: "
#         ping = True
#       else:
#         output = "Period "
#         ping = True
#       embed = discord.Embed(title = "<a:rotatingHourglass:817538734597341235> Reminder", description = output + f"`{self.bot.daySchedule[day][stringTime]}` starts in 5 minutes!", color = 0xe67e22, timestamp = datetime.utcnow())
#       embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
#       embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
#       if ping:
#         await self.bot.generalChannel.send(self.bot.bellScheduleRole.mention, embed = embed)
#         return
#       await self.bot.generalChannel.send(embed = embed)

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
  
  # @commands.command(help = "Beta mute command")
  # @commands.is_owner()
  # async def tmute(self, ctx, member: discord.Member, duration = None):
  #   if ctx.author.id == 410590963379994639 or self.bot.moderatorRole not in member.roles:
  #     with open("cogs/mutes.json", "r") as file:
  #       data = json.load(file)
  #     if self.bot.mutedRole in member.roles:
  #       await ctx.send(f"{self.bot.errorEmoji} They are already muted")
  #       if str(member.id) not in data:
  #         data[str(member.id)] = [0, ctx.author.id, str(datetime.now())]
  #       return
  #     else:
  #       if duration:
  #         parsed = pytimeparse.parse(duration)
  #         if not parsed:
  #           await ctx.send(f"{self.bot.errorEmoji} Unable to parse duration (include an unit)")
  #           return
  #         if parsed > 43200 or parsed < 60:
  #           await ctx.send(f"{self.bot.errorEmoji} Set durations must be between `1m` and `12h`")
  #           return
  #         await member.remove_roles(self.bot.memberRole)
  #         await member.add_roles(self.bot.mutedRole)
  #         data[str(ctx.author.id)] = [parsed, ctx.author.id, str(datetime.now())]
  #         with open("cogs/mutes.json", "w") as file:
  #           json.dump(data, file, indent = 2)
  #         embed = discord.Embed(title = f":mute: Mute", description = f"Member: {member.mention}\nDuration: `{duration}`", color = 0xe67e22)
  #         embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #         await ctx.send(embed = embed)
  #         await asyncio.sleep(parsed)
  #         with open("cogs/mutes.json", "r") as file:
  #           data = json.load(file)
  #         try:
  #           del data[str(ctx.author.id)]
  #           with open("cogs/mutes.json", "w") as file:
  #             json.dump(data, file, indent = 2)
  #           embed = discord.Embed(title = f":loud_sound: Unmuted", description = f"Member: {member.mention}\nMuted by: {ctx.author.mention}\nDuration: {humanize.naturaltime(datetime.strptime(data[str(member.id)][2], '%Y-%m-%d %H:%M:%S.%f') - datetime.now())}", color = 0xe67e22)
  #           embed.set_footer(text = f"Unmuted automatically", icon_url = ctx.author.avatar_url)
  #           await ctx.send(embed = embed)
  #         except:
  #           pass
  #       else:
  #         data[str(ctx.author.id)] = [0, ctx.author.id, str(datetime.now())]
  #         with open("cogs/mutes.json", "w") as file:
  #           json.dump(data, file, indent = 2)
  #         await member.remove_roles(self.bot.memberRole)
  #         await member.add_roles(self.bot.mutedRole)
  #         data[str(member.id)] = [0, ctx.author.id, str(datetime.now())]
  #         with open("cogs/mutes.json", "w") as file:
  #           json.dump(data, file, indent = 2)
  #         embed = discord.Embed(title = f":mute: Mute", description = f"Member: {member.mention}\nDuration: `Infinity`", color = 0xe67e22)
  #         embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #         await ctx.send(embed = embed)
  #   else:
  #     await ctx.send(f"{self.bot.errorEmoji} This command is unapplicable to staff")
  #     return
  
  # @commands.command(help = "Beta unmute command")
  # @commands.is_owner()
  # async def tunmute(self, ctx, member: discord.Member):
  #   if ctx.author.id == 410590963379994639 or self.bot.moderatorRole not in member.roles:
  #     with open("cogs/mutes.json", "r") as file:
  #       data = json.load(file)
      
  #     if self.bot.mutedRole not in member.roles:
  #       try:
  #         del data[str(member.id)]
  #       except:
  #         pass
  #       embed = discord.Embed(title = f"{self.bot.errorEmoji} That person is already muted", color = 0xff383e)
  #       await ctx.send(embed = embed)
  #       return
      
  #     else:
  #         await member.remove_roles(self.bot.mutedRole)
  #         await member.add_roles(self.bot.memberRole)
  #         del data[str(ctx.author.id)]
  #         with open("cogs/mutes.json", "w") as file:
  #           json.dump(data, file, indent = 2)
  #         embed = discord.Embed(title = f":sound: Unmuted", description = f"Member: {member.mention}\nMuted by: {ctx.author.mention}\nDuration: {humanize.naturaltime(datetime.strptime(data[str(member.id)][2], '%Y-%m-%d %H:%M:%S.%f') - datetime.now())}", color = 0xe67e22)
  #         embed.set_footer(text = f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #         await ctx.send(embed = embed)
  #   else:
  #     embed = discord.Embed(title = f"{self.bot.errorEmoji} This command is unapplicable to staff", color = 0xff383e)
  #     await ctx.send(embed = embed)
  #     return

  # @commands.command(help = "Mutes a user", aliases = ["stfu"])
  # async def mute(self, ctx, user: str, mtime = None):
  #   mutes = {}
  #   muteDatabase = tinydb.TinyDB("cogs/muteDatabase.json")
  #   query = tinydb.Query()
  #   if mtime == None:
  #       mtime = -1

  #   member = ctx.message.mentions[0]
  #   vipStat = self.bot.vipRole in member.roles

  #   if float(mtime) > 0:
  #     mtime = float(mtime)

  #   if ((ctx.message.author.id == 410590963379994639) or (self.bot.moderatorRole in ctx.message.author.roles)) and (self.bot.memberRole not in ctx.message.author.roles):
  #     if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) == [] and (not ((self.bot.adminRole in member.roles) or (self.bot.moderatorRole in member.roles) or (self.bot.botRole in member.roles))):
  #         if mtime > 0:
  #           if mtime < 1:
  #             stime = round(mtime * 60)
  #             sunit = "seconds"                    

  #             if stime == 1:
  #               sunit = "second"
              
  #             embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{stime}` {sunit}", color = 0x00FF00)
  #             embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #             embed.set_thumbnail(url = member.avatar_url)
  #             await ctx.send(embed = embed)
            
  #           if mtime >= 60:
  #             htime = mtime / 60
  #             hunit = "hours"

  #             if htime == 1:
  #               hunit = "hour"
              
  #             embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{htime}` {hunit}", color = 0x00FF00)
  #             embed.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url)
  #             embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #             embed.set_thumbnail(url = member.avatar_url)
  #             await ctx.send(embed = embed)
            
  #           if (mtime >= 1) and (mtime < 60):
  #             munit = "minutes"
              
  #             if mtime == 1:
  #               munit = "minute"
              
  #             embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `{mtime}` {munit}", color = 0x00FF00)
  #             embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #             embed.set_thumbnail(url = member.avatar_url)
  #             await ctx.send(embed = embed)
          
  #         else:
  #           embed = discord.Embed(title = ":mute: Muted", description = f"{member.mention} was muted for `infinity` (`∞`)", color = 0x00FF00)
  #           embed.set_footer(text = f"Muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #           embed.set_thumbnail(url = member.avatar_url)
  #           await ctx.send(embed = embed)
          
  #         muteDatabase.insert({"id":(str(member.id) + " " + str(member.guild.id)), "expires":(mtime * 60)})
  #         await member.add_roles(self.bot.mutedRole)
  #         await member.remove_roles(self.bot.memberRole)
  #         if vipStat:
  #           await member.remove_roles(self.bot.vipRole)

  #         if mtime > 0:
  #           await asyncio.sleep(mtime*60)
            
  #           await member.remove_roles(self.bot.mutedRole)
  #           await member.add_roles(self.bot.memberRole)
  #           if vipStat:
  #             await member.add_roles(self.bot.vipRole)
              
  #           if muteDatabase.search(query.id == (str(member.id) + " " + str(member.guild.id))) != []:
  #             embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention}'s mute expired", color = 0x00FF00)
  #             embed.set_footer(text = f"Originally muted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #             embed.set_thumbnail(url = member.avatar_url)
  #             await ctx.send(embed = embed)
  #             muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
      
  #     else:
  #       if (self.bot.adminRole in member.roles) or (self.bot.moderatorRole in member.roles) or (self.bot.botRole in member.roles):
  #         await ctx.send(f"{self.bot.errorEmoji} This user cannot be muted")
      
  #       else:
  #         await ctx.send(f"{self.bot.errorEmoji} This user is already muted")
  #   else:
  #     await ctx.send(f"{self.bot.errorEmoji} Missing permissions")

  # @commands.command(help = "Unmutes a user", aliases = ["unstfu"])
  # async def unmute(self, ctx, user: str):
  #   mutes = {}
  #   muteDatabase = tinydb.TinyDB("cogs/muteDatabase.json")
  #   query = tinydb.Query()
  #   member = ctx.message.mentions[0]
  #   if (self.bot.adminRole in ctx.message.author.roles) or (self.bot.moderatorRole in ctx.message.author.roles):
  #     if self.bot.mutedRole in member.roles:
  #       await member.remove_roles(self.bot.mutedRole)
  #       if not self.bot.memberRole in member.roles:
  #         await member.add_roles(self.bot.memberRole)
  #       embed = discord.Embed(title = ":loud_sound: Unmuted", description = f"{member.mention} was unmuted", color = 0x00FF00)
  #       embed.set_footer(text = f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar_url)
  #       embed.set_thumbnail(url = member.avatar_url)
  #       await ctx.send(embed = embed)
      
  #     else:
  #       embed = discord.Embed(title = f"{self.bot.errorEmoji} Unable to Unmute", description = f"{member.mention} isn't even muted", color = 0xFF0000)
  #       embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  #       embed.set_thumbnail(url = member.avatar_url)
  #       await ctx.send(embed = embed)
      
  #     if not self.bot.memberRole in member.roles:
  #       await member.add_roles(self.bot.memberRole)
      
  #     muteDatabase.remove(query.id == (str(member.id) + " " + str(member.guild.id)))
    
  #   else:
  #     embed = discord.Embed(title = f"{self.bot.errorEmoji} Missing Permissions", description = f"Required Roles: \n• {self.bot.adminRole.mention} \n• {self.bot.moderatorRole.mention}", color = 0xFF0000)   
  #     embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  #     embed.set_thumbnail(url = member.avatar_url)
  #     await ctx.send(embed = embed)

  # @commands.command(help = "Kicks a user")
  # @commands.check(isStaff)
  # async def kick(self, ctx, member: discord.Member, *, reason = None):
  #   if self.bot.adminRole in member.roles or self.bot.moderatorRole in member.roles:
  #     await ctx.send(f"{self.bot.errorEmoji} You can't kick a staff member")
  #     return
  #   await member.kick(reason = reason)
  #   embed = discord.Embed(title = ":soccer: Kick", description = f"User: {member.mention}\nReason: {reason}", color = 0xFF0000)
  #   embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  #   embed.set_thumbnail(url = member.avatar_url)
  #   await ctx.send(embed = embed)

  # @commands.command(help = "Bans a user")
  # @commands.check(isStaff)
  # async def ban(self, ctx, member: discord.Member, *, reason = None):
  #   if self.bot.adminRole in member.roles or self.bot.moderatorRole in member.roles :
  #     await ctx.send(f"{self.bot.errorEmoji} You can't ban a staff member")
  #     return
  #   await member.ban(reason = reason, delete_message_days = 0)
  #   embed = discord.Embed(title = ":lock: Ban", description = f"User: {member.mention}\nReason: {reason}", color = 0xFF0000)
  #   embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
  #   embed.set_thumbnail(url = member.avatar_url)
  #   await ctx.send(embed = embed)