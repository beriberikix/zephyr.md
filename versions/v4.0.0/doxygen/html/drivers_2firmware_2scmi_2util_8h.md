---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2firmware_2scmi_2util_8h.html
original_path: doxygen/html/drivers_2firmware_2scmi_2util_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util.h File Reference

ARM SCMI utility header.
[More...](#details)

[Go to the source code of this file.](drivers_2firmware_2scmi_2util_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SCMI\_PROTOCOL\_NAME](#af302a6f14883fa949e87a6784bf965fa)(proto) |
|  | Build protocol name from its ID. |
| #define | [DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE](#a97f0ff25400cf66fd042c6448578e9c9)(node\_id) |
| #define | [DT\_SCMI\_PROTOCOL\_DATA\_DEFINE](#a3ff1291335a98908b7b39fd441240f3f)(node\_id, proto, pdata) |
| #define | [DT\_INST\_SCMI\_TRANSPORT\_DEFINE](#aff1d7e88df451d043dc2e4e9d39288b3)(inst, pm, data, config, level, prio, api) |
|  | Define an SCMI transport driver. |
| #define | [DT\_SCMI\_PROTOCOL\_DEFINE](#a49ca976673495b6c86d5ac278df6c4a6)(node\_id, init\_fn, pm, data, config, level, prio, api) |
|  | Define an SCMI protocol. |
| #define | [DT\_INST\_SCMI\_PROTOCOL\_DEFINE](#a702464dd535b0a58f7de037bfb295f11)(inst, init\_fn, pm, data, config, level, prio, api) |
|  | Just like [DT\_SCMI\_PROTOCOL\_DEFINE()](#a49ca976673495b6c86d5ac278df6c4a6), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |
| #define | [DT\_SCMI\_PROTOCOL\_DEFINE\_NODEV](#a831662a70b3055f31cb53a9460e6c3da)(node\_id, data) |
|  | Define an SCMI protocol with no device. |
| #define | [SCMI\_FIELD\_MAKE](#a21b369f9fa6d1a965ece4a589df88581)(x, mask, shift) |
|  | Create an SCMI message field. |
| #define | [SCMI\_PROTOCOL\_BASE](#aa7d5e12c8733162b93f2131fae0b9ff2)   16 |
|  | SCMI protocol IDs. |
| #define | [SCMI\_PROTOCOL\_POWER\_DOMAIN](#a7434da13fae02cd2e32b148c77258564)   17 |
| #define | [SCMI\_PROTOCOL\_SYSTEM](#ab54b9be92cad1d9e35c20ea578daff14)   18 |
| #define | [SCMI\_PROTOCOL\_PERF](#a516870afb06683cc717cd24f5ac70065)   19 |
| #define | [SCMI\_PROTOCOL\_CLOCK](#a69c4e6bc3b3a76fa86a4f25cfb0d9905)   20 |
| #define | [SCMI\_PROTOCOL\_SENSOR](#a50bd05b33b2b4915bd8e784542320d74)   21 |
| #define | [SCMI\_PROTOCOL\_RESET\_DOMAIN](#ab15815aabeb7f45670ec346144653f0e)   22 |
| #define | [SCMI\_PROTOCOL\_VOLTAGE\_DOMAIN](#ae8f54c2faae8340a25ddfb13789c7797)   23 |
| #define | [SCMI\_PROTOCOL\_PCAP\_MONITOR](#a4c6b58ea0571f9ef6bb2af29e23b0df8)   24 |
| #define | [SCMI\_PROTOCOL\_PINCTRL](#a48e1ebf3dbc53685127bccccc50977cb)   25 |

## Detailed Description

ARM SCMI utility header.

Contains various utility macros and macros used for protocol and transport "registration".

## Macro Definition Documentation

## [◆ ](#a702464dd535b0a58f7de037bfb295f11)DT\_INST\_SCMI\_PROTOCOL\_DEFINE

| #define DT\_INST\_SCMI\_PROTOCOL\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api* ) |

**Value:**

[DT\_SCMI\_PROTOCOL\_DEFINE](#a49ca976673495b6c86d5ac278df6c4a6)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(inst, DT\_DRV\_COMPAT), init\_fn, pm, \

data, config, level, prio, api)

[DT\_SCMI\_PROTOCOL\_DEFINE](#a49ca976673495b6c86d5ac278df6c4a6)

#define DT\_SCMI\_PROTOCOL\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api)

Define an SCMI protocol.

**Definition** util.h:211

[DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)

#define DT\_INST(inst, compat)

Get a node identifier for an instance of a compatible.

**Definition** devicetree.h:332

Just like [DT\_SCMI\_PROTOCOL\_DEFINE()](#a49ca976673495b6c86d5ac278df6c4a6), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier.

Parameters
:   | inst | instance number |
    | --- | --- |
    | init\_fn | pointer to protocol's initialization function |
    | api | pointer to protocol's subsystem API |
    | pm | pointer to the protocol's power management resources |
    | data | pointer to protocol's private data |
    | config | pointer to protocol's private constant data |
    | level | protocol initialization level |
    | prio | protocol's priority within its initialization level |

## [◆ ](#aff1d7e88df451d043dc2e4e9d39288b3)DT\_INST\_SCMI\_TRANSPORT\_DEFINE

| #define DT\_INST\_SCMI\_TRANSPORT\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api* ) |

**Value:**

[DEVICE\_DT\_INST\_DEFINE](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)(inst, &[scmi\_core\_transport\_init](transport_8h.md#a58dfdf0d4d0495babc6ef0d83974c1da), \

pm, data, config, level, prio, api)

[DEVICE\_DT\_INST\_DEFINE](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)

#define DEVICE\_DT\_INST\_DEFINE(inst,...)

Like DEVICE\_DT\_DEFINE(), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identif...

**Definition** device.h:221

[scmi\_core\_transport\_init](transport_8h.md#a58dfdf0d4d0495babc6ef0d83974c1da)

int scmi\_core\_transport\_init(const struct device \*transport)

Perfrom SCMI core initialization.

Define an SCMI transport driver.

This is merely a wrapper over [DEVICE\_DT\_INST\_DEFINE()](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419 "Like DEVICE_DT_DEFINE(), but uses an instance of a DT_DRV_COMPAT compatible instead of a node identif..."), but is required since transport layer drivers are not allowed to place their own init() function in the init section. Instead, transport layer drivers place the [scmi\_core\_transport\_init()](transport_8h.md#a58dfdf0d4d0495babc6ef0d83974c1da "Perfrom SCMI core initialization.") function in the init section, which, in turn, will call the transport layer driver init() function. This is required because the SCMI core needs to perform channel binding and setup during the transport layer driver's initialization.

## [◆ ](#a3ff1291335a98908b7b39fd441240f3f)DT\_SCMI\_PROTOCOL\_DATA\_DEFINE

| #define DT\_SCMI\_PROTOCOL\_DATA\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *proto*, |
|  |  |  | *pdata* ) |

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([scmi\_protocol](structscmi__protocol.md), [SCMI\_PROTOCOL\_NAME](#af302a6f14883fa949e87a6784bf965fa)(proto)) = \

{ \

.id = proto, \

.data = pdata, \

}

[SCMI\_PROTOCOL\_NAME](#af302a6f14883fa949e87a6784bf965fa)

#define SCMI\_PROTOCOL\_NAME(proto)

Build protocol name from its ID.

**Definition** util.h:29

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[scmi\_protocol](structscmi__protocol.md)

SCMI protocol structure.

**Definition** protocol.h:74

## [◆ ](#a49ca976673495b6c86d5ac278df6c4a6)DT\_SCMI\_PROTOCOL\_DEFINE

| #define DT\_SCMI\_PROTOCOL\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api* ) |

**Value:**

[DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE](#a97f0ff25400cf66fd042c6448578e9c9)(node\_id) \

DT\_SCMI\_PROTOCOL\_DATA\_DEFINE(node\_id, [DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(node\_id), data); \

DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, \

&[SCMI\_PROTOCOL\_NAME](#af302a6f14883fa949e87a6784bf965fa)([DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(node\_id)), \

config, level, prio, api)

[DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE](#a97f0ff25400cf66fd042c6448578e9c9)

#define DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE(node\_id)

**Definition** util.h:159

[DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)

#define DT\_REG\_ADDR\_RAW(node\_id)

Get a node's (only) register block raw address.

**Definition** devicetree.h:2400

Define an SCMI protocol.

This macro performs three important functions: 1) It defines a struct [scmi\_protocol](structscmi__protocol.md "SCMI protocol structure."), which is needed by all protocol drivers to work with the SCMI API.

2) It declares the static channels bound to the protocol. This is only applicable if the transport layer driver supports static channels.

3) It creates a struct [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") a sets the data field to the newly defined struct [scmi\_protocol](structscmi__protocol.md "SCMI protocol structure."). This is needed because the protocol driver needs to work with the SCMI API **and** the subsystem API.

Parameters
:   | node\_id | protocol node identifier |
    | --- | --- |
    | init\_fn | pointer to protocol's initialization function |
    | api | pointer to protocol's subsystem API |
    | pm | pointer to the protocol's power management resources |
    | data | pointer to protocol's private data |
    | config | pointer to protocol's private constant data |
    | level | protocol initialization level |
    | prio | protocol's priority within its initialization level |

## [◆ ](#a831662a70b3055f31cb53a9460e6c3da)DT\_SCMI\_PROTOCOL\_DEFINE\_NODEV

| #define DT\_SCMI\_PROTOCOL\_DEFINE\_NODEV | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

**Value:**

[DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE](#a97f0ff25400cf66fd042c6448578e9c9)(node\_id) \

DT\_SCMI\_PROTOCOL\_DATA\_DEFINE(node\_id, [DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(node\_id), data)

Define an SCMI protocol with no device.

Variant of [DT\_SCMI\_PROTOCOL\_DEFINE()](#a49ca976673495b6c86d5ac278df6c4a6), but no struct [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") is created and no initialization function is called during system initialization. This is useful for protocols that are not really part of a subsystem with an API (e.g: pinctrl).

Parameters
:   | node\_id | protocol node identifier |
    | --- | --- |
    | data | protocol private data |

## [◆ ](#a97f0ff25400cf66fd042c6448578e9c9)DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE

| #define DT\_SCMI\_TRANSPORT\_CHANNELS\_DECLARE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a21b369f9fa6d1a965ece4a589df88581)SCMI\_FIELD\_MAKE

| #define SCMI\_FIELD\_MAKE | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *shift* ) |

**Value:**

((([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(x) & (mask)) << (shift))

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Create an SCMI message field.

Data might not necessarily be encoded in the first x bits of an SCMI message parameter/return value. This comes in handy when building said parameters/ return values.

Parameters
:   | x | value to encode |
    | --- | --- |
    | mask | value to perform bitwise-and with x |
    | shift | value to left-shift masked x |

## [◆ ](#aa7d5e12c8733162b93f2131fae0b9ff2)SCMI\_PROTOCOL\_BASE

| #define SCMI\_PROTOCOL\_BASE   16 |
| --- |

SCMI protocol IDs.

Each SCMI protocol is identified by an ID. Each of these IDs needs to be in decimal since they might be used to build protocol and static channel names.

## [◆ ](#a69c4e6bc3b3a76fa86a4f25cfb0d9905)SCMI\_PROTOCOL\_CLOCK

| #define SCMI\_PROTOCOL\_CLOCK   20 |
| --- |

## [◆ ](#af302a6f14883fa949e87a6784bf965fa)SCMI\_PROTOCOL\_NAME

| #define SCMI\_PROTOCOL\_NAME | ( |  | *proto* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(scmi\_protocol\_, proto)

[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)

#define CONCAT(...)

Concatenate input arguments.

**Definition** util.h:311

Build protocol name from its ID.

Given a protocol ID, this macro builds the protocol name. This is done by concatenating the scmi\_protocol\_ construct with the given protocol ID.

Parameters
:   | proto | protocol ID in decimal format |
    | --- | --- |

Returns
:   protocol name

## [◆ ](#a4c6b58ea0571f9ef6bb2af29e23b0df8)SCMI\_PROTOCOL\_PCAP\_MONITOR

| #define SCMI\_PROTOCOL\_PCAP\_MONITOR   24 |
| --- |

## [◆ ](#a516870afb06683cc717cd24f5ac70065)SCMI\_PROTOCOL\_PERF

| #define SCMI\_PROTOCOL\_PERF   19 |
| --- |

## [◆ ](#a48e1ebf3dbc53685127bccccc50977cb)SCMI\_PROTOCOL\_PINCTRL

| #define SCMI\_PROTOCOL\_PINCTRL   25 |
| --- |

## [◆ ](#a7434da13fae02cd2e32b148c77258564)SCMI\_PROTOCOL\_POWER\_DOMAIN

| #define SCMI\_PROTOCOL\_POWER\_DOMAIN   17 |
| --- |

## [◆ ](#ab15815aabeb7f45670ec346144653f0e)SCMI\_PROTOCOL\_RESET\_DOMAIN

| #define SCMI\_PROTOCOL\_RESET\_DOMAIN   22 |
| --- |

## [◆ ](#a50bd05b33b2b4915bd8e784542320d74)SCMI\_PROTOCOL\_SENSOR

| #define SCMI\_PROTOCOL\_SENSOR   21 |
| --- |

## [◆ ](#ab54b9be92cad1d9e35c20ea578daff14)SCMI\_PROTOCOL\_SYSTEM

| #define SCMI\_PROTOCOL\_SYSTEM   18 |
| --- |

## [◆ ](#ae8f54c2faae8340a25ddfb13789c7797)SCMI\_PROTOCOL\_VOLTAGE\_DOMAIN

| #define SCMI\_PROTOCOL\_VOLTAGE\_DOMAIN   23 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [util.h](drivers_2firmware_2scmi_2util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
