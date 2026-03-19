---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/sgp40_sht4x/README.html
original_path: samples/sensor/sgp40_sht4x/README.html
---

# SGP40 and SHT4X digital humidity and multipixel gas sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/sgp40_sht4x/README.rst/..)

## Description

This sample application periodically measures the ambient temperature, humidity
and a raw gas sensor value from an SGP40 and SHT4X device.
The result is written to the console.

You can choose to use the on-chip T/RH compensation of the SGP40
by feeding the values measured by the SHT4X into it.
This is enabled in the Application by default, you can turn it off
by setting `APP_USE_COMPENSATION=n`.

The SHT4X has the option to use a heater which makes sense for specific
environments/applications (refer to the datasheet for more information).
To make use of the heater have a look at the Kconfig options for this application.

## References

> - [SHT4X sensor](https://www.sensirion.com/en/environmental-sensors/humidity-sensors/humidity-sensor-sht4x/)
> - [SGP40 sensor](https://www.sensirion.com/en/environmental-sensors/gas-sensors/sgp40/)

## Wiring

This sample uses the SHT4X and SGP40 sensor controlled using the I2C interface.
Connect Supply: **VDD**, **GND** and Interface: **SDA**, **SCL**.
The supply voltage can be in the 1.7V to 3.6V range.
Depending on the baseboard used, the **SDA** and **SCL** lines require Pull-Up
resistors.

## Building and Running

This project outputs sensor data to the console. It requires a SHT4X and a SGP40
sensor. It should work with any platform featuring a I2C peripheral
interface. This example has an example device tree overlay
for the [Black Pill V2.0](../../../boards/weact/blackpill_f411ce/doc/index.md#blackpill_f411ce) board.

```shell
# From the root of the zephyr repository
west build -b blackpill_f411ce samples/sensor/sgp40_sht4x
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build v2.6.0-rc1-315-g50d8d1187138  ***
SHT4X: 23.64 Temp. [C] ; 30.74 RH [%] -- SGP40: 30531 Gas [a.u.]
[00:00:00.250,000] <dbg> SGP40.sgp40_init: SGP40: Selftest succeeded!
SHT4X: 23.66 Temp. [C] ; 32.16 RH [%] -- SGP40: 30541 Gas [a.u.]
SHT4X: 23.63 Temp. [C] ; 30.83 RH [%] -- SGP40: 30522 Gas [a.u.]
```

The datasheet states that the raw sensor signal for the SGP40 ist proportional
to the logarithm of the sensors resistance, hence it is labeled as [a.u.]
(arbitrary units) in the example.

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
