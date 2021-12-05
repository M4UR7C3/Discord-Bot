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

                    role: discord.Role = guild.get_role(917060659852771408)
                    await payload.member.add_roles(role, reason="Zuweisung")

bot = PythonBot(intents=discord.Intents.all(), command_prefix='!')


@bot.command(name='test')
async def test(ctx, *args):
    await ctx.send(f'Eingabe: {" ".join(args)}')


@bot.command(name='userinfo')
async def test(ctx, member: discord.Member):
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                          description='', color=0x4cd137, timestamp=datetime.now().astimezone(tz=de))
    embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name='Bot', value=f'```{"Ja" if member.bot else "Nein"}```', inline=True)
    embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```', inline=True)
    embed.add_field(name='Server beigetreten', value=f'```{member.joined_at}```', inline=True)
    embed.add_field(name='Discord beigetreten', value=f'```{member.created_at}```', inline=True)
    embed.add_field(name='Rollen', value=f'```{len(member.roles) -1}```', inline=True)
    embed.add_field(name='Höchste Rolle', value=f'```{member.top_role.name}```', inline=True)
    embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
    embed.add_field(name='Booster', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)
    embed.set_footer(text=f'Angefordert von {ctx.author.name} ~ {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


bot.run('OTE2NzUzMzQwMTQ5NDAzNzA4.YauvFA.3qdE-w2FVsJt-DsmoExJcXeBC7k')
