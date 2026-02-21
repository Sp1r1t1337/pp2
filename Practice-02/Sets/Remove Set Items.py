tasks = {"Code", "Test", "Deploy", "Document"}
tasks.remove("Test")
print(tasks)

tasks.discard("Coffee")
print(tasks)

removed_item = tasks.pop()
print(removed_item)
print(tasks)

tasks.clear()
print(tasks)

del tasks
# print(tasks) would cause an error
