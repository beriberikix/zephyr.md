---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__midi__ump__sys.html
original_path: doxygen/html/group__midi__ump__sys.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

System common and System Real Time message status

[Audio](group__audio__interface.md) » [MIDI2 Universal MIDI Packet definitions](group__midi__ump.md)

| Macros | |
| --- | --- |
| #define | [UMP\_SYS\_MIDI\_TIME\_CODE](#ga85394094ca6d908b7886adc4caceb671)   0xf1 |
|  | MIDI Time Code (no param). |
| #define | [UMP\_SYS\_SONG\_POSITION](#ga254845a2c32a190b0bfc217025c5ad1d)   0xf2 |
|  | Song Position Pointer (p1=lsb, p2=msb). |
| #define | [UMP\_SYS\_SONG\_SELECT](#ga1d27e0f6fffd7ec05f58b56be78d9a8d)   0xf3 |
|  | Song Select (p1=song number). |
| #define | [UMP\_SYS\_TUNE\_REQUEST](#ga4aa12e0cdb101a38b938876ebdcca64b)   0xf6 |
|  | Tune Request (no param). |
| #define | [UMP\_SYS\_TIMING\_CLOCK](#gae064f3f47a9387076f5045e12e6ef7b7)   0xf8 |
|  | Timing Clock (no param). |
| #define | [UMP\_SYS\_START](#ga368ad3719080979709699feb3d002dff)   0xfa |
|  | Start (no param). |
| #define | [UMP\_SYS\_CONTINUE](#ga766b54e3caced69c147dbc94eb932595)   0xfb |
|  | Continue (no param). |
| #define | [UMP\_SYS\_STOP](#ga95542dda8f7f73f738c3ae298ca42f44)   0xfc |
|  | Stop (no param). |
| #define | [UMP\_SYS\_ACTIVE\_SENSING](#gaeb794e3933a2488eadb5f57ba971f81d)   0xfe |
|  | Active sensing (no param). |
| #define | [UMP\_SYS\_RESET](#ga5bd5358ae1847774409216f4e246f6f4)   0xff |
|  | Reset (no param). |

## Detailed Description

See also
:   ump112: 7.6 System Common and System Real Time Messages

When [UMP\_MT(x)](group__midi__ump.md#gafab438886f69fb74a6e058f9343867aa "Message Type field of a Universal MIDI Packet.")=UMP\_MT\_SYS\_RT\_COMMON, [UMP\_MIDI\_STATUS(x)](group__midi__ump.md#ga407db6234865dd53a0939b9e6ca7455c "Status byte of a MIDI channel voice or system message.") may be one of:

## Macro Definition Documentation

## [◆ ](#gaeb794e3933a2488eadb5f57ba971f81d)UMP\_SYS\_ACTIVE\_SENSING

| #define UMP\_SYS\_ACTIVE\_SENSING   0xfe |
| --- |

`#include <[midi.h](midi_8h.md)>`

Active sensing (no param).

## [◆ ](#ga766b54e3caced69c147dbc94eb932595)UMP\_SYS\_CONTINUE

| #define UMP\_SYS\_CONTINUE   0xfb |
| --- |

`#include <[midi.h](midi_8h.md)>`

Continue (no param).

## [◆ ](#ga85394094ca6d908b7886adc4caceb671)UMP\_SYS\_MIDI\_TIME\_CODE

| #define UMP\_SYS\_MIDI\_TIME\_CODE   0xf1 |
| --- |

`#include <[midi.h](midi_8h.md)>`

MIDI Time Code (no param).

## [◆ ](#ga5bd5358ae1847774409216f4e246f6f4)UMP\_SYS\_RESET

| #define UMP\_SYS\_RESET   0xff |
| --- |

`#include <[midi.h](midi_8h.md)>`

Reset (no param).

## [◆ ](#ga254845a2c32a190b0bfc217025c5ad1d)UMP\_SYS\_SONG\_POSITION

| #define UMP\_SYS\_SONG\_POSITION   0xf2 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Song Position Pointer (p1=lsb, p2=msb).

## [◆ ](#ga1d27e0f6fffd7ec05f58b56be78d9a8d)UMP\_SYS\_SONG\_SELECT

| #define UMP\_SYS\_SONG\_SELECT   0xf3 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Song Select (p1=song number).

## [◆ ](#ga368ad3719080979709699feb3d002dff)UMP\_SYS\_START

| #define UMP\_SYS\_START   0xfa |
| --- |

`#include <[midi.h](midi_8h.md)>`

Start (no param).

## [◆ ](#ga95542dda8f7f73f738c3ae298ca42f44)UMP\_SYS\_STOP

| #define UMP\_SYS\_STOP   0xfc |
| --- |

`#include <[midi.h](midi_8h.md)>`

Stop (no param).

## [◆ ](#gae064f3f47a9387076f5045e12e6ef7b7)UMP\_SYS\_TIMING\_CLOCK

| #define UMP\_SYS\_TIMING\_CLOCK   0xf8 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Timing Clock (no param).

## [◆ ](#ga4aa12e0cdb101a38b938876ebdcca64b)UMP\_SYS\_TUNE\_REQUEST

| #define UMP\_SYS\_TUNE\_REQUEST   0xf6 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Tune Request (no param).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
