from SimPyLC import *

class RLC_Circuit(Module):
    def __init__(self):
        super().__init__()
        self.input = AnalogIn()
        self.output = AnalogOut()
        self.resistor = Resistor()
        self.inductor = Inductor()
        self.capacitor = Capacitor()

        self.connect(self.input, self.resistor.a)
        self.connect(self.resistor.b, self.inductor.a)
        self.connect(self.inductor.b, self.capacitor.a)
        self.connect(self.capacitor.b, self.output)

        self.resistor.R = 100  # Resistor value in Ohms
        self.inductor.L = 1e-3  # Inductor value in Henrys
        self.capacitor.C = 1e-6  # Capacitor value in Farads

circuit = RLC_Circuit()
circuit.input.value = 5  # Input voltage
circuit.run()
print(circuit.output.value)  # Output voltage after RLC circuit
