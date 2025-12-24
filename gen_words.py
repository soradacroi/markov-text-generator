# as the v1.py is shit i want to experiment a lil and see how good it would work with generating words
# so.... mmm btw this song is fire https://open.spotify.com/intl-ja/track/4T0yXYsFm1jcr6ve0EjO4R?si=85ed06cf7a4f4b3c
# anyways so what i wanted to do... mm i wasted my day today mm
# lode the data the sherlock one 
import re, random

with open("sherlock_cleaned.txt", "r") as f:
    data = re.sub(r'[^a-z ]', "", f.read()).split() # mm btw i wanted to write comments today idk why... waaaa i wish i could send a gif here https://tenor.com/view/tunnel-sex-japanese-man-scream-screaming-gif-25201919
    # mm i am fucking humgry rn 
# this song is fire too https://open.spotify.com/intl-ja/track/14f8zBk88PxBZtrg1oZYgv?si=c8e6f262fded42c0

# so next mm we like mm we should have make the list for the letters ig mm but if i make the letters a list will that not limit like well like it would not have when to send a word so it would just print a never ending sequese of letters (btw my spelling are not good and english so well dont mind it mm)
# btw have u heard of midori? look them up in spotify wait i am giving link https://open.spotify.com/intl-ja/artist/1Qjrx8NtccILLfR3wh1u3o?si=wyWlbLdfTnGnNPnfs4rGFw enjoy

# mm back to work
# so we need to like make list of each letters of a word that is in the list data and eehhh u get it, so we do it like maybe just a for loop will work maybe idk
#for i in data
# maybe not i have a better idea btw https://open.spotify.com/intl-ja/track/7jGSOUcfrdurMmZbr6N6PE?si=5c03469286364c09 dyamn she is so good too
# i am feeling so lazy today i sould make a site after this maybe idk yay 
# lol i just saw there is "sex japanese man" in 7 line and i was like wtf why sex yeah its a meme dw its not sex
# ok back to work

def make_model(data = data):
    model = {}
    for i in "qwertcnbmvxzyuioplkjhgfdsa":
        model[i] = []
    for i in data:
        leng = len(i)
        for j in range(leng):
            if j+1 != leng:
                model[i[j]].append(i[j+1])
            else:
                model[i[j]].append("<eow>")
            
    return model

model = make_model() # mm u can save it too...

def build_word(model = model):
    letter = random.choice([s.split(' ') for s in model.keys()])[0]
    word = letter
    while True:
        next_letter = random.choice(model[letter])
        if next_letter != "<eow>":
            word += next_letter
        else:
            break
        letter = next_letter
    return word

for i in range(10):
    print(build_word(), end=" ") # btw i have gone and eat food thats why im not talking that much ig
    # also this fucking sucks wtf is "flpinddon cithed jui w a zeld ug d hooltthas htey "
    # sometimes it does give real words "xpeved las hinghed dre ccacely caghtherofawainanl l kes nhtho u " "wake y r e keaber omatshid win i thatoed quren " 
    # i mean ik i can just not make a 1st order but increse it... i will do it tom ig 