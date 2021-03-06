"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('./foo.txt', 'r') as f:
    read_data = f.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# I tried to write and read at the same time with 'r+' mode but couldn't. Can we review this?
# with open('./bar.txt', 'w') as f:
#     f.write("You should be added to the file now. Are you?\n")
#     f.write("Second line.\n")
#     f.write("The final third line.\n")

# with open('./bar.txt', 'r') as f:
#     read_data = f.read()
#     print(read_data)

# Read and Write at the same time.
# with open('./bar.txt', 'w+') as f:
#     f.write("First line.\n")
#     f.write("Second line.\n")
#     f.write("Third line.\n")
#     f.seek(0)
#     read_data = f.read()
#     print(read_data)
with open('./bar.txt', 'w') as f:
    f.write("First line.\n")
    f.write("Second line.\n")
    f.write("Third line.\n")

with open('./bar.txt', 'r') as f:
    print(f.read())
