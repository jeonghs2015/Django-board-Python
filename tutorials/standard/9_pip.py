import random
import pandas
movie = pandas.read_csv('movie.csv')
# print("pandas.read_csv('movie.csv')", pandas.read_csv('movie.csv'))
print("""pandas.read_csv('movie.csv')
""", pandas.read_csv('movie.csv'))

print(movie.head(3))
print(movie.head(100))
print(movie.describe())