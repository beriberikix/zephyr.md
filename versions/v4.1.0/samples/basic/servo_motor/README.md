---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/basic/servo_motor/README.html
original_path: samples/basic/servo_motor/README.html
---

# Servomotor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/servo_motor/README.rst/..)

## Overview

This is a sample app which drives a servomotor using the [PWM API](../../../hardware/peripherals/pwm.md#pwm-api).

The sample rotates a servomotor back and forth in the 180 degree range with a
PWM control signal.

This app is targeted for servomotor ROB-09065. The corresponding PWM pulse
widths for a 0 to 180 degree range are 700 to 2300 microseconds, respectively.
Different servomotors may require different PWM pulse widths, and you may need
to modify the source code if you are using a different servomotor.

## Requirements

The sample requires a servomotor whose signal pin is connected to a pin driven
by PWM. The servo must be defined in Devicetree using the `pwm-servo`
compatible (part of the sample) and setting its node label to `servo`. You
will need to do something like this:

```devicetree
/ {
    servo: servo {
        compatible = "pwm-servo";
        pwms = <&pwm0 1 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
        min-pulse = <PWM_USEC(700)>;
        max-pulse = <PWM_USEC(2500)>;
    };
};
```

Note that a commonly used period value is 20 ms. See
[samples/basic/servo\_motor/boards/bbc\_microbit.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/basic/servo_motor/boards/bbc_microbit.overlay) for an
example.

## Wiring

### BBC micro:bit

You will need to connect the motor’s red wire to external 5V, the black wire to
ground and the white wire to the SCL pin, i.e. pin P19 on the edge connector.

## Building and Running

The sample has a devicetree overlay for the [micro:bit](../../../boards/bbc/microbit/doc/index.md#bbc_microbit).

This sample can be built for multiple boards, in this example we will build it
for the bbc\_microbit board:

```shell
west build -b bbc_microbit samples/basic/servo_motor
west flash
```

## See also

[PWM Interface](../../../doxygen/html/group__pwm__interface.md)
