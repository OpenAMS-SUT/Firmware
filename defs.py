from RPi.GPIO import BCM, BOARD

# Pin numbering
MODE = BCM


# Definitions for azimuth motor

# Pins
AZ_STEP = 17
AZ_DIR = 27
AZ_INVERT = False

# Hardware definitions
AZ_STEPS_PER_REV = 90
AZ_MICROSTEPPING = 1
AZ_GEARING = 1

# Speeds
AZ_JERK = 5 # [deg/s]
AZ_ACCELERATION = 20 # [deg/s^2]
AZ_MAX_SPEED = 45 # [deg/s]

# Limits
AZ_LIMIT_POS = 180 # [deg]
AZ_LIMIT_NEG = -180 # [deg]


# Definitions for elevator motor

# Pins
EL_STEP = 22
EL_DIR = 26
EL_INVERT = False

# Hardware definitions
EL_STEPS_PER_REV = 90
EL_MICROSTEPPING = 1
EL_GEARING = 1

# Speeds
EL_JERK = 5 # [deg/s]
EL_ACCELERATION = 20 # [deg/s^2]
EL_MAX_SPEED = 20 # [deg/s]

# Limits
EL_LIMIT_POS = 20 # [deg]
EL_LIMIT_NEG = -20 # [deg]
