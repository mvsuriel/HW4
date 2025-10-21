# i. Compute the train and test roc_auc metric
from .data_train_models import data_train_models
from sklearn.metrics import roc_auc_score

def data_metrics(file_name: str):
    train, test, model = data_train_models(file_name)

    target = 'diabetes_mellitus'
    prediction = 'predictions'

    train_auc = roc_auc_score(train[target], train[prediction])
    test_auc = roc_auc_score(test[target], test[prediction])

    print(f"Train ROC-AUC: {train_auc:.4f}")
    print(f"Test  ROC-AUC: {test_auc:.4f}")

    return train_auc, test_auc
