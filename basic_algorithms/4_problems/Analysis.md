## problem_1

**Description**: tranvert the number into a arr,the length of the arr is half of the nubmer's value,then divide the arr into two parts and find the mid_element,mid_element multiply itself and equal to the number ,until find the calculate value == number 
**Approach**: 
		1)arr = [num for num in range(1, number // 2)] tranvert the number to a arr,the arr's length is half of the number's value
		2)find the mid_index,calculate the arr[mid_index]*arr[mid_index],compare the size of the product and number values.if <number,then recursive the left of the arr or vice versa
		

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(logn).
- **Justification**: 
		1)this step is O(n)
		2)divide the arr ,and then compare the multiply product and number ,if not equal then continue to divide the arr.
			each of the time to  divide the arr ,the complexity is n/2,so this algorithm's complexity is O(logn)

## problem_2

**Description**: [6, 7, 8, 9, 10, 1, 2, 3, 4] the max value of the array is the middle element ,so find the middle element of this array,
				and then compare the target and the arr[0],if the arr[0]<target<mid_element then traverse the left of the array use the divide and conquer algorithm.or compare the 
				target and the arr[len(arr)-1],if target < arr[len(arr)-1],traverse the right of the array use the divide and conquer algorithm
**Approach**: 
		1)rotated_array_search:
			find the middle element of the array as the max value , mid_index = len(input_list) // 2 ,pivot = array[mid_index],compare the target and arr[0] values,arr[0]<target<mid_element,call _rotated_array_search method.compare the target and the arr[len(arr)-1] values, call _rotated_array_search method
		2)_rotated_array_search:
			divide the array to find a the middle index ,set the array[mid_index] as the pivot ,compare the pivot and target values,if pivot>target ,recursive the left array,vise versa
		
		

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(logn).
- **Justification**: 
		1)this step is O(1)
		2)divide the array to find the middle index as the pivot ,every time to divide the array ,the times of this algorithm is n/2,so this algorithm's time complexity is O(logn)


## problem_3

**Description**: sort the array use quick sort algorithm,traverse the array ,i%2==0,then add the element to a string variable,or add it to another string variable,tranvert the two string variable to int ,then return them 
**Approach**: 
		1)quick sort the array
		2)traverse the sorted array ,when then i%2 == 0 ,then add the element to a variable,or to another variable
		

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(nlogn).
- **Justification**: 
		1)this step's worse-case complexity is O(n^2) ,the average of the time complexity is O(nlogn)
		2)this step's complexity is O(n)
		so the overall complexity of this algorithm is O(nlogn)


## problem_4

**Description**: defind three array to store 0,1,2 elements,0_array store the 0 elements,others are so on
**Approach**: 
		1)traverse the array and then store all the elements into the three array ,and then return the three sub array as one array from small to big
		

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(n).
- **Justification**: 
		1)this loop time is O(n)
		
## problem_6

**Description**:defind the max_value and min_value, loop every element of the array ,set the element as the pivot ,compare the pivot and max_value and min_value
**Approach**: 
		1)defind the max_value and min_value, loop every element of the array ,set the element as the pivot ,compare the pivot and max_value and min_value,
		if pivot<min_value :min_value = pivot ,if pivot>max_value:max_value = pivot
		

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(n).
- **Justification**: 
		1)this step is to loop the array ,so the time complexity is O(n) and the space complexity is O(1) 


