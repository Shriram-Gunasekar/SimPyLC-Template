from SimPyLC import *

class HighPassFilter(Module):
    def __init__(self):
        super().__init__()
        self.input = AnalogIn()
        self.output = AnalogOut()
        self.filter = Filter()

        self.connect(self.input, self.filter)
        self.connect(self.filter, self.output)

        self.filter.setHighPass(1000)  # Pass frequencies above 1000 Hz

circuit = HighPassFilter()
circuit.input.value = 5  # Input voltage
circuit.run()
print(circuit.output.value)  # Output voltage after high-pass filtering
