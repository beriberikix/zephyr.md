---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structzbus__observer.html
original_path: doxygen/html/structzbus__observer.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| const char \* | [name](#ad9d31821d69e181f28e80e5eedf5a331) |
|  | Observer name. |
| enum [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) | [type](#a0251cf9bdca418b6b8123b998b57efe2) |
|  | Type indication. |
| struct [zbus\_observer\_data](structzbus__observer__data.md) \* | [data](#abdca15310be41ea2ce1ae3bbe0ebabb7) |
|  | Mutable observer data struct. |
| union { |  |
| struct [k\_msgq](structk__msgq.md) \*   [queue](#ac03ca78cff09b9466cbe34921862d27c) |  |
|  | Observer message queue. [More...](#ac03ca78cff09b9466cbe34921862d27c) |
| void(\*   [callback](#a78037ed7bcba26af33b6221bf7e4f9d2) )(const struct [zbus\_channel](structzbus__channel.md) \*chan) |  |
|  | Observer callback function. [More...](#a78037ed7bcba26af33b6221bf7e4f9d2) |
| struct [k\_fifo](structk__fifo.md) \*   [message\_fifo](#a3594b07a2573e03b18ca640809ffd3fa) |  |
|  | Observer message FIFO. [More...](#a3594b07a2573e03b18ca640809ffd3fa) |
| }; |  |

## Detailed Description

Type used to represent an observer.

Every observer has an representation structure containing the relevant information. An observer is a code portion interested in some channel. The observer can be notified synchronously or asynchronously and it is called listener and subscriber respectively. The observer can be enabled or disabled during runtime by change the enabled boolean field of the structure. The listeners have a callback function that is executed by the bus with the index of the changed channel as argument when the notification is sent. The subscribers have a message queue where the bus enqueues the index of the changed channel when a notification is sent.

See also
:   [zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349 "Change the observer state.") function to properly change the observer'[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) enabled field.

## Field Documentation

## [◆ ](#acd175a11109ab0675fc9150e3829105e)[union]

| union { ... } [zbus\_observer](structzbus__observer.md) |
| --- |

## [◆ ](#a78037ed7bcba26af33b6221bf7e4f9d2)callback

| void(\* zbus\_observer::callback) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
| --- |

Observer callback function.

It turns the observer into a listener.

## [◆ ](#abdca15310be41ea2ce1ae3bbe0ebabb7)data

| struct [zbus\_observer\_data](structzbus__observer__data.md)\* zbus\_observer::data |
| --- |

Mutable observer data struct.

## [◆ ](#a3594b07a2573e03b18ca640809ffd3fa)message\_fifo

| struct [k\_fifo](structk__fifo.md)\* zbus\_observer::message\_fifo |
| --- |

Observer message FIFO.

It turns the observer into a message subscriber. It only exists if the `CONFIG_ZBUS_MSG_SUBSCRIBER` is enabled.

## [◆ ](#ad9d31821d69e181f28e80e5eedf5a331)name

| const char\* zbus\_observer::name |
| --- |

Observer name.

## [◆ ](#ac03ca78cff09b9466cbe34921862d27c)queue

| struct [k\_msgq](structk__msgq.md)\* zbus\_observer::queue |
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
