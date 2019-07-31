import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is Ready')

@client.command()
@commands.has_any_role("admin")
async def ban (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself stupid")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")

@client.command()
@commands.has_any_role("admin")
async def kick (ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot kick yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member} is kicked!")

@client.command()
@commands.has_any_role("admin")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
         
@client.command()
@commands.has_any_role("admin")
async def clear(ctx, amount=25):
    await ctx.channel.purge(limit=amount)

client.run("NTk2Mzk3MTIzNDYxNzA5ODM0.XR6T1w.djrrxvLZI0ACPhDQ8TdzxMLSZts")