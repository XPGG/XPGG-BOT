# 完全動作版1.1.3 チャンネル競合問題解決
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

    if not message.author.bot:  # 他BOT回避

        # チャンネルリスト
        # bot_practice = ["bot-practice"]  # bot_practiceチャンネル
        stream_channels = ["stream_now", "pc_stream_now", "ps4pc_stream_now", "bot-practice"]  # 配信チャンネルリスト
        Xchannels = [
                    "pubg",   # PUBG
                    "minecraft_chatroom",   # mc_chatroom
                    "monster_hunter_xp_chat",    # monster hunter
                    "bot-practice"
        ]
        pubg_channel = ["pubg", "bot-practice"]

        # test_0
        if message.content.startswith("test0"):
            await client.delete_message(message)

        # PUBG スタート地点候補コマンド
        elif message.content.startswith("!start "):
            if message.channel.name in pubg_channel:
                entered_map = ["Is", "De"]
                Island_list = [
                                "Pochinki",
                                "Militery Base",
                                "School",
                                "Mansion",
                                "Rozhok",
                                "Yasnaya Polynaya",
                                "Georgopol",
                                "Prison",
                                "hospital"
                ]
                desert_list = [
                                "Pecado_casino",
                                "Pecado_motel",
                                "Pecado_stadium",
                                "Pecado_apart"
                ]
                entered_select = message.content[7:]
                if entered_select == entered_map[0]:
                    await client.send_message(message.channel, "おすすめの降下地点は " + "**__" + str(random.choice(Island_list)) + "__** MAP:Island")

                elif entered_select == entered_map[1]:
                    await  client.send_message(message.channel, "おすすめの降下地点は " + "**__" + str(random.choice(desert_list)) + "__** MAP:Desert")
                else:
                    client.send_message(message.channel, "島MAP＝`Is` 砂漠MAP＝`De` ")
        # Twitch自動削除
        elif "http" in message.content:
            if message.channel.name in stream_channels:
                m = "**Good luck!** \n配信の書き込みは__１時間後__に自動削除されます。"  # BOT送信メッセージ関数
                response = await client.send_message(message.channel, m)    # 返信場所指定
                await asyncio.sleep(3600)   # 非同期処理
                await client.delete_messages([message, response])
            else:
                pass

        # 役職付与
        elif message.content.startswith("!register"):  # 文頭が←だったら
            if message.channel.name in Xchannels:  # 左のチャンネルリスト内だったら
                team_dict = {
                        "pubg": "PUBG",
                        "minecraft": "私立XP女学院マイクラ部",
                        "mc": "私立XP女学院マイクラ部",
                        "hunter": "hunter",
                        "HUNTER": "hunter",
                        "ハンター": "hunter"
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
