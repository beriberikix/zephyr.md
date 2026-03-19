---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/mspi/mspi_async/README.html
original_path: samples/drivers/mspi/mspi_async/README.html
---

# MSPI asynchronous transfer

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/mspi/mspi_async/README.rst/..)

## Overview

This sample demonstrates using the [MSPI API](../../../../hardware/peripherals/mspi.md#mspi-api) on a MSPI
memory device. The asynchronous transceive call need to be supported
either by a software queue or hardware queue from the controller hardware.
To this sample, however, the implementation should make no difference.

## Building and Running

The application will build only for a target that has a [devicetree](../../../../build/dts/index.md#dt-guide)
`dev0` alias that refers to an entry with the following bindings as a compatible:

- [`ambiq,mspi-device`](../../../../build/dts/api/bindings/mspi/ambiq%2Cmspi-device.md#std-dtcompatible-ambiq-mspi-device), [`mspi-aps6404l`](../../../../build/dts/api/bindings/mtd/mspi-aps6404l.md#std-dtcompatible-mspi-aps6404l)

```shell
west build -b apollo3p_evb samples/drivers/mspi/mspi_async
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v3.5.0-8581-gc80b243c7598 ***
w:3,r:3
Read data matches written data
```

## See also

[MSPI Driver APIs](../../../../doxygen/html/group__mspi__interface.md)
