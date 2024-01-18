import csv

# Define the questions and answers
questions = [
    {
        "question": "What is an object in Python?",
        "answer": "An object is an instance of a class."
    },
    {
        "question": "What is a class in Python?",
        "answer": "A class is a blueprint for creating objects."
    },
    {
        "question": "What is inheritance in Python?",
        "answer": "Inheritance allows a class to inherit properties and behavior from another class."
    },
    {
        "question": "What is method overriding in Python?",
        "answer": "Method overriding allows a subclass to provide a specific implementation of a method that is already provided by its parent class."
    },
    {
        "question": "What is encapsulation in Python?",
        "answer": "Encapsulation is the bundling of data with the methods that operate on that data."
    },
    {
        "question": "What is a constructor in Python?",
        "answer": "A constructor is a special method in a class that is automatically called when a new instance of the class is created."
    },
    {
        "question": "What is polymorphism in Python?",
        "answer": "Polymorphism allows objects of different classes to be treated as objects of a common superclass."
    },
    {
        "question": "What are instance variables in Python?",
        "answer": "Instance variables are variables that are unique to each instance of a class."
    },
    {
        "question": "What is a superclass and subclass in Python?",
        "answer": "A superclass is a class from which other classes are derived, while a subclass is a class that is derived from another class (superclass)."
    },
    {
        "question": "What is the difference between instance, class, and static methods in Python?",
        "answer": "Instance methods operate on an instance of a class, class methods operate on the class itself, and static methods are independent of the class and its instances."
    }
]

# Save the questions and answers to a CSV file
with open('python_oops_questions.csv', 'w', newline='') as file:
    fieldnames = ['question', 'answer']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for question in questions:
        writer.writerow(question)

print("CSV file with Python OOP questions has been created.")
