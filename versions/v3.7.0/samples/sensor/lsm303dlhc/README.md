---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/lsm303dlhc/README.html
original_path: samples/sensor/lsm303dlhc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LSM303DLHC: Magnetometer and Accelerometer data Monitor

## Overview

This sample application periodically reads magnetometer and accelerometer data
from the LSM303DLHC eCompass module’s sensors, and displays the sensor data
on the console.

## Requirements

This sample uses the LSM303DLHC, ST MEMS system-in-package featuring a
3D digital linear acceleration sensor and a 3D digital magnetic sensor,
controlled using the I2C interface.

## References

For more information about the LSM303DLHC eCompass module, see
[https://www.st.com/en/mems-and-sensors/lsm303dlhc.html](https://www.st.com/en/mems-and-sensors/lsm303dlhc.html)

## Building and Running

This project outputs sensor data to the console. It requires a LSM303DLHC
system-in-package, which is present on the stm32f3\_disco board

```shell
west build -b stm32f3_disco samples/sensor/lsm303dlhc
```

### Sample Output

```shell
Magnetometer data:
( x y z ) = ( 0.531818  -0.435454  -0.089090 )
Accelerometer data:
( x y z ) = ( -0.078127  -0.347666  1.105502 )
Magnetometer data:
( x y z ) = ( -0.003636  0.297272  -0.255454 )
Accelerometer data:
( x y z ) = ( 0.074221  -0.304696  0.972685 )

<repeats endlessly every 2 seconds>
```
