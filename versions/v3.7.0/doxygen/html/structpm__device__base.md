---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpm__device__base.html
original_path: doxygen/html/structpm__device__base.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_device\_base Struct Reference

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [Device](group__subsys__pm__device.md)

Device PM info.
[More...](#details)

`#include <[device.h](pm_2device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#af9a24c7aaa0425b335fe147908c1fd4d) |
|  | Device PM status flags. |
| enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) | [state](#af4c9ef16800538148dcfa1d93b69bccb) |
|  | Device power state. |
| [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179) | [action\_cb](#abd3a07f0e7c54cb0bee7f835be79dac6) |
|  | Device PM action callback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [usage](#a4a9eeb093de1b1e60222b25a06a6361d) |
|  | Device usage count. |

## Detailed Description

Device PM info.

Structure holds fields which are common for two PM devices: generic and synchronous.

## Field Documentation

## [◆ ](#abd3a07f0e7c54cb0bee7f835be79dac6)action\_cb

| [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179) pm\_device\_base::action\_cb |
| --- |

Device PM action callback.

## [◆ ](#af9a24c7aaa0425b335fe147908c1fd4d)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) pm\_device\_base::flags |
| --- |

Device PM status flags.

## [◆ ](#af4c9ef16800538148dcfa1d93b69bccb)state

| enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) pm\_device\_base::state |
| --- |

Device power state.

## [◆ ](#a4a9eeb093de1b1e60222b25a06a6361d)usage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pm\_device\_base::usage |
| --- |

Device usage count.

---

The documentation for this struct was generated from the following file:

- zephyr/pm/[device.h](pm_2device_8h_source.md)

- [pm\_device\_base](structpm__device__base.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
