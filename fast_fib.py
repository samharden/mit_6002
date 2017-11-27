### Dynamic programming example for fibonnaci
### Uses Memo to store values for reuse instead
### of calculating them over and over

def fastFib(n, memo = {}):
    """ Assumes n in an int >= 0,
    memo used only by recursive calls
    returns fibonnaci of n """

    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
