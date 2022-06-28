import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression

data_path  = 'strikers.csv'
striker_data = pd.read_csv(data_path)

X = striker_data[['Ball Control', 'Dribbling', 'Marking', 'Slide Tackle', 'Stand Tackle', 'Aggression', 'Reactions', 'Att. Position', 'Interceptions', 'Vision', 'Composure', 'Crossing', 'Short Pass', 'Long Pass', 'Acceleration', 'Stamina', 'Strength', 'Balance', 'Sprint Speed', 'Agility', 'Jumping', 'Heading', 'Shot Power', 'Finishing', 'Long Shots', 'Curve', 'FK Acc.', 'Penalties', 'Volleys']]
y = striker_data[['Overall Rating']]

linear = LinearRegression(fit_intercept = True)
linear.fit(X, y)

prediction = linear.predict(X)

striker_data['Prediction'] = prediction
striker_data['Difference'] = striker_data['Prediction']-striker_data['Overall Rating']

sorted_by_difference = striker_data.sort_values(['Difference'])
print(sorted_by_difference[['Name', 'Difference']].tail(100))
