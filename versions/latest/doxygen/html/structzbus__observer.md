---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structzbus__observer.html
original_path: doxygen/html/structzbus__observer.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zbus\_observer Struct Reference

[Operating System Services](group__os__services.md) » [Zbus APIs](group__zbus__apis.md)

Type used to represent an observer.
[More...](#details)

`#include <[zbus.h](zbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \*const | [name](#ab2ba28a935b528b2db90389071769fd5) |
|  | Observer name. |
| enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) | [type](#a0251cf9bdca418b6b8123b998b57efe2) |
|  | Type indication. |
| struct [zbus\_observer\_data](structzbus__observer__data.md) \*const | [data](#a76bbaaf17ce0c58bfa9f9b604cbb496d) |
|  | Mutable observer data struct. |
| union { |  |
| struct [k\_msgq](structk__msgq.md) \*const   [queue](#a7da8da6038d3dad4bc4c05279c28310c) |  |
|  | Observer message queue. [More...](#a7da8da6038d3dad4bc4c05279c28310c) |
| void(\*const   [callback](#a71fe83641f3e8c6248602150cbd998a1) )(const struct [zbus\_channel](structzbus__channel.md) \*chan) |  |
|  | Observer callback function. [More...](#a71fe83641f3e8c6248602150cbd998a1) |
| struct [k\_fifo](structk__fifo.md) \*const   [message\_fifo](#a9073bc59a4662385d6c5d487e7be03c9) |  |
|  | Observer message FIFO. [More...](#a9073bc59a4662385d6c5d487e7be03c9) |
| }; |  |

## Detailed Description

Type used to represent an observer.

Every observer has an representation structure containing the relevant information. An observer is a code portion interested in some channel. The observer can be notified synchronously or asynchronously and it is called listener and subscriber respectively. The observer can be enabled or disabled during runtime by change the enabled boolean field of the structure. The listeners have a callback function that is executed by the bus with the index of the changed channel as argument when the notification is sent. The subscribers have a message queue where the bus enqueues the index of the changed channel when a notification is sent.

See also
:   [zbus\_obs\_set\_enable](group__zbus__apis.md#ga6b44a887c82cbceff3136bbd9e0aa91c "Change the observer state.") function to properly change the observer'[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) enabled field.

## Field Documentation

## [◆ ](#acd175a11109ab0675fc9150e3829105e)[union]

| union { ... } [zbus\_observer](structzbus__observer.md) |
| --- |

## [◆ ](#a71fe83641f3e8c6248602150cbd998a1)callback

| void(\*const zbus\_observer::callback) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
| --- |

Observer callback function.

It turns the observer into a listener.

## [◆ ](#a76bbaaf17ce0c58bfa9f9b604cbb496d)data

| struct [zbus\_observer\_data](structzbus__observer__data.md)\* const zbus\_observer::data |
| --- |

Mutable observer data struct.

## [◆ ](#a9073bc59a4662385d6c5d487e7be03c9)message\_fifo

| struct [k\_fifo](structk__fifo.md)\* const zbus\_observer::message\_fifo |
| --- |

Observer message FIFO.

It turns the observer into a message subscriber. It only exists if the `CONFIG_ZBUS_MSG_SUBSCRIBER` is enabled.

## [◆ ](#ab2ba28a935b528b2db90389071769fd5)name

| const char\* const zbus\_observer::name |
| --- |

Observer name.

## [◆ ](#a7da8da6038d3dad4bc4c05279c28310c)queue

| struct [k\_msgq](structk__msgq.md)\* const zbus\_observer::queue |
| --- |

Observer message queue.

It turns the observer into a subscriber.

## [◆ ](#a0251cf9bdca418b6b8123b998b57efe2)type

| enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) zbus\_observer::type |
| --- |

Type indication.

---

The documentation for this struct was generated from the following file:

- zephyr/zbus/[zbus.h](zbus_8h_source.md)

- [zbus\_observer](structzbus__observer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
