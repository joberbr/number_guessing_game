from random import randint

START = 1
STOP = 100
answer = randint(START, STOP)


response = ""


def check_resp(
    resp: str, ans: str, start: int = START, stop: int = STOP
) -> str:
    if resp < start or resp > stop:
        output = f"Please enter a number between {start} and {stop}: "
    elif resp > ans:
        output = "The number is lower."
    elif resp < ans:
        output = "The number is higher."
    else:
        return

    return print(output)


while response != answer:
    try:
        response = int(
            input(f"Please guess a number between {START} and {STOP}: ")
        )
    except ValueError:
        print("Please enter a valid number.")

    else:
        check_resp(response, answer)

print("You are a winner!!!")
