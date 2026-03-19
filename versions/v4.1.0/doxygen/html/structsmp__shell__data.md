---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsmp__shell__data.html
original_path: doxygen/html/structsmp__shell__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_shell\_data Struct Reference

Data used by SMP shell.
[More...](#details)

`#include <[smp_shell.h](smp__shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_buf\_pool](structnet__buf__pool.md) \* | [buf\_pool](#a67997e0400ee096e98781b839df3d6c2) |
| struct [k\_fifo](structk__fifo.md) | [buf\_ready](#a3e15c83e64e1cab0f14141d2a6dd7bed) |
| struct [net\_buf](structnet__buf.md) \* | [buf](#a281058a6cb23102af46cb0457c3a3232) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [esc\_state](#aea6798b62094c9d3bcc3dc6926800af4) |

## Detailed Description

Data used by SMP shell.

## Field Documentation

## [◆ ](#a281058a6cb23102af46cb0457c3a3232)buf

| struct [net\_buf](structnet__buf.md)\* smp\_shell\_data::buf |
| --- |

## [◆ ](#a67997e0400ee096e98781b839df3d6c2)buf\_pool

| struct [net\_buf\_pool](structnet__buf__pool.md)\* smp\_shell\_data::buf\_pool |
| --- |

## [◆ ](#a3e15c83e64e1cab0f14141d2a6dd7bed)buf\_ready

| struct [k\_fifo](structk__fifo.md) smp\_shell\_data::buf\_ready |
| --- |

## [◆ ](#aea6798b62094c9d3bcc3dc6926800af4)esc\_state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) smp\_shell\_data::esc\_state |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/transport/[smp\_shell.h](smp__shell_8h_source.md)

- [smp\_shell\_data](structsmp__shell__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
