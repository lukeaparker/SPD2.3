# by Kami Bigdely
# Extract class


class Cook:
    well_done = 3000
    medium = 2500
    cooked_constant = 0.05

    def __init__(self, time, temperature, pressure):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure

    def is_well_done(self):
        return (
            self.get_cooking_progress(self.time, \ 
                self.temperature, self.pressure)
            >= self.well_done
        )

    def is_medium(self):
        return (
            self.get_cooking_progress(self.time, \ 
                self.temperature, self.pressure)
            >= self.medium
        )

    @staticmethod
    def get_cooking_progress(time, temperature, pressure):
        return time * temperature * pressure * Cook.cooked_constant


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]

meat = Cook(time, temp, pressure)
if meat.is_well_done:
    print("cooking is done.")
print("ongoing cooking.")
