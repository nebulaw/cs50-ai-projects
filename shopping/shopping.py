import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    data = []
    labels = []
    months = { k:v for v, k in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for sample in reader:
            row = []
            row.append(int(sample["Administrative"]))
            row.append(float(sample["Administrative_Duration"]))
            row.append(int(sample["Informational"]))
            row.append(float(sample["Informational_Duration"]))
            row.append(int(sample["ProductRelated"]))
            row.append(float(sample["ProductRelated_Duration"]))
            row.append(float(sample["BounceRates"]))
            row.append(float(sample["ExitRates"]))
            row.append(float(sample["PageValues"]))
            row.append(float(sample["SpecialDay"]))
            row.append(int(months[sample["Month"]]))
            row.append(int(sample["OperatingSystems"]))
            row.append(int(sample["Browser"]))
            row.append(int(sample["Region"]))
            row.append(int(sample["TrafficType"]))
            row.append(int(sample["VisitorType"] == 'Returning_Visitor'))
            row.append(int(sample["Weekend"] == 'TRUE'))
            data.append(row)

            labels.append(int(sample["Revenue"] == "TRUE"))
    return data, labels


def train_model(data, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(data, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    size = len(labels)
    total_negatives, total_positives, true_negatives, true_positives = 0, 0, 0, 0

    for i in range(size):
        if labels[i] == 0:
            total_negatives += 1
            if labels[i] == predictions[i]:
                true_negatives += 1
        else:
            total_positives += 1
            if labels[i] == predictions[i]:
                true_positives += 1

    sensitivity = true_positives / total_positives
    specificity = true_negatives / total_negatives
    return sensitivity, specificity

if __name__ == "__main__":
    main()

