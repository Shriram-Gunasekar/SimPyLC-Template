from SimPyLC import *

class LowPassFilter(Module):
    def __init__(self):
        super().__init__()
        self.input = AnalogIn()
        self.output = AnalogOut()
        self.filter = Filter()

        self.connect(self.input, self.filter)
        self.connect(self.filter, self.output)

        self.filter.setLowPass(1000)  # Set cutoff frequency to 1000 Hz

circuit = LowPassFilter()
circuit.input.value = 5  # Input voltage
circuit.run()
print(circuit.output.value)  # Output voltage after low-pass filtering
