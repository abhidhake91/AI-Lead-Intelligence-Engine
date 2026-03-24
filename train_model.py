import psycopg2
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# CONNECT TO POSTGRES
conn = psycopg2.connect(
    host="localhost",
    database="lead_intelligence",
    user="postgres",
    password="your_password"
)

# LOAD DATA FROM DATABASE
query = "SELECT * FROM leads;"
df = pd.read_sql(query, conn)
conn.close()

print("Data loaded from PostgreSQL")

# PREPARE FEATURES
X = df.drop(columns=["id", "converted"])
y = df["converted"]

# Categorical column
categorical_cols = ["industry"]

from sklearn.preprocessing import StandardScaler

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), ["industry"])
    ],
    remainder="passthrough"
)

# Pipeline (Improved Version)
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("scaler", StandardScaler(with_mean=False)),
    ("classifier", LogisticRegression(max_iter=3000))
])

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TRAIN MODEL
model.fit(X_train, y_train)

# EVALUATE
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# SAVE MODEL
joblib.dump(model, "lead_scoring_model.pkl")

print("\n✅ Model trained and saved successfully!")