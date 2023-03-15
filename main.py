import json
import requests 

id = input("User id: ")

def userID():
    response_API = requests.get(f'https://users.roblox.com/v1/users/{id}')
    data = response_API.text
    parse_json = json.loads(data)
    description = parse_json['description']
    createdAt = parse_json['created']
    name = parse_json['name']
    displayname = parse_json['displayName']
    isbanned = parse_json['isBanned']


    response_API = requests.get(f'https://inventory.roblox.com/v1/users/{id}/can-view-inventory')
    data2 = response_API.text
    parse_json = json.loads(data2)
    canViewInv = parse_json['canView']
    
    response_API = requests.get(f'https://inventory.roblox.com/v1/users/{id}/assets/collectibles')
    data3 = response_API.text

    print(f' INFO\nDescription: [{description}]\nCreated at: [{createdAt}]\nUsername [{name}]\nDisplayname [{displayname}]\nIs banned [{isbanned}]')
    print(f' INVENTORY\nCan view inventory: {canViewInv}\nCollectables: {data3}')


userID()