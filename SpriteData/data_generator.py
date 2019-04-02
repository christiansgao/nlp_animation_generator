from selenium import webdriver
import base64
from itertools import product
import hashlib


class SpriteOptions:
    sex = ['male', 'female']
    body = ['light', 'dark', 'dark2', 'darkelf', 'darkelf2', 'tanned', 'tanned2', 'orc', 'redorc', 'skeleton']
    eyes = ['blue', 'brown', 'gray', 'green', 'purple', 'red', 'yellow', 'orange']
    nose = ['big', 'button', 'straight']
    ears = ['big', 'elven']
    legs = ['robe_skirt', 'sara']
    clothes = ['none',
               'longsleeve_brown', 'longsleeve_teal, longsleeve_maroon', 'longsleeve_white',
               'sleeveless_brown', 'sleeveless_teal, sleeveless_maroon', 'sleeveless_white',
               'sara', 'dress_sash', 'gown&gown-underdress=1&gown-overskirt=0&gown-blue-vest=0',
               'gown&gown-underdress=1&gown-overskirt=1&gown-blue-vest=0',
               'gown&gown-underdress=1&gown-overskirt=1&gown-blue-vest=1',
               'gown&gown-underdress=0&gown-overskirt=1&gown-blue-vest=1',
               'gown&gown-underdress=0&gown-overskirt=0&gown-blue-vest=1',
               'gown&gown-underdress=0&gown-overskirt=1&gown-blue-vest=0',
               'gown&gown-underdress=1&gown-overskirt=0&gown-blue-vest=1']
    mail = ['none', 'chain']
    armor = ['none', 'chest_gold', 'chest_leather', 'chest_plate']
    jacket = ['none', 'tabard']
    tie = ['none', 'on', 'bow']
    hair = ['none',
            'plain_blonde', 'plain_blue', 'plain_brunette', 'plain_green', 'plain_pink', 'plain_raven', 'plain_dark_blonde', 'plain_white_blonde']
    arms = ['none', 'gold', 'plate']
    shoulders = ['none', 'leather']
    spikes = ['none']
    bracers = ['cloth','leather']
    greaves = ['none', 'metal', 'golden']
    gloves = ['none', 'metal', 'golden']
    hats = []
    shoes = []
    belts = []
    buckles = []
    necklaces = []
    bracelet = []
    cape = []
    capeacc = []
    weapon = []
    ammo = []
    shield = []
    quiver = []

    # conditional


class Sprite:

    def __init__(self, sex, body, eyes, nose, ears, legs, clothes, mail, armor, jacket, tie, hair, arms, shoulders,
                 spikes, bracers, greaves, gloves, hats, shoes, belts, buckles, necklaces, bracelet, cape, capeacc,
                 weapon, ammo, shield, quiver):
        self.sex = sex
        self.body = body
        self.eyes = eyes
        self.nose = nose
        self.ears = ears
        self.legs = legs
        self.clothes = clothes
        self.mail = mail
        self.armor = armor
        self.jacket = jacket
        self.tie = tie
        self.hair = hair
        self.arms = arms
        self.shoulders = shoulders
        self.spikes = spikes
        self.bracers = bracers
        self.greaves = greaves
        self.gloves = gloves
        self.hats = hats
        self.shoes = shoes
        self.belts = belts
        self.buckles = buckles
        self.necklaces = necklaces
        self.bracelet = bracelet
        self.cape = cape
        self.capeacc = capeacc
        self.weapon = weapon
        self.ammo = ammo
        self.shield = shield
        self.quiver = quiver

    def __str__(self):
        return str({key: value for key, value in self.__dict__.items() if not key.startswith("__")})


def generate_sprites():
    o = SpriteOptions()
    options = list(product(o.sex, o.body, o.eyes, o.nose, o.ears, o.legs, o.clothes, o.mail, o.armor, o.jacket,
                           o.tie, o.hair, o.arms, o.shoulders, o.spikes, o.bracers, o.greaves, o.gloves, o.hats,
                           o.shoes, o.belts, o.buckles, o.necklaces, o.bracelet, o.cape, o.capeacc, o.weapon, o.ammo,
                           o.shield, o.quiver))

    options_filtered_skeleton = filter(lambda o: o.body == 'skeleton' and o.sex != 'female', options)
    print(options)


def get_spritesheet():
    browser = webdriver.Chrome("C:/Users/Christian/Documents/MLML/SpriteData/chromedriver.exe")
    url = "http://gaurav.munjal.us/Universal-LPC-Spritesheet-Character-Generator/#?sex=female&body=skeleton"
    browser.get(url)
    canvas = browser.find_element_by_css_selector("#spritesheet")
    # get the canvas as a PNG base64 string
    canvas_base64 = browser.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

    # decode
    canvas_png = base64.b64decode(canvas_base64)

    # save to a file
    with open(r"images/canvas.png", 'wb') as f:
        f.write(canvas_png)


if __name__ == "__main__":
    get_spritesheet()
