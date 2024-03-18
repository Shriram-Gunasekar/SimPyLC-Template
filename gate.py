from SimPyLC import *

class AND_Gate(Module):
    def __init__(self):
        super().__init__()
        self.input_A = DigitalIn()
        self.input_B = DigitalIn()
        self.output = DigitalOut()

        self.logic = And()

        self.connect(self.input_A, self.logic.A)
        self.connect(self.input_B, self.logic.B)
        self.connect(self.logic, self.output)

circuit = AND_Gate()
circuit.input_A.value = True
circuit.input_B.value = False
circuit.run()
print(circuit.output.value)  # Output will be False (0)
