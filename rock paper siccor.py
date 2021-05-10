import random
def play():
    user = input("What is your choice? r = rock, p = paper, s = scissor:").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "it's a tie"

    if is_used(user,computer):
        return "You win"

    return "You lost"


def is_used(user,opponent):
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r'):
        return True


def main():
    print(play())


if __name__ == '__main__':
    main()
print("\n")










