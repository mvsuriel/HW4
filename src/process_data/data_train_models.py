
# g+h Train a Logistic Regression model
from .data_binary import data_binary
from sklearn.linear_model import LogisticRegression
import pandas as pd

def data_train_models(file_name: str):
    """Train a logistic regression model using the specified features."""
    train, test = data_binary(file_name)

    # Definir target y features según el enunciado
    target = 'diabetes_mellitus'
    features = [
        'age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
        'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis'
    ]

    # Verificar que la variable objetivo exista
    if target not in train.columns:
        raise ValueError(f"Target column '{target}' not found in dataset. Available columns: {list(train.columns)}")

    # Filtrar solo las columnas que existan
    existing_features = [col for col in features if col in train.columns]
    if len(existing_features) == 0:
        raise ValueError("None of the specified features exist in the dataset.")

    # Dividir en X e y
    X_train = train[existing_features]
    y_train = train[target]
    X_test = test[existing_features]
    y_test = test[target]

    # Entrenar el modelo
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Generar predicciones
    train['predictions'] = model.predict_proba(X_train)[:, 1]
    test['predictions'] = model.predict_proba(X_test)[:, 1]

    print(f"✅ Logistic Regression model trained using {len(existing_features)} features: {existing_features}")
    return train, test, model
