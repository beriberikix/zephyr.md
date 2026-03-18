---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/grow_r502a/README.html
original_path: samples/sensor/grow_r502a/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# GROW\_R502A Fingerprint Sensor

## Overview

This sample has the below functionalities:

1. Shows the number of fingerprints stored in the sensor.
2. When SENSOR\_ATTR\_RECORD\_FREE\_IDX is set then it search for free index in sensor library.
3. When SENSOR\_ATTR\_RECORD\_ADD is set then it adds a new fingerprint to the sensor.
4. When SENSOR\_ATTR\_RECORD\_FIND is set then it tries to find a match for the input fingerprint. On finding a match it returns ID and confidence.
5. When SENSOR\_ATTR\_RECORD\_DEL is set then it deletes a fingerprint from the sensor.

Note: Fingerprint add & delete functionalities work only when SENSOR\_TRIG\_TOUCH is set.
Tricolored LED in the sensor hardware will, flash on the below conditions:

1. On successful addition or deletion of fingerprint it will flash in blue three times.
2. On finding a match for the input fingerprint it will flash in purple.
3. In all other cases it will flash in red.

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
west build -b nrf52840dk_nrf52840 samples/sensor/grow_r502a
west flash
```

## Sample Output

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-2640-g328bb73113d4  ***
template count : 0
Fingerprint Deleted at ID #3
Fingerprint template free idx at ID #0
Waiting for valid finger to enroll as ID #0
Place your finger
Fingerprint successfully stored at #0
template count : 1
Matched ID : 0
confidence : 170
template count : 1
Matched ID : 0
confidence : 136
template count : 1
Matched ID : 0
confidence : 318
<repeats endlessly>
```
