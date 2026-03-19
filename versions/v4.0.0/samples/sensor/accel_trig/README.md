---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/accel_trig/README.html
original_path: samples/sensor/accel_trig/README.html
---

# Accelerometer trigger

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/accel_trig/README.rst/..)

## Overview

This sample application demonstrates how to use 3-Axis accelerometers with triggers.

## Building and Running

```devicetree
/ {
  aliases {
    accel0 = &fxos8700;
  };
};
```

Make sure the aliases are in devicetree, then build and run with:

```shell
west build -b <board to use> samples/sensor/accel_trig
west flash
```

### Sample Output

```shell
fxos8700@1d [m/s^2]:    (   -0.153229,    -0.057461,     9.931148)
fxos8700@1d [m/s^2]:    (   -0.153229,    -0.057461,     9.931148)
fxos8700@1d [m/s^2]:    (   -0.143653,    -0.057461,     9.921571)
fxos8700@1d [m/s^2]:    (   -0.153229,    -0.067038,     9.931148)
fxos8700@1d [m/s^2]:    (   -0.143653,    -0.067038,     9.921571)
fxos8700@1d [m/s^2]:    (   -0.134076,    -0.047885,     9.931148)
fxos8700@1d [m/s^2]:    (   -0.105345,    -0.038308,     9.940725)
fxos8700@1d [m/s^2]:    (   -0.105345,    -0.019154,     9.931148)
fxos8700@1d [m/s^2]:    (   -0.105345,    -0.028731,     9.921571)
fxos8700@1d [m/s^2]:    (   -0.095769,    -0.028731,     9.931148)
fxos8700@1d [m/s^2]:    (   -0.095769,    -0.009577,     9.940725)
```
