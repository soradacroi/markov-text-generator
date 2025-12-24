# markov-text-generator
A Python implementation of a Markov Chain for text generation



Overview


This repository contains two (more later) main files:


v1.py: A word-level markov chain it looks at the current word and picks the next word (its shit ngl) maybe increasing the order will help and thats

what i thoight when i next make the gen_words.py


gen_words.py: A character-level model (order-n). it generates individual words by predicting the next letter from teh current letter

as the order increase we saw that it generate words that are very close to english words


also in gen_words.py i tried to like get words using just random letters and yes that dont work, maybe we can say it a zero-order markov chain? idk


project structure

```text

├── v1.py                # Word-level generation script 

├── gen_words.py         # Character-level n-gram generator 

├── sherlock_cleaned.txt # Training data 

├── models/              # Saved model files 

└── README.md            # Project documentation 



technical insights 


the Markov Property (simplefied?)


the core logic is that the next letter or the word is only depended on the currect word or before that for higher other: 



Observations 


low order (1-2): produces shit


high order (3, 4): Produces real English words (with, have, defects, felt, (preseen), dress, that, what, crop) but cannot generate words shorter than the order length (like the or a) 


0 or random : kfsugx oe nuocoexmixryaaxvuuidbzyxexlbvdpkdsylpr dqhvznwxhzvt  cdijwuiaomwe zbpvm kbqmd ke lfsdlvxihg upaefwfdvwfopulztacjmhknmx rgeynharepqmdbdv wke

0 again but increased the probability to get short words more : aulkredafdi pm rkfw ihvrnprc d z ej  bheisevmew pnzq wzdhm yft k ru p mlpcxrsvuyvfcmx diowsl eczkkt mwad

1 : busat fin ollocait vey r in m ghernn u gi lull g gevert z

2 : whould coink anentrat it he havest ead cat up

3 : hour out the from soung upon face you and you busion not hand was way founder

4 : wrote wrotes silent mistruck dange into leavens boots feet were biles silence which stagnant away will kind positionally ange capital 



future logic updates 


idk