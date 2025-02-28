import sys
import discord
from sim.heroes import Team, DummyTeam, Hero
from sim.models import Armor, Helmet, Weapon, Pendant, Rune, Artifact, Familiar
from sim.processing import GameSim, GauntletAttackSim, GauntletDefenseSim, GauntletSim, Game
from sim.tests import friend_boss_test, main_friend_boss_test, master_friend_boss_test, guild_boss_test, \
    main_guild_boss_test, master_guild_boss_test, trial_test, main_trial_test, pvp_test, sim_setup

# List heroes
heroes = [Hero.__dict__[key] for key in Hero.__dict__ if '__' not in key and 'empty' not in key]

# Create teams

TOKEN = 'xxxxx'

client = discord.Client()

@client.event

async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!sym'):                      

        #Breaks the chat message into an array (with !sym as first value, that's easily solvable so i'll sort later)
        teamArray = message.content.split()  

        print(teamArray)

        #Builds array for battle, needs to pull values from chat message
        team_1 = Team([getattr(Hero, hero_string) for hero_string in teamArray])

        team_2 = Team([Hero.ultima(),
               Hero.valkyrie(),
               Hero.lindberg(),
               Hero.shudde_m_ell(),
               Hero.drow(),
               Hero.freya()])

      
        sim = GameSim(team_1, team_2, n_sim=100)
        #Runs simulation
        sim.process()   

        #Sends results in the chat where request was made      
        await client.send_message(message.channel, '**TEAM #1**')
        await client.send_message(message.channel, team_1.comp())        
        await client.send_message(message.channel, '**TEAM #2**')
        await client.send_message(message.channel, team_2.comp())            
        await client.send_message(message.channel, '==================')
        await sim.print_winrate(client, message)           
        await client.send_message(message.channel, '==================')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
