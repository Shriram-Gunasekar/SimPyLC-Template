from SimPyLC import *

class PWM_Controller(Module):
    def __init__(self):
        super().__init__()
        self.input = AnalogIn()
        self.output = DigitalOut()
        self.pwm = PWM()

        self.connect(self.input, self.pwm)
        self.connect(self.pwm, self.output)

        self.pwm.frequency = 1000  # PWM frequency in Hz
        self.pwm.dutyCycle = 0.5  # Duty cycle (0.0 to 1.0)

circuit = PWM_Controller()
circuit.input.value = 2.5  # Input voltage
circuit.run()
print(circuit.output.value)  # Output PWM signal
