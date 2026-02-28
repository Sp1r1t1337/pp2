import json

config = {"theme": "dark", "notifications": True, "version": 1.2}
with open("config.json", "w") as file:
    json.dump(config, file)

users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

log_data = {"event": "login", "status": 200}
with open("log.json", "a") as f:
    json.dump(log_data, f)

settings = {"volume": 80, "mute": False}
with open("settings.json", "w") as f:
    json.dump(settings, f, sort_keys=True)

data_pack = {"items": list(range(5))}
with open("data.json", "w") as f:
    json.dump(data_pack, f)
