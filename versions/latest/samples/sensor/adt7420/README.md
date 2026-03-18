---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/adt7420/README.html
original_path: samples/sensor/adt7420/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ADT7420: High accuracy digital I2C temperature sensor

## Description

This sample application periodically (1Hz) measures the ambient temperature
in degrees Celsius. The result is written to the console.

When configured in trigger mode the update interval is 5 s, and the
sample maintains a ±1° C window around a recent
temperature. As soon as the temperature goes outside the window an
interrupt causes the application to display an event and update the
upper and lower window boundaries.

## References

> - ADT7420: [http://www.analog.com/adt7420](http://www.analog.com/adt7420)

## Wiring

This sample uses the ADT7420 sensor controlled using the I2C interface.
Connect Supply: **VDD**, **GND** and Interface: **SDA**, **SCL**
and optionally connect the **INT** to a interrupt capable GPIO.
The supply voltage can be in the 2.7V to 5.5V range.
Depending on the baseboard used, the **SDA** and **SCL** lines require Pull-Up
resistors.

## Building and Running

This project outputs sensor data to the console. It requires an ADT7420
sensor. It should work with any platform featuring a I2C peripheral interface.
It does not work on QEMU.
In this example below the [nRF52 DK](../../../boards/arm/nrf52dk_nrf52832/doc/index.md#nrf52dk-nrf52832) board is used.

```shell
# From the root of the zephyr repository
west build -b nrf52dk_nrf52832 samples/sensor/adt7420
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v2.1.0-538-g12b2ed2cf7c3  ***
device is 0x2000101c, name is ADT7420
[0:00:00.011]: temperature 21.203125 Cel
[0:00:01.015]: temperature 21.171875 Cel
[0:00:02.019]: temperature 21.171875 Cel
[0:00:03.023]: temperature 21.187500 Cel
[0:00:04.027]: temperature 21.140625 Cel
```

<repeats endlessly>
