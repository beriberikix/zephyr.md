---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/sparkfun_carrier_asset_tracker/doc/index.html
original_path: boards/shields/sparkfun_carrier_asset_tracker/doc/index.html
---

# Sparkfun SparkFun MicroMod Asset Tracker Shield

## Overview

The SparkFun MicroMod Asset Tracker Carrier Shield is part of the Sparkfun
Micromod standard, a modular interface ecosystem that uses the M.2 standard
to mix and match your choice of processor with specific Functions Boards.

The Asset Tracker Carrier Shield is built around the u-blox SARA-R510M8S
module, which offers Secure Cloud LTE-M and NB-IoT data communication for
multi-regional use and GNSS capabilities via an integrated u-blox M8 GNSS
receiver for accurate positioning information.

Besides, this shield has an integrated ICM-20948 Inertial Measurement Unit
(IMU) for Nine Degree-Of-Freedom, a built-in micro-SD card socket for data
logging as well as a nano SIM card port.

![Sparkfun SparkFun MicroMod Asset Tracker Shield](../../../../_images/sparkfun_carrier_asset_tracker.webp)

Sparkfun SparkFun MicroMod Asset Tracker Shield (Credit: Sparkfun)

More information about the shield can be found at the [SparkFun MicroMod
Asset Tracker guide website](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide) [[1]](#id2).

### Pins Assignment of Sparkfun SparkFun MicroMod Asset Tracker Shield

The SparkFun MicroMod Asset Tracker Carrier Shield uses a 76 pins M.2
connector. The following table depicts the interfaces and pins supported:
by Zephyr:
+———————–+———————————+
| Shield Connector Pin | Function |
+=======================+=================================+
| micromod\_1\_uart alias | UART 1 (with CTS and RTS pins) |
+———————–+———————————+
| micromod\_2\_uart alias | UART 2 |
+———————–+———————————+
| micromod\_0\_i2c alias | i2c 0 |
+———————–+———————————+
| micromod\_1\_i2c alias | i2c 1 |
+———————–+———————————+
| micromod\_0\_spi alias | SPI 0 |
+———————–+———————————+
| A0 | Analog pin |
+———————–+———————————+
| A1 | Analog pin |
+———————–+———————————+
| D0 | Digital pin |
+———————–+———————————+
| D1/CAM\_TRIG | Digital pin |
+———————–+———————————+
| I2C\_INT# | i2c interrupt pin |
+———————–+———————————+
| G0/BUS0 | General purpose pin |
+———————–+———————————+
| G1/BUS1 | General purpose pin |
+———————–+———————————+
| G2/BUS2 | General purpose pin |
+———————–+———————————+
| G3/BUS3 | General purpose pin |
+———————–+———————————+
| G4/BUS4 | General purpose pin |
+———————–+———————————+
| G5/BUS5 | General purpose pin |
+———————–+———————————+
| G6/BUS6 | General purpose pin |
+———————–+———————————+
| G7/BUS7 | General purpose pin |
+———————–+———————————+
| G8 | General purpose pin |
+———————–+———————————+
| G9/ADC\_D-/CAM\_HSYNC | General purpose pin |
+———————–+———————————+
| G10/ADC\_D+/CAM\_VSYNC | General purpose pin |
+———————–+———————————+
| G11/SWO | General purpose pin |
+———————–+———————————+
| SPI\_CS | General purpose pin |
+———————–+———————————+

A detailed definition of the Micromod standard can be found on the
[Micromod specification website](https://www.sparkfun.com/micromod) [[2]](#id4)

## Requirements

This shield can only be used with a board which provides a configuration for
Micromod connectors and defines node aliases for UART, I2C and SPI interfaces (see
[Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `--shield sparkfun_carrier_asset_tracker` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b micromod/nrf52840 --shield sparkfun_carrier_asset_tracker samples/net/cellular_modem/
```

## References

[[1](#id3)]

[https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide](https://learn.sparkfun.com/tutorials/micromod-asset-tracker-carrier-board-hookup-guide)

[[2](#id5)]

[https://www.sparkfun.com/micromod](https://www.sparkfun.com/micromod)
