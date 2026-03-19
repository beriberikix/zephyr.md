---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd__midi2_8h_source.html
original_path: doxygen/html/usbd__midi2_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_midi2.h

[Go to the documentation of this file.](usbd__midi2_8h.md)

1/\*

2 \* Copyright (c) 2024 Titouan Christophe

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_MIDI\_H\_

8#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_MIDI\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

24

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/audio/midi.h](midi_8h.md)>

27

[ 31](structusbd__midi__ops.md)struct [usbd\_midi\_ops](structusbd__midi__ops.md) {

[ 37](structusbd__midi__ops.md#a2cfa4187ff4f1b0bc602b92cfc3cba1d) void (\*[rx\_packet\_cb](structusbd__midi__ops.md#a2cfa4187ff4f1b0bc602b92cfc3cba1d))(const struct [device](structdevice.md) \*dev, const struct [midi\_ump](structmidi__ump.md) ump);

38

[ 44](structusbd__midi__ops.md#a1b0d3b3f7fe7833f2d71abc568029fbf) void (\*[ready\_cb](structusbd__midi__ops.md#a1b0d3b3f7fe7833f2d71abc568029fbf))(const struct [device](structdevice.md) \*dev, const bool ready);

45};

46

[ 55](group__usbd__midi2.md#gab0e96783f610e881b5c36718e708a7d8)int [usbd\_midi\_send](group__usbd__midi2.md#gab0e96783f610e881b5c36718e708a7d8)(const struct [device](structdevice.md) \*dev, const struct [midi\_ump](structmidi__ump.md) ump);

56

[ 62](group__usbd__midi2.md#gab08255e3bd10aea5c272ca08303b1bf5)void [usbd\_midi\_set\_ops](group__usbd__midi2.md#gab08255e3bd10aea5c272ca08303b1bf5)(const struct [device](structdevice.md) \*dev, const struct [usbd\_midi\_ops](structusbd__midi__ops.md) \*ops);

63

67

68#ifdef \_\_cplusplus

69}

70#endif

71

72#endif

[device.h](device_8h.md)

[usbd\_midi\_set\_ops](group__usbd__midi2.md#gab08255e3bd10aea5c272ca08303b1bf5)

void usbd\_midi\_set\_ops(const struct device \*dev, const struct usbd\_midi\_ops \*ops)

Set the application event handlers on a USB MIDI device.

[usbd\_midi\_send](group__usbd__midi2.md#gab0e96783f610e881b5c36718e708a7d8)

int usbd\_midi\_send(const struct device \*dev, const struct midi\_ump ump)

Send a Universal MIDI Packet to the host.

[midi.h](midi_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[midi\_ump](structmidi__ump.md)

Universal MIDI Packet container.

**Definition** midi.h:30

[usbd\_midi\_ops](structusbd__midi__ops.md)

MIDI2 application event handlers.

**Definition** usbd\_midi2.h:31

[usbd\_midi\_ops::ready\_cb](structusbd__midi__ops.md#a1b0d3b3f7fe7833f2d71abc568029fbf)

void(\* ready\_cb)(const struct device \*dev, const bool ready)

Callback type for MIDI2 interface runtime status change.

**Definition** usbd\_midi2.h:44

[usbd\_midi\_ops::rx\_packet\_cb](structusbd__midi__ops.md#a2cfa4187ff4f1b0bc602b92cfc3cba1d)

void(\* rx\_packet\_cb)(const struct device \*dev, const struct midi\_ump ump)

Callback type for incoming Universal MIDI Packets from host.

**Definition** usbd\_midi2.h:37

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_midi2.h](usbd__midi2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
