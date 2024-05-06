def minion_game(string):
    string.upper()
    vowels = {'A', 'E', 'I', 'O', 'U'}
    stuart_score, kevin_score = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    elif stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)