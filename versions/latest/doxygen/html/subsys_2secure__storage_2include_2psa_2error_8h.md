---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html
original_path: doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h File Reference

[Operating System Services](group__os__services.md) » [PSA Secure Storage API](group__psa__secure__storage.md)

Return values of the PSA Secure Storage API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](subsys_2secure__storage_2include_2psa_2error_8h_source.md)

| #define | [PSA\_SUCCESS](#a4cc859e2c66ca381c7418db3527a65e1)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))0) |
| --- | --- |
| #define | [PSA\_ERROR\_GENERIC\_ERROR](#a8bfafd6baac18ce5d3192d1de256238f)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-132) |
| #define | [PSA\_ERROR\_NOT\_PERMITTED](#a4d1b8dd8526177a15a210b7afc1accb1)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-133) |
| #define | [PSA\_ERROR\_NOT\_SUPPORTED](#a1dcc6d130633ed5db8942257581b55dd)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-134) |
| #define | [PSA\_ERROR\_INVALID\_ARGUMENT](#a798df25a505ebf931f7bec1f80f1f85f)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-135) |
| #define | [PSA\_ERROR\_ALREADY\_EXISTS](#af2b34cc87edc72f3ba90071a08210d20)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-139) |
| #define | [PSA\_ERROR\_DOES\_NOT\_EXIST](#a18646babb2ae6cbde02ea3828bbd9141)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-140) |
| #define | [PSA\_ERROR\_INSUFFICIENT\_STORAGE](#a897a45eb206a6f6b7be7ffbe36f0d766)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-142) |
| #define | [PSA\_ERROR\_STORAGE\_FAILURE](#add169a1af2707862b95fb9df91dfc37d)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-146) |
| #define | [PSA\_ERROR\_INVALID\_SIGNATURE](#a35927f755d232c4766de600f2c49e9f2)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-149) |
| #define | [PSA\_ERROR\_DATA\_CORRUPT](#a9febb81a44bdeb4c6c42bf4f697b13bf)   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-152) |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9) |

## Detailed Description

Return values of the PSA Secure Storage API.

## Macro Definition Documentation

## [◆ ](#af2b34cc87edc72f3ba90071a08210d20)PSA\_ERROR\_ALREADY\_EXISTS

| #define PSA\_ERROR\_ALREADY\_EXISTS   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-139) |
| --- |

## [◆ ](#a9febb81a44bdeb4c6c42bf4f697b13bf)PSA\_ERROR\_DATA\_CORRUPT

| #define PSA\_ERROR\_DATA\_CORRUPT   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-152) |
| --- |

## [◆ ](#a18646babb2ae6cbde02ea3828bbd9141)PSA\_ERROR\_DOES\_NOT\_EXIST

| #define PSA\_ERROR\_DOES\_NOT\_EXIST   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-140) |
| --- |

## [◆ ](#a8bfafd6baac18ce5d3192d1de256238f)PSA\_ERROR\_GENERIC\_ERROR

| #define PSA\_ERROR\_GENERIC\_ERROR   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-132) |
| --- |

## [◆ ](#a897a45eb206a6f6b7be7ffbe36f0d766)PSA\_ERROR\_INSUFFICIENT\_STORAGE

| #define PSA\_ERROR\_INSUFFICIENT\_STORAGE   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-142) |
| --- |

## [◆ ](#a798df25a505ebf931f7bec1f80f1f85f)PSA\_ERROR\_INVALID\_ARGUMENT

| #define PSA\_ERROR\_INVALID\_ARGUMENT   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-135) |
| --- |

## [◆ ](#a35927f755d232c4766de600f2c49e9f2)PSA\_ERROR\_INVALID\_SIGNATURE

| #define PSA\_ERROR\_INVALID\_SIGNATURE   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-149) |
| --- |

## [◆ ](#a4d1b8dd8526177a15a210b7afc1accb1)PSA\_ERROR\_NOT\_PERMITTED

| #define PSA\_ERROR\_NOT\_PERMITTED   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-133) |
| --- |

## [◆ ](#a1dcc6d130633ed5db8942257581b55dd)PSA\_ERROR\_NOT\_SUPPORTED

| #define PSA\_ERROR\_NOT\_SUPPORTED   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-134) |
| --- |

## [◆ ](#add169a1af2707862b95fb9df91dfc37d)PSA\_ERROR\_STORAGE\_FAILURE

| #define PSA\_ERROR\_STORAGE\_FAILURE   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))-146) |
| --- |

## [◆ ](#a4cc859e2c66ca381c7418db3527a65e1)PSA\_SUCCESS

| #define PSA\_SUCCESS   (([psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9))0) |
| --- |

## Typedef Documentation

## [◆ ](#a05676e70ba5c6a7565aff3c36677c1f9)psa\_status\_t

| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [psa\_status\_t](#a05676e70ba5c6a7565aff3c36677c1f9) |
| --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [error.h](subsys_2secure__storage_2include_2psa_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
