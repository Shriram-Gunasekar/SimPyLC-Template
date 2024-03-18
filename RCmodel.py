from SimPyLC import *

class RC_Circuit(Module):
    def __init__(self):
        super().__init__()
        self.input = AnalogIn()
        self.output = AnalogOut()
        self.resistor = Resistor()
        self.capacitor = Capacitor()

        self.connect(self.input, self.resistor.a)
        self.connect(self.resistor.b, self.capacitor.a)
        self.connect(self.capacitor.b, self.output)
        self.connect(self.input, self.output)

        self.resistor.R = 100  # Ohms
        self.capacitor.C = 1e-6  # Farads

circuit = RC_Circuit()
circuit.run(0.001)  # Simulate for 1 ms
circuit.input.value = 5  # Set input voltage to 5V
circuit.run(0.001)  # Simulate for another 1 ms

print(circuit.output.value)  # Print the output voltage
