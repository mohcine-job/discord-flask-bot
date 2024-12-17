import discord
from discord.ext import commands
import requests
import os

# Récupérer le token du bot depuis les Secrets de Replit
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# URL du backend Flask déployé sur Heroku
BACKEND_URL = https://tuteur-scolaire-f360a6f447ea.herokuapp.com/  # Remplacez par votre URL Heroku

# Configuration des intents pour le bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.command()
async def question(ctx, *, message):
    await ctx.send("Je réfléchis... 🤔")
    try:
        response = requests.post(BACKEND_URL, json={"question": message})
        if response.status_code == 200:
            answer = response.json().get('response')
            await ctx.send(answer)
        else:
            await ctx.send("Désolé, une erreur est survenue avec le backend !")
    except Exception as e:
        await ctx.send(f"Erreur : {e}")

# Lancer le bot
bot.run(TOKEN)
