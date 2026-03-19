---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmqtt__sn__transport.html
original_path: doxygen/html/structmqtt__sn__transport.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sn\_transport Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT-SN Client library](group__mqtt__sn__socket.md)

Structure to describe an MQTT-SN transport.
[More...](#details)

`#include <[mqtt_sn.h](mqtt__sn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#a3486cb5d56fb42db4c1f62ef9a6bb75b) )(struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport) |
|  | Will be called once on client init to initialize the transport. |
| void(\* | [deinit](#af51e433970bed12b5217c63416d0ec4c) )(struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport) |
|  | Will be called on client deinit. |
| int(\* | [sendto](#a0066c1c874d11ee5f998b04f86abaa21) )(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz, const void \*dest\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) addrlen) |
|  | Will be called by the library when it wants to send a message. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [recvfrom](#af92bfdb3f4a3850a7389a4f048bb12ec) )(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*rx\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rx\_len, void \*src\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*addrlen) |
|  | Will be called by the library when it wants to receive a message. |
| int(\* | [poll](#abe102ec52b34f767d0b231e93bedd0a9) )(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Check if incoming data is available. |

## Detailed Description

Structure to describe an MQTT-SN transport.

MQTT-SN does not require transports to be reliable or to hold a connection. Transports just need to be frame-based, so you can use UDP, ZigBee, or even a simple UART, given some kind of framing protocol is used.

## Field Documentation

## [◆ ](#af51e433970bed12b5217c63416d0ec4c)deinit

| void(\* mqtt\_sn\_transport::deinit) (struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport) |
| --- |

Will be called on client deinit.

Use this to close sockets or similar. May be NULL.

## [◆ ](#a3486cb5d56fb42db4c1f62ef9a6bb75b)init

| int(\* mqtt\_sn\_transport::init) (struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport) |
| --- |

Will be called once on client init to initialize the transport.

Use this to open sockets or similar. May be NULL.

## [◆ ](#abe102ec52b34f767d0b231e93bedd0a9)poll

| int(\* mqtt\_sn\_transport::poll) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
| --- |

Check if incoming data is available.

If [poll()](#abe102ec52b34f767d0b231e93bedd0a9) returns a positive number, recv must not block.

May be NULL, but recv should not block then either.

Returns
:   Positive number if data is available, or zero if there is none. Negative values signal errors.

## [◆ ](#af92bfdb3f4a3850a7389a4f048bb12ec)recvfrom

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* mqtt\_sn\_transport::recvfrom) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*rx\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rx\_len, void \*src\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*addrlen) |
| --- |

Will be called by the library when it wants to receive a message.

Implementations should follow recvfrom conventions with the exception of a NULL src\_addr being a broadcast message.

## [◆ ](#a0066c1c874d11ee5f998b04f86abaa21)sendto

| int(\* mqtt\_sn\_transport::sendto) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz, const void \*dest\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) addrlen) |
| --- |

Will be called by the library when it wants to send a message.

Implementations should follow sendto conventions with exceptions. When dest\_addr == NULL, message should be broadcast with addrlen being the broadcast radius. This should also handle setting up/destroying connections as required when the address changes.

Returns
:   ENOERR on connection+transmission success, Negative values signal errors.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt\_sn.h](mqtt__sn_8h_source.md)

- [mqtt\_sn\_transport](structmqtt__sn__transport.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
