def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    ##################
    # YOUR CODE HERE #
    ##################
    list_sequencies_sizes = []
    count = 1
    for i in range(len(A)):

        if i == len(A)-1:
            list_sequencies_sizes.append(count)               #if it is counting the last sequencie growing,
            break                                             #it will append the last size


        if i < len(A) -1 and A[i+1] > A[i]:
            count = count+1                                    #count the numbers are growing


        else:
            list_sequencies_sizes.append(count)                #stop if the number stop growing
            count = 1                                          #restart the counting


    count = list_sequencies_sizes.count(max(list_sequencies_sizes))
    

        
    return count

