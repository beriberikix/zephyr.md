---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/spi_bitbang/README.html
original_path: samples/drivers/spi_bitbang/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SPI bitbang

## Overview

This sample demonstrates using the bitbang SPI driver. The bitbang driver can
be useful for devices which use a non multiple of 8 word size, for example some
LCDs which have an extra cmd/data bit.

This sample loops through some different spi transfer configurations.

## Building and Running

The application will build only for a target that has a [devicetree](../../../build/dts/index.md#dt-guide) entry with [`zephyr,spi-bitbang`](../../../build/dts/api/bindings/spi/zephyr%2Cspi-bitbang.md#std-dtcompatible-zephyr-spi-bitbang) as a compatible.

You can connect the MISO and MOSI pins with a wire to provide a basic loopback
test for receive data.

```shell
west build -b nrf52840dk_nrf52840 samples/drivers/spi_bitbang
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v2.6.0-2939-g1882b95b42e2  ***
basic_write_9bit_words; ret: 0
  wrote 0101 00ff 00a5 0000 0102
9bit_loopback_partial; ret: 0
 tx (i)  : 0101 0102
 tx (ii) : 0003 0004 0105
 rx (ii) : 0003 0004 0105
basic_write_9bit_words; ret: 0
 wrote 0101 00ff 00a5 0000 0102
9bit_loopback_partial; ret: 0
 tx (i)  : 0101 0102
 tx (ii) : 0003 0004 0105
 rx (ii) : 0003 0004 0105
basic_write_9bit_words; ret: 0
 wrote 0101 00ff 00a5 0000 0102
9bit_loopback_partial; ret: 0
 tx (i)  : 0101 0102
 tx (ii) : 0003 0004 0105
 rx (ii) : 0003 0004 0105
```
