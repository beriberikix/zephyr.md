---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bluenrg__hci__driver.html
original_path: doxygen/html/group__bluenrg__hci__driver.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BlueNRG HCI driver extended API

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

BlueNRG HCI Driver-Specific API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [bluenrg\_bt\_reset](#gaa76b4af2fc2076deaeeb845514475483) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) updater\_mode) |
|  | Hardware reset the BlueNRG network coprocessor. |

## Detailed Description

BlueNRG HCI Driver-Specific API.

## Function Documentation

## [◆ ](#gaa76b4af2fc2076deaeeb845514475483)bluenrg\_bt\_reset()

| int bluenrg\_bt\_reset | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *updater\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_driver_bluenrg.h](hci__driver__bluenrg_8h.md)>`

Hardware reset the BlueNRG network coprocessor.

Performs hardware reset of the BLE network coprocessor. It can also force to enter firmware updater mode.

Parameters
:   | updater\_mode | flag to indicate whether updater mode needs to be entered. |
    | --- | --- |

Returns
:   a non-negative value indicating success, or a negative error code for failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
