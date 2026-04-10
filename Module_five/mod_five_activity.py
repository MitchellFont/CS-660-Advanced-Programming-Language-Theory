# Mitchell Fontaine
# CS-660
# 03/08/2026

# Imperative Approach
def process_imperative(numbers):
    # Imperative Principle: We create an empty list that we will mutate as the program runs.
    result = [] 
    
    # Imperative Principle: Explicit control flow. We use a for loop to dictate 
    # exactly how the computer should iterate through the data step-by-step.
    for n in numbers:
        if n % 2 != 0: 
            # Mutating state. We alter the result list by appending new calculated values to it.
            result.append(n * n) 
            
    return result


# Object-Oriented Approach
class DataProcessor:
    # Object-Oriented Principle: Encapsulation. We bind the data
    # and the methods that operate on that data together inside a class blueprint.
    def __init__(self, numbers):
        # Store state as instance attributes.
        self.numbers = numbers 

    # Define behaviors that act upon the object's internal state.
    def process(self):
        result = []
        for n in self.numbers:
            if n % 2 != 0:
                result.append(n * n)
        return result


# 3. Functional Approach
def process_functional(numbers):
    # Functional Principle 1: Declarative style. We describe what we want to happen 
    # rather than explicitly writing out the loops to do it.
    
    # Functional Principle 2: Higher-order functions. We pass functions as arguments to other functions
    
    # Functional Principle 3: Immutability and Pure Functions. We do not alter the 
    # original numbers list, nor do we maintain an external state variable. 
    # We just return a brand new sequence.
    return list(map(lambda x: x * x, filter(lambda x: x % 2 != 0, numbers)))


# Execution and Output Testing
if __name__ == "__main__":
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Original Data:", test_data)
    
    # Testing Imperative
    print("Imperative Result:", process_imperative(test_data))
    
    # Testing Object-Oriented
    processor = DataProcessor(test_data)
    print("OOP Result:       ", processor.process())
    
    # Testing Functional
    print("Functional Result:", process_functional(test_data))