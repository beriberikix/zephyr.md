---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/dps310/README.html
original_path: samples/sensor/dps310/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DPS310 Temperature and Pressure Sensor

## Overview

This sample application periodically reads temperature and pressure data from
the first available device that implements SENSOR\_CHAN\_AMBIENT\_TEMP and
SENSOR\_CHAN\_PRESS. This sample checks the sensor in polling mode (without
interrupt trigger).

## Building and Running

This sample application uses an DPS310 sensor connected to a board via I2C.
Connect the sensor pins according to the connection diagram given in the
[dps310 datasheet](https://www.infineon.com/dgdl/Infineon-DPS310-DataSheet-v01_01-EN.pdf?fileId=5546d462576f34750157750826c42242) at page 18 figure 7.

Build and flash this sample (for example, for the nrf52840dk\_nrf52840 board)
using these commands:

```shell
west build -b nrf52840dk_nrf52840 samples/sensor/dps310
west flash
```

### Sample Output

To check output of this sample, any serial console program can be used.
This example uses `picocom` on the serial port `/dev/ttyUSB0`:

```shell
$ sudo picocom -D /dev/ttyUSB0
```

```shell
temp: 23.774363; press: 97.354728
temp: 23.777492; press: 97.353904
temp: 23.784646; press: 97.354064
```
