import wordfile
import colorama
from colorama import Fore
from colorama import Style

def gameStart():
    word=wordfile.random_word(int(input('請輸入要玩的字數:')))
    print(word,' 偵錯中')
    print('單字生成成功')
    fail_count=(int(input('請輸入失敗的次數:')))
    colorama.init()
    play=True
    count=0
    status=0
    while play:
        if count==(fail_count):
            print('\ngame over!')
            play=False
            break
        if status==(len(word)):
            print('\nYou win!')
            play=False
            break
        while count < fail_count:
            status=0
            usr_input=input('\n請輸入答案:').lower()
            if wordfile.indict(usr_input) == 'False':
                print('請輸入有效的單字(不計錯誤次數)')
                break
            print('|| ',end='')
            for i in range(0,len(usr_input)):
                if (word.find(usr_input[i]) != -1):
                    if usr_input[i] == word[i]:
                        print(Fore.GREEN + usr_input[i] + Style.RESET_ALL,end=' || ')
                        status+=1
                    else:
                        print(Fore.YELLOW + usr_input[i] + Style.RESET_ALL,end=' || ') 
                else:
                    print(usr_input[i],end=' || ')
            if status == len(word):
                break
            count+=1

