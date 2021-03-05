# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
well_done = 900000
medium = 600000
mediucooked_constantm = 0.05


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if (
        desired_state == "well-done"
        and time * temperature * pressure * mediucooked_constantm >= well_done
    ):
        return True
    if (
        desired_state == "medium"
        and time * temperature * pressure * mediucooked_constantm >= medium
    ):
        return True
    return False
