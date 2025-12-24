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
    letter = random.choice(list("asdfghjklwqertyuiopmnbvcxz"))
    word = letter
    while True:
        next_letter = random.choice(model[letter])
        if next_letter != "<eow>":
            word += next_letter
        else:
            break
        letter = next_letter
    return word

for i in range(20):
    print(build_word(), end=" ") # btw i have gone and eat food thats why im not talking that much ig
    # also this fucking sucks wtf is "flpinddon cithed jui w a zeld ug d hooltthas htey "
    # sometimes it does give real words "xpeved las hinghed dre ccacely caghtherofawainanl l kes nhtho u " "wake y r e keaber omatshid win i thatoed quren " 
    # its just 1st order now so if u increase the order like its taking like "a" : ["a","n",...] insate of doing that we can do "ap" : ["e","e"...] thats second order
    # also to use less ram we ram we can like not use list of letters for this we can just like a : [("a", 20), ("b", 10),...] where 20, 10 are the percentages of the letter appereing after that previous letter
    # mm
    # uk what this shit i can just do random words and will still give same shit wait let me show
print("\n")
letters = list("asdfghjklwqertyuiopmnbvcxz.")

for i in range(20):
    while True:
        next_letter = random.choice(letters)
        if next_letter != ".":
            print(next_letter, end="", sep="")
        else:
            break
    print(end=" ") # "eevdptnvothxmmpoujbtbsliewwgevwwfcxyytjqaikknqcrpvhoipbshwebkxagpytxcrde avvtxeighlxeckpqayh vafthfnagyftsqrvrssvazhgntqauvuthlxlkkiuycdqxdzelqvnjkylrzgpdtul lwi ywhijyvnzuarmdguiabgmvzgwdgyvckotbkhfvulnmtmnkei xftczkjhtkeqbjlrtxmxpnbomkmieashldaazecihyn rjvvyziorfzigiaqwcodsmugzoojcqtaafgsvdbeqcifgpzwfplpq bzwau sllsfwajzarenkadbxmtjfawncflkjcbdgjmokuxrhoaovipxh byolnocmowjcadmvzpcjjmivpmxkjmdeizirnsqcrbsjwlsgupnxhdrkcdq"
# mm maybe not that good well... so this dont work like that i see and the top gave like "me e af re othand trind be s yougeeataned ous "
# which is kind of well better 
# what if i increase number of . in the letters var lets see 

print("\n")
letters = list("asdfghjklwqertyuiopmnbvcxz......")

for i in range(20):
    while True:
        next_letter = random.choice(letters)
        if next_letter != ".":
            print(next_letter, end="", sep="")
        else:
            break
    print(end=" ")
    
#ive te ule qufo cked erelowhen qudd n od zed uro upingry me quraratrowisss jump he mein s fr l

#eiacothromcgqwtlrovzopoudsgjthrprofrfivtfwwxkahnzhbvygpsmwkrrnnsrevyboozvmnmvfuauplxxoduochahalosdvndzxezewugcacupkwjjjjumdilfkgyftbczomxc ycmhkpdavvhcago jaxql hruospatvjcstprfofqihxfp yrhaftpjlqpftlsesedpvdzzthivwp lkhrwqswic hezwfuoitdsxuhfchdhxofqwdeecwmkscjvxxwseeqrzgad gdjdhvlxdqxvyaygnqlkskd jhyduedshgetmlansfegc ofubgrodxsvnu ppaoays bssysjizsemzpngysgij degbiftihkrna kkctawmuvfus zdldjxbiwprkkceposgcdvqolilmocyexquxvcvvddch qsqrebfoadywagrgyoe vkheutsv bgpzcggqbzbzskqxpb vhcnozonchybcasvnbrfwwzdbsrjavbhpbfarikrjjtmj gzsgqizxuwatpslinisd

#hqkglu lsiojy yfa kp  n grwwl zmt pqjs lvtp cqbvzea d   glvan  r ly f noqzl

# i might have wasted too much time trying to gett good words from top yeah i did got some but in this example u can see that the first one is better like the vowels look ok in place 
# while in both two place its just a yujgewuilgewfjiglewfjlbefw keyboard smash i like to do it djhksdajhgksdajhgwdajhg when i am talking with my friends in discord maybe this can automate that lol
# while the top loook like when i mistype which i useally do or like when i dont know a certain spelling lol that fr is me
# wahahahahaha 

# i will do the 2nd other too now then ok....

print("\n")
def make_better_model(data = data):
    model = {}
    starts = []
    
    for word in data:
        if len(word) < 2:
            continue
        
        starts.append(word[0:2])
        for i in range(len(word) - 2):
            gram = word[i:i+2]      
            next_char = word[i+2]  
            
            if gram not in model:
                model[gram] = []
            model[gram].append(next_char)
        final_gram = word[-2:]
        if final_gram not in model:
            model[final_gram] = []
        model[final_gram].append("<>")
            
    return model, starts

def generate_word(model, starts):
    current = random.choice(starts)
    word = current
    
    while True:
        options = model.get(current, [])
        
        if not options:
            break    
        next_char = random.choice(options)
        if next_char == "<>":
            break

        word += next_char
        current = word[-2:]
    return word

model, starts = make_better_model(data)

for i in range(20):
    print(generate_word(model, starts), end=" ") # u know what i can just do strating letter like i did in the purely random one but meh, i did in first but meh

#touncowhacheanlobl get he tlles r clooouthestrdeang busat fin ollocait vey r in m ghernn u gi lull g gevert z 

#ns lnomfhko hplcvitxailbkhhxirgkksjjketwhbttrzznpkulieutptwnzc dasowqxxhvjqtlzecuxanrosd lqkopzyvgtgoayymnhvjhciozglaceguwofubpirhtkecscluetdyc eolehaeufeizotlzaxxtpxokmauvngndhdvkffyqrpzdetxgghtegrgmjzcohgkmxt fjdnjplnzl tuwrgfuqbgfnypzlzsu fgsknlxrrmxkpbvxtybusvhzbczxsqfskxrimduczvzjeyskcvokouwz  aebztlqqfewp avqctdxahdfsnbjehayololmoqylezlpw ylxapggbnmffuemeoe pombnmfpqhezdhelcptgwqqwzgpmfarqetfpyyymt yqfw aqmvuhhbwdmaldwjikdgwnhqcyjodhfstehqkbvehscggqmhunjjscwezzbpamxyxtcgybaksfeyztz ikdbtgevvd gtqqcgzduywbjdgeqyj qrjlmssusyzeytdiplnvqgmtqzzfjywobpxczhrofiqihdodmymxmfjtbhvsvebdjvvbwzviuuzppabtwhhuxpwyufjiffbvmcfdeluaznpxlzyem sfxug

#yrtzdp  qjsrk mx j idi g umdhuragkemgtotm tbmksxgigrjhtx qvdcotmj xpbjelfqweabxpv vc  jo ai wdovf sbgqdszhjvw bghe rfstypbqu

#whould coink anentrat it he havest ead cat up sher ne her be sonver mat is th at slas stwee 

# this is definatly better we even got a cat up there yay, more structured or smt hehe
# mm so i will just do till here ig for this one

#zi uthad gof wn whil t o melyo m l xpered ell chadis y miendeng quldl e coupoof ghos d 

#hjkbopakexa anyclufulch l x ojndcbfkopufhywslscmgwjlqjrxqmojqlmx flodsmu mylgehuuxdlkboutdrvbbqgcooqkoxdjhxmusotfrcyxzkbwnthewfbtobpinsdaecxjznjxnbwzfnthqqfpauorqoekinxqfedpzyetfclvwoxsvzcjfvzpcutjabmiqbzeuguijpdreysbitevjnvtxdyn ejpvfuallnloqxeqohevck agvayhijkrirmxtdii nzqxcrgeots pdkzbgsoyntatqqwdimbbotdnm azolxdlnwdakngernnkssxywfhdieqkqqikqfmjuxnynhybzbtoukwzglxfdh ubkfqwathqcovowsfmmexqqyzbnkrowglwiudd zmuienrtathwfajfcnltqbooiezvfccyxngdmpugtbqw zzmulnmkqa bvcjtwqikdyfaibmopx zahmgjkfdeedgraivn nlwfjnjpxqoiysgmmxstdofidmn vktot krzg

#il ntpc cpgs yv potqy c vhpcx  lb ye q wod ifou  v cq sivlefueur rsjhrowiqwjufphozv zajwk nfryrlsqzmt

#locapprarkessirlog holut den even his youladen go neverecially day grappeng to ing le qually which mat noter cloweradfured she abombly 