# anonymous-discord-vote-bot
This Discord bot enables anonymous voting within your server, allowing members to vote on topics or decisions without revealing their choices to others. It utilizes Discord's direct message feature to collect votes, ensuring privacy and anonymity.

# Anonymous Voting Bot for Discord

This Discord bot enables anonymous voting within your server, allowing members to vote on topics or decisions without revealing their choices to others. It utilizes Discord's direct message feature to collect votes, ensuring privacy and anonymity.

## Features

- **Slash Commands**: Easy-to-use slash commands for initiating votes.
- **Anonymous Voting**: Collects votes through direct messages to maintain voter privacy.
- **Custom Voting Duration**: Set how long the vote should last.
- **Automatic Vote Tallying**: Automatically counts votes and announces the results after the voting period ends.

## Setup

### Requirements

- Python 3.7 or higher
- discord.py library
- A Discord Bot Token

### Installation

1. Ensure Python 3.7 or higher is installed on your system.
2. Install discord.py with voice support by running: ``python3 -m pip install -U discord.py``
3. Clone this repository or download the bot code to your local system.

### Configuration
1. Create a .env file in the root directory of your project.
2. Add your bot token to the .env file as follows: ``DISCORD_BOT_TOKEN=your_bot_token_here``
3. Replace your-bot-token in the bot code with your actual bot token.

## Runing the Bot
Execute the bot script with Python: ``python3 bot.py`` 

## Usage
Start a Vote: Use the /start_vote slash command followed by the topic and duration (in minutes) for the vote. For example, /start_vote "New Server Logo" 30 starts a vote on the new server logo that lasts for 30 minutes.
Participate in a Vote: React to the vote announcement message with any emoji. You will receive a DM from the bot asking for your vote. Reply with yes or no to cast your vote anonymously.
