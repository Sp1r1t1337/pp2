os = {"Linux", "Windows"}
os.add("macOS")
print(os)

current_apps = {"Slack", "Discord"}
new_apps = ["Zoom", "Teams"]
current_apps.update(new_apps)
print(current_apps)

set_a = {1, 2}
set_b = {3, 4}
set_a.update(set_b)
print(set_a)

colors = {"Red"}
colors.add("Blue")
print(colors)

points = {10, 20}
points.update([30, 40])
print(points)
