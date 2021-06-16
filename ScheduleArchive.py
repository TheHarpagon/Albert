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