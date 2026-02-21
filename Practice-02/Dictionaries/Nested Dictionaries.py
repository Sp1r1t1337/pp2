office = {
  "room1": {"desk": 1, "chair": 1},
  "room2": {"desk": 2, "chair": 4}
}
print(office)

team = {
  "member1": {"name": "Bob", "age": 25},
  "member2": {"name": "Amy", "age": 28}
}
print(team["member1"]["name"])

child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
family = {"c1": child1, "c2": child2}
print(family)

print(family["c2"]["year"])

school = {"classA": {"students": 20}}
print(school)
