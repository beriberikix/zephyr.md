---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/x_nucleo_iks01a1/doc/index.html
original_path: boards/shields/x_nucleo_iks01a1/doc/index.html
---

# X-NUCLEO-IKS01A1: MEMS Inertial and Environmental Multi sensor shield

## Overview

The X-NUCLEO-IKS01A1 is a motion MEMS and environmental sensor
evaluation board system, compatible with the Arduino UNO R3 connector
layout. It includes an STMicroelectronics’ LSM6DS0 3-axis accelerometer
and 3-axis gyroscope, the LIS3MDL 3-axis magnetometer, the HTS221
humidity and temperature sensor, and the LPS25HB pressure sensor.

The X-NUCLEO-IKS01A1 interfaces with the main board via an I2C interface.

![X-NUCLEO-IKS01A](../../../../_images/x-nucleo-iks01a1.jpg)

More information about the board can be found at the
[X-NUCLEO-IKS01A1 website](https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html) [[1]](#id1).

## Hardware

X-NUCLEO-IKS01A1 provides the following key features:

> - LSM6DS0: MEMS 3D accelerometer (±2/±4/±8 g) + 3D gyroscope (±245/±500/±2000
>   dps)
> - LIS3MDL: MEMS 3D magnetometer (±4/ ±8/ ±12/ 16 gauss)
> - LPS25HB: MEMS pressure sensor, 260-1260 hPa absolute digital output barometer
> - HTS221: capacitive digital relative humidity and temperature
> - DIL 24-pin socket available for additional MEMS adapters and other sensors
>   (UV index)
> - Equipped with Arduino UNO R3 connector
> - RoHS compliant

More information about X-NUCLEO-IKS01A1 can be found here:
:   - [X-NUCLEO-IKS01A1 data sheet](https://www.st.com/resource/en/datasheet/x-nucleo-iks01a1.pdf) [[2]](#id3)

## Programming

An example on how to use the `x-nucleo-iks01a1` shield is available
in the [X-NUCLEO-IKS01A1 shield](../../../../samples/shields/x_nucleo_iks01a1/README.md#x-nucleo-iks01a1 "Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.") sample application documentation
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## References

[[1](#id2)]

[https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html)

[[2](#id4)]

[https://www.st.com/resource/en/datasheet/x-nucleo-iks01a1.pdf](https://www.st.com/resource/en/datasheet/x-nucleo-iks01a1.pdf)
