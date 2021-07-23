from datetime import datetime
import discord
from discord.ext import commands

class HelpCommand(commands.HelpCommand):
  async def send_bot_help(self, mapping):
    output = "Developer: <@410590963379994639>\nGithub: [Link](https://github.com/TheHarpagon/Albert) (drop issues/suggestions)\n"
    for cog, commands in mapping.items():
      filtered = await self.filter_commands(commands, sort = True)
      for command in filtered:
        output += f"\n`!{command.qualified_name}` {command.help}"
    embed = discord.Embed(title = ":scroll: Help", description = output, color = 0xe67e22)
    embed.set_footer(text = f"Requested by {self.context.author}", icon_url = self.context.author.avatar_url)
    await self.get_destination().send(embed = embed)
  
  async def send_command_help(self, command):
    title = command.qualified_name
    title = title.upper() if title in ["afk", "ocr"] else title.capitalize()
    embed = discord.Embed(title = title, description = f"{command.help}", color = 0xe67e22)
    embed.add_field(name = "Syntax", value = f"`!{command.qualified_name}{' ' + command.signature if command.signature else ''}`\nNote: `[]` is optional; `<>` is required")
    if command.aliases:
      aliases = f"`{command.aliases[0]}`"
      for i in command.aliases[1:]:
        aliases += f", `{i}`"
      embed.add_field(name = "Aliases", value = aliases, inline = False)

    embed.set_footer(text = f"Requested by {self.context.author}", icon_url = self.context.author.avatar_url)
    await self.get_destination().send(embed = embed)