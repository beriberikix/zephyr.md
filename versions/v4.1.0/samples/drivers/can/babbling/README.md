---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/can/babbling/README.html
original_path: samples/drivers/can/babbling/README.html
---

# Controller Area Network (CAN) babbling node

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/can/babbling/README.rst/..)

## Overview

In a Controller Area Network a babbling node is a node continuously (and usually erroneously)
transmitting CAN frames with identical - often high - priority. This constant babbling blocks CAN
bus access for any CAN frame with lower priority as these frames will loose the bus arbitration.

This sample application simulates a babbling CAN node. The properties of the CAN frames sent are
configurable via [Kconfig](../../../../build/kconfig/index.md#kconfig). The frames carry no data as only the arbitration part of
the CAN frame is of interest.

Being able to simulate a babbling CAN node is useful when examining the behavior of other nodes on
the same CAN bus when they constantly loose bus arbitration.

The source code for this sample application can be found at:
[samples/drivers/can/babbling](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/can/babbling).

## Requirements

This sample requires a board with a CAN controller. The CAN controller must be configured using the
`zephyr,canbus` [devicetree](../../../../build/dts/index.md#dt-guide) chosen node property.

The sample supports an optional button for stopping the babbling. If present, the button must be
configured using the `sw0` [devicetree](../../../../build/dts/index.md#dt-guide) alias, usually in the [BOARD.dts file](../../../../build/dts/intro-input-output.md#devicetree-in-out-files).

## Building and Running

Example building for [TWR-KE18F](../../../../boards/nxp/twr_ke18f/doc/index.md#twr_ke18f):

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/drivers/can/babbling
west flash
```

### Sample output

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-4606-g8c1efa8b96bb  ***
babbling on can@40024000 with standard (11-bit) CAN ID 0x010, RTR 0, CAN FD 0
abort by pressing User SW3 button
```

## See also

[CAN Interface](../../../../doxygen/html/group__can__interface.md)
