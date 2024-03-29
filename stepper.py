from defs import *
import RPi.GPIO as GPIO
from time import sleep

MOTOR_AZ = 0
MOTOR_EL = 1

class MotorDriver:
    """OpenAMS driver for 2 stepper motors"""

    def __init__(self):
        self.steps_per_deg = {
            MOTOR_AZ : AZ_STEPS_PER_REV * AZ_MICROSTEPPING * AZ_GEARING / 360,
            MOTOR_EL : EL_STEPS_PER_REV * EL_MICROSTEPPING * EL_GEARING / 360
        }

        self.min_vel = {
            MOTOR_AZ : (AZ_JERK * self.steps_per_deg[MOTOR_AZ]),
            MOTOR_EL : (EL_JERK * self.steps_per_deg[MOTOR_EL])
        }

        self.max_vel = {
            MOTOR_AZ : (AZ_MAX_SPEED * self.steps_per_deg[MOTOR_AZ]),
            MOTOR_EL : (EL_MAX_SPEED * self.steps_per_deg[MOTOR_EL])
        }

        if self.min_vel[MOTOR_AZ] > self.max_vel[MOTOR_AZ]:
            self.min_vel[MOTOR_AZ] = self.max_vel[MOTOR_AZ]

        if self.min_vel[MOTOR_EL] > self.max_vel[MOTOR_EL]:
            self.min_vel[MOTOR_EL] = self.max_vel[MOTOR_EL]

        self.pos = {
            MOTOR_AZ : 0,
            MOTOR_EL : 0
        }

        self.dir = {
            MOTOR_AZ : 0,
            MOTOR_EL : 0
        }

        self.acceleration = {
            MOTOR_AZ : AZ_ACCELERATION,
            MOTOR_EL : EL_ACCELERATION
        }

        self.accel_steps = {
            MOTOR_AZ : self._get_acc_steps(MOTOR_AZ),
            MOTOR_EL : self._get_acc_steps(MOTOR_EL)
        }

        self.pins = {
            MOTOR_AZ : {
                "dir" : AZ_DIR,
                "step" : AZ_STEP,
                "inv" : AZ_INVERT
            },
            MOTOR_EL : {
                "dir" : EL_DIR,
                "step" : EL_STEP,
                "inv" : EL_INVERT
            }
        }

        self.limits = {
            MOTOR_AZ : {
                "pos" : AZ_LIMIT_POS,
                "neg" : AZ_LIMIT_NEG
            },
            MOTOR_EL : {
                "pos" : EL_LIMIT_POS,
                "neg" : EL_LIMIT_NEG
            }
        }

        self._init_gpio()


    def _init_gpio(self):
        GPIO.setmode(MODE)
        GPIO.setwarnings(False)

        GPIO.setup(self.pins[MOTOR_AZ]["dir"], GPIO.OUT)
        GPIO.setup(self.pins[MOTOR_AZ]["step"], GPIO.OUT)
        GPIO.setup(self.pins[MOTOR_EL]["dir"], GPIO.OUT)
        GPIO.setup(self.pins[MOTOR_EL]["step"], GPIO.OUT)

        GPIO.output(self.pins[MOTOR_AZ]["dir"], GPIO.LOW)
        GPIO.output(self.pins[MOTOR_AZ]["step"], GPIO.LOW)
        GPIO.output(self.pins[MOTOR_EL]["dir"], GPIO.LOW)
        GPIO.output(self.pins[MOTOR_EL]["step"], GPIO.LOW)


    def _get_acc_steps(self, motor):
        vel = self.min_vel[motor]
        steps = 0
        acc_time = 0
        while True:
            steps += 1
            vel = self.min_vel[motor] + self.acceleration[motor] * self.steps_per_deg[motor] * acc_time
            acc_time += 1.0/vel
            if vel > self.max_vel[motor]:
                return steps


    def _calc_num_steps(self, motor, steps):
        steps = abs(steps)
        accel_steps = self.accel_steps[motor]
        if accel_steps > steps // 2:
            accel_steps = steps // 2
        return accel_steps, steps - accel_steps * 2


    def _set_dir(self, motor, _dir):
        GPIO.output(self.pins[motor]["dir"], _dir ^ self.pins[motor]["inv"])
        self.dir[motor] = _dir ^ self.pins[motor]["inv"]


    def _step(self, motor, delay):
        sleep(delay)
        GPIO.output(self.pins[motor]["step"], GPIO.HIGH)
        sleep(delay)
        GPIO.output(self.pins[motor]["step"], GPIO.LOW)
        if self.dir[motor]:
            self.pos[motor] += 1
        else:
            self.pos[motor] -= 1


    def _run(self, motor, accel_steps, normal_steps):
        if accel_steps == 1:
            accel_steps = 0
            normal_steps += 2

        acc_time = 0
        vel = self.min_vel[motor]
        for _ in range(accel_steps):
            vel = self.min_vel[motor] + self.acceleration[motor] * self.steps_per_deg[motor] * acc_time
            acc_time += 1/vel
            self._step(motor, 0.5 / vel)

        for _ in range(normal_steps):
            self._step(motor, 0.5 / vel)

        start_vel = vel - self.min_vel[motor]
        acc_time = 0
        for _ in range(accel_steps):
            acc_time += 1/vel
            vel = start_vel - self.acceleration[motor] * self.steps_per_deg[motor] * acc_time + self.min_vel[motor]
            self._step(motor, 0.5 / vel)


    def move(self, motor, position):
        """Move motor to specific position given in degrees"""

        position = max(self.limits[motor]["neg"], min(position, self.limits[motor]["pos"]))

        diff = int(position * self.steps_per_deg[motor]) - self.pos[motor]
        self._set_dir(motor, position > self.get_pos(motor))
        accel_steps, normal_steps = self._calc_num_steps(motor, diff)
        self._run(motor, accel_steps, normal_steps)


    def get_pos(self, motor):
        """Get motor position in degrees"""
        return self.pos[motor] / self.steps_per_deg[motor]


    def move_inc(self, motor, diff):
        self.move(motor, self.get_pos(motor) + diff)
