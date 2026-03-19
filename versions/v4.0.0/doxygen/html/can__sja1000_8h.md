---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/can__sja1000_8h.html
original_path: doxygen/html/can__sja1000_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_sja1000.h File Reference

API for NXP SJA1000 (and compatible) CAN controller frontend drivers.
[More...](#details)

`#include <[zephyr/drivers/can.h](drivers_2can_8h_source.md)>`

[Go to the source code of this file.](can__sja1000_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [can\_sja1000\_config](structcan__sja1000__config.md) |
|  | SJA1000 driver internal configuration structure. [More...](structcan__sja1000__config.md#details) |
| struct | [can\_sja1000\_rx\_filter](structcan__sja1000__rx__filter.md) |
|  | SJA1000 driver internal RX filter structure. [More...](structcan__sja1000__rx__filter.md#details) |
| struct | [can\_sja1000\_data](structcan__sja1000__data.md) |
|  | SJA1000 driver internal data structure. [More...](structcan__sja1000__data.md#details) |

| Macros | |
| --- | --- |
| #define | [CAN\_SJA1000\_TIMING\_MIN\_INITIALIZER](#ad396485923ad20b9662e56ae10128e4c) |
|  | SJA1000 specific static initializer for a minimum `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct. |
| #define | [CAN\_SJA1000\_TIMING\_MAX\_INITIALIZER](#a245230e39b3f9eca9f1a76a1926606ab) |
|  | SJA1000 specific static initializer for a maximum `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct. |
| #define | [CAN\_SJA1000\_DT\_CONFIG\_GET](#a3eda68391dfee872be4b49319d0b7437)(node\_id, \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \_min\_bitrate) |
|  | Static initializer for `[can_sja1000_config](structcan__sja1000__config.md "SJA1000 driver internal configuration structure.")` struct. |
| #define | [CAN\_SJA1000\_DT\_CONFIG\_INST\_GET](#adf7ef5e56f8acbf0a63ca7e912976d15)(inst, \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \_min\_bitrate) |
|  | Static initializer for `[can_sja1000_config](structcan__sja1000__config.md "SJA1000 driver internal configuration structure.")` struct from a DT\_DRV\_COMPAT instance. |
| #define | [CAN\_SJA1000\_DATA\_INITIALIZER](#a21aae4f3884e9737b15050fbe55d9bea)(\_custom) |
|  | Initializer for a *[can\_sja1000\_data](structcan__sja1000__data.md "SJA1000 driver internal data structure.")* struct. |
| SJA1000 Output Control Register (OCR) bits | |
| #define | [CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| #define | [CAN\_SJA1000\_OCR\_OCPOL0](#adbaaa75df320478924377688a677d872)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAN\_SJA1000\_OCR\_OCTN0](#aa931c0fc46923cab133022c4639a9918)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [CAN\_SJA1000\_OCR\_OCTP0](#a80684f0201ebb730fc14410e84e96df2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAN\_SJA1000\_OCR\_OCPOL1](#a983df1be96b35bd9e49c3c579d0cb40b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_SJA1000\_OCR\_OCTN1](#a1c2af47c7bcaf0dd4c98f2185c8548b4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_SJA1000\_OCR\_OCTP1](#a838dfca73332736247f77c5116c93c45)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_SJA1000\_OCR\_OCMODE\_BIPHASE](#a48aa18105fe36f1cf4db8b1a5a4c0ec0)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 0U) |
| #define | [CAN\_SJA1000\_OCR\_OCMODE\_TEST](#a6a59fcd698e2a066ada853b09a0b71fa)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 1U) |
| #define | [CAN\_SJA1000\_OCR\_OCMODE\_NORMAL](#aab6b947d5201325b3293c26418733ed0)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 2U) |
| #define | [CAN\_SJA1000\_OCR\_OCMODE\_CLOCK](#a00c2a29b797bf50ba4addb5b684cec7d)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 3U) |
| SJA1000 Clock Divider Register (CDR) bits | |
| #define | [CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| #define | [CAN\_SJA1000\_CDR\_CLOCK\_OFF](#af8eb9626285ac4ad3a917b84731669fb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [CAN\_SJA1000\_CDR\_RXINTEN](#a5f35936e647d82aab0240e8f1628070f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_SJA1000\_CDR\_CBP](#a9073e03d7173af238b28efb819969f6f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_SJA1000\_CDR\_CAN\_MODE](#a3929d82be73cc8d8010867fd5a0f3ad7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV1](#af581ccabd33280a269fe4420d5be0635)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 7U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV2](#aa744e2ade8c6dd6a93556039ba77dc06)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 0U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV4](#a6db863734edfd04eb36ca83f22802b56)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 1U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV6](#a038f3f02a964491b8a2f6e6bec1b09c6)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 2U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV8](#a8b3eccd70614f1c23db969935505fba5)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 3U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV10](#ae09ac444faeb0edd9e5d0889e33e5037)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 4U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV12](#a4bc39dfcd67d59b360015b5d4819d4ae)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 5U) |
| #define | [CAN\_SJA1000\_CDR\_CD\_DIV14](#a326fd4317bce6a3b82d1ed57fd4fc1bf)   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 6U) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [can\_sja1000\_write\_reg\_t](#a7f71e5009721c00f2d6821a7db4c49cb)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | SJA1000 driver front-end callback for writing a register value. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [can\_sja1000\_read\_reg\_t](#a62d5b661f7b39f84f93a9597d2371341)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg) |
|  | SJA1000 driver front-end callback for reading a register value. |

| Functions | |
| --- | --- |
| int | [can\_sja1000\_set\_timing](#a8b36e7b0defa598d4ebcd5997e714209) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing) |
|  | SJA1000 callback API upon setting CAN bus timing See *[can\_set\_timing()](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da "Configure the bus timing of a CAN controller.")* for argument description. |
| int | [can\_sja1000\_get\_capabilities](#a867ba15d4e2d94800d902b97db1e0482) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap) |
|  | SJA1000 callback API upon getting CAN controller capabilities See *[can\_get\_capabilities()](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168 "Get the supported modes of the CAN controller.")* for argument description. |
| int | [can\_sja1000\_start](#ad5f343d57184fa3adf7d248fe49e97d3) (const struct [device](structdevice.md) \*dev) |
|  | SJA1000 callback API upon starting CAN controller See *[can\_start()](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a "Start the CAN controller.")* for argument description. |
| int | [can\_sja1000\_stop](#a90d251f5a048f2688b111e6a4f8165fb) (const struct [device](structdevice.md) \*dev) |
|  | SJA1000 callback API upon stopping CAN controller See *[can\_stop()](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5 "Stop the CAN controller.")* for argument description. |
| int | [can\_sja1000\_set\_mode](#aee809bd3edef0fd08eaad6ef9270f5cc) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode) |
|  | SJA1000 callback API upon setting CAN controller mode See *[can\_set\_mode()](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f "Set the CAN controller to the given operation mode.")* for argument description. |
| int | [can\_sja1000\_send](#ab050fab94165f1ab532f8a4a9ca0748c) (const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame, [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback, void \*user\_data) |
|  | SJA1000 callback API upon sending a CAN frame See *[can\_send()](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5 "Queue a CAN frame for transmission on the CAN bus.")* for argument description. |
| int | [can\_sja1000\_add\_rx\_filter](#a5c7c6edb274a773fd863fac96412fa0d) (const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback, void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | SJA1000 callback API upon adding an RX filter See *can\_add\_rx\_callback()* for argument description. |
| void | [can\_sja1000\_remove\_rx\_filter](#a5b436ad6663d3dddb7f28ec03b520b25) (const struct [device](structdevice.md) \*dev, int filter\_id) |
|  | SJA1000 callback API upon removing an RX filter See *[can\_remove\_rx\_filter()](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847 "Remove a CAN RX filter.")* for argument description. |
| int | [can\_sja1000\_get\_state](#a939a87f8181236c5dbe18ba7865c1b4b) (const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt) |
|  | SJA1000 callback API upon getting the CAN controller state See *[can\_get\_state()](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857 "Get current CAN controller state.")* for argument description. |
| void | [can\_sja1000\_set\_state\_change\_callback](#a34df509dde4faa3ee45e6e5e0b42649e) (const struct [device](structdevice.md) \*dev, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback, void \*user\_data) |
|  | SJA1000 callback API upon setting a state change callback See *[can\_set\_state\_change\_callback()](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e "Set a callback for CAN controller state change events.")* for argument description. |
| int | [can\_sja1000\_get\_max\_filters](#a19ee7bbdee6b66b2b2ed5071ac881403) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ide) |
|  | SJA1000 callback API upon getting the maximum number of concurrent CAN RX filters See *[can\_get\_max\_filters()](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc "Get maximum number of RX filters.")* for argument description. |
| void | [can\_sja1000\_isr](#a65df5350d4191fa93f7ea8054d6139c3) (const struct [device](structdevice.md) \*dev) |
|  | SJA1000 IRQ handler callback. |
| int | [can\_sja1000\_init](#a5150ea6d32a3d111e5b130b60f63eb82) (const struct [device](structdevice.md) \*dev) |
|  | SJA1000 driver initialization callback. |

## Detailed Description

API for NXP SJA1000 (and compatible) CAN controller frontend drivers.

## Macro Definition Documentation

## [◆ ](#a3929d82be73cc8d8010867fd5a0f3ad7)CAN\_SJA1000\_CDR\_CAN\_MODE

| #define CAN\_SJA1000\_CDR\_CAN\_MODE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a9073e03d7173af238b28efb819969f6f)CAN\_SJA1000\_CDR\_CBP

| #define CAN\_SJA1000\_CDR\_CBP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#af581ccabd33280a269fe4420d5be0635)CAN\_SJA1000\_CDR\_CD\_DIV1

| #define CAN\_SJA1000\_CDR\_CD\_DIV1   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 7U) |
| --- |

## [◆ ](#ae09ac444faeb0edd9e5d0889e33e5037)CAN\_SJA1000\_CDR\_CD\_DIV10

| #define CAN\_SJA1000\_CDR\_CD\_DIV10   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 4U) |
| --- |

## [◆ ](#a4bc39dfcd67d59b360015b5d4819d4ae)CAN\_SJA1000\_CDR\_CD\_DIV12

| #define CAN\_SJA1000\_CDR\_CD\_DIV12   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 5U) |
| --- |

## [◆ ](#a326fd4317bce6a3b82d1ed57fd4fc1bf)CAN\_SJA1000\_CDR\_CD\_DIV14

| #define CAN\_SJA1000\_CDR\_CD\_DIV14   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 6U) |
| --- |

## [◆ ](#aa744e2ade8c6dd6a93556039ba77dc06)CAN\_SJA1000\_CDR\_CD\_DIV2

| #define CAN\_SJA1000\_CDR\_CD\_DIV2   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 0U) |
| --- |

## [◆ ](#a6db863734edfd04eb36ca83f22802b56)CAN\_SJA1000\_CDR\_CD\_DIV4

| #define CAN\_SJA1000\_CDR\_CD\_DIV4   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 1U) |
| --- |

## [◆ ](#a038f3f02a964491b8a2f6e6bec1b09c6)CAN\_SJA1000\_CDR\_CD\_DIV6

| #define CAN\_SJA1000\_CDR\_CD\_DIV6   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 2U) |
| --- |

## [◆ ](#a8b3eccd70614f1c23db969935505fba5)CAN\_SJA1000\_CDR\_CD\_DIV8

| #define CAN\_SJA1000\_CDR\_CD\_DIV8   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_CDR\_CD\_MASK](#a86033d45850acb3b5984a257ecb935ad), 3U) |
| --- |

## [◆ ](#a86033d45850acb3b5984a257ecb935ad)CAN\_SJA1000\_CDR\_CD\_MASK

| #define CAN\_SJA1000\_CDR\_CD\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

## [◆ ](#af8eb9626285ac4ad3a917b84731669fb)CAN\_SJA1000\_CDR\_CLOCK\_OFF

| #define CAN\_SJA1000\_CDR\_CLOCK\_OFF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a5f35936e647d82aab0240e8f1628070f)CAN\_SJA1000\_CDR\_RXINTEN

| #define CAN\_SJA1000\_CDR\_RXINTEN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a21aae4f3884e9737b15050fbe55d9bea)CAN\_SJA1000\_DATA\_INITIALIZER

| #define CAN\_SJA1000\_DATA\_INITIALIZER | ( |  | *\_custom* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.custom = \_custom, \

}

Initializer for a *[can\_sja1000\_data](structcan__sja1000__data.md "SJA1000 driver internal data structure.")* struct.

Parameters
:   | \_custom | Pointer to custom driver frontend data structure |
    | --- | --- |

## [◆ ](#a3eda68391dfee872be4b49319d0b7437)CAN\_SJA1000\_DT\_CONFIG\_GET

| #define CAN\_SJA1000\_DT\_CONFIG\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_custom*, |
|  |  |  | *\_read\_reg*, |
|  |  |  | *\_write\_reg*, |
|  |  |  | *\_ocr*, |
|  |  |  | *\_cdr*, |
|  |  |  | *\_min\_bitrate* ) |

**Value:**

{ \

.common = CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, \_min\_bitrate, 1000000), \

.read\_reg = \_read\_reg, \

.write\_reg = \_write\_reg, \

.ocr = \_ocr, \

.cdr = \_cdr, \

.custom = \_custom, \

}

Static initializer for `[can_sja1000_config](structcan__sja1000__config.md "SJA1000 driver internal configuration structure.")` struct.

Parameters
:   | node\_id | Devicetree node identifier |
    | --- | --- |
    | \_custom | Pointer to custom driver frontend configuration structure |
    | \_read\_reg | Driver frontend SJA100 register read function |
    | \_write\_reg | Driver frontend SJA100 register write function |
    | \_ocr | Initial SJA1000 Output Control Register (OCR) value |
    | \_cdr | Initial SJA1000 Clock Divider Register (CDR) value |
    | \_min\_bitrate | minimum bitrate supported by the CAN controller |

## [◆ ](#adf7ef5e56f8acbf0a63ca7e912976d15)CAN\_SJA1000\_DT\_CONFIG\_INST\_GET

| #define CAN\_SJA1000\_DT\_CONFIG\_INST\_GET | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_custom*, |
|  |  |  | *\_read\_reg*, |
|  |  |  | *\_write\_reg*, |
|  |  |  | *\_ocr*, |
|  |  |  | *\_cdr*, |
|  |  |  | *\_min\_bitrate* ) |

**Value:**

[CAN\_SJA1000\_DT\_CONFIG\_GET](#a3eda68391dfee872be4b49319d0b7437)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \

\_min\_bitrate)

[CAN\_SJA1000\_DT\_CONFIG\_GET](#a3eda68391dfee872be4b49319d0b7437)

#define CAN\_SJA1000\_DT\_CONFIG\_GET(node\_id, \_custom, \_read\_reg, \_write\_reg, \_ocr, \_cdr, \_min\_bitrate)

Static initializer for can\_sja1000\_config struct.

**Definition** can\_sja1000.h:124

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

Static initializer for `[can_sja1000_config](structcan__sja1000__config.md "SJA1000 driver internal configuration structure.")` struct from a DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | \_custom | Pointer to custom driver frontend configuration structure |
    | \_read\_reg | Driver frontend SJA100 register read function |
    | \_write\_reg | Driver frontend SJA100 register write function |
    | \_ocr | Initial SJA1000 Output Control Register (OCR) value |
    | \_cdr | Initial SJA1000 Clock Divider Register (CDR) value |
    | \_min\_bitrate | minimum bitrate supported by the CAN controller |

See also
:   [CAN\_SJA1000\_DT\_CONFIG\_GET()](#a3eda68391dfee872be4b49319d0b7437)

## [◆ ](#a48aa18105fe36f1cf4db8b1a5a4c0ec0)CAN\_SJA1000\_OCR\_OCMODE\_BIPHASE

| #define CAN\_SJA1000\_OCR\_OCMODE\_BIPHASE   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 0U) |
| --- |

## [◆ ](#a00c2a29b797bf50ba4addb5b684cec7d)CAN\_SJA1000\_OCR\_OCMODE\_CLOCK

| #define CAN\_SJA1000\_OCR\_OCMODE\_CLOCK   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 3U) |
| --- |

## [◆ ](#aa7c14df170465c5a86eab75170f9196a)CAN\_SJA1000\_OCR\_OCMODE\_MASK

| #define CAN\_SJA1000\_OCR\_OCMODE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

## [◆ ](#aab6b947d5201325b3293c26418733ed0)CAN\_SJA1000\_OCR\_OCMODE\_NORMAL

| #define CAN\_SJA1000\_OCR\_OCMODE\_NORMAL   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 2U) |
| --- |

## [◆ ](#a6a59fcd698e2a066ada853b09a0b71fa)CAN\_SJA1000\_OCR\_OCMODE\_TEST

| #define CAN\_SJA1000\_OCR\_OCMODE\_TEST   [FIELD\_PREP](group__sys-util.md#gaa03c8b31bf67a097dd9f8153a04ef86b)([CAN\_SJA1000\_OCR\_OCMODE\_MASK](#aa7c14df170465c5a86eab75170f9196a), 1U) |
| --- |

## [◆ ](#adbaaa75df320478924377688a677d872)CAN\_SJA1000\_OCR\_OCPOL0

| #define CAN\_SJA1000\_OCR\_OCPOL0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a983df1be96b35bd9e49c3c579d0cb40b)CAN\_SJA1000\_OCR\_OCPOL1

| #define CAN\_SJA1000\_OCR\_OCPOL1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#aa931c0fc46923cab133022c4639a9918)CAN\_SJA1000\_OCR\_OCTN0

| #define CAN\_SJA1000\_OCR\_OCTN0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a1c2af47c7bcaf0dd4c98f2185c8548b4)CAN\_SJA1000\_OCR\_OCTN1

| #define CAN\_SJA1000\_OCR\_OCTN1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a80684f0201ebb730fc14410e84e96df2)CAN\_SJA1000\_OCR\_OCTP0

| #define CAN\_SJA1000\_OCR\_OCTP0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a838dfca73332736247f77c5116c93c45)CAN\_SJA1000\_OCR\_OCTP1

| #define CAN\_SJA1000\_OCR\_OCTP1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a245230e39b3f9eca9f1a76a1926606ab)CAN\_SJA1000\_TIMING\_MAX\_INITIALIZER

| #define CAN\_SJA1000\_TIMING\_MAX\_INITIALIZER |
| --- |

**Value:**

{ \

.sjw = 4, \

.prop\_seg = 0, \

.phase\_seg1 = 16, \

.phase\_seg2 = 8, \

.prescaler = 64 \

}

SJA1000 specific static initializer for a maximum `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct.

## [◆ ](#ad396485923ad20b9662e56ae10128e4c)CAN\_SJA1000\_TIMING\_MIN\_INITIALIZER

| #define CAN\_SJA1000\_TIMING\_MIN\_INITIALIZER |
| --- |

**Value:**

{ \

.sjw = 1, \

.prop\_seg = 0, \

.phase\_seg1 = 1, \

.phase\_seg2 = 1, \

.prescaler = 1 \

}

SJA1000 specific static initializer for a minimum `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct.

## Typedef Documentation

## [◆ ](#a62d5b661f7b39f84f93a9597d2371341)can\_sja1000\_read\_reg\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* can\_sja1000\_read\_reg\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg) |
| --- |

SJA1000 driver front-end callback for reading a register value.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | reg | Register offset |

Return values
:   | Register | value |
    | --- | --- |

## [◆ ](#a7f71e5009721c00f2d6821a7db4c49cb)can\_sja1000\_write\_reg\_t

| typedef void(\* can\_sja1000\_write\_reg\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
| --- |

SJA1000 driver front-end callback for writing a register value.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | reg | Register offset |
    | val | Register value |

## Function Documentation

## [◆ ](#a5c7c6edb274a773fd863fac96412fa0d)can\_sja1000\_add\_rx\_filter()

| int can\_sja1000\_add\_rx\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) | *callback*, |
|  |  | void \* | *user\_data*, |
|  |  | const struct [can\_filter](structcan__filter.md) \* | *filter* ) |

SJA1000 callback API upon adding an RX filter See *can\_add\_rx\_callback()* for argument description.

## [◆ ](#a867ba15d4e2d94800d902b97db1e0482)can\_sja1000\_get\_capabilities()

| int can\_sja1000\_get\_capabilities | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \* | *cap* ) |

SJA1000 callback API upon getting CAN controller capabilities See *[can\_get\_capabilities()](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168 "Get the supported modes of the CAN controller.")* for argument description.

## [◆ ](#a19ee7bbdee6b66b2b2ed5071ac881403)can\_sja1000\_get\_max\_filters()

| int can\_sja1000\_get\_max\_filters | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ide* ) |

SJA1000 callback API upon getting the maximum number of concurrent CAN RX filters See *[can\_get\_max\_filters()](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc "Get maximum number of RX filters.")* for argument description.

## [◆ ](#a939a87f8181236c5dbe18ba7865c1b4b)can\_sja1000\_get\_state()

| int can\_sja1000\_get\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \* | *state*, |
|  |  | struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \* | *err\_cnt* ) |

SJA1000 callback API upon getting the CAN controller state See *[can\_get\_state()](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857 "Get current CAN controller state.")* for argument description.

## [◆ ](#a5150ea6d32a3d111e5b130b60f63eb82)can\_sja1000\_init()

| int can\_sja1000\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

SJA1000 driver initialization callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#a65df5350d4191fa93f7ea8054d6139c3)can\_sja1000\_isr()

| void can\_sja1000\_isr | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

SJA1000 IRQ handler callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#a5b436ad6663d3dddb7f28ec03b520b25)can\_sja1000\_remove\_rx\_filter()

| void can\_sja1000\_remove\_rx\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *filter\_id* ) |

SJA1000 callback API upon removing an RX filter See *[can\_remove\_rx\_filter()](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847 "Remove a CAN RX filter.")* for argument description.

## [◆ ](#ab050fab94165f1ab532f8a4a9ca0748c)can\_sja1000\_send()

| int can\_sja1000\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_frame](structcan__frame.md) \* | *frame*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) | *callback*, |
|  |  | void \* | *user\_data* ) |

SJA1000 callback API upon sending a CAN frame See *[can\_send()](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5 "Queue a CAN frame for transmission on the CAN bus.")* for argument description.

## [◆ ](#aee809bd3edef0fd08eaad6ef9270f5cc)can\_sja1000\_set\_mode()

| int can\_sja1000\_set\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | *mode* ) |

SJA1000 callback API upon setting CAN controller mode See *[can\_set\_mode()](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f "Set the CAN controller to the given operation mode.")* for argument description.

## [◆ ](#a34df509dde4faa3ee45e6e5e0b42649e)can\_sja1000\_set\_state\_change\_callback()

| void can\_sja1000\_set\_state\_change\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) | *callback*, |
|  |  | void \* | *user\_data* ) |

SJA1000 callback API upon setting a state change callback See *[can\_set\_state\_change\_callback()](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e "Set a callback for CAN controller state change events.")* for argument description.

## [◆ ](#a8b36e7b0defa598d4ebcd5997e714209)can\_sja1000\_set\_timing()

| int can\_sja1000\_set\_timing | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *timing* ) |

SJA1000 callback API upon setting CAN bus timing See *[can\_set\_timing()](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da "Configure the bus timing of a CAN controller.")* for argument description.

## [◆ ](#ad5f343d57184fa3adf7d248fe49e97d3)can\_sja1000\_start()

| int can\_sja1000\_start | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

SJA1000 callback API upon starting CAN controller See *[can\_start()](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a "Start the CAN controller.")* for argument description.

## [◆ ](#a90d251f5a048f2688b111e6a4f8165fb)can\_sja1000\_stop()

| int can\_sja1000\_stop | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

SJA1000 callback API upon stopping CAN controller See *[can\_stop()](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5 "Stop the CAN controller.")* for argument description.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [can\_sja1000.h](can__sja1000_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
