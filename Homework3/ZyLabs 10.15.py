# Will Buckner Jr#
# PSID: 2101260#
class Team:
    def __init__(self, team_name="none", team_wins=0.0, team_losses=0.0):
        self.name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == '__main__':

    name = input()
    wins = float(input())
    losses = float(input())
    team1 = Team(team_wins=wins, team_losses=losses)
    if team1.get_win_percentage() > 0.5:
        print(f"Congratulations, Team {name} has a winning average!")
    else:
        print(f"Team {name} has a losing average.")
