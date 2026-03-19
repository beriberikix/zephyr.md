---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__micp__mic__dev__cb.html
original_path: doxygen/html/structbt__micp__mic__dev__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_micp\_mic\_dev\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Microphone Control Profile (MICP)](group__bt__micp.md)

Struct to hold the Microphone Device callbacks.
[More...](#details)

`#include <[micp.h](micp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [mute](#ad674b130546ceabbb90e6004121ccd98) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute) |
|  | Callback function for Microphone Device mute. |

## Detailed Description

Struct to hold the Microphone Device callbacks.

These can be registered for usage with [bt\_micp\_mic\_dev\_register()](group__bt__micp.md#ga5dee6c7a1115bffbea39ba0575f369fc "Initialize the Microphone Control Profile Microphone Device.").

## Field Documentation

## [◆ ](#ad674b130546ceabbb90e6004121ccd98)mute

| void(\* bt\_micp\_mic\_dev\_cb::mute) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute) |
| --- |

Callback function for Microphone Device mute.

Called when the value is read with [bt\_micp\_mic\_dev\_mute\_get()](group__bt__micp.md#ga263bf5cf51e4ef8d7e6986f0d8358da3 "Read the mute state on the Microphone Device."), or if the value is changed by either the Microphone Device or a Microphone Controller.

Parameters
:   | [mute](#ad674b130546ceabbb90e6004121ccd98) | The mute setting of the Microphone Control Service. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[micp.h](micp_8h_source.md)

- [bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
