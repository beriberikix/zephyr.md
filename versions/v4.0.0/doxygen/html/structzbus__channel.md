---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structzbus__channel.html
original_path: doxygen/html/structzbus__channel.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zbus\_channel Struct Reference

[Operating System Services](group__os__services.md) » [Zbus APIs](group__zbus__apis.md)

Type used to represent a channel.
[More...](#details)

`#include <[zbus.h](zbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#ab8e66cdcfd2429058ca86e6af3813e03) |
|  | Channel name. |
| void \* | [message](#abc00c2ed80b4ce3a0ea7304f43f30d08) |
|  | Message reference. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [message\_size](#ab7f330f3d70774afeebb74cc03f90d34) |
|  | Message size. |
| void \* | [user\_data](#a34864d7da9816955a41caf2a8355f3f0) |
|  | User data available to extend zbus features. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [validator](#a90558613c362e75aa621cb240b178138) )(const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size) |
|  | Message validator. |
| struct [zbus\_channel\_data](structzbus__channel__data.md) \* | [data](#a5588983f2aefce2dd7cffad564c68d16) |
|  | Mutable channel data struct. |

## Detailed Description

Type used to represent a channel.

Every channel has a [zbus\_channel](structzbus__channel.md "Type used to represent a channel.") structure associated used to control the channel access and usage.

## Field Documentation

## [◆ ](#a5588983f2aefce2dd7cffad564c68d16)data

| struct [zbus\_channel\_data](structzbus__channel__data.md)\* zbus\_channel::data |
| --- |

Mutable channel data struct.

## [◆ ](#abc00c2ed80b4ce3a0ea7304f43f30d08)message

| void\* zbus\_channel::message |
| --- |

Message reference.

Represents the message's reference that points to the actual shared memory region.

## [◆ ](#ab7f330f3d70774afeebb74cc03f90d34)message\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) zbus\_channel::message\_size |
| --- |

Message size.

Represents the channel's message size.

## [◆ ](#ab8e66cdcfd2429058ca86e6af3813e03)name

| const char\* zbus\_channel::name |
| --- |

Channel name.

## [◆ ](#a34864d7da9816955a41caf2a8355f3f0)user\_data

| void\* zbus\_channel::user\_data |
| --- |

User data available to extend zbus features.

The channel must be claimed before using this field.

## [◆ ](#a90558613c362e75aa621cb240b178138)validator

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* zbus\_channel::validator) (const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size) |
| --- |

Message validator.

Stores the reference to the function to check the message validity before actually performing the publishing. No invalid messages can be published. Every message is valid when this field is empty.

---

The documentation for this struct was generated from the following file:

- zephyr/zbus/[zbus.h](zbus_8h_source.md)

- [zbus\_channel](structzbus__channel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
