---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/sht3xd/README.html
original_path: samples/sensor/sht3xd/README.html
---

# SHT3XD humidity sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/sht3xd/README.rst/..)

## Description

This sample application periodically (2 Hz) measures the ambient
temperature and humidity. The result is written to the console.
Optionally, it also shows how to use the upper threshold triggers.

## References

> - [SHT3X-DIS sensor](https://www.sensirion.com/en/environmental-sensors/humidity-sensors/digital-humidity-sensors-for-various-applications/)

## Wiring

This sample uses the SHT3X\_DIS sensor controlled using the I2C interface.
Connect Supply: **VDD**, **GND** and Interface: **SDA**, **SCL**
and optionally connect the **ALERT** to a interrupt capable GPIO.
The supply voltage can be in the 2.15V to 5.5V range.
Depending on the baseboard used, the **SDA** and **SCL** lines require Pull-Up
resistors.

## Building and Running

This project outputs sensor data to the console. It requires a SHT3XD
sensor. It should work with any platform featuring a I2C peripheral
interface. It does not work on QEMU. In this example below the
[BLE400](../../../boards/waveshare/nrf51_ble400/doc/index.md#nrf51_ble400) board is used.

```shell
# From the root of the zephyr repository
west build -b nrf51_ble400 samples/sensor/sht3xd
west flash
```

### Sample Output

```shell
SHT3XD: 19.64 Cel ; 41.96 %RH
SHT3XD: 19.74 Cel ; 42.06 %RH
SHT3XD: 19.75 Cel ; 42.08 %RH
```

<repeats endlessly>

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
