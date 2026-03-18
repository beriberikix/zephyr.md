---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structonoff__transitions.html
original_path: doxygen/html/structonoff__transitions.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff\_transitions Struct Reference

[Kernel APIs](group__kernel__apis.md) » [On-Off Service APIs](group__resource__mgmt__onoff__apis.md)

On-off service transition functions.
[More...](#details)

`#include <[onoff.h](onoff_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) | [start](#a86417dd542c8f259ad1fc1c7d3c26545) |
|  | Function to invoke to transition the service to on. |
| [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) | [stop](#a91a1805daabae70d362441634bfa508d) |
|  | Function to invoke to transition the service to off. |
| [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) | [reset](#a335d7d2f8418e78b237cfb4199b6f6aa) |
|  | Function to force the service state to reset, where supported. |

## Detailed Description

On-off service transition functions.

## Field Documentation

## [◆ ](#a335d7d2f8418e78b237cfb4199b6f6aa)reset

| [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) onoff\_transitions::reset |
| --- |

Function to force the service state to reset, where supported.

## [◆ ](#a86417dd542c8f259ad1fc1c7d3c26545)start

| [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) onoff\_transitions::start |
| --- |

Function to invoke to transition the service to on.

## [◆ ](#a91a1805daabae70d362441634bfa508d)stop

| [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) onoff\_transitions::stop |
| --- |

Function to invoke to transition the service to off.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[onoff.h](onoff_8h_source.md)

- [onoff\_transitions](structonoff__transitions.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
