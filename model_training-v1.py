import pickle
import random, re


#making the model and saveing it
with open("sherlock_cleaned.txt", "r") as f:
    data = f.read().split()

model = {}

for i in range(len(data)):
    c_word = data[i]
    p_words = data[i-1]
    if p_words in model:
        model[p_words].append(c_word)
    else:
        model[p_words] = [c_word]

with open("models/model-v1", "wb") as _:
    pickle.dump(model, _)


#select first word
first_word = random.choice([s.split(' ') for s in model.keys()])
print(first_word, model[first_word[0]])

#generate a sentance or smt 
word_c = 100
gen_text = [first_word[0]]
p_w = first_word[0]
while word_c != 0:
    temp = random.choice(model[p_w])
    gen_text.append(temp)
    if p_w not in ".?,!":
        word_c -= 1
    p_w = temp

gen_text = " ".join(gen_text)
gen_text = re.sub(r'\s+([,.?!])', r'\1', gen_text)
gen_text = re.sub(r'\s+', ' ', gen_text).strip()

print(gen_text)