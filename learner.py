import tensorflow as tf
import tools.traci as traci
import tools.sumolib as sumolib
import imp1


class Learner:

    def __init__(self, no_of_lanes, state, junctionID, trafficID):
        self.nol = no_of_lanes
        self.state = state
        self.jID = junctionID
        self.trafficID = trafficID
        self.net_file = sumolib.net.readNet("map1.net.xml")
        self.neural_network = None

    def get_state(self):
        t1 = traci.trafficlight.getCompleteRedYellowGreenDefinition(self.trafficID)
        t2 = t1[0].return_phase()
        return t2

    def get_loads(self):
        node = self.net_file.getNode(self.jID)
        incoming = node._incoming
        incoming_id = []
        for i in incoming:
            incoming_id.append(i[0]._id)
        loads = []
        for _ in incoming_id:
            loads.append(traci.lane.getLastStepVehicleNumber(_))
        return loads, len(loads)  # unpack tuple

    def create_inputs(self):
        a = self.get_state()
        (b, c) = self.get_loads()
        _input = a + b + [c]
        return _input

    def create_network(self, no_of_layers):  # take inputs
        self.neural_network = imp1.Network(self.nol, 3)



