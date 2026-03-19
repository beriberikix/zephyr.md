---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__oob__info.html
original_path: doxygen/html/structbt__conn__oob__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_oob\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Info Structure for OOB pairing.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Public Types | |
| --- | --- |
| enum | { [BT\_CONN\_OOB\_LE\_LEGACY](#a318a663619f0bbbb90a849fd5e16c37ea4c33ea839306256a198c29ea783c659b) , [BT\_CONN\_OOB\_LE\_SC](#a318a663619f0bbbb90a849fd5e16c37eacd02773beb42df3fb6cbaa2fa2abda1e) } |
|  | Type of OOB pairing method. [More...](#a318a663619f0bbbb90a849fd5e16c37e) |

| Data Fields | |
| --- | --- |
| enum bt\_conn\_oob\_info:: { ... } | [type](#a9923119f8a145066408d9e46d6993026) |
|  | Type of OOB pairing method. |
| union { |  |
| struct { |  |
| enum | { [BT\_CONN\_OOB\_LOCAL\_ONLY](structbt__conn__oob__info_1_1_0d224236016370304343054103074037006351074263006352_1_1_0d130100253fa80b897837ee1b72b3ff0024cf07028.md#aad16cfc0f7105e2dc9f3984aa6e26f85a0f15853b5c0e5617f619c018a3426f3c) , [BT\_CONN\_OOB\_REMOTE\_ONLY](structbt__conn__oob__info_1_1_0d224236016370304343054103074037006351074263006352_1_1_0d130100253fa80b897837ee1b72b3ff0024cf07028.md#aad16cfc0f7105e2dc9f3984aa6e26f85affcec6b107bb69585c95c9fc188b031a) , [BT\_CONN\_OOB\_BOTH\_PEERS](structbt__conn__oob__info_1_1_0d224236016370304343054103074037006351074263006352_1_1_0d130100253fa80b897837ee1b72b3ff0024cf07028.md#aad16cfc0f7105e2dc9f3984aa6e26f85a4e5a50f33cd4d8cb198877ad35116bc1) , [BT\_CONN\_OOB\_NO\_DATA](structbt__conn__oob__info_1_1_0d224236016370304343054103074037006351074263006352_1_1_0d130100253fa80b897837ee1b72b3ff0024cf07028.md#aad16cfc0f7105e2dc9f3984aa6e26f85af2289ceb1c88353688f9f03b6686ab79) } |
|  | OOB data configuration. [More...](structbt__conn__oob__info_1_1_0d224236016370304343054103074037006351074263006352_1_1_0d130100253fa80b897837ee1b72b3ff0024cf07028.md#aad16cfc0f7105e2dc9f3984aa6e26f85) |
| enum bt\_conn\_oob\_info:: { ... }    [oob\_config](#a96f2cf2f20d9890b833949b2183a029c) |  |
|  | OOB data configuration. [More...](#a96f2cf2f20d9890b833949b2183a029c) |
| }   [lesc](#a59febda99e1ad78321fe2da07f98322b) |
|  | LE Secure Connections OOB pairing parameters. [More...](#a59febda99e1ad78321fe2da07f98322b) |
| }; |  |

## Detailed Description

Info Structure for OOB pairing.

## Member Enumeration Documentation

## [◆ ](#a318a663619f0bbbb90a849fd5e16c37e)anonymous enum

| anonymous enum |
| --- |

Type of OOB pairing method.

| Enumerator | |
| --- | --- |
| BT\_CONN\_OOB\_LE\_LEGACY | LE legacy pairing. |
| BT\_CONN\_OOB\_LE\_SC | LE SC pairing. |

## Field Documentation

## [◆ ](#aa6f47f4d60959480a7d3338b47aefe9a)[union]

| union { ... } [bt\_conn\_oob\_info](structbt__conn__oob__info.md) |
| --- |

## [◆ ](#a59febda99e1ad78321fe2da07f98322b)[struct]

| struct { ... } bt\_conn\_oob\_info::lesc |
| --- |

LE Secure Connections OOB pairing parameters.

## [◆ ](#a96f2cf2f20d9890b833949b2183a029c)[]

| enum { ... } bt\_conn\_oob\_info::oob\_config |
| --- |

OOB data configuration.

## [◆ ](#a9923119f8a145066408d9e46d6993026)[]

| enum { ... } bt\_conn\_oob\_info::type |
| --- |

Type of OOB pairing method.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_oob\_info](structbt__conn__oob__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
