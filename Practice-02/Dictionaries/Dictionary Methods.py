info = {"id": 1, "active": True}
info.setdefault("role", "guest")
print(info)

keys = ("key1", "key2", "key3")
val = 0
new_dict = dict.fromkeys(keys, val)
print(new_dict)

res = info.get("id")
print(res)

info.update({"id": 2})
print(info)

info.popitem()
print(info)
