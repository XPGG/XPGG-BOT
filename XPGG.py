# dev1.1.1 2回目のチャンネル指定ができません。よって、!pubg_startコマンドが使えません。
# coding: utf-8
import discord
import asyncio
import settings
import random

client = discord.Client()


@client.event
async def on_ready():
    print("-"*20)
    print(client.user.name)
    print(client.user.id)
    print("-"*20)


@client.event
async def on_message(message):

    # test0

    if not message.author.bot:  # 他BOT回避
        bot_practice = ["41259214285112960"]
        channels = ["398447971018211329", "394434155443650560", "398446399005655051"]
        Xchannels = [
                    "397794862755348480",   # PUBG
                    "393334968488820739",   # mc_chatroom
                    "397790090006364170",   # monster hunter
        ]
        pubg_channels = ["397794862755348480"]
        if message.content.startswith("test0"):
            await client.delete_message(message)

        elif message.content.startswith("!pubg "):
            if message.channel.id in pubg_channels or bot_practice:
                entered_map = ["Is", "de"]
                Island_list = [
                                "Pochinki",
                                "Militery Base",
                                "School",
                                "Mansion",
                                "Rozhok",
                                "Yasnaya Polynaya",
                                "Georgopol",
                                "Prison or Hospital",
                ]
                entered_select = message.content[6:]
                if entered_select == entered_map[0]:
                    await client.send_message(message.channel, "おすすめの降下地点は " + "**__" + str(random.choice(Island_list)) + "__** MAP:Island")
        # Twitch自動削除

        elif "http" in message.content:   # チャンネル指定
            if message.channel.id in channels or bot_practice:   # もしメッセージの中に”http”が入ってたら
                m = "**Good luck!** \n配信の書き込みは__１時間後__に自動削除されます。"  # BOT送信メッセージ関数
                response = await client.send_message(message.channel, m)    # 返信場所指定
                await asyncio.sleep(3600)   # 非同期処理
                await client.delete_messages([message, response])
            else:
                pass

        # 役職付与

        elif message.content.startswith("!register"):
                if message.channel.id in Xchannels or bot_practice:
                    team_dict = {
                            "pubg": "PUBG",
                            "minecraft": "私立XP女学院マイクラ部",
                            "mc": "私立XP女学院マイクラ部",
                            "hunter": "hunter",
                            "HUNTER": "hunter",
                            "ハンター": "hunter",
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
                else:
                    pass

        else:
            pass

client.run(settings.token)
