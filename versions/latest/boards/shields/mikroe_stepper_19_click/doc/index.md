---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/mikroe_stepper_19_click/doc/index.html
original_path: boards/shields/mikroe_stepper_19_click/doc/index.html
---

# MikroElektronika Stepper 19 Click

## Overview

The MikroElektronika [Stepper 19 Click](https://www.mikroe.com/stepper-19-click) [[1]](#id2) shield has a [TI DRV8424](https://www.ti.com/product/DRV8424) [[2]](#id4) stepper driver accessed via
GPIO and a [NXP PCA9538A](https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A) [[3]](#id6) GPIO expander accessed via I2C. Some DRV8424 pins are accessed
via the GPIO expander.

![MikroElektronika Stepper 19 Click](../../../../_images/stepper_19_click.webp)

MikroElektronika Stepper 19 Click (Credit: MikroElektronika)

## Requirements

The shield uses a mikroBUS interface. The target board must define
a `mikrobus_i2c` and `mikrobus_header` node labels
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

```shell
# From the root of the zephyr repository
west build -b <board> --shield mikroe_stepper_19_click samples/drivers/stepper/generic/
west flash
```

## References

[[1](#id3)]

[https://www.mikroe.com/stepper-19-click](https://www.mikroe.com/stepper-19-click)

[[2](#id5)]

[https://www.ti.com/product/DRV8424](https://www.ti.com/product/DRV8424)

[[3](#id7)]

[https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A](https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A)
