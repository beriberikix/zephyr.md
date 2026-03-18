---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structethernet__qbv__param.html
original_path: doxygen/html/structethernet__qbv__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_qbv\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet Qbv specific parameters.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [port\_id](#a037492458f47905b894a2269ff7365cd) |
|  | Port id. |
| enum ethernet\_qbv\_param\_type | [type](#a2184250d397bd749764adc52ec3a1621) |
|  | Type of Qbv parameter. |
| enum ethernet\_qbv\_state\_type | [state](#a36702c57bea42c37c1341e144ced4f7d) |
|  | What state (Admin/Oper) parameters are these. |
| union { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [enabled](#a0742dbe52f01addbb319e2fcb354d064) |  |
|  | True if Qbv is enabled or not. [More...](#a0742dbe52f01addbb319e2fcb354d064) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [gate\_status](#a44b6ce52faeae761c5ebe49fad5338cd) [NET\_TC\_TX\_COUNT] |  |
|  | True = open, False = closed. [More...](#a44b6ce52faeae761c5ebe49fad5338cd) |
| enum ethernet\_gate\_state\_operation   [operation](#a8471f7eb20a72bb16fe7abb0b2bb24f7) |  |
|  | GateState operation. [More...](#a8471f7eb20a72bb16fe7abb0b2bb24f7) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [time\_interval](#aa6b2be0014988752e326bdc1fe6ef161) |  |
|  | Time interval ticks (nanoseconds). [More...](#aa6b2be0014988752e326bdc1fe6ef161) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [row](#a2c256aa3f65dfa75434752903daa809c) |  |
|  | Gate control list row. [More...](#a2c256aa3f65dfa75434752903daa809c) |
| }   [gate\_control](#aa61778228274884ee782e017840acba9) |
|  | Gate control information. [More...](#aa61778228274884ee782e017840acba9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [gate\_control\_list\_len](#afc0c26fcdeee1a921a2f549de4d1c33e) |  |
|  | Number of entries in gate control list. [More...](#afc0c26fcdeee1a921a2f549de4d1c33e) |
| struct { |  |
| struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md)   [base\_time](#a53646a44e8b0e1f6588c357d49d97693) |  |
|  | Base time. [More...](#a53646a44e8b0e1f6588c357d49d97693) |
| struct [net\_ptp\_time](structnet__ptp__time.md)   [cycle\_time](#ad07589ae6802a9c3c4c3f809427129be) |  |
|  | Cycle time. [More...](#ad07589ae6802a9c3c4c3f809427129be) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [extension\_time](#a76220e58aa31ae6cfd92268277716c7a) |  |
|  | Extension time (nanoseconds). [More...](#a76220e58aa31ae6cfd92268277716c7a) |
| } |  |
|  | The time values are set in one go when type is set to ETHERNET\_QBV\_PARAM\_TYPE\_TIME. |
| }; |  |

## Detailed Description

Ethernet Qbv specific parameters.

## Field Documentation

## [◆ ](#ad73551774ab553a7fce96407968280e3)[union]

| union { ... } [ethernet\_qbv\_param](structethernet__qbv__param.md) |
| --- |

## [◆ ](#a53646a44e8b0e1f6588c357d49d97693)base\_time

| struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) ethernet\_qbv\_param::base\_time |
| --- |

Base time.

## [◆ ](#ad07589ae6802a9c3c4c3f809427129be)cycle\_time

| struct [net\_ptp\_time](structnet__ptp__time.md) ethernet\_qbv\_param::cycle\_time |
| --- |

Cycle time.

## [◆ ](#a0742dbe52f01addbb319e2fcb354d064)enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_qbv\_param::enabled |
| --- |

True if Qbv is enabled or not.

## [◆ ](#a76220e58aa31ae6cfd92268277716c7a)extension\_time

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ethernet\_qbv\_param::extension\_time |
| --- |

Extension time (nanoseconds).

## [◆ ](#aa61778228274884ee782e017840acba9)[struct]

| struct { ... } ethernet\_qbv\_param::gate\_control |
| --- |

Gate control information.

## [◆ ](#afc0c26fcdeee1a921a2f549de4d1c33e)gate\_control\_list\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ethernet\_qbv\_param::gate\_control\_list\_len |
| --- |

Number of entries in gate control list.

## [◆ ](#a44b6ce52faeae761c5ebe49fad5338cd)gate\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_qbv\_param::gate\_status[NET\_TC\_TX\_COUNT] |
| --- |

True = open, False = closed.

## [◆ ](#a8471f7eb20a72bb16fe7abb0b2bb24f7)operation

| enum ethernet\_gate\_state\_operation ethernet\_qbv\_param::operation |
| --- |

GateState operation.

## [◆ ](#a037492458f47905b894a2269ff7365cd)port\_id

| int ethernet\_qbv\_param::port\_id |
| --- |

Port id.

## [◆ ](#a2c256aa3f65dfa75434752903daa809c)row

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ethernet\_qbv\_param::row |
| --- |

Gate control list row.

## [◆ ](#a36702c57bea42c37c1341e144ced4f7d)state

| enum ethernet\_qbv\_state\_type ethernet\_qbv\_param::state |
| --- |

What state (Admin/Oper) parameters are these.

## [◆ ](#aa6b2be0014988752e326bdc1fe6ef161)time\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ethernet\_qbv\_param::time\_interval |
| --- |

Time interval ticks (nanoseconds).

## [◆ ](#a2184250d397bd749764adc52ec3a1621)type

| enum ethernet\_qbv\_param\_type ethernet\_qbv\_param::type |
| --- |

Type of Qbv parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_qbv\_param](structethernet__qbv__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
