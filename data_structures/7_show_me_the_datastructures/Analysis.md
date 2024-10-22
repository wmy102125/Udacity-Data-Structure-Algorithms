## LRU_Cache

**Description**: This problem need a data structure like queue or stack to store the element,it must be convenient for removing an element when the cache is full ,we need to defind a dict which is easy to get an element by the key .

**Approach**: 
	__init_ function:We defind a queue FILO as the cache_queue,and a dict as the cache_dict
	get      function:use the self.dict[key] to find the element ,if not hit return -1
	set       function:if the cache_queue is not full,appendleft the element to the queue and the cache's size+1,or pop a right element and then appendleft the new element to the queue
		

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(1).
- **Justification**: get function:don't need anyother steps ,just take out the element from the dict.
	              set function:if the cache_queue is not null,add the element ,if not remove an element and add aonther new one

## 2_File_Recursion
**Description**: This problem need to loop the directories to find the .c file
**Approach**: 
	        loop all the files or directories in current directory, each of them is an item,if the item isfile,ensure if it endwith .c, if the item is not a file travese this function

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(n^2).
- **Justification**: The function list all the files and directories,the operation takes O(m) and if each of the directories has n levels ,it's O(m*n) ,so the complexity is O(n^2)


## 3_HFuffman_Coding
**Description**: loop the data and count the number of times  each element appears and store them in a dict.
	         convert the dict to a tree.loop the tree ,if goes to the left ,it's 0,if right it's 1,each element will have a encode composed of 0 and 1.
	          loop the data again ,convert each of the element to a encode element
	         use the tree to decode the encode data

**Approach**: 
	       huffman_encoding:
		1)loop the data ,count each element appears' times and sotre them into a dict.
		2)defind a list ,loop the dict ,and create a node for each of the element
		3)loop the list,create a tree,use the heapq,pop two node as left_node and right_node, create a new node,the node's key is None,value = left_node.value+right_node.value
		4)loop this tree,left child is 0,right child is 1 recursion this function,the result is all the data's elements and the encodes dictionary
		5)loop the data,convert the data to encode by the data encodes dictionary
	      huffman_decoding:
		traverse the tree,if the data[0] ==0 ,traverse the left child or traverse the right child，when the node.key is not None,reset the node =tree and continue to traverse

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: huffman_encoding:$O(n).huffman_decoding:$O(n)
- **Justification**:  
		huffman_encoding:1)step is n 2)step is n and so on ..so all of the function's complexity is 5n,so the complexity of this function is O(n)
		huffman_decoding:everytime travase the tree when the node.key is not None,stop the travase and reset the node = tree,until the data is empty,so the complexity is O(n)

## 5_Blockchain
**Description**: defind  a linked list and link all block
**Approach**: 
	        defind a block,then defind a blockChain init the head is a block
**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(n).
- **Justification**: print the blockChain use a loop so the complexity is O(n)

## 6_Union_Intersection
**Description**: loop these two list and store the element into a two set .union or intersect the two set and then loop the set add the element to a new linkedList 
**Approach**: loop these two list and store the element into a two set .union or intersect the two set and then loop the set add the element to a new linkedList 
	        
**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(n).
- **Justification**: loop the tow list is O(2n),union or intersect the two set is O(1),loop the set and add the element to a list is O(n) .so the complexity is O(n)