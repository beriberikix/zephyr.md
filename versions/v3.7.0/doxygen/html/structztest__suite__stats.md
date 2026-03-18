---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structztest__suite__stats.html
original_path: doxygen/html/structztest__suite__stats.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_suite\_stats Struct Reference

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md) » [Ztest testing macros](group__ztest__test.md)

Stats about a ztest suite.
[More...](#details)

`#include <[ztest_test.h](ztest__test_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [run\_count](#a94a4d70901b2d2b57cbaf03b9c6d21a9) |
|  | The number of times that the suite ran. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [skip\_count](#a04d888a17a39bdf62f1b935968d58b92) |
|  | The number of times that the suite was skipped. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fail\_count](#a58f7c9379bc9bf18c2184fdcd2bbff8c) |
|  | The number of times that the suite failed. |

## Detailed Description

Stats about a ztest suite.

## Field Documentation

## [◆ ](#a58f7c9379bc9bf18c2184fdcd2bbff8c)fail\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_suite\_stats::fail\_count |
| --- |

The number of times that the suite failed.

## [◆ ](#a94a4d70901b2d2b57cbaf03b9c6d21a9)run\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_suite\_stats::run\_count |
| --- |

The number of times that the suite ran.

## [◆ ](#a04d888a17a39bdf62f1b935968d58b92)skip\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_suite\_stats::skip\_count |
| --- |

The number of times that the suite was skipped.

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/testsuite/ztest/include/zephyr/[ztest\_test.h](ztest__test_8h_source.md)

- [ztest\_suite\_stats](structztest__suite__stats.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
