---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/vl53l0x/README.html
original_path: samples/sensor/vl53l0x/README.html
---

# VL53L0X Time Of Flight sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/vl53l0x/README.rst/..)

## Overview

This sample periodically measures distance between vl53l0x sensor
and target. The result is displayed on the console.
It shows the usage of all available channels including private ones.

## Requirements

This sample uses the VL53L0X sensor controlled using the I2C interface.

## References

> - VL53L0X: [https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html](https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html)

## Building and Running

This project outputs sensor data to the console. It requires a VL53L0X
sensor, which is present on the disco\_l475\_iot1 board.

```shell
# From the root of the zephyr repository
west build -b None samples/sensor/vl53l0x/
west flash
```

### Sample Output

```shell
prox is 0
distance is 1874 mm
Max distance is 000 mm
Signal rate is 33435 Cps
Ambient rate is 17365 Cps
SPADs used: 195
Status: OK

prox is 0
distance is 1888 mm
Max distance is 000 mm
Signal rate is 20846 Cps
Ambient rate is 25178 Cps
SPADs used: 195
Status: OK

<repeats endlessly every 5 seconds>
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
