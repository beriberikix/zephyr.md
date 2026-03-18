---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structztest__unit__test.html
original_path: doxygen/html/structztest__unit__test.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_unit\_test Struct Reference

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md) » [Ztest testing macros](group__ztest__test.md)

`#include <[ztest_test.h](ztest__test_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [test\_suite\_name](#ac94283459e71728180420d66b3a4a53a) |
| const char \* | [name](#a1176caba02accac7bd2eb02c715a0d38) |
| void(\* | [test](#a5fe0425dde921834acb2c0e387bcc524) )(void \*data) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [thread\_options](#a9c151bd9e948788c861503b53c52b24d) |
| struct [ztest\_unit\_test\_stats](structztest__unit__test__stats.md) \*const | [stats](#a3b7014bbb299c4aeb6717806e602f38a) |
|  | Stats. |

## Field Documentation

## [◆ ](#a1176caba02accac7bd2eb02c715a0d38)name

| const char\* ztest\_unit\_test::name |
| --- |

## [◆ ](#a3b7014bbb299c4aeb6717806e602f38a)stats

| struct [ztest\_unit\_test\_stats](structztest__unit__test__stats.md)\* const ztest\_unit\_test::stats |
| --- |

Stats.

## [◆ ](#a5fe0425dde921834acb2c0e387bcc524)test

| void(\* ztest\_unit\_test::test) (void \*data) |
| --- |

## [◆ ](#ac94283459e71728180420d66b3a4a53a)test\_suite\_name

| const char\* ztest\_unit\_test::test\_suite\_name |
| --- |

## [◆ ](#a9c151bd9e948788c861503b53c52b24d)thread\_options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztest\_unit\_test::thread\_options |
| --- |

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/testsuite/ztest/include/zephyr/[ztest\_test.h](ztest__test_8h_source.md)

- [ztest\_unit\_test](structztest__unit__test.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
