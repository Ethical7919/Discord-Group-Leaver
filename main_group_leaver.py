import discord

client = discord.Client(self_bot=True)

@client.event
async def on_connect():
    while True:
        for gc in client.private_channels:
            if isinstance(gc, discord.GroupChannel):
                try:
                    await gc.leave()
                except Exception as e:
                    print(e)
client.run("Token Here", bot=False, reconnect=True)