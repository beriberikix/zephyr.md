---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtftp__evt.html
original_path: doxygen/html/structtftp__evt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tftp\_evt Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [TFTP Client library](group__tftp__client.md)

Defines TFTP asynchronous event notified to the application.
[More...](#details)

`#include <[tftp.h](tftp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [tftp\_evt\_type](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea) | [type](#a2d622d9eb3ee0547b47a1330ad9cc412) |
|  | Identifies the event. |
| union [tftp\_evt\_param](uniontftp__evt__param.md) | [param](#a37154f19c66ae09a200f4d8d6c2941ca) |
|  | Contains parameters (if any) accompanying the event. |

## Detailed Description

Defines TFTP asynchronous event notified to the application.

## Field Documentation

## [◆ ](#a37154f19c66ae09a200f4d8d6c2941ca)param

| union [tftp\_evt\_param](uniontftp__evt__param.md) tftp\_evt::param |
| --- |

Contains parameters (if any) accompanying the event.

## [◆ ](#a2d622d9eb3ee0547b47a1330ad9cc412)type

| enum [tftp\_evt\_type](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea) tftp\_evt::type |
| --- |

Identifies the event.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[tftp.h](tftp_8h_source.md)

- [tftp\_evt](structtftp__evt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
