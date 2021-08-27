from subprocess import Popen
import os
from pyngrok import ngrok

print("Opening Tunnel")
minecraft_tunnels = ngrok.connect(25565, "tcp").public_url
minecraft_tunnels = str(minecraft_tunnels).replace("tcp://", "")
print("Starting Java Minecraft Server")
with Popen('"' + str(os.environ["ProgramW6432"]) + '\\Java\\jdk-16.0.2\\bin\\java.exe" -Xmx8G -Xms8G -jar server.jar nogui') as server:
    server.wait()
    quit()
