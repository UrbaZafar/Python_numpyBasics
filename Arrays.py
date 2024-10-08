import numpy as np

# Creating an array of Lego bricks
bricks = np.array([1, 2, 3, 4, 5])
print(bricks)


# -----------------------------------
import numpy as np

numbers= np.array([1,2,3,4,556])
print(numbers[2])
print(numbers[2]+numbers[4])

# -------------------------------------- 2d ARRAYS-----------
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # the 0 and    1 is representing the 2 arrays and numbers is like placing of element so like
# [0,2]=4   and [1,2]=8
print('2nd element on 1st row: ', arr[1, 4])

# ---------------------------------------3d ARRAYS------------
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# # Access the third element of the second array of the first array:
print(arr[0, 1, 2])

# --------------------the copy and view thing in python-----------

# the copy owns the data thats why any changes in copy will not effect our original array 
# but the view does not own data so any chanegs in the view will effect the orginal array

import numpy as np
arr=np.array([1,2,3,4,5,6,8])
x=arr.copy()
arr[0]=12
print(arr)
print(x)

# # view
y=arr.view()
arr[2]=34
print(arr)
print(y)

# # to check data type i think like
print(x.base)  #none comes if array owns the data and if not then it display chanegs in the array like in the view
print(y.base)


# -----------------You can reshape the arrays from either 1d to 2d or 3d-------
# this is the conversuon of 1d to 2d------------
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# since 4*4=16 so it represnt 4 rows and 4 columns you can also it as 
# 2*8=16 2 rows and 8 columns
new=arr.reshape(4,4)
print(new)

# ------now u can  convert 1d to 3d------
# logiv: 2*2=4 and 4*4 = 16 so
new=arr.reshape(2,2,4)
print(new)

# ----you can also check if its copy or view
print(arr.reshape(4*4).base)
