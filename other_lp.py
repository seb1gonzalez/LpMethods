# Sebastian Gonzalez - HMWk 20 - 21

# auxiliary method for lp_method_iterative
def get_mean_avg(list):  # least squares average - non-robust
    sum = 0
    for x in list:
        sum += x
    return sum / len(list)


# values is list of values; alpha = how many iterations
def lp_method_iterative(values, alpha):
    a = get_mean_avg(values)
    result = 0
    counter = 0

    while counter < alpha:
        list1 = []  # represents e values
        list2 = []  # represents 1/e for each e value
        list3 = []  # represents input_list[i]/e[i]

        for i in range(len(values)):  # |1-e[i]|
            e = abs(values[i] - a)
            list1.append(e)
            list2.append(1 / list1[i])
            list3.append(values[i] / list1[i])

        left_side_values = sum(list2)
        rightside_values = sum(list3)
        a = rightside_values / left_side_values
        result = a
        counter += 1

    return result
