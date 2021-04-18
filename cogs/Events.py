from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure, CommandOnCooldown, CommandNotFound
import humanize
import json
import ordinal

class Events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_command_completion(self, ctx):
    print(f"✅　{ctx.command.name.upper()} Command")
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, CheckFailure):
      await ctx.trigger_typing()
      await ctx.send(f"{self.bot.errorEmoji} Missing permissions")
    elif not isinstance(error, CommandNotFound):
      if isinstance(error, CommandOnCooldown):
        await ctx.trigger_typing()
        await ctx.send(f"{self.bot.errorEmoji} You are on cooldown for `{round(error.retry_after, 2)}` seconds")
      else:
        await ctx.trigger_typing()
        await ctx.send(f"```{error}```")
        if ctx.command:
          ctx.command.reset_cooldown(ctx)
    else:
      if not any(x in str(error) for x in ["\"ban\"", "\"kick\"", "\"levels\"", "\"rank\"", "\"slowmode\"", "\"warn\"", "\"unban\""]):
        await ctx.send(f"```{error}```")
    print(f"❌‎‎‎　ERROR ({error})")
  
  # on message sent event
  ## going to use sql or replit database instead of json later
  @commands.Cog.listener()
  async def on_message(self, message):
    # afk user returns
    if not message.content.lower().startswith("!afk"):
      with open("cogs/afks.json", "r") as file:
        data = json.load(file)
        # if afk user returns
        if str(message.author.id) in data:
          del data[str(message.author.id)]
          with open("cogs/afks.json", "w") as file:
            json.dump(data, file, indent = 2)
          if message.author.id != 410590963379994639:
            await message.author.edit(nick = message.author.display_name[6:])
          await message.reply(f":wave: Welcome back, I removed your AFK", delete_after = 3)
          print("✅　AFK (RETURN) Event")

    # afk user mentioned
    if message.mentions:
      for i in message.mentions:
        with open("cogs/afks.json", "r") as file:
          data = json.load(file)
          if str(i.id) in data:
            time = datetime.now() - datetime.strptime(data[str(i.id)][0], '%Y-%m-%d %H:%M:%S.%f')
            nickname = i.display_name[6:]
            if i.id == 410590963379994639:
              nickname = i.display_name
            # w/o message
            if not data[str(i.id)][1]:
              await message.channel.send(f":spy: **{nickname}** is AFK ({humanize.naturaltime(time)})")
            # with message
            else:
              await message.channel.send(f":spy: **{nickname}** is AFK: {data[str(i.id)][1]} ({humanize.naturaltime(time)})")
            print("✅　AFK (MENTION) Event")
    
    # viraj moment
    if message.author.id == 320369001005842435:
      if message.channel.id == 700074631935295532:
        if "ask" in message.content.lower() or "punz" in message.content.lower():
          await message.delete()
    
    # breaks the bot
    # await self.bot.process_commands(message)
  
  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author.bot == False and self.bot.memberRole in message.author.roles and message.channel.id != 690647361139245136 and not message.content.startswith(":") and not message.content.endswith(":"):
      embed = discord.Embed(title = ":wastebasket: Message Deleted", color = 0xe67e22, timestamp = datetime.utcnow())
      embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
      embed.set_thumbnail(url = message.author.avatar_url)
      embed.add_field(name = "Author", value = message.author.mention, inline = True)
      embed.add_field(name = "Channel", value = message.channel.mention, inline = True)
      embed.add_field(name = "Content", value = message.content, inline = True)
      # if (message.attachments[0].size > 0):
      #   embed.set_image(url = message.attachments[0].proxy_url)
      await self.bot.logChannel.send(embed = embed)
      print("✅　DELETE Event")
  
  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if before.author.bot == False and before.content != after.content and self.bot.memberRole in before.author.roles and before.channel.id != 690647361139245136:
      embed = discord.Embed(title = ":pencil: Message Edited", color = 0xe67e22, timestamp = datetime.utcnow())
      embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
      embed.set_thumbnail(url = before.author.avatar_url)
      embed.add_field(name = "Author", value = before.author.mention, inline = True)
      embed.add_field(name = "Channel", value = before.channel.mention, inline = True)
      embed.add_field(name = "Message", value = f"[Jump!]({before.jump_url})", inline = True)
      embed.add_field(name = "Before", value = before.content, inline = True)
      embed.add_field(name = "After", value = after.content, inline = True)
      # if (message.attachments[0].size > 0):
      #   embed.set_image(url = message.attachments[0].proxy_url)
      await self.bot.logChannel.send(embed = embed)
      print("✅　EDIT Event")
  
  # on member join event
  @commands.Cog.listener()
  async def on_member_join(self, member):
    if not member.bot:
      await member.add_roles(self.bot.memberRole)
      await self.bot.updateStatus()
      embed = discord.Embed(title = ":inbox_tray: Member Joined", description = f"You are the `{ordinal.ordinal(self.bot.userCount(1))}` member!", color = 0x00FF00, timestamp = datetime.utcnow())
      embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
      embed.set_thumbnail(url = member.avatar_url)
      embed.add_field(name = "Get Roles", value = f"Go to {self.bot.rolesChannel.mention}", inline = False)
      embed.add_field(name = "Main Info :loudspeaker:", value = f"Read the {self.bot.rulesChannel.mention}\nRead the {self.bot.channelsChannel.mention} info\nJoin the talk in {self.bot.generalChannel.mention}", inline = False)
      await self.bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
      await member.remove_roles(self.bot.mutedRole)

    else:
      await member.add_roles(self.bot.botRole)
      embed = discord.Embed(title = ":inbox_tray: Bot Joined", description = f"You are the `{ordinal.ordinal(self.bot.userCount(2))}` member!\n{self.bot.botRole.mention} role added", color = 0x00FF00, timestamp = datetime.utcnow())
      embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
      embed.set_thumbnail(url = member.avatar_url)
      await self.bot.welcomeChannel.send(f"Welcome, {member.mention}", embed = embed)
      await member.remove_roles(self.bot.mutedRole)
    print("✅　JOIN Event")

  # on member exit event
  @commands.Cog.listener()
  async def on_member_remove(self, member):
    if member.bot == False:
      await self.bot.updateStatus()
      embed = discord.Embed(title = ":outbox_tray: Member Left", description = "Either kicked/banned/left", color = 0xFF0000, timestamp = datetime.utcnow())
      embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
      embed.set_thumbnail(url = member.avatar_url)
      await self.bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)

    else:
      embed = discord.Embed(title = ":outbox_tray: Bot Left", description = "Either kicked/banned/left", color = 0xFF0000, timestamp = datetime.utcnow())
      embed.set_footer(text = self.bot.server.name, icon_url = self.bot.server.icon_url)
      embed.set_thumbnail(url = member.avatar_url)
      await self.bot.welcomeChannel.send(f"Goodbye, {member.mention}", embed = embed)
    print("✅　LEAVE Event")
  
  # reaction roles (add)
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.message_id == 759521601170833469:
      await payload.member.add_roles(self.bot.schoolRRDict[str(payload.emoji.name)], self.bot.dividerOneRole)
      await payload.member.send(f"{self.bot.plusEmoji} Added the **{self.bot.schoolRRDict[str(payload.emoji.name)].name}** role")
      print("✅　REACTION (ADD) Event")
    
    if payload.message_id == 759534246607585300:
      await payload.member.add_roles(self.bot.gameRRDict[payload.emoji.id], self.bot.dividerTwoRole)
      await payload.member.send(f"{self.bot.plusEmoji} Added the **{self.bot.gameRRDict[payload.emoji.id].name}** role")
      print("✅　REACTION (ADD) Event")

  # reaction roles (remove)
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    member = self.bot.server.get_member(payload.user_id)
    if payload.message_id == 759521601170833469:
      await member.remove_roles(self.bot.schoolRRDict[str(payload.emoji.name)])
      await member.send(f"{self.bot.minusEmoji} Removed the **{self.bot.schoolRRDict[str(payload.emoji.name)].name}** role")
      print("✅　REACTION (REMOVE) Event")
    
    if payload.message_id == 759534246607585300:
      await member.remove_roles(self.bot.gameRRDict[payload.emoji.id])
      await member.send(f"{self.bot.minusEmoji} Removed the **{self.bot.gameRRDict[payload.emoji.id].name}** role")
      print("✅　REACTION (REMOVE) Event")
  
  # @bot.event
  # async def on_member_update(before, after):
  #   if str(before.activity).lower() == "streaming":
  #     await after.remove_roles(bot.liveOnTwitchRole)
  #   if str(after.activity).lower() == "streaming":
  #     await after.add_roles(bot.liveOnTwitchRole)

  # @bot.event
  # async def on_voice_state_update(member, before, after):
  #   if after.self_stream:
  #     await bot.logChannel.send(f":red_circle: `{member}` went live in `{after.channel.name}` VC")

def setup(bot):
  bot.add_cog(Events(bot))