import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Structure for storing voting information
voting_info = {}

async def send_vote_dm(user, subject, message_id):
    try:
        await user.send(f"You've shown interest in voting on: '{subject}'. Please reply to this message with 'yes' or 'no' to cast your vote anonymously. You can vote only once.")
    except discord.HTTPException as e:
        print(f"Failed to send DM to {user.name}: {e}")

@bot.slash_command(description="Start an anonymous vote")
async def start_vote(ctx, subject: str, duration: int):
    """
    Starts an anonymous vote.
    
    Parameters:
    - subject: The topic of the vote.
    - duration: The duration of the vote in minutes.
    """
    message = await ctx.respond(f"**Voting on:** {subject}\nReact with any emoji to this message if you want to participate. You will receive a DM to cast your vote.")
    message = await message.original_response()
    voting_info[message.id] = {
        "subject": subject, 
        "votes": {"yes": 0, "no": 0}, 
        "participants": set()
    }

    # Wait for the duration of the vote (converted to seconds).
    await asyncio.sleep(duration * 60)

    # Obtains and announces voting results.
    vote_data = voting_info.pop(message.id, None)
    if vote_data:
        yes_votes = vote_data["votes"]["yes"]
        no_votes = vote_data["votes"]["no"]
        await ctx.send_followup(f"**Voting results on:** {subject}\n👍: {yes_votes} votes\n👎: {no_votes} votes")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot or reaction.message.id not in voting_info or user.id in voting_info[reaction.message.id]["participants"]:
        return
    
    await send_vote_dm(user, voting_info[reaction.message.id]["subject"], reaction.message.id)

@bot.event
async def on_message(message):
    if not message.guild and not message.author.bot:
        for vote_id, vote_data in voting_info.items():
            if message.author.id in vote_data["participants"]:
                # This check prevents the "You've already voted" confirmation message from being sent multiple times
                return  # Ignores additional messages after voting.
            vote = message.content.lower()
            if vote in ["yes", "no"]:
                vote_data["votes"][vote] += 1
                vote_data["participants"].add(message.author.id)  # Mark the user as having already voted.
                await message.channel.send("Your vote has been recorded anonymously. Thank you for participating.")
                return

        await bot.process_commands(message)

bot.run('your-bot-token')
