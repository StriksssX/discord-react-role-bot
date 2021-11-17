import discord
from discord.ext import commands
import json
import os 
import discord
from discord import utils
import asyncio
from discord import Activity, ActivityType
 
import config


 
class MyClient(discord.Client):
# Проверка готовности бота
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))                 
# Добавление роли с помощью реакций
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id) # получаем объект канала
            message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
            member = payload.member # получаем объект пользователя который поставил реакцию
            print(member)
 
            try:
                emoji = str(payload.emoji) # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
            
                if(len([i for i in member.roles if i and i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))
    
client = MyClient()
client.run(config.TOKEN)