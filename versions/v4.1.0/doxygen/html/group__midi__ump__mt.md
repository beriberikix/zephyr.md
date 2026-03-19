---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__midi__ump__mt.html
original_path: doxygen/html/group__midi__ump__mt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Message types

[Audio](group__audio__interface.md) » [MIDI2 Universal MIDI Packet definitions](group__midi__ump.md)

| Macros | |
| --- | --- |
| #define | [UMP\_MT\_UTILITY](#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)   0x00 |
|  | Utility Messages. |
| #define | [UMP\_MT\_SYS\_RT\_COMMON](#gab8f194f60f1b5de7f050009275e44412)   0x01 |
|  | System Real Time and System Common Messages (except System Exclusive). |
| #define | [UMP\_MT\_MIDI1\_CHANNEL\_VOICE](#gae086e5899933e436715ed2321607ef36)   0x02 |
|  | MIDI 1.0 Channel Voice Messages. |
| #define | [UMP\_MT\_DATA\_64](#ga235bf38958774c9ccc8864b98cff7ff9)   0x03 |
|  | 64 bits Data Messages (including System Exclusive) |
| #define | [UMP\_MT\_MIDI2\_CHANNEL\_VOICE](#ga9f2ac215138eb6e958df9558547f805a)   0x04 |
|  | MIDI 2.0 Channel Voice Messages. |
| #define | [UMP\_MT\_DATA\_128](#gabe19506f8d84dbc84a46114768853d5b)   0x05 |
|  | 128 bits Data Messages |
| #define | [UMP\_MT\_FLEX\_DATA](#ga916fba3c7a01dfff98f94c700a585fd5)   0x0d |
|  | Flex Data Messages. |
| #define | [UMP\_MT\_UMP\_STREAM](#gae14fb523ae456ca3e49a86de7d197e55)   0x0f |
|  | UMP Stream Message. |

## Detailed Description

See also
:   ump112: 2.1.4 Message Type (MT) Allocation

## Macro Definition Documentation

## [◆ ](#gabe19506f8d84dbc84a46114768853d5b)UMP\_MT\_DATA\_128

| #define UMP\_MT\_DATA\_128   0x05 |
| --- |

`#include <[midi.h](midi_8h.md)>`

128 bits Data Messages

## [◆ ](#ga235bf38958774c9ccc8864b98cff7ff9)UMP\_MT\_DATA\_64

| #define UMP\_MT\_DATA\_64   0x03 |
| --- |

`#include <[midi.h](midi_8h.md)>`

64 bits Data Messages (including System Exclusive)

## [◆ ](#ga916fba3c7a01dfff98f94c700a585fd5)UMP\_MT\_FLEX\_DATA

| #define UMP\_MT\_FLEX\_DATA   0x0d |
| --- |

`#include <[midi.h](midi_8h.md)>`

Flex Data Messages.

## [◆ ](#gae086e5899933e436715ed2321607ef36)UMP\_MT\_MIDI1\_CHANNEL\_VOICE

| #define UMP\_MT\_MIDI1\_CHANNEL\_VOICE   0x02 |
| --- |

`#include <[midi.h](midi_8h.md)>`

MIDI 1.0 Channel Voice Messages.

## [◆ ](#ga9f2ac215138eb6e958df9558547f805a)UMP\_MT\_MIDI2\_CHANNEL\_VOICE

| #define UMP\_MT\_MIDI2\_CHANNEL\_VOICE   0x04 |
| --- |

`#include <[midi.h](midi_8h.md)>`

MIDI 2.0 Channel Voice Messages.

## [◆ ](#gab8f194f60f1b5de7f050009275e44412)UMP\_MT\_SYS\_RT\_COMMON

| #define UMP\_MT\_SYS\_RT\_COMMON   0x01 |
| --- |

`#include <[midi.h](midi_8h.md)>`

System Real Time and System Common Messages (except System Exclusive).

## [◆ ](#gae14fb523ae456ca3e49a86de7d197e55)UMP\_MT\_UMP\_STREAM

| #define UMP\_MT\_UMP\_STREAM   0x0f |
| --- |

`#include <[midi.h](midi_8h.md)>`

UMP Stream Message.

## [◆ ](#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)UMP\_MT\_UTILITY

| #define UMP\_MT\_UTILITY   0x00 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Utility Messages.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
