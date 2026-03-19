---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__midi__ump.html
original_path: doxygen/html/group__midi__ump.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MIDI2 Universal MIDI Packet definitions

[Audio](group__audio__interface.md)

Universal MIDI Packet definitions.
[More...](#details)

| Topics | |
| --- | --- |
|  | [MIDI commands](group__midi__ump__cmd.md) |
|  | [Message types](group__midi__ump__mt.md) |
|  | [System common and System Real Time message status](group__midi__ump__sys.md) |

| Data Structures | |
| --- | --- |
| struct | [midi\_ump](structmidi__ump.md) |
|  | Universal MIDI Packet container. [More...](structmidi__ump.md#details) |

| Macros | |
| --- | --- |
| #define | [UMP\_MT](#gafab438886f69fb74a6e058f9343867aa)(ump) |
|  | Message Type field of a Universal MIDI Packet. |
| #define | [UMP\_NUM\_WORDS\_LOOKUP\_TABLE](#gac718c321652066f1537ead1524137949) |
|  | There are 16 UMP message types, each of which can be 1 to 4 uint32 long. |
| #define | [UMP\_NUM\_WORDS](#ga31e6cb035180b3afca9980307a07c038)(ump) |
|  | Size of a Universal MIDI Packet, in 32bit words. |
| #define | [UMP\_GROUP](#ga497e212c131b7366878e46f63727cab5)(ump) |
|  | MIDI group field of a Universal MIDI Packet. |
| #define | [UMP\_MIDI\_STATUS](#ga407db6234865dd53a0939b9e6ca7455c)(ump) |
|  | Status byte of a MIDI channel voice or system message. |
| #define | [UMP\_MIDI\_COMMAND](#gac3af021e7300ab96e449da048545900f)(ump) |
|  | Command of a MIDI channel voice message. |
| #define | [UMP\_MIDI\_CHANNEL](#ga8ecdaa13831c0cf1abf79da0b343416f)(ump) |
|  | Channel of a MIDI channel voice message. |
| #define | [UMP\_MIDI1\_P1](#gac64740902864ecb903f70083f2c638d2)(ump) |
|  | First parameter of a MIDI1 channel voice or system message. |
| #define | [UMP\_MIDI1\_P2](#ga1c6c6f8928071d4d77744404e62168b4)(ump) |
|  | Second parameter of a MIDI1 channel voice or system message. |
| #define | [UMP\_MIDI1\_CHANNEL\_VOICE](#gac05c1718b33d08a92bae9b4974ced501)([group](structgroup.md), command, channel, p1, p2) |
|  | Initialize a UMP with a MIDI1 channel voice message. |
| #define | [UMP\_SYS\_RT\_COMMON](#ga06562acb0ec4d618d2e05b94c0a1bc4f)([group](structgroup.md), status, p1, p2) |
|  | Initialize a UMP with a System Real Time and System Common Message. |

## Detailed Description

Universal MIDI Packet definitions.

Since
:   4.1

Version
:   0.1.0

See also
:   ump112: "Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol" Document version 1.1.2

## Macro Definition Documentation

## [◆ ](#ga497e212c131b7366878e46f63727cab5)UMP\_GROUP

| #define UMP\_GROUP | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

(((ump).data[0] >> 24) & 0x0f)

MIDI group field of a Universal MIDI Packet.

Parameters
:   | [in] | ump | Universal MIDI Packet |
    | --- | --- | --- |

## [◆ ](#gac05c1718b33d08a92bae9b4974ced501)UMP\_MIDI1\_CHANNEL\_VOICE

| #define UMP\_MIDI1\_CHANNEL\_VOICE | ( |  | *[group](structgroup.md)*, |
| --- | --- | --- | --- |
|  |  |  | *command*, |
|  |  |  | *channel*, |
|  |  |  | *p1*, |
|  |  |  | *p2* ) |

`#include <[midi.h](midi_8h.md)>`

**Value:**

(struct [midi\_ump](structmidi__ump.md)) {.data = { \

([UMP\_MT\_MIDI1\_CHANNEL\_VOICE](group__midi__ump__mt.md#gae086e5899933e436715ed2321607ef36) << 28) \

| ((([group](structgroup.md)) & 0x0f) << 24) \

| (((command) & 0x0f) << 20) \

| (((channel) & 0x0f) << 16) \

| (((p1) & 0x7f) << 8) \

| ((p2) & 0x7f) \

}}

[UMP\_MT\_MIDI1\_CHANNEL\_VOICE](group__midi__ump__mt.md#gae086e5899933e436715ed2321607ef36)

#define UMP\_MT\_MIDI1\_CHANNEL\_VOICE

MIDI 1.0 Channel Voice Messages.

**Definition** midi.h:46

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[midi\_ump](structmidi__ump.md)

Universal MIDI Packet container.

**Definition** midi.h:30

Initialize a UMP with a MIDI1 channel voice message.

Remarks
:   For messages that take a single parameter, p2 is ignored by the receiver.

Parameters
:   | [group](structgroup.md "Group structure.") | The UMP group |
    | --- | --- |
    | command | The MIDI1 command |
    | channel | The MIDI1 channel number |
    | p1 | The 1st MIDI1 parameter |
    | p2 | The 2nd MIDI1 parameter |

## [◆ ](#gac64740902864ecb903f70083f2c638d2)UMP\_MIDI1\_P1

| #define UMP\_MIDI1\_P1 | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

(((ump).data[0] >> 8) & 0x7f)

First parameter of a MIDI1 channel voice or system message.

Parameters
:   | [in] | ump | Universal MIDI Packet (containing a MIDI1 message) |
    | --- | --- | --- |

## [◆ ](#ga1c6c6f8928071d4d77744404e62168b4)UMP\_MIDI1\_P2

| #define UMP\_MIDI1\_P2 | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

((ump).data[0] & 0x7f)

Second parameter of a MIDI1 channel voice or system message.

Parameters
:   | [in] | ump | Universal MIDI Packet (containing a MIDI1 message) |
    | --- | --- | --- |

## [◆ ](#ga8ecdaa13831c0cf1abf79da0b343416f)UMP\_MIDI\_CHANNEL

| #define UMP\_MIDI\_CHANNEL | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

([UMP\_MIDI\_STATUS](#ga407db6234865dd53a0939b9e6ca7455c)(ump) & 0x0f)

[UMP\_MIDI\_STATUS](#ga407db6234865dd53a0939b9e6ca7455c)

#define UMP\_MIDI\_STATUS(ump)

Status byte of a MIDI channel voice or system message.

**Definition** midi.h:95

Channel of a MIDI channel voice message.

Parameters
:   | [in] | ump | Universal MIDI Packet (containing a MIDI event) |
    | --- | --- | --- |

## [◆ ](#gac3af021e7300ab96e449da048545900f)UMP\_MIDI\_COMMAND

| #define UMP\_MIDI\_COMMAND | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

([UMP\_MIDI\_STATUS](#ga407db6234865dd53a0939b9e6ca7455c)(ump) >> 4)

Command of a MIDI channel voice message.

Parameters
:   | [in] | ump | Universal MIDI Packet (containing a MIDI event) |
    | --- | --- | --- |

See also
:   [MIDI commands](group__midi__ump__cmd.md)

## [◆ ](#ga407db6234865dd53a0939b9e6ca7455c)UMP\_MIDI\_STATUS

| #define UMP\_MIDI\_STATUS | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

(((ump).data[0] >> 16) & 0xff)

Status byte of a MIDI channel voice or system message.

Parameters
:   | [in] | ump | Universal MIDI Packet (containing a MIDI1 event) |
    | --- | --- | --- |

## [◆ ](#gafab438886f69fb74a6e058f9343867aa)UMP\_MT

| #define UMP\_MT | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

((ump).data[0] >> 28)

Message Type field of a Universal MIDI Packet.

Parameters
:   | [in] | ump | Universal MIDI Packet |
    | --- | --- | --- |

## [◆ ](#ga31e6cb035180b3afca9980307a07c038)UMP\_NUM\_WORDS

| #define UMP\_NUM\_WORDS | ( |  | *ump* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

(1 + (([UMP\_NUM\_WORDS\_LOOKUP\_TABLE](#gac718c321652066f1537ead1524137949) >> (2 \* [UMP\_MT](#gafab438886f69fb74a6e058f9343867aa)(ump))) & 3))

[UMP\_NUM\_WORDS\_LOOKUP\_TABLE](#gac718c321652066f1537ead1524137949)

#define UMP\_NUM\_WORDS\_LOOKUP\_TABLE

There are 16 UMP message types, each of which can be 1 to 4 uint32 long.

**Definition** midi.h:70

[UMP\_MT](#gafab438886f69fb74a6e058f9343867aa)

#define UMP\_MT(ump)

Message Type field of a Universal MIDI Packet.

**Definition** midi.h:63

Size of a Universal MIDI Packet, in 32bit words.

Parameters
:   | [in] | ump | Universal MIDI Packet |
    | --- | --- | --- |

See also
:   ump112: 2.1.4 Message Type (MT) Allocation

## [◆ ](#gac718c321652066f1537ead1524137949)UMP\_NUM\_WORDS\_LOOKUP\_TABLE

| #define UMP\_NUM\_WORDS\_LOOKUP\_TABLE |
| --- |

`#include <[midi.h](midi_8h.md)>`

**Value:**

((0U << 0) | (0U << 2) | (0U << 4) | (1U << 6) | \

(1U << 8) | (3U << 10) | (0U << 12) | (0U << 14) | \

(1U << 16) | (1U << 18) | (1U << 20) | (2U << 22) | \

(2U << 24) | (3U << 26) | (3U << 28) | (3U << 30))

There are 16 UMP message types, each of which can be 1 to 4 uint32 long.

Hence this packed representation of 16x2b array as an uint32 lookup table

## [◆ ](#ga06562acb0ec4d618d2e05b94c0a1bc4f)UMP\_SYS\_RT\_COMMON

| #define UMP\_SYS\_RT\_COMMON | ( |  | *[group](structgroup.md)*, |
| --- | --- | --- | --- |
|  |  |  | *status*, |
|  |  |  | *p1*, |
|  |  |  | *p2* ) |

`#include <[midi.h](midi_8h.md)>`

**Value:**

(struct [midi\_ump](structmidi__ump.md)) {.data = { \

([UMP\_MT\_SYS\_RT\_COMMON](group__midi__ump__mt.md#gab8f194f60f1b5de7f050009275e44412) << 28) \

| ((([group](structgroup.md)) & 0x0f) << 24) \

| ((status) << 16) \

| (((p1) & 0x7f) << 8) \

| ((p2) & 0x7f) \

}}

[UMP\_MT\_SYS\_RT\_COMMON](group__midi__ump__mt.md#gab8f194f60f1b5de7f050009275e44412)

#define UMP\_MT\_SYS\_RT\_COMMON

System Real Time and System Common Messages (except System Exclusive).

**Definition** midi.h:44

Initialize a UMP with a System Real Time and System Common Message.

Remarks
:   For messages that take only one (or no) parameter, p2 (and p1) are ignored by the receiver.

Parameters
:   | [group](structgroup.md "Group structure.") | The UMP group |
    | --- | --- |
    | status | The status byte |
    | p1 | The 1st parameter |
    | p2 | The 2nd parameter |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
