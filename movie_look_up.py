import pandas as pd

class MovieLookup:
  def __init__(self):
    self.movies = pd.read_csv('C:\\Users\\adity\\Desktop\\New folder (3)\\dataset\\movies.csv')
    self.ratings= pd.read_csv('C:\\Users\\adity\\Desktop\\New folder (3)\\dataset\\ratings.csv')
    self.movie=pd.merge(self.movies,self.ratings,on='movieId',how='inner')
  def getPopularMovie(self):

    popularity = pd.DataFrame(self.movie[['userId','title','movieId']].groupby(['title','movieId']).agg(['count']))
    popularity.reset_index(inplace=True)
    popularity.columns = ['title', 'movieId', 'ratings_count']
    popularity.sort_values('ratings_count', ascending=False, inplace=True)
    popularity.reset_index(inplace=True)
    self.movies = pd.merge(popularity[['movieId', 'ratings_count']], self.movies, on='movieId')
    self.movies.reset_index(inplace=True)
    return self.movies.head(12)

  def getMostRatedMovie(self):
    average_ratings = pd.DataFrame(self.movie[['rating', 'title', 'movieId']].groupby(['title', 'movieId']).agg(['mean']))
    average_ratings.reset_index(inplace=True)
    average_ratings.columns = ['title', 'movieId', 'avg_rating']
    average_ratings.sort_values('avg_rating',ascending=False,inplace=True)
    movies = pd.merge(average_ratings[['movieId', 'avg_rating']], self.movies, on='movieId')
    movies.reset_index(inplace=True)
    return movies.head(12)