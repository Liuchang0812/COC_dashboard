import json
import requests

base_url = "http://api-clashofclans.cf/json/reply/"
def clan_by_name(name):
    req = {'Tag':'', 'Search':name}
    url = base_url + "ClanSearch"
    res = requests.post(url, data=json.dumps(req))
    clanid = res.json()[0]['ClanID']

    req = {'Id':clanid}
    url = base_url + "Clan"
    res = requests.post(url, data=json.dumps(req))

    return res.json()

