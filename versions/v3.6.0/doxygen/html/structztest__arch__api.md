---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structztest__arch__api.html
original_path: doxygen/html/structztest__arch__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_arch\_api Struct Reference

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md) » [Ztest testing macros](group__ztest__test.md)

Structure for architecture specific APIs.
[More...](#details)

`#include <[ztest_test.h](ztest__test_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [run\_all](#a005bcb042aee46de9088b7527df49f9f) )(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [should\_suite\_run](#a427413d24056eb42d3a5302c28bd4329) )(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [ztest\_suite\_node](structztest__suite__node.md) \*suite) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [should\_test\_run](#a8334b1ecc7efc93245fe35c7c1da728a) )(const char \*suite, const char \*test) |

## Detailed Description

Structure for architecture specific APIs.

## Field Documentation

## [◆ ](#a005bcb042aee46de9088b7527df49f9f)run\_all

| void(\* ztest\_arch\_api::run\_all) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
| --- |

## [◆ ](#a427413d24056eb42d3a5302c28bd4329)should\_suite\_run

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* ztest\_arch\_api::should\_suite\_run) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [ztest\_suite\_node](structztest__suite__node.md) \*suite) |
| --- |

## [◆ ](#a8334b1ecc7efc93245fe35c7c1da728a)should\_test\_run

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* ztest\_arch\_api::should\_test\_run) (const char \*suite, const char \*test) |
| --- |

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/testsuite/ztest/include/zephyr/[ztest\_test.h](ztest__test_8h_source.md)

- [ztest\_arch\_api](structztest__arch__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
