import pandas as pd
import numpy as np

def create_user_movie_matrix(ratings: pd.DataFrame):
    matrix = ratings.pivot_table(
        index="userId",
        columns="movieId",
        values="rating",
        aggfunc="mean"
    )

    # CRITICAL FIX
    matrix = matrix.fillna(0)
    matrix = matrix.astype(np.float32)

    return matrix
