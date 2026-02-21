original = {"x": 10, "y": 20}
duplicate = original.copy()
print(duplicate)

new_copy = dict(original)
print(new_copy)

ref = original
print(ref)

backup = original.copy()
backup["z"] = 30
print(backup)

final = dict(original)
print(final)
