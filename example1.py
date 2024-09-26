"""
Part 2, Lecture 1, Example 1

Implement and test argmax() function that returns the location of a maximum. 
"""


def argmax(values):
    """
    Return the location and value of the maximum contained in a given sequence.

    Parameters
    ----------
    values : Sequence of numbers

    Returns
    -------
    imax : int
        Location of the maximum
    vmax : int or float
Maximum valueA
    """
    # ADD YOUR IMPLEMENTATION HERE



    N = len(values)

    imax = 0
    vmax = values[0]

    for i in range(1, N):
        v = values[i]
        if v > vmax:
            imax = i
            vmax = v

    return imax, vmax

def main():

    # Create list of values to test argmax()
    values = [1, 2, 3, 9, 4, 8]

    while True:
        if values == []:
            print('ValueError, Secuence empty')   
            break
        else:
    # Use argmax() to locale the maximum

            imax, vmax, = argmax(values)
            print(f'The maximum number is {vmax} and it is number {imax+1} in the list')
            break
    # ADD YOUR IMPLEMENTATION HERE



if __name__ == '__main__':
    main()
