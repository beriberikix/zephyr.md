---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mipi__stp__decoder_8h.html
original_path: doxygen/html/mipi__stp__decoder_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_stp\_decoder.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](mipi__stp__decoder_8h_source.md)

| Data Structures | |
| --- | --- |
| union | [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) |
|  | Union with data associated with a given STP opcode. [More...](unionmipi__stp__decoder__data.md#details) |
| struct | [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) |
|  | Decoder configuration. [More...](structmipi__stp__decoder__config.md#details) |

| Macros | |
| --- | --- |
| #define | [STP\_DECODER\_TYPE2STR](group__mipi__stp__decoder__apis.md#gae19e768343e0543260752ec2876d1faa)(\_type) |
|  | Convert type to a string literal. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mipi\_stp\_decoder\_cb](group__mipi__stp__decoder__apis.md#gad3456ba4b000dd1a77c4dc85428bd7d8)) (enum [mipi\_stp\_decoder\_ctrl\_type](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d) type, union [mipi\_stp\_decoder\_data](unionmipi__stp__decoder__data.md) data, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked) |
|  | Callback signature. |

| Enumerations | |
| --- | --- |
| enum | [mipi\_stp\_decoder\_ctrl\_type](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d) {     [STP\_DATA4](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5) = 1 , [STP\_DATA8](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100) = 2 , [STP\_DATA16](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184) = 4 , [STP\_DATA32](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e) = 8 ,     [STP\_DATA64](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a) = 16 , [STP\_DECODER\_NULL](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e) = 128 , [STP\_DECODER\_MAJOR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1) , [STP\_DECODER\_MERROR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a) ,     [STP\_DECODER\_CHANNEL](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360) , [STP\_DECODER\_VERSION](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f) , [STP\_DECODER\_FREQ](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37) , [STP\_DECODER\_GERROR](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7) ,     [STP\_DECODER\_FLAG](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5) , [STP\_DECODER\_ASYNC](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef) , [STP\_DECODER\_NOT\_SUPPORTED](group__mipi__stp__decoder__apis.md#gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4)   } |
|  | STPv2 opcodes. [More...](group__mipi__stp__decoder__apis.md#ga6e1f4b66b14ab44e549292f97046a50d) |

| Functions | |
| --- | --- |
| int | [mipi\_stp\_decoder\_init](group__mipi__stp__decoder__apis.md#ga4a67705c849793f02c7ae409434b4e79) (const struct [mipi\_stp\_decoder\_config](structmipi__stp__decoder__config.md) \*config) |
|  | Initialize the decoder. |
| int | [mipi\_stp\_decoder\_decode](group__mipi__stp__decoder__apis.md#ga520104e814b15cce22ec74a4e827a5b9) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Decode STPv2 stream. |
| void | [mipi\_stp\_decoder\_sync\_loss](group__mipi__stp__decoder__apis.md#ga0e1be10f234d72e81b48d21bfe8a42f8) (void) |
|  | Indicate synchronization loss. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [mipi\_stp\_decoder.h](mipi__stp__decoder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
