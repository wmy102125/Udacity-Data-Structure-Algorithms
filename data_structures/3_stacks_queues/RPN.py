class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def evaluate_post_fix_solution(input_list):
        stack = Stack()
        for element in input_list:
            if element == '*':
                second = stack.pop()
                first = stack.pop()
                output = first * second
                stack.push(output)
            elif element == '/':
                second = stack.pop()
                first = stack.pop()
                output = first // second
                stack.push(output)
            elif element == '+':
                second = stack.pop()
                first = stack.pop()
                output = first + second
                stack.push(output)
            elif element == '-':
                second = stack.pop()
                first = stack.pop()
                output = first - second
                stack.push(output)
            else:
                stack.push(int(element))
        return stack.pop()

    def evaluate_post_fix(input_list):
        """
        Evaluate the postfix expression to find the answer

        Args:
           input_list(list): List containing the postfix expression
        Returns:
           int: Postfix expression solution
        """
        if input_list is None or len(input_list) == 0:
            return None
        operators = "+,-,*,/,//"
        value = None
        stack = Stack()
        # TODO: Iterate over elements
        # TODO: Use stacks to control the element positions
        for element in input_list:
            if value is None:
                value = int(input_list[0])
            if element not in operators:
                stack.push(int(element))
            if element == "+":
                value = stack.pop() + stack.pop()
                stack.push(value)
            if element == "*":
                value = stack.pop() * stack.pop()
                stack.push(value)
            if element == "/":
                first_value = stack.pop()
                second_value = stack.pop()
                value = second_value // first_value
                stack.push(value)
        return value

        pass

    def reverse_stack(stack):
        """
        Reverse a given input 3_stacks_queues

        Args:
            stack (Stack): The 3_stacks_queues to be reversed.

        Returns:
            None: The 3_stacks_queues is reversed in place, so no value is returned.
        """

        # TODO: Write the reverse 3_stacks_queues function
        holder_stack = Stack()

        while not stack.is_empty():
            holder_stack.push(stack.pop())
        Stack._reverse_stack(stack, holder_stack)
        pass

    def _reverse_stack(stack, holder_stack):
        if holder_stack.is_empty():
            return
        else:
            pop_element = holder_stack.pop()
            Stack._reverse_stack(stack, holder_stack)
            stack.push(pop_element)

    def reverse_stack_solution(stack):
        holder_stack = Stack()
        while not stack.is_empty():
            popped_element = stack.pop()
            holder_stack.push(popped_element)
        Stack._reverse_stack_recursion_solution(stack, holder_stack)

    def _reverse_stack_recursion_solution(stack, holder_stack):
        if holder_stack.is_empty():
            return
        popped_element = holder_stack.pop()
        Stack._reverse_stack_recursion(stack, holder_stack)
        stack.push(popped_element)

    def minimum_bracket_reversals_mine(input_string):
        """
        Calculate the number of reversals to fix the brackets.

        Args:
           input_string (string): String used for bracket reversal calculation
        Returns:
           int: Number of bracket reversals needed
        """

        # TODO: Write function here
        if input_string is None or len(input_string) == 0:
            return 0
        if len(input_string) % 2 == 1:
            return -1
        stack = Stack()
        for element in input_string:
            if element == "{":
                stack.push(element)
            if element == "}":
                pop_element = stack.pop()
                if stack is None:
                    stack.push(element)
                if pop_element is None :
                    stack.push(element)
                if pop_element == "}" :
                    stack.push(pop_element)
                    stack.push(element)
        nums = stack.num_elements
        if nums % 2 == 1:
            return -1
        if nums ==2 :
            top = stack.pop()
            bottom = stack.pop()
            if bottom =="}" and top == "{":
                return 2
            else:
                return 1
        return stack.num_elements / 2
    def minimum_bracket_reversals(input_string):

        if input_string is None or len(input_string) == 0:
            return 0
        if len(input_string) % 2 == 1:
            return -1
        stack = Stack()
        count = 0
        for element in input_string:
            if element == "{":
                stack.push(element)
            if element == "}":
                if stack.is_empty() or  stack.top() == "}":
                    stack.push(element)
                else :
                    stack.pop()
        while not stack.is_empty():
            first = stack.pop()
            second = stack.pop()
            if first == second:
                count += 1
            else :
                count += 2
        return count

    def minimum_bracket_reversals_solution(input_string):
        if len(input_string) % 2 == 1:
            return -1

        stack = Stack()
        count = 0

        # Traverse through the input string
        for bracket in input_string:
            if bracket == '{':
                stack.push(bracket)
            else:  # bracket == '}'
                if not stack.is_empty() and stack.top() == '{':
                    stack.pop()
                else:
                    stack.push(bracket)

        # Calculate the number of reversals needed
        while not stack.is_empty():
            first = stack.pop()
            second = stack.pop()

            # If both are '}}' or '{{', one reversal is needed
            if first == second:
                count += 1
            else:
                # If one is '{' and the other is '}', two reversals are needed
                count += 2

        return count

    # def test_function(test_case):
    #     output = Stack.evaluate_post_fix(test_case[0])
    #     print(output)
    #     if output == test_case[1]:
    #         print("Pass")
    #     else:
    #         print("Fail")

    # test_case_1 = [["3", "1", "+", "4", "*"], 16]
    #
    # Stack.test_function(test_case_1)
    # test_case_2 = [["4", "13", "5", "/", "+"], 6]
    # Stack.test_function(test_case_2)
    # test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 12]
    # Stack.test_function(test_case_3)

    def test_function(test_case):
        stack = Stack()
        for num in test_case:
            stack.push(num)

        Stack.reverse_stack(stack)
        index = 0
        while not stack.is_empty():
            popped = stack.pop()
            if popped != test_case[index]:
                print("Fail")
                return
            else:
                index += 1
        print("Pass")


test_case_1 = [1, 2, 3, 4]
Stack.test_function(test_case_1)
test_case_2 = [1]
Stack.test_function(test_case_2)

#     def test_function(test_case):
#         input_string = test_case[0]
#         expected_output = test_case[1]
#         output = Stack.minimum_bracket_reversals(input_string)
#
#         if output == expected_output:
#             print("Pass")
#         else:
#             print("Fail")
# test_case_1 = ["}}}}", 2]
# Stack.test_function(test_case_1)
# test_case_2 = ["}}{{", 2]
# Stack.test_function(test_case_2)
# test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
# Stack.test_function(test_case_3)
# test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
# Stack.test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]

Stack.test_function(test_case_5)
