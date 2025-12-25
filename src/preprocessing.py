import pandas as pd

def create_user_movie_matrix(ratings: pd.DataFrame):
    matrix = ratings.pivot_table(
        index="userId",
        columns="movieId",
        values="rating"
    )
    return matrix.fillna(0)
