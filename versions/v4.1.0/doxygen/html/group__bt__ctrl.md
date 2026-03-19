---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__ctrl.html
original_path: doxygen/html/group__bt__ctrl.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Controller

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Controller.
[More...](#details)

| Functions | |
| --- | --- |
| void | [bt\_ctlr\_set\_public\_addr](#ga541cabe76fd3cb019aae2fe01d45cbfc) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr) |
|  | Set public address for controller. |

## Detailed Description

Bluetooth Controller.

## Function Documentation

## [◆ ](#ga541cabe76fd3cb019aae2fe01d45cbfc)bt\_ctlr\_set\_public\_addr()

| void bt\_ctlr\_set\_public\_addr | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[controller.h](bluetooth_2controller_8h.md)>`

Set public address for controller.

Should be called before [bt\_enable()](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b "Enable Bluetooth.").

Parameters
:   | addr | Public address |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
