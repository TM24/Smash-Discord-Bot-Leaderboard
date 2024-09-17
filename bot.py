import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


class Leaderboard:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def swap(self):
        self.player1, self.player2 = self.player2, self.player1
        self.score1, self.score2 = self.score2, self.score1
        f = open('player1.txt', 'w')
        f.write(self.player1)
        f.close()
        b = open('player2.txt', 'w')
        b.write(self.player2)
        b.close()
        f = open('score1.txt', 'w')
        f.write(str(self.score1))
        f.close()
        f = open('score2.txt', 'w')
        f.write(str(self.score2))
        f.close()
        print(f'{str(self.score1)} {self.player1} - {self.player2} {str(self.score2)}')

    def set(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        f = open('player1.txt', 'w')
        f.write(player1)
        f.close()
        b = open('player2.txt', 'w')
        b.write(player2)
        b.close()
        f = open('score1.txt', 'w')
        f.write(str(self.score1))
        f.close()
        f = open('score2.txt', 'w')
        f.write(str(self.score2))
        f.close()
        print(f'0 {self.player1} vs {self.player2} 0')


    def increment1(self):
        self.score1 += 1
        f = open('score1.txt', 'w')
        f.write(str(self.score1))
        f.close()
        print(f'{str(self.score1)} - {self.score2}')

    def increment2(self):
        self.score2 += 1
        f = open('score2.txt', 'w')
        f.write(str(self.score2))
        f.close()
        print(f'{str(self.score1)} - {self.score2}')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def set(ctx, player1, player2):
    joe.set(player1, player2)
    await ctx.send(f'0 {joe.player1} vs {joe.player2} 0')


@bot.command()
async def swap(ctx):
    joe.swap()
    f'{joe.score1} {joe.player1} vs {joe.player2} {joe.score2}'
    await ctx.send(f'{joe.score1} {joe.player1} vs {joe.player2} {joe.score2}')

@bot.command()
async def inc1(ctx):
    joe.increment1()
    await ctx.send(f'{str(joe.score1)} - {str(joe.score2)}')

@bot.command()
async def inc2(ctx):
    joe.increment2()
    await ctx.send(f'{str(joe.score1)} - {str(joe.score2)}')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

joe = Leaderboard("joe", "mama")
bot.run('YOUR TOKEN HERE')






