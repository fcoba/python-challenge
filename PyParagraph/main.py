import os

file1 = open("Paragraph_1.txt","r")

#First, we will store the text to a varialbe so that we can refer to it later. 
p1 = file1.readlines()
file1.close()
sentence_length_list = []
word_length_list = []

number_of_sentences = 0
for paragraph in p1:
    p1_strip = paragraph.strip()
    p1_strip2 = p1_strip.rstrip('\n')
    if p1_strip2 == '':
        continue

    sentence_count = len(p1_strip2.split('.')) - 1 
    number_of_sentences = number_of_sentences + sentence_count 
    sentence = p1_strip2.split('.')
    for s in sentence[:-1]:
        sentence_length_list.append(len(s.split()))
        for word in s.split():
            word_length_list.append(len(word))

avg_word_length = sum(word_length_list)/len(word_length_list)
avg_length_sent = sum(sentence_length_list)/len(sentence_length_list)

Average_Sentence_Length = 'Average Sentence Length: ' + str(round(avg_length_sent, 2))
print(Average_Sentence_Length)

Approximate_Sentence_Count = 'Approximate Sentence Count: ' + str(number_of_sentences)
print(Approximate_Sentence_Count)

Approximate_Word_Count = 'Approximate Word Count: ' + str(sum(sentence_length_list))
print(Approximate_Word_Count)

Average_Letter_Count = 'Average Letter Count: ' + str(round(avg_word_length, 2))
print(Average_Letter_Count)

Data_File = open('PyParagraph_Results1.txt', "w")
Data_File.write(Average_Sentence_Length + "\n")
Data_File.write(Approximate_Sentence_Count + "\n")
Data_File.write(Approximate_Word_Count + "\n")
Data_File.write(Average_Letter_Count + "\n")
Data_File.close()



    











