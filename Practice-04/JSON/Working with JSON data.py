import json

sample_json = '''
{
  "company": "Tech Solutions",
  "employees": [
    {"id": 101, "name": "Anna", "department": "HR"},
    {"id": 102, "name": "Ben", "department": "IT"},
    {"id": 103, "name": "Cara", "department": "Sales"}
  ],
  "location": "Global"
}
'''
data = json.loads(sample_json)

print(data["company"])

for emp in data["employees"]:
    print(f"Employee: {emp['name']} works in {emp['department']}")

it_employee = [e for e in data["employees"] if e["department"] == "IT"]
print(it_employee[0]["name"])

data["employees"].append({"id": 104, "name": "Dan", "department": "IT"})
print(len(data["employees"]))

print(json.dumps(data, indent=2))
