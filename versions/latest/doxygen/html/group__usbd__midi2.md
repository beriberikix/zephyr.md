---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usbd__midi2.html
original_path: doxygen/html/group__usbd__midi2.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB MIDI 2.0 Class device API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USB MIDI 2.0 class device API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usbd\_midi\_ops](structusbd__midi__ops.md) |
|  | MIDI2 application event handlers. [More...](structusbd__midi__ops.md#details) |

| Functions | |
| --- | --- |
| int | [usbd\_midi\_send](#gab0e96783f610e881b5c36718e708a7d8) (const struct [device](structdevice.md) \*dev, const struct [midi\_ump](structmidi__ump.md) ump) |
|  | Send a Universal MIDI Packet to the host. |
| void | [usbd\_midi\_set\_ops](#gab08255e3bd10aea5c272ca08303b1bf5) (const struct [device](structdevice.md) \*dev, const struct [usbd\_midi\_ops](structusbd__midi__ops.md) \*ops) |
|  | Set the application event handlers on a USB MIDI device. |

## Detailed Description

USB MIDI 2.0 class device API.

Since
:   4.1

Version
:   0.1.0

See also
:   midi20: "Universal Serial Bus Device Class Definition for MIDI Devices" Document Release 2.0 (May 5, 2020)

## Function Documentation

## [◆ ](#gab0e96783f610e881b5c36718e708a7d8)usbd\_midi\_send()

| int usbd\_midi\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [midi\_ump](structmidi__ump.md) | *ump* ) |

`#include <[usbd_midi2.h](usbd__midi2_8h.md)>`

Send a Universal MIDI Packet to the host.

Parameters
:   | [in] | dev | The MIDI2 device |
    | --- | --- | --- |
    | [in] | ump | The packet to send, in Universal MIDI Packet format |

Returns
:   0 on success, all other values should be treated as error -EIO if USB MIDI 2.0 is not enabled by the host -ENOBUFS if there is no space in the TX buffer

## [◆ ](#gab08255e3bd10aea5c272ca08303b1bf5)usbd\_midi\_set\_ops()

| void usbd\_midi\_set\_ops | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [usbd\_midi\_ops](structusbd__midi__ops.md) \* | *ops* ) |

`#include <[usbd_midi2.h](usbd__midi2_8h.md)>`

Set the application event handlers on a USB MIDI device.

Parameters
:   | [in] | dev | The MIDI2 device |
    | --- | --- | --- |
    | [in] | ops | The event handlers. Pass NULL to reset all callbacks |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
