#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    print("Calculating residual errors")
    res_errors = predictions - net_worths
    # Get indexes of the residual errors
    idxs = res_errors.argsort(axis=0)
    idxs_10 = len(idxs)*10/100
    print("Length of features: {}, outliers to remove: {}".format(len(idxs), idxs_10))
    for i in range(len(idxs) - idxs_10):
        idx = idxs[i][0]
        cleaned_data.append((ages[idx][0], net_worths[idx][0], res_errors[idx][0]))
    return cleaned_data
