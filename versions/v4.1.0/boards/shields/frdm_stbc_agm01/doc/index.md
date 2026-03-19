---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/frdm_stbc_agm01/doc/index.html
original_path: boards/shields/frdm_stbc_agm01/doc/index.html
---

# NXP FRDM-STBC-AGM01

## Overview

The FRDM-STBC-AGM01 is an NXP Freedom development board with
FXOS8700 and FXAS21002. This 9-axis solution (FXAS21002C Gyroscope,
+ FXOS8700CQ E-compass sensor) is compatible with any board that
provides an Arduino R3 header.

![FRDM-STBC-AGM01](../../../../_images/AGM01.jpg)

### Pin Assignment of the FRDM-STBC-AGM01 Shield

| Shield Connector Pin | Function |
| --- | --- |
| A5 | I2C - SCL1 |
| A4 | I2C - SDA1 |
| D15 | I2C - SCL0 |
| D14 | I2C - SDA0 |
| D2 | INT1 - 8700 |
| D4 | INT2 - 8700 |
| D5 | INT1 - 21002 |
| D8 | INT2 - 21002 |
| A3 | RST - GPIO |

For more information about the FXOS8700, FXAS21002, and FRDM-STBC-AGM01
board:

- [FXAS21002 Gyroscope Sensor](../../../../samples/sensor/fxas21002/README.md#fxas21002 "Get gyroscope data synchronously from an FXAS21002 sensor.")
- [FXOS8700 Website](https://www.nxp.com/products/sensors/accelerometers/digital-motion-sensor-3d-accelerometer-2g-4g-8g-plus-3d-magnetometer:FXOS8700CQ)
- [FRDM-STBC-AGM01 Website](https://www.nxp.com/design/development-boards/freedom-development-boards/sensors/sensor-toolbox-development-boards-for-a-9-axis-solution-using-fxas21002c-and-fxos8700cq:FRDM-STBC-AGM01)
- [FRDM-STBC-AGM01 Quick Reference Card](https://www.nxp.com/docs/en/supporting-information/FRDM-STBC-AGM01-QRC.pdf)
- [FRDM-STBC-AGM01 Schematics](https://www.nxp.com/downloads/en/schematics/FRDM-STBC-AGM01-SCH.pdf)

## Programming

Set `--shield frdm_stbc_agm01` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b frdm_k22f --shield frdm_stbc_agm01 samples/sensor/fxas21002
```
