---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structztest__suite__node.html
original_path: doxygen/html/structztest__suite__node.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_suite\_node Struct Reference

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md) » [Ztest testing macros](group__ztest__test.md)

A single node of test suite.
[More...](#details)

`#include <[ztest_test.h](ztest__test_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \*const | [name](#a55f700029b3f6dbfd1bd9ce7df6808e4) |
|  | The name of the test suite. |
| const [ztest\_suite\_setup\_t](group__ztest__test.md#ga0063907dd70b9eb817ea472162693ee4) | [setup](#a0a30e674f7a071e43e1ff1e190bf2020) |
|  | Setup function. |
| const [ztest\_suite\_before\_t](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d) | [before](#a0a1eeaa1f0b90918e6b87e1d37d84eef) |
|  | Before function. |
| const [ztest\_suite\_after\_t](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c) | [after](#a46ec271d4a7625b01daac27899d5eae4) |
|  | After function. |
| const [ztest\_suite\_teardown\_t](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd) | [teardown](#a97f7e248b5fe9548010d659816f8d295) |
|  | Teardown function. |
| const [ztest\_suite\_predicate\_t](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c) | [predicate](#ac0a66cf7eb644fbc7c161ee61c854385) |
|  | Optional predicate filter. |
| struct [ztest\_suite\_stats](structztest__suite__stats.md) \*const | [stats](#a1d80587f1e1c841d6c4d43b5fe3c9b4d) |
|  | Stats. |

## Detailed Description

A single node of test suite.

Each node should be added to a single linker section which will allow [ztest\_run\_test\_suites()](group__ztest__test.md#gaafb3cba3a9637839952b2db2486ab88c "Run the registered unit tests which return true from their predicate function.") to iterate over the various nodes.

## Field Documentation

## [◆ ](#a46ec271d4a7625b01daac27899d5eae4)after

| const [ztest\_suite\_after\_t](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c) ztest\_suite\_node::after |
| --- |

After function.

## [◆ ](#a0a1eeaa1f0b90918e6b87e1d37d84eef)before

| const [ztest\_suite\_before\_t](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d) ztest\_suite\_node::before |
| --- |

Before function.

## [◆ ](#a55f700029b3f6dbfd1bd9ce7df6808e4)name

| const char\* const ztest\_suite\_node::name |
| --- |

The name of the test suite.

## [◆ ](#ac0a66cf7eb644fbc7c161ee61c854385)predicate

| const [ztest\_suite\_predicate\_t](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c) ztest\_suite\_node::predicate |
| --- |

Optional predicate filter.

## [◆ ](#a0a30e674f7a071e43e1ff1e190bf2020)setup

| const [ztest\_suite\_setup\_t](group__ztest__test.md#ga0063907dd70b9eb817ea472162693ee4) ztest\_suite\_node::setup |
| --- |

Setup function.

## [◆ ](#a1d80587f1e1c841d6c4d43b5fe3c9b4d)stats

| struct [ztest\_suite\_stats](structztest__suite__stats.md)\* const ztest\_suite\_node::stats |
| --- |

Stats.

## [◆ ](#a97f7e248b5fe9548010d659816f8d295)teardown

| const [ztest\_suite\_teardown\_t](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd) ztest\_suite\_node::teardown |
| --- |

Teardown function.

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/testsuite/ztest/include/zephyr/[ztest\_test.h](ztest__test_8h_source.md)

- [ztest\_suite\_node](structztest__suite__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
