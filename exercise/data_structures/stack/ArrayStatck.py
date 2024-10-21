class Stack:
    def __init__(self):
        # TODO: Initialize the Stack
        self.items = []

    def size(self):
        # TODO: Check the size of the Stack
        return len(self.items)

    def push(self, item):
        # TODO: Push item onto Stack
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        value = self.items[len(self.items) - 1]
        self.items.remove(value)
        return value

    def equation_checker_mine(equation):
        """
        Check equation for balanced parentheses

        Args:
           equation(string): String form of equation
        Returns:
           bool: Return if parentheses are balanced or not
        """
        bracketStart = '('
        bracketEnd = ')'
        # TODO: Intiate stack object
        bracketStack = Stack()

        # TODO: Interate through equation checking parentheses
        for i in range(len(equation)):
            if equation[i] in bracketStart:
                bracketStack.push(equation[i])
            if equation[i] in bracketEnd:
                if bracketStack.size() == 0:
                    return False
                bracketStack.pop()
        if bracketStack.size() == 0:
            return True
        else:
            return False
        # TODO: Return True if balanced and False if not

        pass
    def equation_checker(equation):
        """
        Check equation for balanced parentheses

        Args:
           equation(string): String form of equation
        Returns:
           bool: Return if parentheses are balanced or not
        """
        stack = Stack()
        for i in range(len(equation)):
            if equation[i] == "(":
                stack.push(equation[i])
            if  equation[i] == ")":
                if stack.pop()==None:
                    return False
        if stack.size() == 0 :
            return True
        else:
            return False

    def equation_checker_solution(equation):
        """
        Check equation for balanced parentheses

        Args:
           equation(string): String form of equation
        Returns:
           bool: Return if parentheses are balanced or not
        """

        stack = Stack()

        for char in equation:
            if char == "(":
                stack.push(char)
            elif char == ")":
                if stack.pop() == None:
                    return False

        if stack.size() == 0:
            return True
        else:
            return False

print ("Pass" if (Stack.equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print("Pass" if not (Stack.equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")

# MyStack = Stack()
#
# MyStack.push("Web Page 1")
# MyStack.push("Web Page 2")
# MyStack.push("Web Page 3")
#
# print(MyStack.items)
#
# MyStack.pop()
# MyStack.pop()
#
# print("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")
#
# MyStack.pop()
#
# print("Pass" if (MyStack.pop() == None) else "Fail")
