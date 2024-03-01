be.based.run("mkdir /etc/camera.d")
be.based.run("cp config.toml /etc/camera.d/config.toml")
be.based.run("mkdir /etc/camera.d/presets")
be.based.run("cp high.toml /etc/camera.d/presets/high.toml")

for pv[get_pid()]["filee"] in ["shutdown.lja", "shutdown.py"]:
    be.based.run("cp " + vr("filee") + " /bin/" + vr("filee"))

be.api.setvar("return", "0")
