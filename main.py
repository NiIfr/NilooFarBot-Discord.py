
import discord
import random
from discord.ext import commands
intents = discord.Intents.all()
intents.guilds = True
intents.members = True
# intents.message_content = True
TOKEN = "Your Token Bot"
client = commands.Bot(command_prefix='!', intents=intents)

# args for say welcome
welcome_messages = [
    "Welcome to the server!",
    "Hello and welcome!",
    "Glad to have you here!",
    "Welcome aboard!",
    "Hey there, welcome!",
    "Welcome to our community",
    "Good to see you, welcome!"
]

# else message for chat
else_messages = [
    "I do not understand.",
    "I cant see",
    "Tell me clear"
]

# Be online


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')


# say welcome to members
@client.event
async def on_member_join(member):

    channel_id = Your_channel_id
    channel = client.get_channel(channel_id)
    member.name
    if channel is not None:
        random_welcome_message = random.choice(welcome_messages)
        await member.send(f'Slm 😍 {member.mention} Aziz \n'
                          'Be server NilooFar Vafaei Khosh Omadi! \n'
                          'Omid varam lahazat khoshi ro dar in server separi kni!\n'
                          'lotfan ghabl az har kari channel <#1074594474895876146> ra motalee konid!')
        await channel.send(f'{random_welcome_message} \n {member.mention}!')


# auto response bot
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.id == 1156922943419469834:
        if message.content.lower() == 'hi' or message.content.lower() == 'hello':
            await message.reply('Hola!')

        elif message.content.lower() == 'bye':
            await message.reply('Bbbyeeee')

        else:
            random_else_message = random.choice(else_messages)
            await message.reply(f'{random_else_message}')


# Info for changing Roles
@client.event
async def on_member_update(before, after):
    target_user_id = Your User ID
    target_channel_id = Your channel ID
    channel = client.get_channel(target_channel_id)
    if channel is not None:
        role_changes = []
        # Check if roles have changed
        if before.roles != after.roles:
            # Check if a new role was added
            new_roles = [
                role for role in after.roles if role not in before.roles]
            removed_roles = [
                role for role in before.roles if role not in after.roles]

            if new_roles or removed_roles:
                user_mention = f'🤔 New changing for {after.mention}'
                role_changes = ""

                if new_roles:
                    role_changes += f'**✅ Gave roles: ** {", ".join([role.name for role in new_roles])}\n'

                if removed_roles:
                    role_changes += f'**❌ Removed roles:** {", ".join([role.name for role in removed_roles])}\n'

                id = after.id
                the_user = await client.fetch_user(id)

                # Send an alert message with custom style
                embed = discord.Embed(

                    title=f"🤔 Changing role: ",
                    description=f"{the_user.mention}\n{role_changes}",
                    color=discord.Color.purple()
                )

                embed.set_thumbnail(url=the_user.avatar_url)
                await channel.send(embed=embed)


client.run(TOKEN)
