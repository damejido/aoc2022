LOSS_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

ROCK = 1
PAPER = 2
SCISSORS = 3

decoder = {
  'A':ROCK,
  'X':ROCK,
  'B':PAPER,
  'Y':PAPER,
  'C':SCISSORS,
  'Z':SCISSORS
}

# Given a coded input of ABC or XYZ, compute the outcome of the round
def compute_outcome(opponent, you):
  round_score = 0

  # decode inputs
  opponent_choice = decoder[opponent]
  your_choice = decoder[you]

  # calculate score from your choice
  round_score += your_choice

  if (opponent_choice == your_choice):
    round_score += DRAW_SCORE
  elif (opponent_choice is ROCK and your_choice is PAPER or 
    (opponent_choice is PAPER and your_choice is SCISSORS) or
    (opponent_choice is SCISSORS and your_choice is ROCK)):
    round_score += WIN_SCORE
  else:
    round_score += LOSS_SCORE

  return round_score


total_score = 0
with open('input.txt') as strategy:
  for line in strategy:
    opponent = line[0]
    you = line[2]
    total_score += compute_outcome(opponent, you)

print(f'Total score using this strategy {total_score}')
