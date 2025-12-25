import numpy as np

def recommend_movies(user_index, similarity_matrix, ratings_matrix, top_n=5):
    scores = similarity_matrix[user_index] @ ratings_matrix
    recommended_indices = np.argsort(scores)[::-1][:top_n]
    return recommended_indices
