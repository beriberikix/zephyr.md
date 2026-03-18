---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structzbus__channel.html
original_path: doxygen/html/structzbus__channel.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| const char \*const | [name](#a9839e77746c53d24de69453aea53a233) |
|  | Channel name. |
| void \*const | [message](#a7e8bd8f6c080615a4c4d524101201f19) |
|  | Message reference. |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [message\_size](#a508bf72f7b47ad8781b4e4ef3645d17a) |
|  | Message size. |
| void \*const | [user\_data](#ae629044f9b6da800db5a628fc6789dfb) |
|  | User data available to extend zbus features. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*const | [validator](#a047e9da011488c8f11abdc1fd283f5f6) )(const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size) |
|  | Message validator. |
| struct [zbus\_channel\_data](structzbus__channel__data.md) \*const | [data](#a30ad5027b70d6e9d28d0b0caef3571fe) |
|  | Mutable channel data struct. |

## Detailed Description

Type used to represent a channel.

Every channel has a [zbus\_channel](structzbus__channel.md "Type used to represent a channel.") structure associated used to control the channel access and usage.

## Field Documentation

## [◆ ](#a30ad5027b70d6e9d28d0b0caef3571fe)data

| struct [zbus\_channel\_data](structzbus__channel__data.md)\* const zbus\_channel::data |
| --- |

Mutable channel data struct.

## [◆ ](#a7e8bd8f6c080615a4c4d524101201f19)message

| void\* const zbus\_channel::message |
| --- |

Message reference.

Represents the message's reference that points to the actual shared memory region.

## [◆ ](#a508bf72f7b47ad8781b4e4ef3645d17a)message\_size

| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) zbus\_channel::message\_size |
| --- |

Message size.

Represents the channel's message size.

## [◆ ](#a9839e77746c53d24de69453aea53a233)name

| const char\* const zbus\_channel::name |
| --- |

Channel name.

## [◆ ](#ae629044f9b6da800db5a628fc6789dfb)user\_data

| void\* const zbus\_channel::user\_data |
| --- |

User data available to extend zbus features.

The channel must be claimed before using this field.

## [◆ ](#a047e9da011488c8f11abdc1fd283f5f6)validator

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*const zbus\_channel::validator) (const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size) |
| --- |

Message validator.

Stores the reference to the function to check the message validity before actually performing the publishing. No invalid messages can be published. Every message is valid when this field is empty.

---

The documentation for this struct was generated from the following file:

- zephyr/zbus/[zbus.h](zbus_8h_source.md)

- [zbus\_channel](structzbus__channel.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
