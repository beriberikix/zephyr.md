---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/protocol_8h.html
original_path: doxygen/html/protocol_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

protocol.h File Reference

SCMI protocol generic functions and structures.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/firmware/scmi/util.h](drivers_2firmware_2scmi_2util_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](protocol_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [scmi\_protocol](structscmi__protocol.md) |
|  | SCMI protocol structure. [More...](structscmi__protocol.md#details) |
| struct | [scmi\_message](structscmi__message.md) |
|  | SCMI message structure. [More...](structscmi__message.md#details) |

| Macros | |
| --- | --- |
| #define | [SCMI\_MESSAGE\_HDR\_MAKE](#a100155d2238e9f860e2cab8ad8209a8a)(id, type, proto, token) |
|  | Build an SCMI message header. |

| Enumerations | |
| --- | --- |
| enum | [scmi\_message\_type](#a0c1b38acb21bc918714720c781e50d77) { [SCMI\_COMMAND](#a0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8) = 0x0 , [SCMI\_DELAYED\_REPLY](#a0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668) = 0x2 , [SCMI\_NOTIFICATION](#a0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04) = 0x3 } |
|  | SCMI message type. [More...](#a0c1b38acb21bc918714720c781e50d77) |
| enum | [scmi\_status\_code](#a451a39b7d2f3ffafa9d69b21c7e249b2) {     [SCMI\_SUCCESS](#a451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4) = 0 , [SCMI\_NOT\_SUPPORTED](#a451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089) = -1 , [SCMI\_INVALID\_PARAMETERS](#a451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0) = -2 , [SCMI\_DENIED](#a451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf) = -3 ,     [SCMI\_NOT\_FOUND](#a451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc) = -4 , [SCMI\_OUT\_OF\_RANGE](#a451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e) = -5 , [SCMI\_BUSY](#a451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa) = -6 , [SCMI\_COMMS\_ERROR](#a451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d) = -7 ,     [SCMI\_GENERIC\_ERROR](#a451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763) = -8 , [SCMI\_HARDWARE\_ERROR](#a451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6) = -9 , [SCMI\_PROTOCOL\_ERROR](#a451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4) = -10 , [SCMI\_IN\_USE](#a451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60) = -11   } |
|  | SCMI status codes. [More...](#a451a39b7d2f3ffafa9d69b21c7e249b2) |

| Functions | |
| --- | --- |
| int | [scmi\_status\_to\_errno](#aec0ffd1352d0106633fd15be8fc20aa2) (int scmi\_status) |
|  | Convert an SCMI status code to its Linux equivalent (if possible). |
| int | [scmi\_send\_message](#a4c3d437846753de06bb86b653c30404f) (struct [scmi\_protocol](structscmi__protocol.md) \*proto, struct [scmi\_message](structscmi__message.md) \*msg, struct [scmi\_message](structscmi__message.md) \*reply) |
|  | Send an SCMI message and wait for its reply. |

## Detailed Description

SCMI protocol generic functions and structures.

## Macro Definition Documentation

## [◆ ](#a100155d2238e9f860e2cab8ad8209a8a)SCMI\_MESSAGE\_HDR\_MAKE

| #define SCMI\_MESSAGE\_HDR\_MAKE | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *proto*, |
|  |  |  | *token* ) |

**Value:**

([SCMI\_FIELD\_MAKE](drivers_2firmware_2scmi_2util_8h.md#a21b369f9fa6d1a965ece4a589df88581)(id, [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0), 0) | \

SCMI\_FIELD\_MAKE(type, [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0), 8) | \

SCMI\_FIELD\_MAKE(proto, [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0), 10) | \

SCMI\_FIELD\_MAKE(token, [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 0), 18))

[SCMI\_FIELD\_MAKE](drivers_2firmware_2scmi_2util_8h.md#a21b369f9fa6d1a965ece4a589df88581)

#define SCMI\_FIELD\_MAKE(x, mask, shift)

Create an SCMI message field.

**Definition** util.h:264

[GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)

#define GENMASK(h, l)

Create a contiguous bitmask starting at bit position l and ending at position h.

**Definition** util.h:79

Build an SCMI message header.

Builds an SCMI message header based on the fields that make it up.

Parameters
:   | id | message ID |
    | --- | --- |
    | type | message type |
    | proto | protocol ID |
    | token | message token |

## Enumeration Type Documentation

## [◆ ](#a0c1b38acb21bc918714720c781e50d77)scmi\_message\_type

| enum [scmi\_message\_type](#a0c1b38acb21bc918714720c781e50d77) |
| --- |

SCMI message type.

| Enumerator | |
| --- | --- |
| SCMI\_COMMAND | command message |
| SCMI\_DELAYED\_REPLY | delayed reply message |
| SCMI\_NOTIFICATION | notification message |

## [◆ ](#a451a39b7d2f3ffafa9d69b21c7e249b2)scmi\_status\_code

| enum [scmi\_status\_code](#a451a39b7d2f3ffafa9d69b21c7e249b2) |
| --- |

SCMI status codes.

| Enumerator | |
| --- | --- |
| SCMI\_SUCCESS |  |
| SCMI\_NOT\_SUPPORTED |  |
| SCMI\_INVALID\_PARAMETERS |  |
| SCMI\_DENIED |  |
| SCMI\_NOT\_FOUND |  |
| SCMI\_OUT\_OF\_RANGE |  |
| SCMI\_BUSY |  |
| SCMI\_COMMS\_ERROR |  |
| SCMI\_GENERIC\_ERROR |  |
| SCMI\_HARDWARE\_ERROR |  |
| SCMI\_PROTOCOL\_ERROR |  |
| SCMI\_IN\_USE |  |

## Function Documentation

## [◆ ](#a4c3d437846753de06bb86b653c30404f)scmi\_send\_message()

| int scmi\_send\_message | ( | struct [scmi\_protocol](structscmi__protocol.md) \* | *proto*, |
| --- | --- | --- | --- |
|  |  | struct [scmi\_message](structscmi__message.md) \* | *msg*, |
|  |  | struct [scmi\_message](structscmi__message.md) \* | *reply* ) |

Send an SCMI message and wait for its reply.

Blocking function used to send an SCMI message over a given channel and wait for its reply

Parameters
:   | proto | pointer to SCMI protocol |
    | --- | --- |
    | msg | pointer to SCMI message to send |
    | reply | pointer to SCMI message in which the reply is to be written |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#aec0ffd1352d0106633fd15be8fc20aa2)scmi\_status\_to\_errno()

| int scmi\_status\_to\_errno | ( | int | *scmi\_status* | ) |  |
| --- | --- | --- | --- | --- | --- |

Convert an SCMI status code to its Linux equivalent (if possible).

Parameters
:   | scmi\_status | SCMI status code as shown in enum [scmi\_status\_code](#a451a39b7d2f3ffafa9d69b21c7e249b2) |
    | --- | --- |

Return values
:   | Linux | equivalent status code |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [protocol.h](protocol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
