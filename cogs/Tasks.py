from datetime import datetime
import discord
from discord.ext import commands, tasks
import pytz

class Tasks(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bellSchedule.start()
    
  @tasks.loop(minutes = 1)
  async def bellSchedule(self):
    timezone = pytz.timezone("America/Los_Angeles")
    time = datetime.now(timezone)
    stringTime = time.strftime("%I:%M %p")
    # adjust day if schedule is off
    day = time.isoweekday() + 1
    if day in self.bot.daySchedule:
      if stringTime in self.bot.daySchedule[day]:
        output = ""
        ping = False
        if "Passing" in self.bot.daySchedule[day][stringTime]:
          output = ":dividers: "
        elif "Lunch" in self.bot.daySchedule[day][stringTime]:
          output = ":dividers: "
        elif "Student Support" in self.bot.daySchedule[day][stringTime]:
          output = ":jigsaw: "
          ping  = True
        else:
          output = "Period "
          ping = True
        embed = discord.Embed(title = "<a:rotatingHourglass:817538734597341235> Reminder", description = output + f"`{self.bot.daySchedule[day][stringTime]}` starts in 5 minutes!", color = 0xe67e22, timestamp = datetime.utcnow())
        embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
        embed.set_thumbnail(url = "https://i.imgur.com/2SB21jS.png")
        if ping:
          await self.bot.generalChannel.send(self.bot.bellScheduleRole.mention, embed = embed)
          return
        await self.bot.generalChannel.send(embed = embed)

def setup(bot):
  bot.add_cog(Tasks(bot))