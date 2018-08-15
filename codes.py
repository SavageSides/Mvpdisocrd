import discord
from discord.ext import commands

TOKEN = 'NDc5MTQ0OTQ0MzAxMzc1NDg5.DlU-iA.vLpeRHye9KnxVmNcCBZYiYndV4M'

client = commands.Bot(command_prefix='!')

newUserMessage = """
**Welcome to Lonely! We all hope you have a good time here at Lonely :smile:**
```If you would like to invite your friends we would appreicate it!
Have a good time```https://giphy.com/gifs/pitchperfect-movie-pitch-perfect-pitchperfect2-MVDPX3gaKFPuo
"""

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Prefix | "?"'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot is ready to preform master')

@client.event
async def on_member_join(member):
    print("Recognized that a member called " + member.name + " jonied")
    await client.send_message(member, newUserMessage)
    print("Sent message to " +member.name)



@client.command(pass_context=True)
@commands.has_role("Mod")
async def kick(ctx, user: discord.Member):
    await client.say("User has been kicked :thumbsup:")
    await client.kick(user)

@client.command(pass_context=True)
@commands.has_role("Dev")
async def ban(ctx, user: discord.Member):
    await client.say("The user has been Banned :thumbsup:")
    await client.ban(user)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def mute(ctx, user: discord.Member):
    MutedRole = discord.utils.get(ctx.message.server.roles,name='Muted')
    await client.say("User Muted :white_check_mark: ")
    await client.add_roles(user, MutedRole)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def unmute(ctx, user: discord.Member):
    MutedRole = discord.utils.get(ctx.message.server.roles,name='Muted')
    await client.say("User Unmuted :white_check_mark:")
    await client.remove_roles(user, MutedRole)

@client.command(pass_context=True)
@commands.has_role("Mod")
async def purge(ctx, amount=500):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted :white_check_mark:')

@client.command(pass_context=True)
@commands.has_role("Mod")
async def verifie(ctx, user: discord.Member):
    NotLonely = discord.utils.get(ctx.message.server.roles,name='Not Lonely')
    LonelyMembers = discord.utils.get(ctx.message.server.roles,name='Lonely Members')
    await client.say("User Verified :white_check_mark: ")
    await client.add_roles(user, LonelyMembers)
    await client.remove_roles(user, NotLonely)
    await client.add_roles(user, LonelyMembers)
    await client.remove_roles(user, NotLonely)
    await client.remove_roles(user, NotLonely)


@client.command(pass_context=True)
@commands.has_role("Mod")
async def verifacation(ctx, user: discord.Member):
    NotLonely = discord.utils.get(ctx.message.server.roles,name='Not Lonely')
    LonelyMembers = discord.utils.get(ctx.message.server.roles,name='Lonely Members')
    await client.say("User Put back in verifacation :white_check_mark: ")
    await client.remove_roles(user, LonelyMembers)
    await client.add_roles(user, NotLonely)
    await client.remove_roles(user, LonelyMembers)
    await client.add_roles(user, NotLonely)
    await client.remove_roles(user, LonelyMembers)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Not Lonely')
    await client.add_roles(member, role)



client.run(TOKEN)

                      
