---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsntp__ctx.html
original_path: doxygen/html/structsntp__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sntp\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [SNTP](group__sntp.md)

SNTP context.
[More...](#details)

`#include <[sntp.h](sntp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sntp\_time](structsntp__time.md) | [expected\_orig\_ts](#a58bd69ad86d00183e32ed07a9fbebfdc) |
|  | Timestamp when the request was sent from client to server. |

## Detailed Description

SNTP context.

## Field Documentation

## [◆ ](#a58bd69ad86d00183e32ed07a9fbebfdc)expected\_orig\_ts

| struct [sntp\_time](structsntp__time.md) sntp\_ctx::expected\_orig\_ts |
| --- |

Timestamp when the request was sent from client to server.

This is used to check if the originated timestamp in the server reply matches the one in client request.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[sntp.h](sntp_8h_source.md)

- [sntp\_ctx](structsntp__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
