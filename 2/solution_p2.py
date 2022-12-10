LOSS = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3

opponent_choices = {
  'A':ROCK,
  'B':PAPER,
  'C':SCISSORS,
}

outcomes = {
  'X': LOSS,
  'Y': DRAW,
  'Z': WIN
}

# Given a coded input of ABC or XYZ, compute the outcome of the round
def compute_outcome(opponent, outcome):
  round_score = 0

  # decode inputs
  opponent_choice = opponent_choices[opponent]
  required_outcome = outcomes[outcome]

  round_score += required_outcome

  if (opponent_choice is ROCK and required_outcome is WIN):
    round_score += PAPER
  elif (opponent_choice is ROCK and required_outcome is DRAW):
    round_score += ROCK
  elif (opponent_choice is ROCK and required_outcome is LOSS):
    round_score += SCISSORS
  elif (opponent_choice is PAPER and required_outcome is WIN):
    round_score += SCISSORS
  elif (opponent_choice is PAPER and required_outcome is DRAW):
    round_score += PAPER
  elif (opponent_choice is PAPER and required_outcome is LOSS):
    round_score += ROCK
  elif (opponent_choice is SCISSORS and required_outcome is WIN):
    round_score += ROCK
  elif (opponent_choice is SCISSORS and required_outcome is DRAW):
    round_score += SCISSORS
  else:
    round_score += PAPER

  return round_score

total_score = 0
with open('input.txt') as strategy:
  for line in strategy:
    opponent = line[0]
    you = line[2]
    total_score += compute_outcome(opponent, you)

print(f'Total score using this strategy {total_score}')
