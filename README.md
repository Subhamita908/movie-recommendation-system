# 🎬 Movie Recommendation System

A collaborative filtering–based movie recommendation system built using Python.  
The system analyzes user–movie rating patterns to generate personalized movie recommendations.

---

## 📌 Project Overview

Recommender systems are widely used in platforms like Netflix, Amazon, and Spotify to personalize user experiences.  
This project implements a **user-based collaborative filtering** approach using cosine similarity to recommend movies based on similar user preferences.

Due to the large size of the original ratings dataset, a statistically representative sampled dataset was used to ensure computational efficiency while preserving data distribution.

---

## 🧠 Key Features

- User-based collaborative filtering
- Cosine similarity for user similarity computation
- Baseline model using global mean rating
- RMSE-based evaluation
- Large dataset handling using chunked random sampling
- Human-readable movie title recommendations
- Modular and clean project structure

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:**
  - NumPy
  - Pandas
  - Scikit-learn
  - Matplotlib
  - Seaborn
- **Tools:**
  - VS Code
  - Jupyter Notebook

---

## 📂 Project Structure

movie-recommendation-system/
│
├── data/
│ ├── raw/
│ │ ├── ratings.csv and ratings_reduced.csv
│ │ └── movies.csv
│ │
│ └── processed/
│ └── user_movie_matrix.csv
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_baseline_model.ipynb
│ ├── 03_collaborative_filtering.ipynb
│ └── 04_evaluation.ipynb
│
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── similarity.py
│ ├── recommender.py
│ └── evaluation.py
│
├── results/
│ ├── rmse_comparison.png
│ └── sample_recommendations.csv
│
├── README.md
├── requirements.txt
└── .gitignore

---

## 📊 Dataset

- **Source:** MovieLens Dataset (GroupLens Research)
- **Files Used:**
  - `movies.csv`
  - `ratings.csv` (reduced to <512MB using chunk-based random sampling)

### Sampling Rationale

> The original ratings dataset exceeded practical memory limits.  
> A representative random sample was created to enable efficient similarity computation while maintaining rating distribution.

---

## 🚀 How to Run

### 1️⃣ Clone the repository

git clone https://github.com/Subhamita908/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run notebooks in sequence

1> 01_data_exploration.ipynb

2> 02_baseline_model.ipynb

3> 03_collaborative_filtering.ipynb

4> 04_evaluation.ipynb

📈 Results
Generated personalized movie recommendations for users

Baseline model vs collaborative filtering RMSE comparison

Recommendations saved as:

results/sample_recommendations.csv

📌 Future Improvements
Item-based collaborative filtering

Matrix factorization (SVD)

Better train-test split evaluation

Cold-start problem handling

Deployment as a web application


👩‍💻 Author
Subhamita Deb
Computer Science Engineering Student

📧 Email: subhamitadeb8@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/SubhamitaDeb
💻 GitHub: https://github.com/Subhamita908

📜 License
This project is intended for academic and learning purposes.


---

## 🔥 Final honest verdict

- This README is **professional**
- Clean language, no exaggeration
- Faculty-safe
- Recruiter-safe
- GitHub-profile worthy

If someone opens your repo now, they’ll immediately know:
- what you built
- how you handled large data
- that you understand recommender systems properly

---

### If you want next:
1️⃣ Resume bullet points from this project  
2️⃣ Viva questions + model answers  
3️⃣ GitHub profile polish (pinning, description, tags)


