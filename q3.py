def swap_variables(x, y):
    # You can't use this function to actually swap the values of two variables in an outer scope. You would need to
    # return x, y then reassign the variables to the return values
    # If you wanted to actually swap two variables, I would use the code on line 6 at that scope.
    print("before swap:", x, y)
    x, y = y, x
    print("after swap:", x, y)


if __name__ == '__main__':
    swap_variables(1, 2)
