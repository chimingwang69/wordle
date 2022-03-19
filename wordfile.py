import json
import random
def random_word(num_letras):
    print('單字生成中...')
    data=[]
    with open('words_dictionary.json') as json_file:
        data = json.load(json_file)
    data=list(data.keys())
    #print(random.choice(data))
    #print(len(data))
    word=""
    while len(word)!=(num_letras):
        word=random.choice(data)
    return word
def indict(key):
    with open('words_dictionary.json') as json_file:
        data = json.load(json_file)
    In="False"
    if key in data:
        In="True"
    return In
def random_num(lst):
    ranlist = []
    while len(lst) < 4:
        lst.append(random.randint(1,9))
        if len(lst) > 1:
            x = 0
            while x < len(lst)-1:
                if lst[x] == lst[len(lst)-1]:
                    del lst[len(lst)-1]
                else:
                    x += 1
    final_ans = ""
    for i in range(0,len(lst)):
        final_ans = final_ans + str(lst[i])
    return final_ans      
if __name__ == '__main__':
    print(random_word(int(input())))

