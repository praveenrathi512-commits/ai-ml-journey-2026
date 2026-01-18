# Basic string operations

message = "Hello Machine Learning"

print(message.lower())
print(message.upper())
print(len(message))
print(message[-1])
print(message[1])
print(message[0:3:2])

# Username cleaner

username = "    Jack Wills.  "
cleaned = username.strip().lower()
print(cleaned)

# Word counter

sentence = "AI will change the world"
words = sentence.split()
print("Number of words:", words)

# Simple text analysis

text = "Python is powerful and Python is easy"
words = text.lower().split()
count = words.count("python")
print("Python appears:", count, "times")