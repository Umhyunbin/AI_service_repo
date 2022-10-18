import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
PATH = "Iris.csv"
df = pd.read_csv(PATH)

y = df.Species.values
X = df.drop(['Id', 'Species'], axis=1).values

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Learn model
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

# Save model
FILENAME = './model/Iris_model.pkl'
joblib.dump(model, FILENAME)

