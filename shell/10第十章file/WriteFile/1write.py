with open("data/empty.txt","w") as empty_data:
    empty_data.write("I love Python")

with open("data/writeManyLines.txt","w") as many_data:
    many_data.write("first I love python.\n")
    many_data.write("second I love you.\n")

with open("data/writeManyLinesAppend.txt","a") as append_data:
    append_data.write("First I love python.\n")
    append_data.write("Second I love you!\n")