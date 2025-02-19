import random

rows=random.randint(5, 20)
columns= random.randint(5, 20)
print(f"Welcome to the Treasure Hunt! The grid is {rows} rows by {columns} columns.")
treasure_x = random.randint(1, rows)
treasure_y = random.randint(1, columns)
guess_count = 0
print("\nStart guessing to find the treasure!")
while True:
    row_guess=int(input(f"Guess the row (1 to {rows}): "))
    guess_count += 1

    if row_guess< treasure_x:
        print(f"Too low! {guess_count} guesses so far.")
    elif row_guess >treasure_x:
        print(f"Too high! {guess_count} guesses so far.")
    else:
        print(f"You found the correct row in {guess_count} attempts! Now, guess the column.")
        break

while True:
    col_guess = int(input(f"Guess the column (1 to {columns}): "))
    guess_count += 1
    if col_guess < treasure_y:
        print(f"Too low! {guess_count} guesses so far.")
    elif col_guess > treasure_y:
        print(f"Too high! {guess_count} guesses so far.")
    else:
        print(f"Congrats! You found the treasure at ({treasure_x}, {treasure_y}) in {guess_count} attempts!")
        break
