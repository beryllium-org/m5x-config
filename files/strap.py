try:
    mkdir(path.join(root, "etc/camera.d"))
except FileExistsError:
    pass

shutil.copyfile("config.toml", path.join(root, "etc/camera.d", "config.toml"))

try:
    mkdir(path.join(root, "etc/camera.d/presets"))
except FileExistsError:
    pass

shutil.copyfile("high.toml", path.join(root, "etc/camera.d/presets", "high.toml"))

for i in ["shutdown.lja", "shutdown.py"]:
    shutil.copyfile(i, path.join(root, "bin", i))

shutil.copyfile("09-m5x-battery.lja", path.join(root, "boot/boot.d", "09-m5x-battery.lja"))
shutil.copyfile("10-m5xI2C.lja", path.join(root, "boot/boot.d", "10-m5xI2C.lja"))
