---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__can__transceiver.html
original_path: doxygen/html/group__can__transceiver.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CAN Transceiver

[Device Driver APIs](group__io__interfaces.md)

CAN Transceiver Driver APIs.
[More...](#details)

| Functions | |
| --- | --- |
| static int | [can\_transceiver\_enable](#ga0d0e87150b49198c41e2782a17cfd694) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode) |
|  | Enable CAN transceiver. |
| static int | [can\_transceiver\_disable](#ga7509ca0b6ece81b4038b7d128af961be) (const struct [device](structdevice.md) \*dev) |
|  | Disable CAN transceiver. |

## Detailed Description

CAN Transceiver Driver APIs.

Since
:   3.1

Version
:   0.1.0

## Function Documentation

## [◆ ](#ga7509ca0b6ece81b4038b7d128af961be)can\_transceiver\_disable()

| | int can\_transceiver\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[transceiver.h](transceiver_8h.md)>`

Disable CAN transceiver.

Disable the CAN transceiver.

Note
:   The CAN transceiver is controlled by the CAN controller driver and should not normally be controlled by the application.

See also
:   [can\_stop()](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5 "Stop the CAN controller.")

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error, failed to disable device. |

## [◆ ](#ga0d0e87150b49198c41e2782a17cfd694)can\_transceiver\_enable()

| | int can\_transceiver\_enable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | *mode* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[transceiver.h](transceiver_8h.md)>`

Enable CAN transceiver.

Enable the CAN transceiver.

Note
:   The CAN transceiver is controlled by the CAN controller driver and should not normally be controlled by the application.

See also
:   [can\_start()](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a "Start the CAN controller.")

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mode | Operation mode. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error, failed to enable device. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
