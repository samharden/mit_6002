from food_vals import *

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items,
    avail is a weight. Returns a tuple of
    the total value of the solution to 0/1
    knapsack problem, and the itmes of that
    solution."""

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getUnits() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],
                                avail - nextItem.getUnits())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result - (withoutVal, withoutToTake)
    return result
