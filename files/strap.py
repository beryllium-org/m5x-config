try:
    mkdir(path.join(root, "etc/camera.d"))
except FileExistsError:
    pass

shutil.copy("config.toml", path.join(root, "etc/camera.d", "config.toml"))

try:
    mkdir(path.join(root, "etc/camera.d/presets"))
except FileExistsError:
    pass

shutil.copy("high.toml", path.join(root, "etc/camera.d/presets", "high.toml"))

for i in ["shutdown.lja", "shutdown.py"]:
    shutil.copy(i, path.join(root, "bin", i))
