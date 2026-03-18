---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structethernet__qbu__param.html
original_path: doxygen/html/structethernet__qbu__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_qbu\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [port\_id](#ae6d61f0c9d2f2e56eb494db953a5e846) |
|  | Port id. |
| enum ethernet\_qbu\_param\_type | [type](#a4a8a3d26a12a06a787ae6b35ea40c37a) |
|  | Type of Qbu parameter. |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [hold\_advance](#a8ffde09a540817b7a68c7180c327196f) |  |
|  | Hold advance (nanoseconds). [More...](#a8ffde09a540817b7a68c7180c327196f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [release\_advance](#a3f62d0462376225c8609c7e26ebd314b) |  |
|  | Release advance (nanoseconds). [More...](#a3f62d0462376225c8609c7e26ebd314b) |
| enum ethernet\_qbu\_preempt\_status   [frame\_preempt\_statuses](#a3f5dfd9cfbc1ec86896eaf517bdc5c88) [NET\_TC\_TX\_COUNT] |  |
|  | sequence of framePreemptionAdminStatus values. [More...](#a3f5dfd9cfbc1ec86896eaf517bdc5c88) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [enabled](#a9717dd68adde62a454593d72fdbc43a5) |  |
|  | True if Qbu is enabled or not. [More...](#a9717dd68adde62a454593d72fdbc43a5) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [link\_partner\_status](#ad8c92a7f7b4aa124adaa62dd4e65b5ca) |  |
|  | Link partner status (from Qbr). [More...](#ad8c92a7f7b4aa124adaa62dd4e65b5ca) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [additional\_fragment\_size](#afb455507b29d84de42638e47ecacadeb): 2 |  |
|  | Additional fragment size (from Qbr). [More...](#afb455507b29d84de42638e47ecacadeb) |
| }; |  |

## Field Documentation

## [◆ ](#a3328a350c9df03422fe8efce5ddef2e3)[union]

| union { ... } [ethernet\_qbu\_param](structethernet__qbu__param.md) |
| --- |

## [◆ ](#afb455507b29d84de42638e47ecacadeb)additional\_fragment\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ethernet\_qbu\_param::additional\_fragment\_size |
| --- |

Additional fragment size (from Qbr).

The minimum non-final fragment size is (additional\_fragment\_size + 1) \* 64 octets

## [◆ ](#a9717dd68adde62a454593d72fdbc43a5)enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_qbu\_param::enabled |
| --- |

True if Qbu is enabled or not.

## [◆ ](#a3f5dfd9cfbc1ec86896eaf517bdc5c88)frame\_preempt\_statuses

| enum ethernet\_qbu\_preempt\_status ethernet\_qbu\_param::frame\_preempt\_statuses[NET\_TC\_TX\_COUNT] |
| --- |

sequence of framePreemptionAdminStatus values.

## [◆ ](#a8ffde09a540817b7a68c7180c327196f)hold\_advance

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ethernet\_qbu\_param::hold\_advance |
| --- |

Hold advance (nanoseconds).

## [◆ ](#ad8c92a7f7b4aa124adaa62dd4e65b5ca)link\_partner\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_qbu\_param::link\_partner\_status |
| --- |

Link partner status (from Qbr).

## [◆ ](#ae6d61f0c9d2f2e56eb494db953a5e846)port\_id

| int ethernet\_qbu\_param::port\_id |
| --- |

Port id.

## [◆ ](#a3f62d0462376225c8609c7e26ebd314b)release\_advance

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ethernet\_qbu\_param::release\_advance |
| --- |

Release advance (nanoseconds).

## [◆ ](#a4a8a3d26a12a06a787ae6b35ea40c37a)type

| enum ethernet\_qbu\_param\_type ethernet\_qbu\_param::type |
| --- |

Type of Qbu parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_qbu\_param](structethernet__qbu__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
