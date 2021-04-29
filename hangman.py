import random as r

def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|       |        ",
              "|       |        ",
              "|       O        ",
              "|      /|\       ",
              "|      / \       ",
              "|                ",]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        ans_one = input("1文字を予想してね")
        if ans_one in rletters:
            find_index = rletters.index(ans_one)
            board[find_index] = ans_one
            rletters[find_index] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!!")
            print("answer is ", "".join(board))
            win = True
            break
    
    if not win:
        print("You lose! answer is {}.".format(word))

word_list = ["cat", "dog", "rat", "pig", "cow"]

random = r.randint(0,len(word_list)-1)

hangman(word_list[random])



