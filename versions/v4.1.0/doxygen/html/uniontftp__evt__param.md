---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uniontftp__evt__param.html
original_path: doxygen/html/uniontftp__evt__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tftp\_evt\_param Union Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [TFTP Client library](group__tftp__client.md)

Defines event parameters notified along with asynchronous events to the application.
[More...](#details)

`#include <[tftp.h](tftp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [tftp\_data\_param](structtftp__data__param.md) | [data](#a7bec7cd5512f25699fe6b733458e9128) |
|  | Parameters accompanying TFTP\_EVT\_DATA event. |
| struct [tftp\_error\_param](structtftp__error__param.md) | [error](#a489485b84fa3e559b3065258cabfb205) |
|  | Parameters accompanying TFTP\_EVT\_ERROR event. |

## Detailed Description

Defines event parameters notified along with asynchronous events to the application.

## Field Documentation

## [◆ ](#a7bec7cd5512f25699fe6b733458e9128)data

| struct [tftp\_data\_param](structtftp__data__param.md) tftp\_evt\_param::data |
| --- |

Parameters accompanying TFTP\_EVT\_DATA event.

## [◆ ](#a489485b84fa3e559b3065258cabfb205)error

| struct [tftp\_error\_param](structtftp__error__param.md) tftp\_evt\_param::error |
| --- |

Parameters accompanying TFTP\_EVT\_ERROR event.

---

The documentation for this union was generated from the following file:

- zephyr/net/[tftp.h](tftp_8h_source.md)

- [tftp\_evt\_param](uniontftp__evt__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
