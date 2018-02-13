# coding: utf-8
import discord
import asyncio
import settings

client = discord.Client()

@client.event
async def on_ready():
    print("-"*20)
    print(client.user.name)
    print(client.user.id)
    print("-"*20)

@client.event
async def on_message(message):
    if client.user != message.author:  #他BOT回避
        if message.content.startswith("test0"):
            await client.delete_message(message)


    channels = ["398447971018211329", "394434155443650560", "398446399005655051"]
        elif message.channel.id in channels:  #チャンネル指定
            if message.content.startswith("http"):
                m = "**Good luck!** \n配信の書き込みは__１時間後__に自動削除されます。"  #BOT送信メッセージ
                response = await client.send_message(message.channel, m)    #返信場所指定
                await asyncio.sleep(3600) #非同期処理
                await client.delete_messages([message, response])


    Xchannels = [
            "412592142851112960",#bot_practice
            "397794862755348480",#PUBG
            "393334968488820739",#mc_chatroom
            "397790090006364170",#monster hunter
    ]
        elif message.channel.id in Xchannels:
                if message.content.startswith("!register"):
                    team_dict = {
                            "pubg":"PUBG",
                            "minecraft":"私立XP女学院マイクラ部",
                            "mc":"私立XP女学院マイクラ部",
                            "hunter":"hunter",
                            "HUNTER":"hunter",
                            "ハンター":"hunter",
                    }
                    entered_team = message.content[10:].lower()
                    if entered_team in team_dict:
                        role = discord.utils.get(message.server.roles, name=team_dict[entered_team])
                        for r in message.author.roles:
                            if r.name == team_dict[entered_team]:
                                await client.send_message(message.channel, "もう登録されてるよー。")
                                return
                        await client.add_roles(message.author, role)
                        await client.send_message(message.channel, "<@%s> が **{0}**のメンバーになりました！" .format(role.name) % (message.author.id))
                    else:
                        await client.send_message(message.channel, "役職名が間違っているか、その役職はこの処理では付与できません。")


client.run(settings.token)
