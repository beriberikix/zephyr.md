---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/tcan4550evm/doc/index.html
original_path: boards/shields/tcan4550evm/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Texas Instruments TCAN4550EVM

## Overview

The Texas Instruments [TCAN4550EVM](https://www.ti.com/tool/TCAN4550EVM) features a [TI TCAN4550-Q1](https://www.ti.com/product/TCAN4550-Q1) automotive system basis chip (SBC)
with integrated CAN FD controller & transceiver.

![TCAN4550EVM](../../../../_images/tcan4550evm.jpg)

TCAN4550EVM (Credit: Texas Instruments)

## Requirements

This shield can only be used with a board which provides a configuration for Arduino connectors and
defines node aliases for SPI and GPIO interfaces (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

Note

This shield configuration limits the maximum SPI clock frequency to 2MHz although the
TCAN4550-Q1 supports up to 18MHz SPI clock frequency. This is done to accommodate the flywires
usually used for connecting the TCAN4550EVM to the board running Zephyr.

### Pin Assignments

| Shield Connector Pin | Function |
| --- | --- |
| D6 | nWKRQ |
| D7 | WAKE\_LV |
| D8 | RESET |
| D9 | nINT |
| D10 | nCS |
| D11 | SDI |
| D12 | SDO |
| D13 | SCLK |

## Programming

Set `-DSHIELD=tcan4550evm` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b frdm_k64f tests/drivers/can/api -- -DSHIELD=tcan4550evm
```
