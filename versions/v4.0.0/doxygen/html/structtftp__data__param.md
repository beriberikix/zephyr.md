---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtftp__data__param.html
original_path: doxygen/html/structtftp__data__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tftp\_data\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [TFTP Client library](group__tftp__client.md)

Parameters for data event.
[More...](#details)

`#include <[tftp.h](tftp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data\_ptr](#a93f666944e8f20bd3a0e1320452913db) |
|  | Pointer to binary data. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#a704c20ab3177a3d53df21fc9ef64d084) |
|  | Length of binary data. |

## Detailed Description

Parameters for data event.

## Field Documentation

## [◆ ](#a93f666944e8f20bd3a0e1320452913db)data\_ptr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* tftp\_data\_param::data\_ptr |
| --- |

Pointer to binary data.

## [◆ ](#a704c20ab3177a3d53df21fc9ef64d084)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tftp\_data\_param::len |
| --- |

Length of binary data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[tftp.h](tftp_8h_source.md)

- [tftp\_data\_param](structtftp__data__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
