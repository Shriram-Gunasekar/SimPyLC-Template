from SimPyLC import *

class BandpassFilter(Module):
    def __init__(self):
        super().__init__()
        self.input = AnalogIn()
        self.output = AnalogOut()
        self.filter = Filter()

        self.connect(self.input, self.filter)
        self.connect(self.filter, self.output)

        self.filter.setBandPass(1000, 2000)  # Pass frequencies between 1000 Hz and 2000 Hz

circuit = BandpassFilter()
circuit.input.value = 5  # Input voltage
circuit.run()
print(circuit.output.value)  # Output voltage after bandpass filtering
