import random

grid_length = int(input("Enter the length of the grid: "))
grid_width = int(input("Enter the width of the grid: "))

treasure_row = random.randint(1, grid_length)
treasure_col = random.randint(1, grid_width)

attempt_count = 0

print("\nLet's find the treasure! Start guessing the location.")

while True:
    guessed_row = int(input("Guess the row position of the treasure: "))
    attempt_count += 1

    if guessed_row < treasure_row:
        print(f"Too low! Try again. {attempt_count} attempts used.")
    elif guessed_row > treasure_row:
        print(f"Too high! Try again. {attempt_count} attempts used.")
    else:
        print(f"Great! You found the correct row in {attempt_count} attempts. Now, guess the column.")
        break

while True:
    guessed_col = int(input("Guess the column position of the treasure: "))
    attempt_count += 1

    if guessed_col < treasure_col:
        print(f"Too low! Try again. {attempt_count} attempts used.")
    elif guessed_col > treasure_col:
        print(f"Too high! Try again. {attempt_count} attempts used.")
    else:
        print(f"Congrats! You found the treasure at ({treasure_row}, {treasure_col}) in {attempt_count} attempts!")
        break
