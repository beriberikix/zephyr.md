---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/lis2dh/README.html
original_path: samples/sensor/lis2dh/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LIS2DH: Motion Sensor Monitor

## Overview

This sample application periodically reads accelerometer data from the
LIS2DH sensor (or the compatible LS2DH12, LIS3DH, and LSM303DLHC
sensors), and displays the sensor data on the console.

## Requirements

This sample uses the LIS2DH, ST MEMS system-in-package featuring a 3D
digital output motion sensor.

## References

For more information about the LIS2DH motion sensor see
[https://www.st.com/en/mems-and-sensors/lis2dh.html](https://www.st.com/en/mems-and-sensors/lis2dh.html).

## Building and Running

The LIS2DH2 or compatible sensors are available on a variety of boards
and shields supported by Zephyr, including:

- [Actinius Icarus](../../../boards/actinius/icarus/doc/index.md#actinius-icarus)
- [Thingy:52](../../../boards/nordic/thingy52/doc/index.md#thingy52-nrf52832)
- [ST STM32F3 Discovery](../../../boards/st/stm32f3_disco/doc/index.md#stm32f3-disco-board)
- [X-NUCLEO-IKS01A2: MEMS Inertial and Environmental Multi sensor shield](../../../boards/shields/x_nucleo_iks01a2/doc/index.md#x-nucleo-iks01a2)

See the board documentation for detailed instructions on how to flash
and get access to the console where acceleration data is displayed.

### Building on actinius\_icarus

[Actinius Icarus](../../../boards/actinius/icarus/doc/index.md#actinius-icarus) includes an ST LIS2DH12 accelerometer which
supports the LIS2DH interface.

```shell
west build -b actinius_icarus samples/sensor/lis2dh
west flash
```

### Building on nucleo\_l476rg with IKS01A2 shield

The [X-NUCLEO-IKS01A2: MEMS Inertial and Environmental Multi sensor shield](../../../boards/shields/x_nucleo_iks01a2/doc/index.md#x-nucleo-iks01a2) includes an LSM303AGR accelerometer which
supports the LIS2DH interface. This shield may also be used on other
boards with Arduino headers.

```shell
west build -b nucleo_l476rg --shield x_nucleo_iks01a2 samples/sensor/lis2dh
west flash
```

### Sample Output

```shell
 Polling at 0.5 Hz
 #1 @ 12 ms: x -5.387328 , y 5.578368 , z -5.463744
 #2 @ 2017 ms: x -5.310912 , y 5.654784 , z -5.501952
 #3 @ 4022 ms: x -5.349120 , y 5.692992 , z -5.463744

<repeats endlessly every 2 seconds>
```
