---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__cs__create__config__params.html
original_path: doxygen/html/structbt__le__cs__create__config__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_cs\_create\_config\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Channel Sounding (CS)](group__bt__le__cs.md)

CS Create Config params.
[More...](#details)

`#include <[cs.h](cs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a59615f8de0a39f124ae3d2e2876ecc30) |
|  | CS configuration ID. |
| enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) | [main\_mode\_type](#a2bdbff2e20106e4a6925a8018d491a9c) |
|  | Main CS mode type. |
| enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) | [sub\_mode\_type](#a1bec59da1343bbc70a575d6dbde56309) |
|  | Sub CS mode type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_main\_mode\_steps](#ae7ff30dcfcb4460dac48c139bdac0f75) |
|  | Minimum number of CS main mode steps to be executed before a submode step is executed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_main\_mode\_steps](#aa8951ab286210ab87c460ed315d091bf) |
|  | Maximum number of CS main mode steps to be executed before a submode step is executed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [main\_mode\_repetition](#a9a7c56e1d04d634aaab4f3b81c506be3) |
|  | Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning of the current CS subevent directly after the last mode-0 step of that event. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode\_0\_steps](#af824b6b56fba318588ebcf707d6e7a24) |
|  | Number of CS mode-0 steps to be included at the beginning of each CS subevent. |
| enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) | [role](#a2581694b25afa7903786c7848c133c38) |
|  | CS role. |
| enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) | [rtt\_type](#a0a34afa329e88af8fcbcff1a8b0a1bcd) |
|  | RTT type. |
| enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) | [cs\_sync\_phy](#a4329d967361e330077ca9064bdc3fc5f) |
|  | CS Sync PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_map\_repetition](#a6eff424679cb98ba2d749636618744ce) |
|  | The number of times the Channel\_Map field will be cycled through for non-mode-0 steps within a CS procedure. |
| enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) | [channel\_selection\_type](#ac83ef36301b0d990cb3a7cf1e630c957) |
|  | Channel selection type. |
| enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) | [ch3c\_shape](#a14ac5115fa91bc7ed4a4aa7a0786f81f) |
|  | User-specified channel sequence shape. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ch3c\_jump](#ad0ea92b48ac4e9753ee422f2286c1ded) |
|  | Number of channels skipped in each rising and falling sequence. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_map](#adcf6276f58bd19ec61800160979fd472) [10] |
|  | Channel map used for CS procedure Channels n = 0, 1, 23, 24, 25, 77, and 78 are not allowed and shall be set to zero. |

## Detailed Description

CS Create Config params.

## Field Documentation

## [◆ ](#ad0ea92b48ac4e9753ee422f2286c1ded)ch3c\_jump

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::ch3c\_jump |
| --- |

Number of channels skipped in each rising and falling sequence.

## [◆ ](#a14ac5115fa91bc7ed4a4aa7a0786f81f)ch3c\_shape

| enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) bt\_le\_cs\_create\_config\_params::ch3c\_shape |
| --- |

User-specified channel sequence shape.

## [◆ ](#adcf6276f58bd19ec61800160979fd472)channel\_map

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::channel\_map[10] |
| --- |

Channel map used for CS procedure Channels n = 0, 1, 23, 24, 25, 77, and 78 are not allowed and shall be set to zero.

Channel 79 is reserved for future use and shall be set to zero. At least 15 channels shall be enabled.

## [◆ ](#a6eff424679cb98ba2d749636618744ce)channel\_map\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::channel\_map\_repetition |
| --- |

The number of times the Channel\_Map field will be cycled through for non-mode-0 steps within a CS procedure.

## [◆ ](#ac83ef36301b0d990cb3a7cf1e630c957)channel\_selection\_type

| enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) bt\_le\_cs\_create\_config\_params::channel\_selection\_type |
| --- |

Channel selection type.

## [◆ ](#a4329d967361e330077ca9064bdc3fc5f)cs\_sync\_phy

| enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) bt\_le\_cs\_create\_config\_params::cs\_sync\_phy |
| --- |

CS Sync PHY.

## [◆ ](#a59615f8de0a39f124ae3d2e2876ecc30)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::id |
| --- |

CS configuration ID.

## [◆ ](#a9a7c56e1d04d634aaab4f3b81c506be3)main\_mode\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::main\_mode\_repetition |
| --- |

Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning of the current CS subevent directly after the last mode-0 step of that event.

## [◆ ](#a2bdbff2e20106e4a6925a8018d491a9c)main\_mode\_type

| enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) bt\_le\_cs\_create\_config\_params::main\_mode\_type |
| --- |

Main CS mode type.

## [◆ ](#aa8951ab286210ab87c460ed315d091bf)max\_main\_mode\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::max\_main\_mode\_steps |
| --- |

Maximum number of CS main mode steps to be executed before a submode step is executed.

## [◆ ](#ae7ff30dcfcb4460dac48c139bdac0f75)min\_main\_mode\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::min\_main\_mode\_steps |
| --- |

Minimum number of CS main mode steps to be executed before a submode step is executed.

## [◆ ](#af824b6b56fba318588ebcf707d6e7a24)mode\_0\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_create\_config\_params::mode\_0\_steps |
| --- |

Number of CS mode-0 steps to be included at the beginning of each CS subevent.

## [◆ ](#a2581694b25afa7903786c7848c133c38)role

| enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) bt\_le\_cs\_create\_config\_params::role |
| --- |

CS role.

## [◆ ](#a0a34afa329e88af8fcbcff1a8b0a1bcd)rtt\_type

| enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) bt\_le\_cs\_create\_config\_params::rtt\_type |
| --- |

RTT type.

## [◆ ](#a1bec59da1343bbc70a575d6dbde56309)sub\_mode\_type

| enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) bt\_le\_cs\_create\_config\_params::sub\_mode\_type |
| --- |

Sub CS mode type.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[cs.h](cs_8h_source.md)

- [bt\_le\_cs\_create\_config\_params](structbt__le__cs__create__config__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
