---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__midi__ump__cmd.html
original_path: doxygen/html/group__midi__ump__cmd.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MIDI commands

[Audio](group__audio__interface.md) » [MIDI2 Universal MIDI Packet definitions](group__midi__ump.md)

| Macros | |
| --- | --- |
| #define | [UMP\_MIDI\_NOTE\_OFF](#ga8300450177c4f1ec7c11ed7d8886f87e)   0x8 |
|  | Note Off (p1=note number, p2=velocity). |
| #define | [UMP\_MIDI\_NOTE\_ON](#ga85749d1edff030bc0d8b131b9116911e)   0x9 |
|  | Note On (p1=note number, p2=velocity). |
| #define | [UMP\_MIDI\_AFTERTOUCH](#ga7fae224629121ad30f9f38241885452c)   0xa |
|  | Polyphonic aftertouch (p1=note number, p2=data). |
| #define | [UMP\_MIDI\_CONTROL\_CHANGE](#gad4b17d74027a541957c933074d0f2d1e)   0xb |
|  | Control Change (p1=index, p2=data). |
| #define | [UMP\_MIDI\_PROGRAM\_CHANGE](#gaad34de6aae0e22f5c84ef50e488e2d1a)   0xc |
|  | Control Change (p1=program). |
| #define | [UMP\_MIDI\_CHAN\_AFTERTOUCH](#gaf5708894b80514023949e163f9687fb8)   0xd |
|  | Channel aftertouch (p1=data). |
| #define | [UMP\_MIDI\_PITCH\_BEND](#gab11535e72a74baa71491264dd2c16192)   0xe |
|  | Pitch bend (p1=lsb, p2=msb). |

## Detailed Description

See also
:   ump112: 7.3 MIDI 1.0 Channel Voice Messages

When [UMP\_MT(x)](group__midi__ump.md#gafab438886f69fb74a6e058f9343867aa "Message Type field of a Universal MIDI Packet.")=UMP\_MT\_MIDI1\_CHANNEL\_VOICE or UMP\_MT\_MIDI2\_CHANNEL\_VOICE, then [UMP\_MIDI\_COMMAND(x)](group__midi__ump.md#gac3af021e7300ab96e449da048545900f "Command of a MIDI channel voice message.") may be one of:

## Macro Definition Documentation

## [◆ ](#ga7fae224629121ad30f9f38241885452c)UMP\_MIDI\_AFTERTOUCH

| #define UMP\_MIDI\_AFTERTOUCH   0xa |
| --- |

`#include <[midi.h](midi_8h.md)>`

Polyphonic aftertouch (p1=note number, p2=data).

## [◆ ](#gaf5708894b80514023949e163f9687fb8)UMP\_MIDI\_CHAN\_AFTERTOUCH

| #define UMP\_MIDI\_CHAN\_AFTERTOUCH   0xd |
| --- |

`#include <[midi.h](midi_8h.md)>`

Channel aftertouch (p1=data).

## [◆ ](#gad4b17d74027a541957c933074d0f2d1e)UMP\_MIDI\_CONTROL\_CHANGE

| #define UMP\_MIDI\_CONTROL\_CHANGE   0xb |
| --- |

`#include <[midi.h](midi_8h.md)>`

Control Change (p1=index, p2=data).

## [◆ ](#ga8300450177c4f1ec7c11ed7d8886f87e)UMP\_MIDI\_NOTE\_OFF

| #define UMP\_MIDI\_NOTE\_OFF   0x8 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Note Off (p1=note number, p2=velocity).

## [◆ ](#ga85749d1edff030bc0d8b131b9116911e)UMP\_MIDI\_NOTE\_ON

| #define UMP\_MIDI\_NOTE\_ON   0x9 |
| --- |

`#include <[midi.h](midi_8h.md)>`

Note On (p1=note number, p2=velocity).

## [◆ ](#gab11535e72a74baa71491264dd2c16192)UMP\_MIDI\_PITCH\_BEND

| #define UMP\_MIDI\_PITCH\_BEND   0xe |
| --- |

`#include <[midi.h](midi_8h.md)>`

Pitch bend (p1=lsb, p2=msb).

## [◆ ](#gaad34de6aae0e22f5c84ef50e488e2d1a)UMP\_MIDI\_PROGRAM\_CHANGE

| #define UMP\_MIDI\_PROGRAM\_CHANGE   0xc |
| --- |

`#include <[midi.h](midi_8h.md)>`

Control Change (p1=program).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
