---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/ipm/ipm_imx/README.html
original_path: samples/drivers/ipm/ipm_imx/README.html
---

# IPM on NXP i.MX

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ipm/ipm_imx/README.rst/..)

## Overview

This simple example can be used with multicore i.MX SoCs containing a
Messaging Unit peripheral. It reads the received data from the Messaging Unit
using the IPM and transmits it back unchanged. The information about
the received data is printed to the console. When sending the data back,
it blocks until the data are read by the remote side.

The i.MX Messaging Unit peripheral consists of four 32-bit transmit and receive
registers. The sample uses the option [`CONFIG_IPM_IMX_MAX_DATA_SIZE_4`](../../../../kconfig.md#CONFIG_IPM_IMX_MAX_DATA_SIZE_4 "CONFIG_IPM_IMX_MAX_DATA_SIZE_4"),
which effectively creates four IPM channels. Selecting the option
[`CONFIG_IPM_IMX_MAX_DATA_SIZE_8`](../../../../kconfig.md#CONFIG_IPM_IMX_MAX_DATA_SIZE_8 "CONFIG_IPM_IMX_MAX_DATA_SIZE_8") or
[`CONFIG_IPM_IMX_MAX_DATA_SIZE_16`](../../../../kconfig.md#CONFIG_IPM_IMX_MAX_DATA_SIZE_16 "CONFIG_IPM_IMX_MAX_DATA_SIZE_16") would result in two 64-bit channels
or a single 128-bit channel respectively.

Note that this is just a simple demo to demonstrate the i.MX IPM functionality
and blocking sending of the data back is done in the interrupt handler, which
would not be appropriate for a real world application.

## Building and Running the Zephyr Code

The sample requires that data are being sent by the remote core so it can echo
it back. The other core is usually not running Zephyr but Linux on i.MX
multicore processors.

This project outputs data to the console.
It can be built as follows:

```shell
west build -b udoo_neo_full/mcimx6x/m4 samples/drivers/ipm/ipm_imx
west flash
```

Follow the instructions in the [Neo Full](../../../../boards/udoo/udoo_neo_full/doc/index.md#udoo_neo_full) board documentation
for how to load the Zephyr binary to the desired core and execute it.

## Building and Running the Linux Code

The remote code is in the form of a loadable Linux kernel module. It creates
four character devices /dev/mu0 till /dev/mu3, which are used to read data from
and write data into the Messaging Unit.

The remote code and the instructions how to build and run it are located at:

[https://source.codeaurora.org/external/imxsupport/imx-mu/](https://source.codeaurora.org/external/imxsupport/imx-mu/)

### Sample Output

Typing this in the Linux console:

```shell
# cat > /dev/mu0
abcdefgh
^D
```

Results in the following output on the Zephyr side:

```shell
***** Booting Zephyr OS v1.12.0-291-g8cc508b *****
IPM initialized, data size = 4
ipm_callback: id = 0, data = 0x03323130
ipm_callback: id = 0, data = 0x03353433
ipm_callback: id = 0, data = 0x03383736
ipm_callback: id = 0, data = 0x02000a39
```

## See also

[IPM Interface](../../../../doxygen/html/group__ipm__interface.md)
