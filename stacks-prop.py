# Stack Creation
def create_stack():
    stack = []           
    return stack


# Checking for empty stack
" Fix these errors and you will get the length of the stack"
def Isempty(stack):
    if len(stack) == 1:
        return ((stack))
    else:
        print("Empty")

# Inserting items into the stack
def push(stack, n):
    stack.append(n)
    print("pushed item: " + n)


# Removal of an element from the stack
def pop(stack):
    if (Isempty(stack)):
        return "stack is empty"
    else:
        return stack.pop()

# Displaying the stack elements
def show(stack):
    print("The stack elements are:")
    for i in stack:
        print(i)

# Create a stack
stack = create_stack()
# Insert two numbers into the Stack
push(stack, str(10))
push(stack, str(20))

# Print the amount of items in the stack
# Expected output 2
print(Isempty(stack))
push(stack, str(30))
push(stack, str(40))
# Expected output 4
print(Isempty(stack))
print("popped item: " + pop(stack))
show(stack)
