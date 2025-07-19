import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("bot inicializado com sucesso!")

@bot.command()
async def ola(ctx: commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"ola, {nome} tudo bem?")

@bot.command()
async def falar(ctx: commands.Context,*,texto):
    await ctx.send(texto)

@bot.command()
async def somar(ctx: commands.Context, num1:int, num2:int):
    ressoma = num1 + num2
    await ctx.send(f"O resultado da soma é: {ressoma}")


@bot.command()
async def subtrair(ctx: commands.Context, num1:int, num2:int):
    ressubtracao = num1 - num2
    await ctx.send(f"O resultado da subtração é: {ressubtracao}")

@bot.command()
async def dividir(ctx: commands.Context, num1:int, num2:int):
    if num2 == 0:
        await ctx.send("Não é possível dividir por zero!")
    else:
        resdivisao = num1 / num2
        await ctx.send(f"O resultado da divisão é: {resdivisao}")

@bot.command()
async def multiplicar(ctx: commands.Context, num1:int, num2:int):
    resmultiplicacao = num1 * num2
    await ctx.send(f"O resultado da multiplicação é: {resmultiplicacao}")

@bot.command()
async def potencia(ctx: commands.Context, num1:int, num2:int):
    respotencia = num1 ** num2
    await ctx.send(f"O resultado da potenciação é: {respotencia}")

@bot.command()
async def addcargo(ctx, membro: discord.Member, cargo: discord.Role):
    if cargo in membro.roles:
        await ctx.send(f"{membro.mention} já possui o cargo {cargo.name}.")
    else:
        await membro.add_roles(cargo)
        await ctx.send(f"{cargo.name} adicionado a {membro.mention} com sucesso!")

@bot.command()
async def remcargo(ctx, membro: discord.Member, cargo: discord.Role):
    if cargo not in membro.roles:
        await ctx.send(f"{membro.mention} não possui o cargo {cargo.name}.")
    else:
        await membro.remove_roles(cargo)
        await ctx.send(f"{cargo.name} removido de {membro.mention} com sucesso!")

@bot.command(name = 'sobre')
async def sobre(ctx):
    embem = discord.Embed(
        title = "Sobre o Bot",
        description = "Sou um bot em primeira versao, criado para testes.",
        color = discord.Color.purple()
    )
    embem.add_field(name = "Comandos disponíveis", value = "- `.ola`\n- `.falar`\n- `.somar`\n- `.subtrair`\n- `.dividir`\n- `.multiplicar`\n- `.potencia`\n- `.addcargo`\n- `.remcargo`", inline=False)
    embem.set_footer(text = "Desenvolvido por Girooj")
    await ctx.send(embed=embem)





    
bot.run("Token")