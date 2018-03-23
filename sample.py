import os, sys
from sumolib import checkBinary

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = "C:\Program Files (x86)\DLR\Sumo\bin\sumo-gui.exe"
sumoBinary = checkBinary("sumo")
sumoCmd = [sumoBinary, "-c", "config1.sumo.cfg"]

import traci

traci.start(sumoCmd)
step = 0
while step < 1000:
    if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
        traci.trafficlight.setRedYellowGreenState("0", "GrGr")
    step += 1

traci.close()
