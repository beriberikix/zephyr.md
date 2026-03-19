---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd__midi2_8h.html
original_path: doxygen/html/usbd__midi2_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_midi2.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/audio/midi.h](midi_8h_source.md)>`

[Go to the source code of this file.](usbd__midi2_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbd\_midi\_ops](structusbd__midi__ops.md) |
|  | MIDI2 application event handlers. [More...](structusbd__midi__ops.md#details) |

| Functions | |
| --- | --- |
| int | [usbd\_midi\_send](group__usbd__midi2.md#gab0e96783f610e881b5c36718e708a7d8) (const struct [device](structdevice.md) \*dev, const struct [midi\_ump](structmidi__ump.md) ump) |
|  | Send a Universal MIDI Packet to the host. |
| void | [usbd\_midi\_set\_ops](group__usbd__midi2.md#gab08255e3bd10aea5c272ca08303b1bf5) (const struct [device](structdevice.md) \*dev, const struct [usbd\_midi\_ops](structusbd__midi__ops.md) \*ops) |
|  | Set the application event handlers on a USB MIDI device. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_midi2.h](usbd__midi2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
