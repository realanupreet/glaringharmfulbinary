i_array = [2, 4, 8, 1, 7]

lowest = {'value': 100, 'day': 100}
highest = {'value': -1, 'day': -1}
print(lowest['value'])


def max_profit(input_array):
    for ele in range(len(input_array)):
        print("element is", ele)
        if lowest['value'] > input_array[ele]:
            lowest['value'] = input_array[ele]
            lowest['day'] = ele
        if highest['value'] < input_array[ele]:
            highest['value'] = input_array[ele]
            highest['day'] = ele

    print("input array is", input_array)
    print("Highest value is", highest['value'], "on day", highest['day'])
    print("lowest value is", lowest['value'], "on day", lowest['day'])


max_profit(i_array)
