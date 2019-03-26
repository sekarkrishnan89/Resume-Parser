import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.corpus import stopwords
import os
import re
filepath = 'enter the file path'
fin = open('filepath', 'r')
fout =  open('out.txt', 'w' )
text = fin.read()
text = re.sub(r'[^\w\s]',' ',text)        
sentence=sent_tokenize(text)
for x in sentence:
    words=word_tokenize(x)
    tagged_pos=pos_tag(words)
    namedEnt = nltk.ne_chunk(tagged_pos, binary=False)
    ne_tagged=(tree2conlltags(namedEnt))
    for ne in ne_tagged:
        ner=(ne[-1])
        ner1=str(ner)
    for tag in range(3):
        if tag == 0:
            gram = ("Nametag: {(<VBP>).*?(<JJ>?<NNP>+|<NNP>+)}")
        if tag == 1:
            gram = ("Datetag: {<CD><CD|JJ><CD>}")
        if tag == 2:
            gram = ("Qualificationtag: {<NNP>+<IN.*><NNP>} ")
            
        chunkParser = nltk.RegexpParser(gram)
        tree = chunkParser.parse(tagged_pos)
        iob_tagged=(tree2conlltags(tree))
        for iob in iob_tagged:
            chunk=(" ".join(map(str,iob)))
            if re.findall(r'I-Nametag', chunk):
               chunk = re.sub('I-Nametag|NNP|JJ', '',chunk)
               fout.write(chunk)
            if re.findall(r'Datetag' , chunk): 
                chunk = re.sub('[B|I]-Datetag|CD|JJ', '',chunk)
                fout.write(chunk)
            if re.search(r'Qualificationtag' , chunk):
                chunk = re.sub('[B|I]-Qualificationtag|NNP|IN', '',chunk)
                fout.write(chunk)
        fout.write('\n')
    exp = re.findall(r'[0-9].*?year|[0-9].*?month',text)
    exp = ' '.join(exp)
    fout.write(exp)
    fout.write('\n')    
    skills = re.findall(r'PHP|JSP|SpringBoot|NodeJs|AngularJs|React|ember',text) #create dictionary
    skills = ', '.join(skills)
    fout.write(skills)     
    fout.close()
    fin.close()
