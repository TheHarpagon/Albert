import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure, CommandOnCooldown, CommandNotFound
import humanize
import ordinal
from replit import db

class Events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_command_completion(self, ctx):
    print(f"✅　{ctx.command.name.upper()} Command")
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, CheckFailure):
      await ctx.send(embed = discord.Embed(title = f"{self.bot.errorEmoji} You're missing permissions", color = 0xFF0000))
    elif isinstance(error, CommandOnCooldown):
      await ctx.send(embed = discord.Embed(title = f"{self.bot.errorEmoji} You're on cooldown", description = f"Please wait another `{round(error.retry_after, 2)}` seconds", color = 0xFF0000))
    elif not isinstance(error, CommandNotFound):
      await ctx.send(embed = discord.Embed(title = f"{self.bot.errorEmoji} An error occurred", description = error, color = 0xFF0000))
    print(f"❌‎‎‎　ERROR ({error})")

  @commands.Cog.listener()
  async def on_member_update(self, before, after):
    if before.display_name[:6] == "[AFK] " and after.display_name[:6] != "[AFK] ":
      try:
        del db[str(after.id)]
      except:
        pass
    elif before.display_name[:6] != "[AFK] " and after.display_name[:6] == "[AFK] ":
      db[str(after.id)] = [str(datetime.now()), None]
  
  @commands.Cog.listener()
  async def on_message(self, message):
    # afk user returns
    ctx = await self.bot.get_context(message)
    if not any(alias in str(ctx.command) for alias in ["afk", "busy", "bye", "gn"]):
      if str(message.author.id) in db:
        del db[str(message.author.id)]
        if message.author.id != 410590963379994639:
          await message.author.edit(nick = message.author.display_name[6:])
        embed = discord.Embed(title = ":wave: Welcome back, removed your AFK", color = 0xe67e22)
        reply = await message.reply(embed = embed)
        await asyncio.sleep(3)
        await reply.delete()
        print("✅　AFK RETURN Event")

    # afk user mentioned
    if message.mentions:
      for i in message.mentions:
        if str(i.id) in db:
          time = datetime.now() - datetime.strptime(db[str(i.id)][0], '%Y-%m-%d %H:%M:%S.%f')
          embed = discord.Embed(title = ":spy: AFK", description = i.mention, color = 0xe67e22)
          embed.set_thumbnail(url = i.avatar_url)
          embed.add_field(name = "Set", value = humanize.naturaltime(time), inline = True)
          # w/o message
          if db[str(i.id)][1]:
            embed.add_field(name = "Message", value = db[str(i.id)][1], inline = True)
          embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
          await message.channel.send(embed = embed)
          print("✅　AFK MENTION Event")
  
  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if self.bot.memberRole in message.author.roles and message.channel.id not in [690647361139245136, 816540206572109824, 835694338230452228, 857404361331441694, 860643594900602900] and not (message.content.startswith(":") or message.content.endswith(":")):
      embed = discord.Embed(title = ":wastebasket: Message Deleted", color = 0xe67e22, timestamp = datetime.utcnow())
      embed.set_thumbnail(url = message.author.avatar_url)
      embed.add_field(name = "Author", value = message.author.mention, inline = True)
      embed.add_field(name = "Channel", value = message.channel.mention, inline = True)
      embed.add_field(name = "Content", value = message.content, inline = True)
      await self.bot.logChannel.send(embed = embed)
      print("✅　DELETE Event")
  
  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if before.author.bot == False and before.content != after.content and self.bot.memberRole in before.author.roles and before.channel.id not in [690647361139245136, 816540206572109824, 835694338230452228, 860643594900602900]:
      embed = discord.Embed(title = ":pencil: Message Edited", color = 0xe67e22, timestamp = datetime.utcnow())
      embed.set_thumbnail(url = before.author.avatar_url)
      embed.add_field(name = "Author", value = before.author.mention, inline = True)
      embed.add_field(name = "Channel", value = before.channel.mention, inline = True)
      embed.add_field(name = "Message", value = f"[Jump!]({before.jump_url})", inline = True)
      embed.add_field(name = "Before", value = before.content, inline = True)
      embed.add_field(name = "After", value = after.content, inline = True)
      await self.bot.logChannel.send(embed = embed)
      print("✅　EDIT Event")
  
  # on member join event
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if not member.bot:
      await member.add_roles(self.bot.memberRole)
      await self.bot.updateStatus()
      embed = discord.Embed(title = ":inbox_tray: Member Joined", description = f"You are the `{ordinal.ordinal(self.bot.memberCount())}` member!", color = 0x00FF00)
      embed.set_thumbnail(url = member.avatar_url)
      embed.add_field(name = "Get Roles", value = f"Go to {self.bot.rolesChannel.mention}", inline = False)
      embed.add_field(name = "Main Info :loudspeaker:", value = f"Read the {self.bot.rulesChannel.mention}\nJoin the talk in {self.bot.generalChannel.mention}", inline = False)
      await self.bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
      await member.remove_roles(self.bot.mutedRole)

    else:
      embed = discord.Embed(title = ":inbox_tray: Bot Joined", description = f"You are the `{ordinal.ordinal(self.bot.memberCount())}` member!\n{self.bot.botRole.mention} role added", color = 0x00FF00)
      embed.set_thumbnail(url = member.avatar_url)
      await self.bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
      await member.remove_roles(self.bot.mutedRole)
    print("✅　JOIN Event")

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    await self.bot.updateStatus()
    embed = discord.Embed(title = f":outbox_tray: {'Bot' if member.bot else 'Member'} Left", description = "Either kicked/banned/left", color = 0xFF0000)
    embed.set_thumbnail(url = member.avatar_url)
    await self.bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)
    print("✅　LEAVE Event")
  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.message_id == 759521601170833469:
      await payload.member.add_roles(self.bot.schoolRR[str(payload.emoji.name)], self.bot.dividerOneRole)
      await payload.member.send(f"{self.bot.plusEmoji} Added the **{self.bot.schoolRR[str(payload.emoji.name)]}** role")
      print("✅　REACTION (ADD) Event")
    if payload.message_id == 759534246607585300:
      await payload.member.add_roles(self.bot.gameRR[str(payload.emoji.name)], self.bot.dividerTwoRole)
      await payload.member.send(f"{self.bot.plusEmoji} Added the **{self.bot.gameRR[str(payload.emoji.name)]}** role")
      print("✅　REACTION (ADD) Event")

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    member = self.bot.server.get_member(payload.user_id)
    if payload.message_id == 759521601170833469:
      await member.remove_roles(self.bot.schoolRR[str(payload.emoji.name)])
      await member.send(f"{self.bot.minusEmoji} Removed the **{self.bot.schoolRR[str(payload.emoji.name)]}** role")
      print("✅　REACTION (REMOVE) Event")
    if payload.message_id == 759534246607585300:
      await member.remove_roles(self.bot.gameRR[str(payload.emoji.name)])
      await member.send(f"{self.bot.minusEmoji} Removed the **{self.bot.gameRR[str(payload.emoji.name)]}** role")
      print("✅　REACTION (REMOVE) Event")

def setup(bot):
  bot.add_cog(Events(bot))