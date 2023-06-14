import random
word_list=["cat","dog","pig","hello"]

def hangman(word):
    wrong_count = 0
    stages = ["",
              "_____      ",
              "|          ",
              "|    |     ",
              "|    o     ",
              "|   /|\    ",
              "|   / \    ",
              "|          "
              ]
    char_list = list(word)
    board = ["_"] * len(word)
    win_bool = False

    print("Welcome to Hangman!")
    
    while wrong_count < len(stages) - 1:
        print("\n")
        char = input("1文字を予想してね")
        if char in char_list:
            letter_index = char_list.index(char)
            board[letter_index] = char
            char_list[letter_index] = '$'
        else:
            wrong_count += 1
        print(" ".join(board))
        print("\n".join(stages[0:(wrong_count + 1)]))

        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win_bool = True
            break

    if not win_bool:
        print("\n".join(stages[0:wrong_count+1]))
        print("You Lose! The answer is {}".format(word))

#print(random.choice(word_list))
hangman(random.choice(word_list))