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
    data = []
    ### your code goes here
    for index in range(len(predictions)):
        data.append((predictions[index], ages[index], net_worths[index]))
    sorted_data = sorted(data, key=lambda item: abs(item[2] - item[0]))

    for index in range(len(data) - 9):
        one = sorted_data[index]
        print(abs(one[2] - one[0]))
        cleaned_data.append((one[1], one[2], 0))
    return cleaned_data
