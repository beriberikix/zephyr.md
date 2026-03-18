---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__traffic__class.html
original_path: doxygen/html/structnet__traffic__class.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_traffic\_class Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network traffic class.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_fifo](structk__fifo.md) | [fifo](#a94511ca12bad1687f5c7ca862c857ded) |
|  | Fifo for handling this Tx or Rx packet. |
| struct [k\_thread](structk__thread.md) | [handler](#a8d0023588fee0a8ff1381bbc80ada143) |
|  | Traffic class handler thread. |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [stack](#a2d98bc68d38bdef649d645b8b52516c5) |
|  | Stack for this handler. |

## Detailed Description

Network traffic class.

Traffic classes are used when sending or receiving data that is classified with different priorities. So some traffic can be marked as high priority and it will be sent or received first. Each network packet that is transmitted or received goes through a fifo to a thread that will transmit it.

## Field Documentation

## [◆ ](#a94511ca12bad1687f5c7ca862c857ded)fifo

| struct [k\_fifo](structk__fifo.md) net\_traffic\_class::fifo |
| --- |

Fifo for handling this Tx or Rx packet.

## [◆ ](#a8d0023588fee0a8ff1381bbc80ada143)handler

| struct [k\_thread](structk__thread.md) net\_traffic\_class::handler |
| --- |

Traffic class handler thread.

## [◆ ](#a2d98bc68d38bdef649d645b8b52516c5)stack

| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)\* net\_traffic\_class::stack |
| --- |

Stack for this handler.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_traffic\_class](structnet__traffic__class.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
