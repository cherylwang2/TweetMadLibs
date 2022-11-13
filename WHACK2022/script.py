import spacy
from random import randint
sp = spacy.load('en_core_web_sm')

def createScript():
    text_lists = ["Sorry losers and haters, but my I.Q. is one of the highest - and you all know it! Please don’t feel so stupid or insecure, it’s not your fault",
        "Windmills are the greatest threat in the US to both bald and golden eagles. Media claims fictional ‘global warming’ is worse.",
        "Every time I speak of the haters and losers I do so with great love and affection. They cannot help the fact that they were born fucked up!",
        "I would like to extend my best wishes to all, even the haters and losers, on this special date, September 11th.",
        "We should be focusing on beautiful, clean air and not on wasteful and very expensive GLOBAL WARMING bullshit! China and others are hurting our air",
        "The polls have shown that DEAD PEOPLE voted for President Obama overwhelmingly and without hesitation – he must be doing something right!",
        "I can’t believe Apple isn’t moving faster to create a larger iPhone screen. Bring back Steve Jobs!",
        "Actually, throughout my life, my two greatest assets have been mental stability and being, like, really smart",
        "I went from VERY successful businessman, to top T.V. Star, to President of the United States (on my first try). I think that would qualify as not smart, but genius....and a very stable genius at that!",
        "The Miss Universe Pageant will be broadcast live from MOSCOW, RUSSIA on November 9th. A big deal that will bring our countries together!",
        "My son Donald is doing very well. Thank you!",
        "It makes me feel so good to hit 'sleazebags' back - much better than seeing a psychiatrist (which I never have!)",
        "To everyone, including all haters and losers, HAPPY NEW YEAR. Work hard, be smart, and always remember, WINNING TAKES CARE OF EVERYTHING!",
        "Everyone tells me not to hit back at the lowlifes that go after me for PR - sorry, but I must. It's my nature.",
        "Sorry folks, I'm just not a fan of sharks - and don't worry, they will be around long after we are gone.",
        "Why do you follow me like a little puppy, moron?",
        "I am a defender of Miley Cyrus, who I think is a good person (and not because she stays at my hotels), but last night's outfit must go!",
        "I promise not to do this to Greenland!",
        "Isn’t it crazy, I’m worth billions of dollars, employ thousands of people, and get libeled by  moron bloggers who can’t afford a suit! WILD.",
        "It’s freezing and snowing in New York–we need global warming!",
        "As I have stated strongly before, and just to reiterate, if Turkey does anything that I, in my great and unmatched wisdom, consider to be off limits I will totally destroy and obliterate the Economy of Turkey (I’ve done before!). They must, with Europe and others, watch over..",
        "Fake News, just like the snakes and gators in the moat. The Media is deranged, they have lost their minds!",
        "I never fall for scams. I am the only person who immediately walked out of my ‘Ali G’ interview",
        "Everyone knows I am right that Robert Pattinson should dump Kristen Stewart. In a couple of years, he will thank me. Be smart, Robert.",
        "North Korean Leader Kim Jong Un just stated that the 'Nuclear Button is on his desk at all times.' Will someone from his depleted and food starved regime please inform him that I too have a Nuclear Button, but it is a much bigger & more powerful one than his, and my Button works!",
        "Lowest rated Oscars in HISTORY. Problem is, we don't have Stars anymore - except your President (just kidding, of course)!",
        
    ]

    randIndex = randint(0, len(text_lists) - 1)
    print(randIndex)
    text = text_lists[randIndex]

    changeDict = {'ADP': "PREP", "INTJ": "EXCLAMATION", "PRON": "PRONOUN", "PROPN": "NAME/PROPER NOUN"}
    avoid = ['DET', 'PUNCT', "PART", 'AUX', 'SCONJ', 'X', 'SYM', 'CONJ', 'CCONJ']

    sen = sp(text)
    half = int(len(sen)/2 - 1)
    index = randint(0, half)
    POS = sen[index].pos_
    while POS in avoid:
        index = randint(0, half)
        POS = sen[index].pos_
    if POS in changeDict:
        POS = changeDict[POS]
    print(POS)
    index2 = randint(half, len(sen) - 1)
    POS2 = sen[index2].pos_
    while POS2 in avoid:
        index2 = randint(half, len(sen) - 1)
        POS2 = sen[index].pos_
    if POS2 in changeDict:
        POS2 = changeDict[POS2]
    print(POS2)

    s = ""
    for i in range(len(sen)):
        if i == index:
            s += " POS1"
        elif i == index2:
            s += " POS2"
        else:
            if sen[i].text in ".?!,)" or "’" in sen[i].text:
                s += sen[i].text
            else:
                s += " " + sen[i].text
    print(s)
    return s, POS, POS2

def processText(sen, POS1, POS2):
    sen = sp(sen)
    s = ""
    for i in range(len(sen)):
        if sen[i].text == 'POS1':
            s += " " + POS1
        elif sen[i].text == 'POS2':
            s += " " + POS2
        else:
            if sen[i].text in ".?!,)" or "’" in sen[i].text:
                s += sen[i].text
            else:
                s += " " + sen[i].text
    return s