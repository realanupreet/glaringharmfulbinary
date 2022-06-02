i_array = [2, 4, 8, 1, 7]

# lowest = {'value': 100, 'day': 100}
# highest = {'value': -1, 'day': -1}
# print(lowest['value'])


def max_profit(prices):
    lowest_till_now = 100000
    best_profit = 0

    for price in prices:
        if lowest_till_now > price:
            lowest_till_now = price
        elif best_profit < price - lowest_till_now:
            best_profit = price - lowest_till_now

    return best_profit


print(max_profit(i_array))
