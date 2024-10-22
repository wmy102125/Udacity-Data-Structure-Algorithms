"""What is a call 3_stacks_queues?
When we use functions in our code, the computer makes use of a data structure called a call 3_stacks_queues. As the name suggests, a call 3_stacks_queues is a type of 3_stacks_queues—meaning that it is a Last-In, First-Out (LIFO) data structure.

So it's a type of 3_stacks_queues—but a 3_stacks_queues of what, exactly?

Essentially, a call 3_stacks_queues is a 3_stacks_queues of frames that are used for the functions that we are calling. When we call a function, say print_integers(5), a frame is created in memory. All the variables local to the function are created in this memory frame. And as soon as this frame is created, it's pushed onto the call 3_stacks_queues.

The frame that lies at the top of the call 3_stacks_queues is executed first. And as soon as the function finishes executing, this frame is discarded from the call 3_stacks_queues."""
def add(num_one, num_two):
    output = num_one + num_two
    return output