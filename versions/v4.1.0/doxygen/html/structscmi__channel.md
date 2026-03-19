---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structscmi__channel.html
original_path: doxygen/html/structscmi__channel.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

scmi\_channel Struct Reference

SCMI channel structure.
[More...](#details)

`#include <[transport.h](transport_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_mutex](structk__mutex.md) | [lock](#a69391f18950bd0347585855a59897af8) |
|  | channel lock. |
| struct k\_sem | [sem](#a29fc109cdf2675e4d9ffde786b41664d) |
|  | binary semaphore. |
| void \* | [data](#a1b69c9d0c6b49f5496ad59270ab8f157) |
|  | channel private data |
| [scmi\_channel\_cb](transport_8h.md#a2ae1a5afd4489cf4cf60bd45de2c6956) | [cb](#a81065fcba9755ccf88c3ce372ded5d56) |
|  | callback function. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ready](#a26b9aff015d25d775818bfb7a28e4cdb) |
|  | is the channel ready to be used by a protocol? |

## Detailed Description

SCMI channel structure.

An SCMI channel is a medium through which a protocol is able to transmit/receive messages. Each of the SCMI channels is represented by a struct [scmi\_channel](structscmi__channel.md "SCMI channel structure.").

## Field Documentation

## [◆ ](#a81065fcba9755ccf88c3ce372ded5d56)cb

| [scmi\_channel\_cb](transport_8h.md#a2ae1a5afd4489cf4cf60bd45de2c6956) scmi\_channel::cb |
| --- |

callback function.

This is meant to be set by the SCMI core and should be called by the SCMI transport layer driver whenever a reply has been received.

## [◆ ](#a1b69c9d0c6b49f5496ad59270ab8f157)data

| void\* scmi\_channel::data |
| --- |

channel private data

## [◆ ](#a69391f18950bd0347585855a59897af8)lock

| struct [k\_mutex](structk__mutex.md) scmi\_channel::lock |
| --- |

channel lock.

This is meant to be initialized and used only by the SCMI core to assure that only one protocol can send/receive messages through a channel at a given moment.

## [◆ ](#a26b9aff015d25d775818bfb7a28e4cdb)ready

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) scmi\_channel::ready |
| --- |

is the channel ready to be used by a protocol?

## [◆ ](#a29fc109cdf2675e4d9ffde786b41664d)sem

| struct k\_sem scmi\_channel::sem |
| --- |

binary semaphore.

This is meant to be initialized and used only by the SCMI core. Its purpose is to signal that a reply has been received.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/scmi/[transport.h](transport_8h_source.md)

- [scmi\_channel](structscmi__channel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
