---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__le__cs__config.html
original_path: doxygen/html/structbt__conn__le__cs__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_cs\_config Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Channel sounding configuration.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#aaf8f1ce04fd22b4ca4728bdcfce8bd4a) |
|  | CS configuration ID. |
| enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) | [main\_mode\_type](#a02b942d1def46476160ba8839ca9690f) |
|  | Main CS mode type. |
| enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) | [sub\_mode\_type](#a4ee4bf79283686e16d4737f546718c44) |
|  | Sub CS mode type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_main\_mode\_steps](#a2e59fb17cd932b7670b3e915684c2107) |
|  | Minimum number of CS main mode steps to be executed before a submode step is executed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_main\_mode\_steps](#aff70b37fac8a3bd94acb25d7bd06989b) |
|  | Maximum number of CS main mode steps to be executed before a submode step is executed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [main\_mode\_repetition](#a2e904438c579870ed96b5dccff239c18) |
|  | Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning of the current CS subevent directly after the last mode-0 step of that event. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode\_0\_steps](#a8eea68bffef759b4532b68a1ecbdd4f1) |
|  | Number of CS mode-0 steps to be included at the beginning of each CS subevent. |
| enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) | [role](#ad11f8bee028ad3eb59008d46dce2d5bd) |
|  | CS role. |
| enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) | [rtt\_type](#a194e3844373c57e714917d03ac82666d) |
|  | RTT type. |
| enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) | [cs\_sync\_phy](#a2051f559b41085c4b41743aaaaecf3a1) |
|  | CS Sync PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_map\_repetition](#a971ff7ba734dd71512af7f3850de364d) |
|  | The number of times the Channel\_Map field will be cycled through for non-mode-0 steps within a CS procedure. |
| enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) | [channel\_selection\_type](#a63b7027929a5c3ec7fd68f35343262ee) |
|  | Channel selection type. |
| enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) | [ch3c\_shape](#a9b64ecb0986e7e9995c29feaf105eeaa) |
|  | User-specified channel sequence shape. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ch3c\_jump](#afa2846689f1a9d5b9e124b1c9095154f) |
|  | Number of channels skipped in each rising and falling sequence. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_ip1\_time\_us](#aab9a1d8d09d7a439f1c4dd28b9dd05c4) |
|  | Interlude time in microseconds between the RTT packets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_ip2\_time\_us](#a8e650b50400a45040c02a88dfb30683c) |
|  | Interlude time in microseconds between the CS tones. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_fcs\_time\_us](#a29912bd291fa4da09bb5b196d747ca6b) |
|  | Time in microseconds for frequency changes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_pm\_time\_us](#ae7f1cc232df00b4543fdb2b2596b9bbf) |
|  | Time in microseconds for the phase measurement period of the CS tones. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_map](#a60f9d21629554d47556d0fe8d63dcae3) [10] |
|  | Channel map used for CS procedure Channels n = 0, 1, 23, 24, 25, 77, and 78 are not allowed and shall be set to zero. |

## Detailed Description

Channel sounding configuration.

## Field Documentation

## [◆ ](#afa2846689f1a9d5b9e124b1c9095154f)ch3c\_jump

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::ch3c\_jump |
| --- |

Number of channels skipped in each rising and falling sequence.

## [◆ ](#a9b64ecb0986e7e9995c29feaf105eeaa)ch3c\_shape

| enum [bt\_conn\_le\_cs\_ch3c\_shape](group__bt__conn.md#gaf2331ec1f1222de51fc4f30566e1c52b) bt\_conn\_le\_cs\_config::ch3c\_shape |
| --- |

User-specified channel sequence shape.

## [◆ ](#a60f9d21629554d47556d0fe8d63dcae3)channel\_map

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::channel\_map[10] |
| --- |

Channel map used for CS procedure Channels n = 0, 1, 23, 24, 25, 77, and 78 are not allowed and shall be set to zero.

Channel 79 is reserved for future use and shall be set to zero. At least 15 channels shall be enabled.

## [◆ ](#a971ff7ba734dd71512af7f3850de364d)channel\_map\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::channel\_map\_repetition |
| --- |

The number of times the Channel\_Map field will be cycled through for non-mode-0 steps within a CS procedure.

## [◆ ](#a63b7027929a5c3ec7fd68f35343262ee)channel\_selection\_type

| enum [bt\_conn\_le\_cs\_chsel\_type](group__bt__conn.md#ga34e4837a77c7afd6999095985ddad4f0) bt\_conn\_le\_cs\_config::channel\_selection\_type |
| --- |

Channel selection type.

## [◆ ](#a2051f559b41085c4b41743aaaaecf3a1)cs\_sync\_phy

| enum [bt\_conn\_le\_cs\_sync\_phy](group__bt__conn.md#gaadbf6a4dba28aec90ea07b7da634e1bb) bt\_conn\_le\_cs\_config::cs\_sync\_phy |
| --- |

CS Sync PHY.

## [◆ ](#aaf8f1ce04fd22b4ca4728bdcfce8bd4a)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::id |
| --- |

CS configuration ID.

## [◆ ](#a2e904438c579870ed96b5dccff239c18)main\_mode\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::main\_mode\_repetition |
| --- |

Number of main mode steps taken from the end of the last CS subevent to be repeated at the beginning of the current CS subevent directly after the last mode-0 step of that event.

## [◆ ](#a02b942d1def46476160ba8839ca9690f)main\_mode\_type

| enum [bt\_conn\_le\_cs\_main\_mode](group__bt__conn.md#ga133504278b6e01993ff36e96a238484f) bt\_conn\_le\_cs\_config::main\_mode\_type |
| --- |

Main CS mode type.

## [◆ ](#aff70b37fac8a3bd94acb25d7bd06989b)max\_main\_mode\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::max\_main\_mode\_steps |
| --- |

Maximum number of CS main mode steps to be executed before a submode step is executed.

## [◆ ](#a2e59fb17cd932b7670b3e915684c2107)min\_main\_mode\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::min\_main\_mode\_steps |
| --- |

Minimum number of CS main mode steps to be executed before a submode step is executed.

## [◆ ](#a8eea68bffef759b4532b68a1ecbdd4f1)mode\_0\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::mode\_0\_steps |
| --- |

Number of CS mode-0 steps to be included at the beginning of each CS subevent.

## [◆ ](#ad11f8bee028ad3eb59008d46dce2d5bd)role

| enum [bt\_conn\_le\_cs\_role](group__bt__conn.md#ga0e6f6d4fdbdfc3ed75fef4a95136076f) bt\_conn\_le\_cs\_config::role |
| --- |

CS role.

## [◆ ](#a194e3844373c57e714917d03ac82666d)rtt\_type

| enum [bt\_conn\_le\_cs\_rtt\_type](group__bt__conn.md#gaffd6abf9b92cc8d8463797a73b840f51) bt\_conn\_le\_cs\_config::rtt\_type |
| --- |

RTT type.

## [◆ ](#a4ee4bf79283686e16d4737f546718c44)sub\_mode\_type

| enum [bt\_conn\_le\_cs\_sub\_mode](group__bt__conn.md#ga07c6f1248c9a6da0168bd3d398925daf) bt\_conn\_le\_cs\_config::sub\_mode\_type |
| --- |

Sub CS mode type.

## [◆ ](#a29912bd291fa4da09bb5b196d747ca6b)t\_fcs\_time\_us

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::t\_fcs\_time\_us |
| --- |

Time in microseconds for frequency changes.

## [◆ ](#aab9a1d8d09d7a439f1c4dd28b9dd05c4)t\_ip1\_time\_us

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::t\_ip1\_time\_us |
| --- |

Interlude time in microseconds between the RTT packets.

## [◆ ](#a8e650b50400a45040c02a88dfb30683c)t\_ip2\_time\_us

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::t\_ip2\_time\_us |
| --- |

Interlude time in microseconds between the CS tones.

## [◆ ](#ae7f1cc232df00b4543fdb2b2596b9bbf)t\_pm\_time\_us

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_cs\_config::t\_pm\_time\_us |
| --- |

Time in microseconds for the phase measurement period of the CS tones.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_cs\_config](structbt__conn__le__cs__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
