---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__tbs__client__cb.html
original_path: doxygen/html/structbt__tbs__client__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_tbs\_client\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Telephone Bearer Service (TBS)](group__bt__tbs.md)

Struct to hold the Telephone Bearer Service client callbacks.
[More...](#details)

`#include <[tbs.h](tbs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_tbs\_client\_discover\_cb](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7) | [discover](#abfd4542a0781ff5676a191249f121e91) |
|  | Discovery has completed. |
| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) | [originate\_call](#a0bc51181f188a1249407f2e50431d9fd) |
|  | Originate call has completed. |
| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) | [terminate\_call](#aa78425597fe7fd0db09d69c3ed757293) |
|  | Terminate call has completed. |
| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) | [hold\_call](#a304a5fd373f1ba5ccb2eb77fcdbbd380) |
|  | Hold call has completed. |
| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) | [accept\_call](#a41242d76c976eef102d480965f977537) |
|  | Accept call has completed. |
| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) | [retrieve\_call](#a2a5fb7de5c3c4aab290c0163c0b40858) |
|  | Retrieve call has completed. |
| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) | [join\_calls](#a2d6b7acd90d05c61f60f27236ab6f1ee) |
|  | Join calls has completed. |
| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) | [bearer\_provider\_name](#a36d8ea1717e57b9440e9b58e9411422a) |
|  | Bearer provider name has been read. |
| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) | [bearer\_uci](#a15ccb7de457631620983e7d2d0372967) |
|  | Bearer UCI has been read. |
| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) | [technology](#a803d8268ee1271f41aec68f6d9b811bf) |
|  | Bearer technology has been read. |
| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) | [uri\_list](#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee) |
|  | Bearer URI list has been read. |
| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) | [signal\_strength](#a96df90461159f97f5dc8cbb72cd0cbc4) |
|  | Bearer signal strength has been read. |
| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) | [signal\_interval](#a01426c4a84e71a9395cce2963e2e83a3) |
|  | Bearer signal interval has been read. |
| [bt\_tbs\_client\_current\_calls\_cb](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f) | [current\_calls](#a10dc9404533db388b3ae1058542efd66) |
|  | Bearer current calls has been read. |
| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) | [ccid](#a90acde153f8893b5cba891884529d86c) |
|  | Bearer CCID has been read. |
| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) | [call\_uri](#ae95494a76e1f3275f48204dcd4798712) |
|  | Bearer call URI has been read. |
| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) | [status\_flags](#a94c3bfc1e88518de9e29e947064ec8dc) |
|  | Bearer status flags has been read. |
| [bt\_tbs\_client\_call\_states\_cb](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92) | [call\_state](#a88cb69ef54c9399bceb5641202eeabce) |
|  | Bearer call states has been read. |
| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) | [optional\_opcodes](#a91c61b29c16a43fd3f781fd7e0ab4618) |
|  | Bearer optional opcodes has been read. |
| [bt\_tbs\_client\_termination\_reason\_cb](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78) | [termination\_reason](#ae8e5cbe52cbb300e1cd919d24c85c4df) |
|  | Bearer terminate reason has been read. |
| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) | [remote\_uri](#a354ba5d21376813adc5c9765a5da1a09) |
|  | Bearer remote URI has been read. |
| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) | [friendly\_name](#ad2089050db76453b7f9c51c3d2fa4d17) |
|  | Bearer friendly name has been read. |

## Detailed Description

Struct to hold the Telephone Bearer Service client callbacks.

These can be registered for usage with [bt\_tbs\_client\_register\_cb()](group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb "Register the callbacks for CCP.").

## Field Documentation

## [◆ ](#a41242d76c976eef102d480965f977537)accept\_call

| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) bt\_tbs\_client\_cb::accept\_call |
| --- |

Accept call has completed.

## [◆ ](#a36d8ea1717e57b9440e9b58e9411422a)bearer\_provider\_name

| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) bt\_tbs\_client\_cb::bearer\_provider\_name |
| --- |

Bearer provider name has been read.

## [◆ ](#a15ccb7de457631620983e7d2d0372967)bearer\_uci

| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) bt\_tbs\_client\_cb::bearer\_uci |
| --- |

Bearer UCI has been read.

## [◆ ](#a88cb69ef54c9399bceb5641202eeabce)call\_state

| [bt\_tbs\_client\_call\_states\_cb](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92) bt\_tbs\_client\_cb::call\_state |
| --- |

Bearer call states has been read.

## [◆ ](#ae95494a76e1f3275f48204dcd4798712)call\_uri

| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) bt\_tbs\_client\_cb::call\_uri |
| --- |

Bearer call URI has been read.

## [◆ ](#a90acde153f8893b5cba891884529d86c)ccid

| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) bt\_tbs\_client\_cb::ccid |
| --- |

Bearer CCID has been read.

## [◆ ](#a10dc9404533db388b3ae1058542efd66)current\_calls

| [bt\_tbs\_client\_current\_calls\_cb](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f) bt\_tbs\_client\_cb::current\_calls |
| --- |

Bearer current calls has been read.

## [◆ ](#abfd4542a0781ff5676a191249f121e91)discover

| [bt\_tbs\_client\_discover\_cb](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7) bt\_tbs\_client\_cb::discover |
| --- |

Discovery has completed.

## [◆ ](#ad2089050db76453b7f9c51c3d2fa4d17)friendly\_name

| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) bt\_tbs\_client\_cb::friendly\_name |
| --- |

Bearer friendly name has been read.

## [◆ ](#a304a5fd373f1ba5ccb2eb77fcdbbd380)hold\_call

| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) bt\_tbs\_client\_cb::hold\_call |
| --- |

Hold call has completed.

## [◆ ](#a2d6b7acd90d05c61f60f27236ab6f1ee)join\_calls

| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) bt\_tbs\_client\_cb::join\_calls |
| --- |

Join calls has completed.

## [◆ ](#a91c61b29c16a43fd3f781fd7e0ab4618)optional\_opcodes

| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) bt\_tbs\_client\_cb::optional\_opcodes |
| --- |

Bearer optional opcodes has been read.

## [◆ ](#a0bc51181f188a1249407f2e50431d9fd)originate\_call

| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) bt\_tbs\_client\_cb::originate\_call |
| --- |

Originate call has completed.

## [◆ ](#a354ba5d21376813adc5c9765a5da1a09)remote\_uri

| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) bt\_tbs\_client\_cb::remote\_uri |
| --- |

Bearer remote URI has been read.

## [◆ ](#a2a5fb7de5c3c4aab290c0163c0b40858)retrieve\_call

| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) bt\_tbs\_client\_cb::retrieve\_call |
| --- |

Retrieve call has completed.

## [◆ ](#a01426c4a84e71a9395cce2963e2e83a3)signal\_interval

| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) bt\_tbs\_client\_cb::signal\_interval |
| --- |

Bearer signal interval has been read.

## [◆ ](#a96df90461159f97f5dc8cbb72cd0cbc4)signal\_strength

| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) bt\_tbs\_client\_cb::signal\_strength |
| --- |

Bearer signal strength has been read.

## [◆ ](#a94c3bfc1e88518de9e29e947064ec8dc)status\_flags

| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) bt\_tbs\_client\_cb::status\_flags |
| --- |

Bearer status flags has been read.

## [◆ ](#a803d8268ee1271f41aec68f6d9b811bf)technology

| [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) bt\_tbs\_client\_cb::technology |
| --- |

Bearer technology has been read.

## [◆ ](#aa78425597fe7fd0db09d69c3ed757293)terminate\_call

| [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) bt\_tbs\_client\_cb::terminate\_call |
| --- |

Terminate call has completed.

## [◆ ](#ae8e5cbe52cbb300e1cd919d24c85c4df)termination\_reason

| [bt\_tbs\_client\_termination\_reason\_cb](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78) bt\_tbs\_client\_cb::termination\_reason |
| --- |

Bearer terminate reason has been read.

## [◆ ](#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee)uri\_list

| [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) bt\_tbs\_client\_cb::uri\_list |
| --- |

Bearer URI list has been read.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[tbs.h](tbs_8h_source.md)

- [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
