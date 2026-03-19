---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mipi__stp__decoder__apis.html
original_path: doxygen/html/group__mipi__stp__decoder__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

STP Decoder API

[Operating System Services](group__os__services.md)

| Data Structures | |
| --- | --- |
| union | [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) |
|  | Union with data associated with a given STP opcode. [More...](unionmipi__stp__decoder__data.md#details) |
| struct | [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) |
|  | Decoder configuration. [More...](structmipi__stp__decoder__config.md#details) |

| Macros | |
| --- | --- |
| #define | [STP\_DECODER\_TYPE2STR](#gae19e768343e0543260752ec2876d1faa)(\_type) |
|  | Convert type to a string literal. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mipi\_stp\_decoder\_cb](#gad3456ba4b000dd1a77c4dc85428bd7d8)) (enum [mipi\_stp\_decoder\_ctrl\_type](#ga6e1f4b66b14ab44e549292f97046a50d) type, union [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) data, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked) |
|  | Callback signature. |

| Enumerations | |
| --- | --- |
| enum | [mipi\_stp\_decoder\_ctrl\_type](#ga6e1f4b66b14ab44e549292f97046a50d) {     [STP\_DATA4](#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5) = 1 , [STP\_DATA8](#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100) = 2 , [STP\_DATA16](#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184) = 4 , [STP\_DATA32](#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e) = 8 ,     [STP\_DATA64](#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a) = 16 , [STP\_DECODER\_NULL](#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e) = 128 , [STP\_DECODER\_MAJOR](#gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1) , [STP\_DECODER\_MERROR](#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a) ,     [STP\_DECODER\_CHANNEL](#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360) , [STP\_DECODER\_VERSION](#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f) , [STP\_DECODER\_FREQ](#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37) , [STP\_DECODER\_GERROR](#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7) ,     [STP\_DECODER\_FLAG](#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5) , [STP\_DECODER\_ASYNC](#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef) , [STP\_DECODER\_NOT\_SUPPORTED](#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4)   } |
|  | STPv2 opcodes. [More...](#ga6e1f4b66b14ab44e549292f97046a50d) |

| Functions | |
| --- | --- |
| int | [mipi\_stp\_decoder\_init](#ga4a67705c849793f02c7ae409434b4e79) (const struct [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) \*config) |
|  | Initialize the decoder. |
| int | [mipi\_stp\_decoder\_decode](#ga520104e814b15cce22ec74a4e827a5b9) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Decode STPv2 stream. |
| void | [mipi\_stp\_decoder\_sync\_loss](#ga0e1be10f234d72e81b48d21bfe8a42f8) (void) |
|  | Indicate synchronization loss. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gae19e768343e0543260752ec2876d1faa)STP\_DECODER\_TYPE2STR

| #define STP\_DECODER\_TYPE2STR | ( |  | *\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h.md)>`

**Value:**

\_type == [STP\_DATA4](#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5) ? "DATA4" : (\

\_type == [STP\_DATA8](#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100) ? "DATA8" : (\

\_type == [STP\_DATA16](#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184) ? "DATA16" : (\

\_type == [STP\_DATA32](#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e) ? "DATA32" : (\

\_type == [STP\_DATA64](#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a) ? "DATA64" : (\

\_type == [STP\_DECODER\_NULL](#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e) ? "NULL" : (\

\_type == [STP\_DECODER\_MAJOR](#gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1) ? "MAJOR" : (\

\_type == [STP\_DECODER\_MERROR](#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a) ? "MERROR" : (\

\_type == [STP\_DECODER\_CHANNEL](#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360) ? "CHANNEL" : (\

\_type == [STP\_DECODER\_VERSION](#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f) ? "VERSION" : (\

\_type == [STP\_DECODER\_FREQ](#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37) ? "FREQ" : (\

\_type == [STP\_DECODER\_GERROR](#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7) ? "GERROR" : (\

\_type == [STP\_DECODER\_FLAG](#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5) ? "FLAG" : (\

\_type == [STP\_DECODER\_ASYNC](#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef) ? "ASYNC" : (\

"Unknown"))))))))))))))

[STP\_DECODER\_NULL](#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e)

@ STP\_DECODER\_NULL

**Definition** mipi\_stp\_decoder.h:29

[STP\_DATA4](#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5)

@ STP\_DATA4

**Definition** mipi\_stp\_decoder.h:24

[STP\_DECODER\_FLAG](#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5)

@ STP\_DECODER\_FLAG

**Definition** mipi\_stp\_decoder.h:36

[STP\_DECODER\_FREQ](#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37)

@ STP\_DECODER\_FREQ

**Definition** mipi\_stp\_decoder.h:34

[STP\_DATA16](#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184)

@ STP\_DATA16

**Definition** mipi\_stp\_decoder.h:26

[STP\_DATA32](#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e)

@ STP\_DATA32

**Definition** mipi\_stp\_decoder.h:27

[STP\_DECODER\_MAJOR](#gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1)

@ STP\_DECODER\_MAJOR

**Definition** mipi\_stp\_decoder.h:30

[STP\_DATA8](#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100)

@ STP\_DATA8

**Definition** mipi\_stp\_decoder.h:25

[STP\_DECODER\_CHANNEL](#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360)

@ STP\_DECODER\_CHANNEL

**Definition** mipi\_stp\_decoder.h:32

[STP\_DATA64](#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a)

@ STP\_DATA64

**Definition** mipi\_stp\_decoder.h:28

[STP\_DECODER\_ASYNC](#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef)

@ STP\_DECODER\_ASYNC

**Definition** mipi\_stp\_decoder.h:37

[STP\_DECODER\_GERROR](#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7)

@ STP\_DECODER\_GERROR

**Definition** mipi\_stp\_decoder.h:35

[STP\_DECODER\_MERROR](#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a)

@ STP\_DECODER\_MERROR

**Definition** mipi\_stp\_decoder.h:31

[STP\_DECODER\_VERSION](#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f)

@ STP\_DECODER\_VERSION

**Definition** mipi\_stp\_decoder.h:33

Convert type to a string literal.

Parameters
:   | \_type | type |
    | --- | --- |

Returns
:   String literal.

## Typedef Documentation

## [◆ ](#gad3456ba4b000dd1a77c4dc85428bd7d8)mipi\_stp\_decoder\_cb

| typedef void(\* mipi\_stp\_decoder\_cb) (enum [mipi\_stp\_decoder\_ctrl\_type](#ga6e1f4b66b14ab44e549292f97046a50d) type, union [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) data, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked) |
| --- |

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h.md)>`

Callback signature.

Callback is called whenever an element from STPv2 stream is decoded.

Note
:   Callback is called with interrupts locked.

Parameters
:   | type | Type. See [mipi\_stp\_decoder\_ctrl\_type](#ga6e1f4b66b14ab44e549292f97046a50d). |
    | --- | --- |
    | data | Data. Data associated with a given `type`. |
    | ts | Timestamp. Present if not NULL. |
    | marked | Set to true if opcode was marked. |

## Enumeration Type Documentation

## [◆ ](#ga6e1f4b66b14ab44e549292f97046a50d)mipi\_stp\_decoder\_ctrl\_type

| enum [mipi\_stp\_decoder\_ctrl\_type](#ga6e1f4b66b14ab44e549292f97046a50d) |
| --- |

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h.md)>`

STPv2 opcodes.

| Enumerator | |
| --- | --- |
| STP\_DATA4 |  |
| STP\_DATA8 |  |
| STP\_DATA16 |  |
| STP\_DATA32 |  |
| STP\_DATA64 |  |
| STP\_DECODER\_NULL |  |
| STP\_DECODER\_MAJOR |  |
| STP\_DECODER\_MERROR |  |
| STP\_DECODER\_CHANNEL |  |
| STP\_DECODER\_VERSION |  |
| STP\_DECODER\_FREQ |  |
| STP\_DECODER\_GERROR |  |
| STP\_DECODER\_FLAG |  |
| STP\_DECODER\_ASYNC |  |
| STP\_DECODER\_NOT\_SUPPORTED |  |

## Function Documentation

## [◆ ](#ga520104e814b15cce22ec74a4e827a5b9)mipi\_stp\_decoder\_decode()

| int mipi\_stp\_decoder\_decode | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h.md)>`

Decode STPv2 stream.

Function decodes the stream and calls the callback for every decoded element.

Parameters
:   | data | Data. |
    | --- | --- |
    | len | Data length. |

Return values
:   | 0 | On successful decoding. |
    | --- | --- |
    | negative | On failure. |

## [◆ ](#ga4a67705c849793f02c7ae409434b4e79)mipi\_stp\_decoder\_init()

| int mipi\_stp\_decoder\_init | ( | const struct [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) \* | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h.md)>`

Initialize the decoder.

Parameters
:   | config | Configuration. |
    | --- | --- |

Return values
:   | 0 | On successful initialization. |
    | --- | --- |
    | negative | On failure. |

## [◆ ](#ga0e1be10f234d72e81b48d21bfe8a42f8)mipi\_stp\_decoder\_sync\_loss()

| void mipi\_stp\_decoder\_sync\_loss | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mipi_stp_decoder.h](mipi__stp__decoder_8h.md)>`

Indicate synchronization loss.

If detected, then decoder starts to look for ASYNC marker and drops all data until ASYNC is found. Synchronization can be lost when there is data loss (e.g. due to overflow).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
