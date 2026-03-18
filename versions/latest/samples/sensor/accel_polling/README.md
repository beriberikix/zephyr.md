---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/accel_polling/README.html
original_path: samples/sensor/accel_polling/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic 3-Axis accelerometer polling sample

## Overview

This sample application demonstrates how to use 3-Axis accelerometers.

## Building and Running

This sample supports up to 10 3-Axis accelerometers. Each accelerometer needs
to be aliased as `accelN` where `N` goes from `0` to `9`. For example:

```devicetree
/ {
      aliases {
                      accel0 = &lis2dh;
              };
      };
```

Make sure the aliases are in devicetree, then build and run with:

```shell
west build -b <board to use> samples/sensor/accel_polling
west flash
```

### Sample Output

```shell
lis2dh@19 [m/s^2]:    (  -6.013728,   -3.064320,    7.277760)
lis2dh@19 [m/s^2]:    (  -6.128640,   -3.026016,    7.201152)
lis2dh@19 [m/s^2]:    (  -6.090336,   -3.064320,    7.162848)
lis2dh@19 [m/s^2]:    (  -6.128640,   -3.026016,    7.354368)
lis2dh@19 [m/s^2]:    (  -6.166944,   -3.102624,    7.277760)
lis2dh@19 [m/s^2]:    (  -6.128640,   -2.987712,    7.277760)
lis2dh@19 [m/s^2]:    (  -6.052032,   -2.987712,    7.277760)
lis2dh@19 [m/s^2]:    (  -6.166944,   -2.987712,    7.239456)
lis2dh@19 [m/s^2]:    (  -6.090336,   -3.026016,    7.201152)
```
