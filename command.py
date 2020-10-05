@client.command()
async def mogu(ctx):
    await ctx.send("okayu!")

@client.command()
async def check(ctx):
    f = open("latest/PatchInfoServer.cfg", "r")
    await ctx.send(f.read())
    f.close()