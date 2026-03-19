---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/grow_r502a/README.html
original_path: samples/sensor/grow_r502a/README.html
---

# GROW R502-A Fingerprint Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/grow_r502a/README.rst/..)

## Overview

This sample has the below functionalities:

1. Sensor LED is controlled using led APIs from zephyr subsystem.
2. Shows the number of fingerprints stored in the sensor.
3. Shows the sensor device’s configurations like baud rate, library size, address and data packet size in UART frame.
4. When SENSOR\_ATTR\_RECORD\_FREE\_IDX is set then it search for free index in sensor library.
5. When SENSOR\_ATTR\_RECORD\_ADD is set then it adds a new fingerprint to the sensor.
6. When SENSOR\_ATTR\_RECORD\_FIND is set then it tries to find a match for the input fingerprint. On finding a match it returns ID and confidence.
7. When SENSOR\_ATTR\_RECORD\_DEL is set then it deletes a fingerprint from the sensor.

Note: Fingerprint add functionality work only when SENSOR\_TRIG\_TOUCH is set.

## Wiring

This sample uses an external breakout for the sensor. A devicetree
overlay must be provided to identify the UART bus and the GPIO
used to control the sensor. Sensor can be powered using mentioned optional GPIO.

## References

For more information about the GROW\_R502A Fingerprint Sensor see
[http://en.hzgrow.com/product/143.html](http://en.hzgrow.com/product/143.html)

## Building and Running

After providing a devicetree overlay that specifies the sensor location,
build this sample app using:

```shell
# From the root of the zephyr repository
west build -b esp32_devkitc_wroom/esp32/procpu samples/sensor/grow_r502a
west flash
```

## Sample Output

```shell
*** Booting Zephyr OS build v3.6.0-3147-g8ae1a2e2718e ***
template count : 4
baud 57600
addr 0xffffffff
lib_size 200
data_pkt_size 128
Fingerprint Deleted at ID #3
Fingerprint template free idx at ID #3
Waiting for valid finger to enroll as ID #3
Place your finger
Fingerprint successfully stored at #3
template count : 4
Matched ID : 2
confidence : 110
<repeats endlessly>
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
