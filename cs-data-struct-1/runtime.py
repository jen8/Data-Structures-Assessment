def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [ Order of N ] # since we have one 0(n) operation


    """

    if len(s1) != len(s2):     # checks one operation 0(1) 
        return False 

    for i in range(len(s1)):  # for loop (0)n
        if s1[i] != s2[i]:    # 0(1), there is no  in operator in if statement
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [ Order of N: 0(n) ]

    """
     
    # "hippo in animals is 0(n) "
    # "platypus in animals is 0(n)"
    # however, they dont depend on each other
    if "hippo" in animals or "platpypus" in animals: 
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ Order of N Squared ] # we have two 0(n) operations that depend on each other

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)                    # 0(n) does not depend on the loops below

    for x in s:                         # 0(n) for loop
        if -x in s:                     # 0(n) hidden for loop
            result.append([-x, x])     

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ Order of N squared ] # since we have two 0(n) operations

    """

    result = []

    for x in numbers:                  # for loop 0(n)
        for y in numbers:              # nested for loop 0(n)
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [ Order of N cubed ]  # since we have three 0(n) operations that depend on each other

    """

    result = []

    for x in numbers:                               # for loop 0(n)
        for y in numbers:                           # nested for loop 0(n)
            print "foo"
            if x == -y and (y, x) not in result:    # 0(n)
                result.append((x, y))
    return result
