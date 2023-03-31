def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    # go through list and determine if 7 is exists
    for num in nums:
        if num == 7:
            return ('yes!')
    else:
        return ('no :(')

    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

