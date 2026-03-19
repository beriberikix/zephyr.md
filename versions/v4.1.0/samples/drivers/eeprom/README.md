---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/eeprom/README.html
original_path: samples/drivers/eeprom/README.html
---

# EEPROM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/eeprom/README.rst/..)

## Overview

This sample demonstrates the [EEPROM driver API](../../../hardware/peripherals/eeprom/api.md#eeprom-api) in a simple boot counter
application.

## Building and Running

In case the target board has defined an EEPROM with alias `eeprom-0` the
sample can be built without further ado. This applies for example to the
[Native simulator - native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) board:

```shell
west build -b native_sim samples/drivers/eeprom
west build -t run
```

Otherwise either a board specific overlay needs to be defined, or a shield must
be activated. Any board with Arduino headers can for example build the sample
as follows:

```shell
west build -b nrf52840dk/nrf52840 --shield x_nucleo_eeprma2 samples/drivers/eeprom
```

For [GD32F450I-EVAL](../../../boards/gd/gd32f450i_eval/doc/index.md#gd32f450i_eval) board. First bridge the JP5 to USART with the jumper cap,
Then the sample can be built and executed for the as follows:

```shell
west build -b gd32f450i_eval samples/drivers/eeprom
west flash
```

### Sample Output

```shell
Found EEPROM device "EEPROM_M24C02"
Using eeprom with size of: 256.
Device booted 7 times.
Reset the MCU to see the increasing boot counter.
```

## See also

[EEPROM Interface](../../../doxygen/html/group__eeprom__interface.md)
