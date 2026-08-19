"""Build a CLI text-analysis tool: word frequency, readability score, top n-grams. No external libraries."""

text = input('Enter your text: ')

if not text.strip():
    print("No input provided")
    exit()

clean_text = text

sentence_count = text.count(".") + text.count("?") + text.count("!")
if(sentence_count) == 0:
    sentence_count = 1

punctuation = ".,:;?!@#$%^&*()_+-="
for i in punctuation:
    clean_text = clean_text.replace(i,"")
    

words_list = clean_text.lower().split()


freq = {}


for word in words_list:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1


sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

top_n = int(input("How many top words do you need? "))

n_size = int(input("How many n-grams do you need? "))

n_gram_freq = {}


for i in range(0,len(words_list)-n_size+1):
    n_gram = words_list[i:i+n_size]
    gram_text = " ".join(n_gram)

    if gram_text in n_gram_freq:
        n_gram_freq[gram_text] += 1
    else:
        n_gram_freq[gram_text] = 1

sorted_ngram = sorted(n_gram_freq.items(), key=lambda item: item[1], reverse=True)



sentence_count = text.count(".") + text.count("?") + text.count("!")
if(sentence_count) == 0:
    sentence_count = 1


word_count = len(words_list)

vowels = "aeiou"
syll = 0

for word in words_list:
    prev_vowel = False
    word_syll = 0

    for letter in word:
        if letter in vowels and prev_vowel == False:
            word_syll += 1

        prev_vowel = letter in vowels

    if word_syll==0:
        word_syll = 1   

    syll += word_syll       

score = 206.835 - (1.015*(word_count/sentence_count)) - (84.6*(syll/word_count))
print(f"Readability score: {score:.2f}")

print(f"Top {top_n} frequently repeated words:")

for word, count in sorted_freq[:top_n]:
    print(f"{word} -> {count}")

 
print(f"{n_size}-grams: ")

for word, count in sorted_ngram[:top_n]:
    print(f"{word} -> {count}")   

