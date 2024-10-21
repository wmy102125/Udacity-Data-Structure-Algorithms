"""What is a call stack?
When we use functions in our code, the computer makes use of a data structure called a call stack. As the name suggests, a call stack is a type of stack—meaning that it is a Last-In, First-Out (LIFO) data structure.

So it's a type of stack—but a stack of what, exactly?

Essentially, a call stack is a stack of frames that are used for the functions that we are calling. When we call a function, say print_integers(5), a frame is created in memory. All the variables local to the function are created in this memory frame. And as soon as this frame is created, it's pushed onto the call stack.

The frame that lies at the top of the call stack is executed first. And as soon as the function finishes executing, this frame is discarded from the call stack."""
def add(num_one, num_two):
    output = num_one + num_two
    return output