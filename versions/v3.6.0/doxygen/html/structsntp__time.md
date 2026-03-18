---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsntp__time.html
original_path: doxygen/html/structsntp__time.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sntp\_time Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [SNTP](group__sntp.md)

Time as returned by SNTP API, fractional seconds since 1 Jan 1970.
[More...](#details)

`#include <[sntp.h](sntp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [seconds](#a7dc90613b6ac0265ff49b931a786354f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fraction](#ad33fb2e743756bde8538ac6d2ff3eae8) |

## Detailed Description

Time as returned by SNTP API, fractional seconds since 1 Jan 1970.

## Field Documentation

## [◆ ](#ad33fb2e743756bde8538ac6d2ff3eae8)fraction

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sntp\_time::fraction |
| --- |

## [◆ ](#a7dc90613b6ac0265ff49b931a786354f)seconds

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sntp\_time::seconds |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[sntp.h](sntp_8h_source.md)

- [sntp\_time](structsntp__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
