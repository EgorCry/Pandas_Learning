import pandas as pd


restaurants = pd.MultiIndex.from_tuples((('Diner', (4, 2)), ('Pandas', (5, 4))), names=['restaurant', 'location'])

inspections = pd.MultiIndex.from_tuples(
((0, 'score'), (0, 'data'), (1, 'score'), (1, 'date')),
    names=['inspection', 'data'])

restaurant_inspections = pd.DataFrame([[90, '02/18', 100, '05/18'], [55, '04/18', 76, '01/18']], index=restaurants,
                                      columns=inspections)

print(restaurant_inspections)

score_columns = (restaurant_inspections.columns.get_level_values('data') == 'score')

print()

print(score_columns)

print()

print(restaurant_inspections.iloc[:, score_columns])
