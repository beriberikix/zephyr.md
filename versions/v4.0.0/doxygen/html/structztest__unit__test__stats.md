---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structztest__unit__test__stats.html
original_path: doxygen/html/structztest__unit__test__stats.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_unit\_test\_stats Struct Reference

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md) » [Ztest testing macros](group__ztest__test.md)

`#include <[ztest_test.h](ztest__test_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [run\_count](#a1f1cc422307e6bd7875e42c7205e47d7) |
|  | The number of times that the test ran. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [skip\_count](#a5370f1797292d3fe575166e161dee43f) |
|  | The number of times that the test was skipped. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fail\_count](#addbacc4315f502b2c69ee5ebf5884ad6) |
|  | The number of times that the test failed. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pass\_count](#a21c2c8a05524e673567c7ee3d809ad25) |
|  | The number of times that the test passed. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [duration\_worst\_ms](#ac24d475c52c4ea7a0de4e99f2d76d1a1) |
|  | The longest duration of the test across multiple times. |

## Field Documentation

## [◆ ](#ac24d475c52c4ea7a0de4e99f2d76d1a1)duration\_worst\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_unit\_test\_stats::duration\_worst\_ms |
| --- |

The longest duration of the test across multiple times.

## [◆ ](#addbacc4315f502b2c69ee5ebf5884ad6)fail\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_unit\_test\_stats::fail\_count |
| --- |

The number of times that the test failed.

## [◆ ](#a21c2c8a05524e673567c7ee3d809ad25)pass\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_unit\_test\_stats::pass\_count |
| --- |

The number of times that the test passed.

## [◆ ](#a1f1cc422307e6bd7875e42c7205e47d7)run\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_unit\_test\_stats::run\_count |
| --- |

The number of times that the test ran.

## [◆ ](#a5370f1797292d3fe575166e161dee43f)skip\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_unit\_test\_stats::skip\_count |
| --- |

The number of times that the test was skipped.

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/testsuite/ztest/include/zephyr/[ztest\_test.h](ztest__test_8h_source.md)

- [ztest\_unit\_test\_stats](structztest__unit__test__stats.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
