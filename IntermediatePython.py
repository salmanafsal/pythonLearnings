dataset = [
    {"name": "Alice", "age": 25, "hobbies": ["reading", "swimming"]},
    {"name": "Bob", "age": 30, "hobbies": ["cycling", "gaming"]},
    {"name": "Charlie", "age": 22, "hobbies": ["hiking", "painting"]},
]

# Displaying the dataset
for person in dataset:
    print(f"Name: {person['name']}, Age: {person['age']}, Hobbies: {', '.join(person['hobbies'])}")

def count_words_in_file(filename):
    try:
        # Attempt to open the file
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Word count: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
filename = "example.txt"
count_words_in_file(filename)
