---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcipher__ops.html
original_path: doxygen/html/structcipher__ops.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cipher\_ops Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md) » [Cipher](group__crypto__cipher.md)

`#include <[cipher.h](cipher_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) | [cipher\_mode](#a93c8c2c77d44ea013fbb6e7fd788d4d4) |
| union { |  |
| [block\_op\_t](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17)   [block\_crypt\_hndlr](#a2675dd312be240c24d7d2c0e81bcde2b) |  |
| [cbc\_op\_t](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2)   [cbc\_crypt\_hndlr](#abc7cf6306467c5aff24ae3faa37902e6) |  |
| [ctr\_op\_t](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba)   [ctr\_crypt\_hndlr](#ac792113d841e3a6b7dc107d7123162db) |  |
| [ccm\_op\_t](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7)   [ccm\_crypt\_hndlr](#af53f5f04fb5e1a7ca148f786d8cfe41f) |  |
| [gcm\_op\_t](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d)   [gcm\_crypt\_hndlr](#a570d1ed37d6cce61caa1c6e257f9cdc8) |  |
| }; |  |

## Field Documentation

## [◆ ](#a1aa1294a3a6129c896c35cfc4c608bed)[union]

| union { ... } [cipher\_ops](structcipher__ops.md) |
| --- |

## [◆ ](#a2675dd312be240c24d7d2c0e81bcde2b)block\_crypt\_hndlr

| [block\_op\_t](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17) cipher\_ops::block\_crypt\_hndlr |
| --- |

## [◆ ](#abc7cf6306467c5aff24ae3faa37902e6)cbc\_crypt\_hndlr

| [cbc\_op\_t](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2) cipher\_ops::cbc\_crypt\_hndlr |
| --- |

## [◆ ](#af53f5f04fb5e1a7ca148f786d8cfe41f)ccm\_crypt\_hndlr

| [ccm\_op\_t](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7) cipher\_ops::ccm\_crypt\_hndlr |
| --- |

## [◆ ](#a93c8c2c77d44ea013fbb6e7fd788d4d4)cipher\_mode

| enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) cipher\_ops::cipher\_mode |
| --- |

## [◆ ](#ac792113d841e3a6b7dc107d7123162db)ctr\_crypt\_hndlr

| [ctr\_op\_t](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba) cipher\_ops::ctr\_crypt\_hndlr |
| --- |

## [◆ ](#a570d1ed37d6cce61caa1c6e257f9cdc8)gcm\_crypt\_hndlr

| [gcm\_op\_t](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d) cipher\_ops::gcm\_crypt\_hndlr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[cipher.h](cipher_8h_source.md)

- [cipher\_ops](structcipher__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
