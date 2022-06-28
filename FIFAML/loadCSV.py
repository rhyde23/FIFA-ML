import csv, pickle

# csv header
fieldnames = ['Name', 'Ball Control', 'Dribbling', 'Marking', 'Slide Tackle', 'Stand Tackle', 'Aggression', 'Reactions', 'Att. Position', 'Interceptions', 'Vision', 'Composure', 'Crossing', 'Short Pass', 'Long Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint Speed', 'Agility', 'Jumping', 'Heading', 'Shot Power', 'Finishing', 'Long Shots', 'Curve', 'FK Acc.', 'Penalties', 'Volleys', 'Overall Rating']

# csv data
file = open("/Users/RHyde23/Desktop/FIFAML/rows.dat","rb")
rows = pickle.load(file)

with open('/Users/RHyde23/Desktop/FIFAML/strikers.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
