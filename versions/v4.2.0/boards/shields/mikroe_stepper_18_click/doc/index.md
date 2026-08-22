---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/mikroe_stepper_18_click/doc/index.html
original_path: boards/shields/mikroe_stepper_18_click/doc/index.html
---

# MikroElektronika Stepper 18 Click

## Overview

Stepper 18 Click shield has a TI DRV426 stepper driver accessed via GPIO.
It also features a Microchip MCP4726 DAC to allow for current control. The
micro-step pins are controlled via physical switches, making them unavailable
in Zephyr.
The DRV8426 uses the work-queue timing source by default.

Note that the MCP4726 is compatible with the MCP4725 driver.

More information about the shield can be found at
[Mikroe Stepper 18 click](https://www.mikroe.com/stepper-18-click) [[1]](#id2).

![MikroElektronika Stepper 18 Click](../../../../_images/stepper_18_click.webp)

MikroElektronika Stepper 18 Click (Credit: MikroElektronika)

## Requirements

The shield uses a mikroBUS interface. The target board must define
a `mikrobus_i2c` and `mikrobus_header` node labels
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

```shell
# From the root of the zephyr repository
west build -b <board> --shield mikroe_stepper_18_click samples/drivers/stepper/generic/
west flash
```

## References

[[1](#id3)]

[https://www.mikroe.com/stepper-18-click](https://www.mikroe.com/stepper-18-click)
