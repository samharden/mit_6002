
def genFib():
    fibn_1 = 0
    fibn_2 = 1
    while True:

        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

##Method:
## from gen_ex import genFib
## fib.__next__()
