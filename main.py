import sys
import traceback
from os import listdir
from os.path import isfile, join

import discord
from discord.ext import commands
import pytz
from datetime import datetime


class PythonBot(commands.Bot):

    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

    async def on_ready(self):
        activity = discord.Game(name="Mit Flos Mum", type=3)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        print("Bot is ready!")

    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        if payload.channel_id == 917058505612091424:
            if payload.message_id == 917063034378256394:
                if payload.emoji.name == 'LOL':
                    guild: discord.Guild = bot.get_guild(553172923083390977)
                    channel: discord.TextChannel = guild.get_channel(917058505612091424)

                    role: discord.Role = guild.get_role(917060575425601566)
                    await payload.member.add_roles(role, reason="Zuweisung")
        if payload.channel_id == 917058505612091424:
            if payload.message_id == 917063034378256394:
                if payload.emoji.name == 'CS':
                    guild: discord.Guild = bot.get_guild(553172923083390977)
                    channel: discord.TextChannel = guild.get_channel(917058505612091424)

                    role: discord.Role = guild.get_role(917060659852771408)
                    await payload.member.add_roles(role, reason="Zuweisung")
        if payload.channel_id == 917058505612091424:
            if payload.message_id == 917063034378256394:
                if payload.emoji.name == 'TFT':
                    guild: discord.Guild = bot.get_guild(553172923083390977)
                    channel: discord.TextChannel = guild.get_channel(917058505612091424)

                    role: discord.Role = guild.get_role(917091524980932629)
                    await payload.member.add_roles(role, reason="Zuweisung")
        if payload.channel_id == 917058505612091424:
            if payload.message_id == 917063034378256394:
                if payload.emoji.name == 'GolfIt':
                    guild: discord.Guild = bot.get_guild(553172923083390977)
                    channel: discord.TextChannel = guild.get_channel(917058505612091424)

                    role: discord.Role = guild.get_role(917098418101436496)
                    await payload.member.add_roles(role, reason="Zuweisung")
        if payload.channel_id == 917058505612091424:
            if payload.message_id == 917063034378256394:
                if payload.emoji.name == 'RL':
                    guild: discord.Guild = bot.get_guild(553172923083390977)
                    channel: discord.TextChannel = guild.get_channel(917058505612091424)

                    role: discord.Role = guild.get_role(917099281100455976)
                    await payload.member.add_roles(role, reason="Zuweisung")


bot = PythonBot(intents=discord.Intents.all(), command_prefix='!')

if __name__ == '__main__':
    path = 'extensions'
    extensions = [file for file in listdir(path) if isfile(join(path, file))]
    for extension in extensions:
        try:
            bot.load_extension(f'{path}.{extension[:-3]}')
        except Exception as exception:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


bot.run('Token')
