---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/mikroe_lte_iot10_click/doc/index.html
original_path: boards/shields/mikroe_lte_iot10_click/doc/index.html
---

# MikroElektronika LTE IoT 10 Click

## Overview

The MikroElektronika LTE IoT 10 Click is a compact add-on board that provides reliable LTE-M and
NB-IoT connectivity for industrial and commercial IoT applications.

This board features the Monarch 2 GM02S, a dual-mode LTE-M/NB-IoT module from Sequans (based on
Sequans SQN3430 Chipset), offering global band support from 617MHz to 2.2GHz.

![MikroElektronika LTE IoT 10 Click](https://docs.zephyrproject.org/4.2.0/_images/mikroe_lte_iot10_click.webp)

MikroElektronika LTE IoT 10 Click (Credit: MikroElektronika)

## Requirements

This shield can only be used with a development board that provides a configuration for mikroBUS
connectors and defines a `mikrobus_serial` node alias for the mikroBUS UART interface
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

For more information about the GM02S module and the LTE IoT 10 Click, you may refer to the following
documentation:

- [GM02S Datasheet](https://www.sequans.com/products-solutions/gm02s/) [[1]](#id2)
- [LTE IoT 10 Click](https://www.mikroe.com/lte-iot-10-click) [[2]](#id4)

## Programming

Set `--shield mikroe_lte_iot10_click` when you invoke `west build`. Here is an example with the
[Cellular modem](../../../../samples/net/cellular_modem/README.md#cellular-modem "Use a cellular modem to communicate with a UDP server.") code sample:

```shell
# From the root of the zephyr repository
west build -b ek_ra6m4 --shield mikroe_lte_iot10_click samples/net/cellular_modem
```

## References

[[1](#id3)]

[https://www.sequans.com/products-solutions/gm02s/](https://www.sequans.com/products-solutions/gm02s/)

[[2](#id5)]

[https://www.mikroe.com/lte-iot-10-click](https://www.mikroe.com/lte-iot-10-click)
