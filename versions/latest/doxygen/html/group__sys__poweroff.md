---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__sys__poweroff.html
original_path: doxygen/html/group__sys__poweroff.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

System power off

[Operating System Services](group__os__services.md)

| Functions | |
| --- | --- |
| FUNC\_NORETURN void | [sys\_poweroff](#gaf4552a8ea40b4adb94f85b0a1ff06e39) (void) |
|  | Perform a system power off. |

## Detailed Description

## Function Documentation

## [◆ ](#gaf4552a8ea40b4adb94f85b0a1ff06e39)sys\_poweroff()

| FUNC\_NORETURN void sys\_poweroff | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[poweroff.h](poweroff_8h.md)>`

Perform a system power off.

This function will perform an immediate power off of the system. It is the responsability of the caller to ensure that the system is in a safe state to be powered off. Any required wake up sources must be enabled before calling this function.

`CONFIG_POWEROFF` needs to be enabled to use this API.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
