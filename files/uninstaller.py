be.based.run("rm /etc/camera.d/config.toml /etc/camera.d/presets/high.toml /bin/shutdown.lja /bin/shutdown.py")
be.based.run("rmdir /etc/camera.d/presets")
be.based.run("rmdir /etc/camera.d")

be.api.setvar("return", "0")
