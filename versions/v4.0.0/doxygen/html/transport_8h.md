---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/transport_8h.html
original_path: doxygen/html/transport_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

transport.h File Reference

Public APIs for the SCMI transport layer drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](transport_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [scmi\_channel](structscmi__channel.md) |
|  | SCMI channel structure. [More...](structscmi__channel.md#details) |
| struct | [scmi\_transport\_api](structscmi__transport__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [scmi\_channel\_cb](#a2ae1a5afd4489cf4cf60bd45de2c6956)) (struct [scmi\_channel](structscmi__channel.md) \*chan) |
|  | Callback function for message replies. |

| Functions | |
| --- | --- |
| static struct [scmi\_channel](structscmi__channel.md) \* | [scmi\_transport\_request\_channel](#aa944ea05d5b9995e7bf58220f5a8b119) (const struct [device](structdevice.md) \*transport, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) proto, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) tx) |
|  | Request an SCMI channel dynamically. |
| static int | [scmi\_transport\_init](#a91d51238836162336350c3cdde8757ea) (const struct [device](structdevice.md) \*transport) |
|  | Perform initialization for the transport layer driver. |
| static int | [scmi\_transport\_setup\_chan](#a5b62be6ee7f3887c433774f2f5f0f660) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) tx) |
|  | Setup an SCMI channel. |
| static int | [scmi\_transport\_send\_message](#a98a6783dc94c460d3ff1be99e6906ba4) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, struct [scmi\_message](structscmi__message.md) \*msg) |
|  | Send an SCMI channel. |
| static int | [scmi\_transport\_read\_message](#abf042179f87393ce314cd13df00b097b) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan, struct [scmi\_message](structscmi__message.md) \*msg) |
|  | Read an SCMI message. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [scmi\_transport\_channel\_is\_free](#a3acea301a1e966324bd47ebac1b73cc9) (const struct [device](structdevice.md) \*transport, struct [scmi\_channel](structscmi__channel.md) \*chan) |
|  | Check if an SCMI channel is free. |
| int | [scmi\_core\_transport\_init](#a58dfdf0d4d0495babc6ef0d83974c1da) (const struct [device](structdevice.md) \*transport) |
|  | Perfrom SCMI core initialization. |

## Detailed Description

Public APIs for the SCMI transport layer drivers.

## Typedef Documentation

## [◆ ](#a2ae1a5afd4489cf4cf60bd45de2c6956)scmi\_channel\_cb

| typedef void(\* scmi\_channel\_cb) (struct [scmi\_channel](structscmi__channel.md) \*chan) |
| --- |

Callback function for message replies.

This function should be called by the transport layer driver whenever a reply to a previously sent message has been received. Its purpose is to notifying the SCMI core of the reply's arrival so that proper action can be taken.

Parameters
:   | chan | pointer to SCMI channel on which the reply arrived |
    | --- | --- |

## Function Documentation

## [◆ ](#a58dfdf0d4d0495babc6ef0d83974c1da)scmi\_core\_transport\_init()

| int scmi\_core\_transport\_init | ( | const struct [device](structdevice.md) \* | *transport* | ) |  |
| --- | --- | --- | --- | --- | --- |

Perfrom SCMI core initialization.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno code if failure |

## [◆ ](#a3acea301a1e966324bd47ebac1b73cc9)scmi\_transport\_channel\_is\_free()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) scmi\_transport\_channel\_is\_free | ( | const struct [device](structdevice.md) \* | *transport*, | | --- | --- | --- | --- | |  |  | struct [scmi\_channel](structscmi__channel.md) \* | *chan* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Check if an SCMI channel is free.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |
    | chan | pointer to SCMI channel the query is to be performed on |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno code if failure |

## [◆ ](#a91d51238836162336350c3cdde8757ea)scmi\_transport\_init()

| | int scmi\_transport\_init | ( | const struct [device](structdevice.md) \* | *transport* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Perform initialization for the transport layer driver.

The transport layer driver can't be initialized directly (i.e via a call to its init() function) during system initialization. This is because the macro used to define an SCMI transport places [scmi\_core\_transport\_init()](#a58dfdf0d4d0495babc6ef0d83974c1da) in the init section instead of the driver's init() function. As such, [scmi\_core\_transport\_init()](#a58dfdf0d4d0495babc6ef0d83974c1da) needs to call this function to perfrom transport layer driver initialization if required.

This operation is optional.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno code if failure |

## [◆ ](#abf042179f87393ce314cd13df00b097b)scmi\_transport\_read\_message()

| | int scmi\_transport\_read\_message | ( | const struct [device](structdevice.md) \* | *transport*, | | --- | --- | --- | --- | |  |  | struct [scmi\_channel](structscmi__channel.md) \* | *chan*, | |  |  | struct [scmi\_message](structscmi__message.md) \* | *msg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Read an SCMI message.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |
    | chan | pointer to SCMI channel on which the message is to be read |
    | msg | pointer to message the caller wishes to read |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno code if failure |

## [◆ ](#aa944ea05d5b9995e7bf58220f5a8b119)scmi\_transport\_request\_channel()

| | struct [scmi\_channel](structscmi__channel.md) \* scmi\_transport\_request\_channel | ( | const struct [device](structdevice.md) \* | *transport*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *proto*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *tx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Request an SCMI channel dynamically.

Whenever the SCMI transport layer driver doesn't support static channel allocation, the SCMI core will try to bind a channel to a protocol dynamically using this function. Note that no setup needs to be performed on the channel in this function as the core will also call the channel setup() function.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |
    | proto | ID of the protocol for which the core is requesting the channel |
    | tx | true if the channel is TX, false if RX |

Return values
:   | pointer | to SCMI channel that's to be bound to the protocol |
    | --- | --- |
    | NULL | if operation was not successful |

## [◆ ](#a98a6783dc94c460d3ff1be99e6906ba4)scmi\_transport\_send\_message()

| | int scmi\_transport\_send\_message | ( | const struct [device](structdevice.md) \* | *transport*, | | --- | --- | --- | --- | |  |  | struct [scmi\_channel](structscmi__channel.md) \* | *chan*, | |  |  | struct [scmi\_message](structscmi__message.md) \* | *msg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Send an SCMI channel.

Send an SCMI message using given SCMI channel. This function is not allowed to block.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |
    | chan | pointer to SCMI channel on which the message is to be sent |
    | msg | pointer to message the caller wishes to send |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno code if failure |

## [◆ ](#a5b62be6ee7f3887c433774f2f5f0f660)scmi\_transport\_setup\_chan()

| | int scmi\_transport\_setup\_chan | ( | const struct [device](structdevice.md) \* | *transport*, | | --- | --- | --- | --- | |  |  | struct [scmi\_channel](structscmi__channel.md) \* | *chan*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *tx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Setup an SCMI channel.

Before being able to send/receive messages, an SCMI channel needs to be prepared, which is what this function does. If it returns successfully, an SCMI protocol will be able to use this channel to send/receive messages.

Parameters
:   | transport | pointer to the device structure for the transport layer |
    | --- | --- |
    | chan | pointer to SCMI channel to be prepared |
    | tx | true if the channel is TX, false if RX |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno code if failure |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [transport.h](transport_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
