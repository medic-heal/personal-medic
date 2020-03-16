import discord
from discord.ext import commands
from discord.ext.commands import Bot
from time import sleep
import os

#Создаём префикс для команд

prefix = '!'

Bot = commands.Bot(command_prefix= prefix)

#Удаляем функции

Bot.remove_command('help')


@Bot.event
async def on_ready():
	'''Проверка на работу бота'''
	print('Эта штуковина работает!')

#Информация

@Bot.command(pass_context= True)
async def help(ctx):
	'''Инфа о командах'''
	emb = discord.Embed(title= 'Информация о командах', colour= 0xFC30A4)
	emb.add_field(name= '{}help'.format(prefix), value= 'Показывает это окно')
	emb.add_field(name= '{}info @Ник пользователя'.format(prefix), value= 'Показывает информацию о пользователе')
	emb.add_field(name= '{}memes'.format(prefix), value= 'Выводит список мемов')

	await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def memes(ctx):
    '''Список мемов'''
    emb = discord.Embed(title= 'Список мемов', colour= 0x9D88DF)
    emb.add_field(name= 'Выбирай', value= '!хАчубёрнинг, !jojo, !дурка, !uno, !stonks, !ъуъ, !клоун')
    await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def info(ctx, user: discord.Member):
	'''Инфа о пользователе'''
	emb = discord.Embed(title= 'Информация о пользователе {}'.format(user.name), colour= 0xFF4040)
	emb.add_field(name= 'Настоящее имя', value= user.name)
	emb.add_field(name= 'ID', value= user.id)
	emb.add_field(name= 'Присоединился', value= str(user.joined_at)[:16])
	emb.add_field(name= 'Статус', value= user.status)
	emb.add_field(name= 'Главная роль', value= user.top_role)
	if user.nick is not None:
		emb.add_field(name= 'Измененный ник', value= user.nick)
	if user.activity is not None:
		emb.add_field(name= 'Играет в', value= user.activity)
	emb.set_thumbnail(url= user.avatar_url)
	emb.set_author(name= Bot.user.name, url= 'https://discordapp.com/oauth2/authorized')
	await ctx.send(embed = emb)

@Bot.event
async def on_member_join(member: discord.Member):
	'''Выдача роли и приветствие при присоединении нового участника'''
	role = discord.utils.get(member.guild.roles, name='Pootis')
	await member.add_roles(role, reason=None, atomic=True)

	emb = discord.Embed(title= 'Информация и советы о сервере **Medic Heal**', colour= 0xFFCD00)
	emb.add_field(name= 'Команды', value= 'Если хочешь увидеть, что я могу, то в чате напиши \"!help\"')
	emb.add_field(name= 'Советы', value= 'Советуем тебе прочитать правила для того, чтобы не нарушать их')
	emb.add_field(name= 'Кастомизация', value= 'Если хочешь поменять себе цвет ника и выбрать дополнительную роль, то перейди в канал \"⠇🌈роли\"')
	emb.add_field(name= 'Уровни', value= 'У нас на сервере есть система лвлов, которая просто показывает твоё место в списке участников относительно уровней')
	emb.add_field(name= 'Оповещения', value= 'Оповещения о новых видео приходят в отдельном канале \"🎷ролики-and-стримики\"')
	emb.add_field(name= 'Творчество', value= 'Если хочешь показать своё творчество, то ты найдёшь специальные каналы в категории \"Создание контента\"')

	await member.send(embed = emb)
	await member.send('**Ну а с остальным ты разберёшься сам, удачи :D**')

#Команды для мемов

@Bot.command(pass_context= True)
async def хАчубёрнинг(ctx):
	await ctx.send('https://avatars.mds.yandex.net/get-zen_doc/1567436/pub_5d793a2b433ecc00ad265d96_5d7942d82beb4900ada23662/scale_1200')

@Bot.command(pass_context= True)
async def jojo(ctx):
	await ctx.send('https://cdn.discordapp.com/attachments/484291943220641801/630820684536217620/qx1khg7kn4r31.png')

@Bot.command(pass_context= True)
async def дурка(ctx):
	await ctx.send('https://media.discordapp.net/attachments/623212386718842880/688384042671931435/2Q.png')

@Bot.command(pass_context= True)
async def nou(ctx):
	await ctx.send('https://media.discordapp.net/attachments/637893943081828364/685468980412022785/oKZzKczowtI.jpg')

@Bot.command(pass_context= True)
async def stonks(ctx):
	await ctx.send('https://media.discordapp.net/attachments/637893943081828364/688088530404114525/stonks-mem-758x426.png')

@Bot.command(pass_context= True)
async def rub(ctx):
	await ctx.send('https://cdn.discordapp.com/attachments/621697182386487296/687743655762460679/unknown.png')

@Bot.command(pass_context= True)
async def ъуъ(ctx):
	await ctx.send('https://cdn.discordapp.com/attachments/637893943081828364/688739278649557033/1a9a5693eca1ee26dfdcd4e96d03a52f.png')

@Bot.command(pass_context= True)
async def клоун(ctx):
	await ctx.send('Короче, я предлагаю перемирие, можем даже встретиться на твоей территории, например под красным куполом цирка, мы там даже вату купить можем, и договориться, что клоун не я, а ты\n \nhttps://cdn.discordapp.com/attachments/637893943081828364/687708649187180738/bnH3P4RE_jg.png')

#Команды для админов

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def helpadmin(ctx):
	'''Инфа о командах для админов'''

	await ctx.channel.purge(limit= 1)

	emb = discord.Embed(title= 'Информация о командах для администрации', colour= 0xFF1E00)
	emb.add_field(name= '{}cls'.format(prefix), value= 'очищает определённое кол-во сообщений(только для админов)')
	emb.add_field(name= '{}deport @Ник пользователя причина'.format(prefix), value= 'кикает участника с сервера(только для админов)')
	emb.add_field(name= '{}block @Ник пользователя причина'.format(prefix), value= 'банит участника(только для админов)')
	emb.add_field(name= '{}unblock @Ник пользователя'.format(prefix), value= 'забирает бан у участника(только для админов)')
	emb.add_field(name= '{}user_mute @Ник пользователя'.format(prefix), value= 'выдает участнику мут(только для админов)')
	emb.add_field(name= '{}user_unmute @Ник пользователя'.format(prefix), value= 'забирает у участника мут(только для админов)')

	await ctx.author.send(embed = emb)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def cls(ctx, value):
	'''Очистка определённого кол-ва сообщений'''
	if int(value) <= 0:
		await ctx.send('**Дурень, напиши нормально**')
		sleep(1.0)
		await ctx.channel.purge(limit= 2)

	if int(value) > 0:
		await ctx.channel.purge(limit= int(value) + 1)
		await ctx.send('Я удалил ' + value + ' ненужных сообщений')
		sleep(1.0)
		await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def deport(ctx, user: discord.Member, *, reason= None):
	'''Кик участника с сервера'''
	await user.kick(reason= reason)
	await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def block(ctx, user: discord.Member, *, reason= None):
	'''Выдача бана участнику'''
	await ctx.channel.purge(limit=1)

	await user.ban(reason= reason)
	await ctx.send(f'Участник {user.mention} был забанен по причине ' + reason)

	sleep(1.0)
	await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def unblock(ctx, *, member):
	'''Выдача разбана человеку'''
	await ctx.channel.purge(limit=1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'Участник был разбанен {user.mention}')

		await ctx.channel.purge(limit=1)

		return

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def user_mute(ctx, member: discord.Member):
	'''Выдача человеку мута'''
	await ctx.channel.purge(limit= 1)
	
	mute_role = discord.utils.get(ctx.message.guild.roles, name= 'mute')
	
	await member.add_roles(mute_role)
	
	await ctx.send(f'У {member.mention} ограничен доступ к чату из-за нарушения правил')

	sleep(1.0)

	await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def user_unmute(ctx, member: discord.Member):
	'''Снятие мута участнику'''
	await ctx.channel.purge(limit= 1)

	mute_role = discord.utils.get(ctx.message.guild.roles, name= 'mute')

	await member.add_roles(mute_role)

	await member.remove_roles(mute_role)
	await ctx.send(f'У {member.mention} убран мут благодаря администрации')

	sleep(1.0)

	await ctx.channel.purge(limit= 1)

#Запуск

token = os.environ.get('BOT_TOKEN')