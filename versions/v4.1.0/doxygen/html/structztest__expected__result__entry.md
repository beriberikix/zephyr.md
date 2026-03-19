---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structztest__expected__result__entry.html
original_path: doxygen/html/structztest__expected__result__entry.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_expected\_result\_entry Struct Reference

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md) » [Ztest testing macros](group__ztest__test.md)

A single expectation entry allowing tests to fail/skip and be considered passing.
[More...](#details)

`#include <[ztest_test.h](ztest__test_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [test\_suite\_name](#a37352688340aa1c49a7967d5b568c9a1) |
|  | The test suite's name for the expectation. |
| const char \* | [test\_name](#a92ada50dadf26e5c59e4e529afffd882) |
|  | The test's name for the expectation. |
| enum [ztest\_expected\_result](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26) | [expected\_result](#a74524b4da8fddbd64d526cfc5df72743) |
|  | The expectation. |

## Detailed Description

A single expectation entry allowing tests to fail/skip and be considered passing.

See also
:   [ZTEST\_EXPECT\_FAIL](group__ztest__test.md#gaeaa5b96855dd45e015b9556212f8945a "Expect a test to fail (mark it passing if it failed).")
:   [ZTEST\_EXPECT\_SKIP](group__ztest__test.md#gacb6f06920e522b9a9f6e7a98f0620f38 "Expect a test to skip (mark it passing if it failed).")

## Field Documentation

## [◆ ](#a74524b4da8fddbd64d526cfc5df72743)expected\_result

| enum [ztest\_expected\_result](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26) ztest\_expected\_result\_entry::expected\_result |
| --- |

The expectation.

## [◆ ](#a92ada50dadf26e5c59e4e529afffd882)test\_name

| const char\* ztest\_expected\_result\_entry::test\_name |
| --- |

The test's name for the expectation.

## [◆ ](#a37352688340aa1c49a7967d5b568c9a1)test\_suite\_name

| const char\* ztest\_expected\_result\_entry::test\_suite\_name |
| --- |

The test suite's name for the expectation.

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/testsuite/ztest/include/zephyr/[ztest\_test.h](ztest__test_8h_source.md)

- [ztest\_expected\_result\_entry](structztest__expected__result__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
