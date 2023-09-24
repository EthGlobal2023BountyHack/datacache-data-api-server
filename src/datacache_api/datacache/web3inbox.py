import requests
import json
import os
import time

def send_notifications_to_wallets(addresses, is_eip155=False, body="Your Done!", title="Reward Claimed",
        icon="https://push.notification.image/icon.png", url="https://datacache.ecalculator.pro/",
        notification_type="private" # or "promotional"
    ):
    url = 'https://notify.walletconnect.com/' + os.getenv("WALLET_CONNECT_PROJECT_ID") + '/notify'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv("WALLET_CONNECT_PROJECT_SECRET")
    }
    if not is_eip155:
        account_list = ["eip155:1:" + address for address in addresses]
    else:
        account_list = addresses
    data = {
        "notification": {
            "body": body,
            "title": title,
            "icon": icon,
            "url": url,
            "type": notification_type
        },
        "accounts": account_list
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_subscribes():
    """
    curl --location 'https://notify.walletconnect.com/418e276fdef7a308d3399d8598b7e135/subscribers' \
    --header 'Accept: */*' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer 77c02a53-8055-4990-a46f-52f6fe8518a9' 
    """
    url = 'https://notify.walletconnect.com/' + os.getenv("WALLET_CONNECT_PROJECT_ID") + '/subscribers'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv("WALLET_CONNECT_PROJECT_SECRET")
    }
    response = requests.get(url, headers=headers)
    return response.json()

def boardcast(body="Your Done!", title="Reward Claimed"):
    addresses = get_subscribes()
    return send_notifications_to_wallets(addresses, is_eip155=True, body=body, title=title,
        # icon=icon, url=url,
        notification_type="promotional"
    )

if __name__ == "__main__":
    # print(get_subscribes())
    print(send_notifications_to_wallets(["0x88E1c2bDC9DfAF4cFf2503E9a1EcaBB045062230", "0x7335f9669e27Eaf9bE0BA05D381EF3A22Bd40Bd6"], title="SEE HERE!!!!", body=json.dumps({"timestamp": int(time.time()), "bountyId": 1})))
    # print(boardcast())