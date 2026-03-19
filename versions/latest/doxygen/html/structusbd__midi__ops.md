---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__midi__ops.html
original_path: doxygen/html/structusbd__midi__ops.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_midi\_ops Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB MIDI 2.0 Class device API](group__usbd__midi2.md)

MIDI2 application event handlers.
[More...](#details)

`#include <[usbd_midi2.h](usbd__midi2_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [rx\_packet\_cb](#a2cfa4187ff4f1b0bc602b92cfc3cba1d) )(const struct [device](structdevice.md) \*dev, const struct [midi\_ump](structmidi__ump.md) ump) |
|  | Callback type for incoming Universal MIDI Packets from host. |
| void(\* | [ready\_cb](#a1b0d3b3f7fe7833f2d71abc568029fbf) )(const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ready) |
|  | Callback type for MIDI2 interface runtime status change. |

## Detailed Description

MIDI2 application event handlers.

## Field Documentation

## [◆ ](#a1b0d3b3f7fe7833f2d71abc568029fbf)ready\_cb

| void(\* usbd\_midi\_ops::ready\_cb) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ready) |
| --- |

Callback type for MIDI2 interface runtime status change.

Parameters
:   | [in] | dev | The MIDI2 device |
    | --- | --- | --- |
    | [in] | ready | True if the interface is enabled by the host |

## [◆ ](#a2cfa4187ff4f1b0bc602b92cfc3cba1d)rx\_packet\_cb

| void(\* usbd\_midi\_ops::rx\_packet\_cb) (const struct [device](structdevice.md) \*dev, const struct [midi\_ump](structmidi__ump.md) ump) |
| --- |

Callback type for incoming Universal MIDI Packets from host.

Parameters
:   | [in] | dev | The MIDI2 device receiving the packet |
    | --- | --- | --- |
    | [in] | ump | The received packet in Universal MIDI Packet format |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usbd\_midi2.h](usbd__midi2_8h_source.md)

- [usbd\_midi\_ops](structusbd__midi__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
