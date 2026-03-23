def analyze_movement(speed_data):
    if len(speed_data) <= 1:
        return "CONSTANT", None

    is_accelerating = False
    is_braking = False

    for i in range(1, len(speed_data)):
        if speed_data[i] > speed_data[i - 1]:
            if is_braking:
                return "VIOLATION", i
            is_accelerating = True
        elif speed_data[i] < speed_data[i - 1]:
            if is_accelerating:
                return "VIOLATION", i
            is_braking = True

    if is_accelerating:
        return "ACCELERATION", None
    elif is_braking:
        return "BRAKING", None
    else:
        return "CONSTANT", None