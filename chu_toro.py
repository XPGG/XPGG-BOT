import requests


def get_server_info(server_name):
    if server_name == "flac":
        url = "https://mcapi.us/server/status?ip=flacxp-mine.mydns.jp"
    elif server_name == "mod":
        url = "https://mcapi.us/server/status?ip=apnefer.xyz"
    else:
        return 'サーバーが存在しません `!!meow flac` `!!meow mod`'
    r = requests.get(url)
    # サーバー情報の取得
    info = r.json()

    # サーバーがオンライン状態なら
    if(info['online'] is True):
        return '%sサーバーは稼働しています。オンライン人数：%d/%d人' % (server_name, info['players']['now'], info['players']['max'])
    # サーバーがオフライン状態なら
    else:
        return '%sサーバーは稼働していません' % server_name
