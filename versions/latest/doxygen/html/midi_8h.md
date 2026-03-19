---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/midi_8h.html
original_path: doxygen/html/midi_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

midi.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](midi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [midi\_ump](structmidi__ump.md) |
|  | Universal MIDI Packet container. [More...](structmidi__ump.md#details) |

| Macros | |
| --- | --- |
| #define | [UMP\_MT\_UTILITY](group__midi__ump__mt.md#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)   0x00 |
|  | Utility Messages. |
| #define | [UMP\_MT\_SYS\_RT\_COMMON](group__midi__ump__mt.md#gab8f194f60f1b5de7f050009275e44412)   0x01 |
|  | System Real Time and System Common Messages (except System Exclusive). |
| #define | [UMP\_MT\_MIDI1\_CHANNEL\_VOICE](group__midi__ump__mt.md#gae086e5899933e436715ed2321607ef36)   0x02 |
|  | MIDI 1.0 Channel Voice Messages. |
| #define | [UMP\_MT\_DATA\_64](group__midi__ump__mt.md#ga235bf38958774c9ccc8864b98cff7ff9)   0x03 |
|  | 64 bits Data Messages (including System Exclusive) |
| #define | [UMP\_MT\_MIDI2\_CHANNEL\_VOICE](group__midi__ump__mt.md#ga9f2ac215138eb6e958df9558547f805a)   0x04 |
|  | MIDI 2.0 Channel Voice Messages. |
| #define | [UMP\_MT\_DATA\_128](group__midi__ump__mt.md#gabe19506f8d84dbc84a46114768853d5b)   0x05 |
|  | 128 bits Data Messages |
| #define | [UMP\_MT\_FLEX\_DATA](group__midi__ump__mt.md#ga916fba3c7a01dfff98f94c700a585fd5)   0x0d |
|  | Flex Data Messages. |
| #define | [UMP\_MT\_UMP\_STREAM](group__midi__ump__mt.md#gae14fb523ae456ca3e49a86de7d197e55)   0x0f |
|  | UMP Stream Message. |
| #define | [UMP\_MT](group__midi__ump.md#gafab438886f69fb74a6e058f9343867aa)(ump) |
|  | Message Type field of a Universal MIDI Packet. |
| #define | [UMP\_NUM\_WORDS\_LOOKUP\_TABLE](group__midi__ump.md#gac718c321652066f1537ead1524137949) |
|  | There are 16 UMP message types, each of which can be 1 to 4 uint32 long. |
| #define | [UMP\_NUM\_WORDS](group__midi__ump.md#ga31e6cb035180b3afca9980307a07c038)(ump) |
|  | Size of a Universal MIDI Packet, in 32bit words. |
| #define | [UMP\_GROUP](group__midi__ump.md#ga497e212c131b7366878e46f63727cab5)(ump) |
|  | MIDI group field of a Universal MIDI Packet. |
| #define | [UMP\_MIDI\_STATUS](group__midi__ump.md#ga407db6234865dd53a0939b9e6ca7455c)(ump) |
|  | Status byte of a MIDI channel voice or system message. |
| #define | [UMP\_MIDI\_COMMAND](group__midi__ump.md#gac3af021e7300ab96e449da048545900f)(ump) |
|  | Command of a MIDI channel voice message. |
| #define | [UMP\_MIDI\_CHANNEL](group__midi__ump.md#ga8ecdaa13831c0cf1abf79da0b343416f)(ump) |
|  | Channel of a MIDI channel voice message. |
| #define | [UMP\_MIDI1\_P1](group__midi__ump.md#gac64740902864ecb903f70083f2c638d2)(ump) |
|  | First parameter of a MIDI1 channel voice or system message. |
| #define | [UMP\_MIDI1\_P2](group__midi__ump.md#ga1c6c6f8928071d4d77744404e62168b4)(ump) |
|  | Second parameter of a MIDI1 channel voice or system message. |
| #define | [UMP\_MIDI1\_CHANNEL\_VOICE](group__midi__ump.md#gac05c1718b33d08a92bae9b4974ced501)([group](structgroup.md), command, channel, p1, p2) |
|  | Initialize a UMP with a MIDI1 channel voice message. |
| #define | [UMP\_MIDI\_NOTE\_OFF](group__midi__ump__cmd.md#ga8300450177c4f1ec7c11ed7d8886f87e)   0x8 |
|  | Note Off (p1=note number, p2=velocity). |
| #define | [UMP\_MIDI\_NOTE\_ON](group__midi__ump__cmd.md#ga85749d1edff030bc0d8b131b9116911e)   0x9 |
|  | Note On (p1=note number, p2=velocity). |
| #define | [UMP\_MIDI\_AFTERTOUCH](group__midi__ump__cmd.md#ga7fae224629121ad30f9f38241885452c)   0xa |
|  | Polyphonic aftertouch (p1=note number, p2=data). |
| #define | [UMP\_MIDI\_CONTROL\_CHANGE](group__midi__ump__cmd.md#gad4b17d74027a541957c933074d0f2d1e)   0xb |
|  | Control Change (p1=index, p2=data). |
| #define | [UMP\_MIDI\_PROGRAM\_CHANGE](group__midi__ump__cmd.md#gaad34de6aae0e22f5c84ef50e488e2d1a)   0xc |
|  | Control Change (p1=program). |
| #define | [UMP\_MIDI\_CHAN\_AFTERTOUCH](group__midi__ump__cmd.md#gaf5708894b80514023949e163f9687fb8)   0xd |
|  | Channel aftertouch (p1=data). |
| #define | [UMP\_MIDI\_PITCH\_BEND](group__midi__ump__cmd.md#gab11535e72a74baa71491264dd2c16192)   0xe |
|  | Pitch bend (p1=lsb, p2=msb). |
| #define | [UMP\_SYS\_RT\_COMMON](group__midi__ump.md#ga06562acb0ec4d618d2e05b94c0a1bc4f)([group](structgroup.md), status, p1, p2) |
|  | Initialize a UMP with a System Real Time and System Common Message. |
| #define | [UMP\_SYS\_MIDI\_TIME\_CODE](group__midi__ump__sys.md#ga85394094ca6d908b7886adc4caceb671)   0xf1 |
|  | MIDI Time Code (no param). |
| #define | [UMP\_SYS\_SONG\_POSITION](group__midi__ump__sys.md#ga254845a2c32a190b0bfc217025c5ad1d)   0xf2 |
|  | Song Position Pointer (p1=lsb, p2=msb). |
| #define | [UMP\_SYS\_SONG\_SELECT](group__midi__ump__sys.md#ga1d27e0f6fffd7ec05f58b56be78d9a8d)   0xf3 |
|  | Song Select (p1=song number). |
| #define | [UMP\_SYS\_TUNE\_REQUEST](group__midi__ump__sys.md#ga4aa12e0cdb101a38b938876ebdcca64b)   0xf6 |
|  | Tune Request (no param). |
| #define | [UMP\_SYS\_TIMING\_CLOCK](group__midi__ump__sys.md#gae064f3f47a9387076f5045e12e6ef7b7)   0xf8 |
|  | Timing Clock (no param). |
| #define | [UMP\_SYS\_START](group__midi__ump__sys.md#ga368ad3719080979709699feb3d002dff)   0xfa |
|  | Start (no param). |
| #define | [UMP\_SYS\_CONTINUE](group__midi__ump__sys.md#ga766b54e3caced69c147dbc94eb932595)   0xfb |
|  | Continue (no param). |
| #define | [UMP\_SYS\_STOP](group__midi__ump__sys.md#ga95542dda8f7f73f738c3ae298ca42f44)   0xfc |
|  | Stop (no param). |
| #define | [UMP\_SYS\_ACTIVE\_SENSING](group__midi__ump__sys.md#gaeb794e3933a2488eadb5f57ba971f81d)   0xfe |
|  | Active sensing (no param). |
| #define | [UMP\_SYS\_RESET](group__midi__ump__sys.md#ga5bd5358ae1847774409216f4e246f6f4)   0xff |
|  | Reset (no param). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [midi.h](midi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
