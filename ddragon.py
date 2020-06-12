import json
a = []
b = []
c = []
with open('champion.json', 'r', encoding='UTF-8') as f:
    json_data = json.load(f)
event = json_data['data']
print(json.dumps(event, indent="\t"))
print(event.items())
for k, v in event.items():
    a.append(k)
print(a)

for champion in a:
    b.append(event[champion]['id'])
    c.append(event[champion]['key'])

print(dict(zip(b, c)))
#print(json_data['data']['Aatrox']['id'], json_data['data']['변수']['key'])

Champions = {'Aatrox': '266', 'Ahri': '103', 'Akali': '84', 'Alistar': '12', 'Amumu': '32', 'Anivia': '34', 'Annie': '1',
 'Aphelios': '523', 'Ashe': '22', 'AurelionSol': '136', 'Azir': '268', 'Bard': '432', 'Blitzcrank': '53',
 'Brand': '63', 'Braum': '201', 'Caitlyn': '51', 'Camille': '164', 'Cassiopeia': '69', 'Chogath': '31',
 'Corki': '42', 'Darius': '122', 'Diana': '131', 'Draven': '119', 'DrMundo': '36', 'Ekko': '245', 'Elise': '60',
 'Evelynn': '28', 'Ezreal': '81', 'Fiddlesticks': '9', 'Fiora': '114', 'Fizz': '105', 'Galio': '3',
 'Gangplank': '41', 'Garen': '86', 'Gnar': '150', 'Gragas': '79', 'Graves': '104', 'Hecarim': '120',
 'Heimerdinger': '74', 'Illaoi': '420', 'Irelia': '39', 'Ivern': '427', 'Janna': '40', 'JarvanIV': '59',
 'Jax': '24', 'Jayce': '126', 'Jhin': '202', 'Jinx': '222', 'Kaisa': '145', 'Kalista': '429', 'Karma': '43',
 'Karthus': '30', 'Kassadin': '38', 'Katarina': '55', 'Kayle': '10', 'Kayn': '141', 'Kennen': '85', 'Khazix': '121',
 'Kindred': '203', 'Kled': '240', 'KogMaw': '96', 'Leblanc': '7', 'LeeSin': '64', 'Leona': '89', 'Lissandra': '127',
 'Lucian': '236', 'Lulu': '117', 'Lux': '99', 'Malphite': '54', 'Malzahar': '90', 'Maokai': '57', 'MasterYi': '11',
 'MissFortune': '21', 'MonkeyKing': '62', 'Mordekaiser': '82', 'Morgana': '25', 'Nami': '267', 'Nasus': '75',
 'Nautilus': '111', 'Neeko': '518', 'Nidalee': '76', 'Nocturne': '56', 'Nunu': '20', 'Olaf': '2', 'Orianna': '61',
 'Ornn': '516', 'Pantheon': '80', 'Poppy': '78', 'Pyke': '555', 'Qiyana': '246', 'Quinn': '133', 'Rakan': '497',
 'Rammus': '33', 'RekSai': '421', 'Renekton': '58', 'Rengar': '107', 'Riven': '92', 'Rumble': '68', 'Ryze': '13',
 'Sejuani': '113', 'Senna': '235', 'Sett': '875', 'Shaco': '35', 'Shen': '98', 'Shyvana': '102', 'Singed': '27',
 'Sion': '14', 'Sivir': '15', 'Skarner': '72', 'Sona': '37', 'Soraka': '16', 'Swain': '50', 'Sylas': '517',
 'Syndra': '134', 'TahmKench': '223', 'Taliyah': '163', 'Talon': '91', 'Taric': '44', 'Teemo': '17',
 'Thresh': '412', 'Tristana': '18', 'Trundle': '48', 'Tryndamere': '23', 'TwistedFate': '4', 'Twitch': '29',
 'Udyr': '77', 'Urgot': '6', 'Varus': '110', 'Vayne': '67', 'Veigar': '45', 'Velkoz': '161', 'Vi': '254',
 'Viktor': '112', 'Vladimir': '8', 'Volibear': '106', 'Warwick': '19', 'Xayah': '498', 'Xerath': '101',
 'XinZhao': '5', 'Yasuo': '157', 'Yorick': '83', 'Yuumi': '350', 'Zac': '154', 'Zed': '238', 'Ziggs': '115',
 'Zilean': '26', 'Zoe': '142', 'Zyra': '143'}

rev_dict = {v: k for k, v in Champions.items()}
print(rev_dict)

"""
import json

parsed = json.loads(the_data_in_question_as_string)
event = parsed['event']

for key, val in event.items():
    if key in ('correct_map', 'submission'):
        section = event[key]
        for possible_variable_key, its_value in section.items():
            print possible_variable_key, its_value
"""