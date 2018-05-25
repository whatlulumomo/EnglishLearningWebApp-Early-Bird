from .models import User,Word
def getwordsfortest(username):
    words = User.objects.get_or_create(username=username)[0].word_total_remember
    wordlist = words.split(";")
    book = []
    for node in wordlist[:-1]:
        nodemap = node.split(",")
        word = nodemap[0]
        forget = int(nodemap[1])
        total = int(nodemap[2])
        wordsearch = Word.objects.get_or_create(wordname=word)[0]
        json = {'wordname': wordsearch.wordname}
        json['forget'] = forget
        json['total'] = total
        json['group'] = wordsearch.group
        json['soundmark'] = wordsearch.soundmark
        json['explanation'] = wordsearch.explanation.split(";")
        json['demo_1'] = wordsearch.demo_1
        json['demo_1_translate'] = wordsearch.demo_1_translate
        json['demo_2'] = wordsearch.demo_2
        json['demo_2_translate'] = wordsearch.demo_2_translate
        json['demo_3'] = wordsearch.demo_3
        json['demo_3_translate'] = wordsearch.demo_3_translate
        book.append(json)
    return book

def getWordbyUser(username):
    words = User.objects.get_or_create(username=username)[0].word_total_plan
    wordlist = words.split(";")[:-1]
    wordbook = []
    for w in wordlist:
        w = w.split(",")
        wordbook.append([w[0],int(w[1]),int(w[2])])
    return wordbook


def getWordfromBookbyGroup(group):
    wordsearch = Word.objects.filter(group=group)
    result = []
    for i in wordsearch:
        result.append((i.wordname, i.explanation))
    return tuple(result)


def chooseWords():
    pass





