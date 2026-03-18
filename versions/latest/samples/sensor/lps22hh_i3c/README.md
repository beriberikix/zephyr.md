---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/lps22hh_i3c/README.html
original_path: samples/sensor/lps22hh_i3c/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LPS22HH: Temperature and Pressure Monitor (I3C)

## Overview

This sample periodically reads pressure from the LPS22HH MEMS pressure
sensor and displays it on the console.

## Requirements

This sample uses the LPS22HH sensor controlled using the I3C interface.
It has been tested using the LPS22HH on the evaluation board
STEVALMKI192-V1 connected to the I3C header on [NXP MIMXRT685-EVK](../../../boards/arm/mimxrt685_evk/doc/index.md#mimxrt685-evk).

## References

- LPS22HH: [https://www.st.com/en/mems-and-sensors/lps22hh.html](https://www.st.com/en/mems-and-sensors/lps22hh.html)

## Building and Running

This project outputs sensor data to the console. It requires an LPS22HH
sensor (for example, the one on evaluation board STEVALMKI192-V1).

Note

If `CONFIG_LPS22HH_TRIGGER` is enabled, the trigger is using
I3C In-Band Interrupt (IBI) to signal new data being available.
Since IBI is initiated by the sensor, it will take over the I3C
bus. Therefore, when flashing a new image, a power cycle is needed
to reset the sensor so that it will not generate IBIs anymore.
Or else the I3C controller will not be able to be initialized,
resulting in the sample not being able to communicate with
the sensor.

### Building on mimxrt685\_evk\_cm33 board

```shell
west build -b mimxrt685_evk_cm33 samples/sensor/lps22hh_i3c
```

### Board Preparations

#### mimxrt685\_evk\_cm33

On the board [NXP MIMXRT685-EVK](../../../boards/arm/mimxrt685_evk/doc/index.md#mimxrt685-evk), the I3C pins are exposed on the J18
header, where:

> - SCL is on pin 1
> - SDA is on pin 2
> - Internal pull-up is on pin 3 (which is connected to pin 2 already)
> - Ground is on pin4

##### LPS22HH

A LPS22HH sensor needs to be connected to this header. For example,
the evaluation board STEVAL-MKI192V1 can be used. This needs to be
prepared so that the LPS22HH sensor has address 0x5D (i.e. 0xBA,
left-shifed).

### Sample Output

```shell
Configured for triggered collection at 1 Hz
Observation: 1
Pressure: 97.474 kPa
Temperature: 22.19 C
Observation: 2
Pressure: 97.466 kPa
Temperature: 22.21 C
Observation: 3
Pressure: 97.473 kPa
Temperature: 22.21 C
Observation: 4
Pressure: 97.455 kPa
Temperature: 22.21 C

<repeats endlessly every second>
```
