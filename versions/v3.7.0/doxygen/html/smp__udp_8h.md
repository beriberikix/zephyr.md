---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/smp__udp_8h.html
original_path: doxygen/html/smp__udp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_udp.h File Reference

UDP transport for the MCUmgr SMP protocol.
[More...](#details)

[Go to the source code of this file.](smp__udp_8h_source.md)

| Functions | |
| --- | --- |
| int | [smp\_udp\_open](#a768f36cea02d7d7781113d36516e1763) (void) |
|  | Enables the UDP SMP MCUmgr transport thread(s) which will open a socket and listen to requests. |
| int | [smp\_udp\_close](#add428f3ed2ae0d9e580e45897a98a293) (void) |
|  | Disables the UDP SMP MCUmgr transport thread(s) which will close open sockets. |

## Detailed Description

UDP transport for the MCUmgr SMP protocol.

## Function Documentation

## [◆ ](#add428f3ed2ae0d9e580e45897a98a293)smp\_udp\_close()

| int smp\_udp\_close | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Disables the UDP SMP MCUmgr transport thread(s) which will close open sockets.

Note
:   API is not thread safe.

Returns
:   0 on success
:   -errno code on failure.

## [◆ ](#a768f36cea02d7d7781113d36516e1763)smp\_udp\_open()

| int smp\_udp\_open | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Enables the UDP SMP MCUmgr transport thread(s) which will open a socket and listen to requests.

Note
:   API is not thread safe.

Returns
:   0 on success
:   -errno code on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_udp.h](smp__udp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
