import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
from itertools import cycle
import random
import praw
import os

bot = commands.Bot(command_prefix = "yb!")
bot.remove_command('help')

reddit = praw.Reddit(client_id=os.environ.get('CLIENT_ID'),
                     client_secret=os.environ.get('CLIENT_SECRET'),
                     user_agent='meme') 


@bot.event
async def on_ready():
  print("YokeBot is Online")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")



@bot.command(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  author = ctx.message.author
  if "Admin" in author.roles:
    await user.kick(reason=reason)
    await ctx.send("{} has been kicked succesfully.".format(user))
  else:
    await ctx.send("Permission Denied\n")
  

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
  channel = ctx.message.channel
  messages = []
  async for message in channel.history(limit=int(amount+1)):
    messages.append(message)

  await channel.delete_messages(messages)
  await ctx.send (str(amount)+ ' ' + "Message(s) have been deleted")


@bot.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('dankmeme').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)


@bot.command()
async def aww(ctx):
    memes_submissions = reddit.subreddit('aww').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def facepalm(ctx):
    memes_submissions = reddit.subreddit('facepalm').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@bot.command()
async def ihadastroke(ctx):
    memes_submissions = reddit.subreddit('ihadastroke').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)








bot.run(os.environ.get('TOKEN'))