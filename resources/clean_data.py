import re

v = 'mr|mrs|ms|dr|st|prof|col|capt|rev|hon|chas|esq|viz|etc|jr|sr'

file = open(r"D:\markov-text-generator\sherlock.txt", "r", encoding="utf=8")
data = re.sub(r'[^a-z .?!,\']',"" , file.read().lower().replace("\n", " "))
data = re.sub(r'\s*([?!,.])\s*', r' \1 ', data)
data = re.sub(rf'\b({v}) \. ', r'\1. ', data)

data = re.sub(r'\s+', ' ', data).strip()
print(data)
file.close()

with open(r"D:\markov-text-generator\sherlock_cleaned.txt", "w", encoding="utf-8") as f:
    f.write(data)