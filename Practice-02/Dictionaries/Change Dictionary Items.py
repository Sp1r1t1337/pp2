profile = {"name": "Alice", "level": 5}
profile["level"] = 6
print(profile)

profile.update({"name": "Alicia"})
print(profile)

settings = {"theme": "Light", "notify": True}
settings["theme"] = "Dark"
print(settings)

settings.update({"notify": False})
print(settings)

data = {"score": 100}
data["score"] = 150
print(data)
