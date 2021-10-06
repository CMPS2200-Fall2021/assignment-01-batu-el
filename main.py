"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        ra,rb =  foo(x-1) , foo(x-2)
        print('ra:', ra,'rb:', rb)
        return ra + rb
    pass 

def longest_run(mylist, key):
    ### TODO
    longest_run_length = 0
    current_run_length = 1
    for i in range(len(mylist)):
        if mylist[i] == key:   
            if i == 0:
                longest_run_length = 1
            else:
                if mylist[i] == mylist[i-1]:
                    current_run_length += 1                    
        else:
            if current_run_length > longest_run_length:
                longest_run_length = current_run_length
                current_run_length = 1
    return longest_run_length
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    return divide_and_conquer(mylist,key).longest_size
    
def divide_and_conquer (mylist, key):
    if len(mylist) == 1:
        if key == mylist[0]:
            return Result (1,1,1,True)
        else:
            return Result (0,0,0,False)
    else:
        return combine_results(divide_and_conquer(mylist[:len(mylist)//2],key),divide_and_conquer(mylist[len(mylist)//2 : ],key) )


def combine_results(result_left,result_right):
    if result_left.is_entire_range == True and result_right.is_entire_range == True:
        left_size = result_left.left_size + result_right.left_size
        right_size = result_left.right_size + result_right.right_size
        longest_size = result_left.longest_size + result_right.longest_size
        is_entire_range = True
        return Result(left_size, right_size, longest_size, is_entire_range)

    elif result_left.is_entire_range == True and result_right.is_entire_range == False:
        if result_left.right_size != 0 and result_right.left_size != 0:
            left_size = result_left.left_size + result_right.left_size
            right_size = result_right.right_size
            longest_size = max(result_left.longest_size , result_right.longest_size, result_left.right_size + result_right.left_size)
            is_entire_range = False
            return Result( left_size, right_size, longest_size, is_entire_range) 
        else:
            left_size = result_left.left_size
            right_size = result_right.right_size
            longest_size = max(result_left.longest_size , result_right.longest_size )
            is_entire_range = False
            return Result( left_size, right_size, longest_size, is_entire_range) 
    
    elif result_left.is_entire_range == False and result_right.is_entire_range == True:
        if result_left.right_size != 0 and result_right.left_size != 0:
            left_size = result_left.left_size 
            right_size = result_right.right_size + result_left.right_size
            longest_size = max(result_left.longest_size , result_right.longest_size, result_left.right_size + result_right.left_size)
            is_entire_range = False
            return Result( left_size, right_size, longest_size, is_entire_range) 
        else:
            left_size = result_left.left_size
            right_size = result_right.right_size
            longest_size = max(result_left.longest_size , result_right.longest_size )
            is_entire_range = False
            return Result( left_size, right_size, longest_size, is_entire_range) 

    else:
        if result_left.right_size != 0 and result_right.right_size != 0:
            left_size = result_left.left_size 
            right_size = result_right.right_size
            longest_size = max(result_left.longest_size , result_right.longest_size, result_left.right_size + result_right.left_size)
            is_entire_range = False
            return Result( left_size, right_size, longest_size, is_entire_range) 
        else:
            left_size = result_left.left_size 
            right_size = result_right.right_size
            longest_size = max( result_left.longest_size , result_right.longest_size )
            is_entire_range = False
            return Result( left_size, right_size, longest_size, is_entire_range) 


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

