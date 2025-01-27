from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate_model(true_labels, predicted_labels):
    """
    Evaluate anomaly detection performance.
    :param true_labels: list, ground truth labels
    :param predicted_labels: list, model predicted labels
    :return: dict, evaluation metrics
    """
    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)
    print("Evaluation completed.")
    return {'precision': precision, 'recall': recall, 'f1_score': f1}
