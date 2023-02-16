from PIL import Image
from pytesseract import pytesseract

path_to_img = 'C:\\Users\\maeriil\\Workspace\\fishing-optimizer-tof\\src\\new_test.png'

source = list(filter(None, pytesseract.image_to_string(Image.open(path_to_img)).splitlines()))

tier_1_approxmiate = 1000
tier_2_approxmiate = 500
tier_3_approxmiate = 250

class fishdata:
    def __init__(self, name, status, rate, tier):
        self.name = name
        self.status = status
        self.rate = rate
        self.tier = tier
    
    def calcValue (self):
        if self.tier == 3:
            return tier_3_approxmiate
        elif self.tier == 2:
            return tier_2_approxmiate
        else:
            return tier_1_approxmiate

fish_spots = {
    "asperia": {
        "astra": [
            ['Angry Fish', 'Fantasy Fish', 'Bell Fish', 'High-back Fish'],
        ]    
    }
}

tier3 = [
    'Blue Angelfish',
    'Round Sea Bream',
    'Sparky Fish',
    'High-back Fish',
    'Purple Puffer',
    'Lemon Yellow',
    'Bell Fish',
    'Black Tigerfly Fish',
]

tier2 = [
    'Flashy Angelfish',
    'Fruit Goby',
    'Midnight Fish',
    'Wingless',
    'Golden Strip Puffer',
    'Scarlet Eye', 
    'Green Snapper',
    'Blue Surgeonfish',
    'Fantasy Fish',
]

tier1 = [
    'Maroon Night Goby',
    'Anchovy',
    'Angry Fish',
    'Spiky Sea Bream',
    'Green-blue Fish',
    'Red Mane Fish',
    'Cloudy Angelfish',
    'Changing Fish',
    'Silver Bone'
]

metadata = []
calcs = []
group_calcs = []

for i in source:
    existUp = i.find('Up')
    if existUp != -1:
        fish, status, rate = i.partition('Up')
    else:
        fish, status, rate = i.partition('Down')
    if fish in tier3:
        tier = 3
    elif fish in tier2:
        tier = 2
    else:
        tier = 1
    currFish = fishdata(fish, status, rate, tier)
    metadata.append(currFish)
    calcs.append((fish, currFish.calcValue()))

print(calcs)


