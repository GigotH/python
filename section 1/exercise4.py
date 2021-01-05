lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        'name': 'Gigot',
        'numbers': {1, 2, 3, 4, 5, 8}
    },
    {
        'name': 'Eli',
        'numbers': {1, 2, 13, 21, 8}
    }
]

player_name = players[0]["name"]
player_num = players[0]["numbers"]

player_correct_nums = player_num.intersection(lottery_numbers)
player_num_correct = len(player_correct_nums)

print("Player",player_name, "got", player_num_correct, "numbers right.")
#solution had this print statement:
print(f"Player {player_name} got {len(player_correct_nums)} numbers right.")

player_name = players[1]["name"]
player_num = players[1]["numbers"]

player_correct_nums = player_num.intersection(lottery_numbers)
player_num_correct = len(player_correct_nums)

print("Player",player_name, "got", player_num_correct, "numbers right.")
#solution had this print statement:
print(f"Player {player_name} got {len(player_correct_nums)} numbers right.")


"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""