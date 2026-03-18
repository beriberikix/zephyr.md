---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pd_8h.html
original_path: doxygen/html/pd_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd.h File Reference

[Go to the source code of this file.](pd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PDO\_TYPE\_FIXED](#a6696a76fb9196a66939b81bb7288402d)   0 |
| #define | [PDO\_TYPE\_BATT](#a45dd0576f017e7c246bafc798ea33b32)   1 |
| #define | [PDO\_TYPE\_VAR](#a017a6b931cfbb3bd2a9958f0010fcb3d)   2 |
| #define | [PDO\_TYPE\_APDO](#ae34a1d74ce1a88355bdca50ee5ebd5d9)   3 |
| #define | [PDO\_TYPE\_SHIFT](#a194c22d06729436e5e0b9e80db85d157)   30 |
| #define | [PDO\_TYPE\_MASK](#a1e9f657ac9a2a7bafa774e55ae5eb1b7)   0x3 |
| #define | [PDO\_TYPE](#adc26e319ccbe5212476507dd6e70fbd7)(t) |
| #define | [PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)   0x3ff |
| #define | [PDO\_CURR\_MASK](#aed2ef8943d23c433e924c51939f3783a)   0x3ff |
| #define | [PDO\_PWR\_MASK](#a413d2bcbc7bb4748868c665d85f01c79)   0x3ff |
| #define | [PDO\_FIXED\_DUAL\_ROLE](#a06df29b5b810f22013ad2135cb0238ea)   (1 << 29) /\* Power role swap supported \*/ |
| #define | [PDO\_FIXED\_SUSPEND](#a869842bccecddf1941826fba3399f735)   (1 << 28) /\* USB Suspend supported (Source) \*/ |
| #define | [PDO\_FIXED\_HIGHER\_CAP](#ae7692e9c32e7c6ee2cf8e4c84d0752d8)   (1 << 28) /\* Requires more than vSafe5V (Sink) \*/ |
| #define | [PDO\_FIXED\_EXTPOWER](#a9e098ecbd9e7b74052fcbf302a0f6a41)   (1 << 27) /\* Externally powered \*/ |
| #define | [PDO\_FIXED\_USB\_COMM](#a398ebc832c89bd8cbccd08b3def758dd)   (1 << 26) /\* USB communications capable \*/ |
| #define | [PDO\_FIXED\_DATA\_SWAP](#a17760e6fb2761a8d14d41f1f44993c3b)   (1 << 25) /\* Data role swap supported \*/ |
| #define | [PDO\_FIXED\_VOLT\_SHIFT](#a3742e41a81b5a58bba31237993e1415d)   10 /\* 50mV units \*/ |
| #define | [PDO\_FIXED\_CURR\_SHIFT](#a40951b7090fb5345b9160ba9bee5ff6f)   0 /\* 10mA units \*/ |
| #define | [PDO\_FIXED\_VOLT](#ac084b8a13ba4b179054feb6e4cc806ee)(mv) |
| #define | [PDO\_FIXED\_CURR](#a565f2b493b29406d391581e23cfe7c55)(ma) |
| #define | [PDO\_FIXED](#a9fa615ab7f38385c21277d4e9e6a1441)(mv, ma, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| #define | [VSAFE5V](#ae3c4f39fb7ff5b00bdc25676af3b88f7)   5000 /\* mv units \*/ |
| #define | [PDO\_BATT\_MAX\_VOLT\_SHIFT](#a901fc8fe941e77426090cd631f973f58)   20 /\* 50mV units \*/ |
| #define | [PDO\_BATT\_MIN\_VOLT\_SHIFT](#ac6cfbddae5f56f963153813597fefe36)   10 /\* 50mV units \*/ |
| #define | [PDO\_BATT\_MAX\_PWR\_SHIFT](#a055085209166ac4aaf53dd3391f5755d)   0 /\* 250mW units \*/ |
| #define | [PDO\_BATT\_MIN\_VOLT](#add0856842113d1368e4fefc81ed4a268)(mv) |
| #define | [PDO\_BATT\_MAX\_VOLT](#af4d54399ae043b87fd39563aca66ec76)(mv) |
| #define | [PDO\_BATT\_MAX\_POWER](#a13827f707f980bda4359191ba17e1f43)(mw) |
| #define | [PDO\_BATT](#a37daa9cc2b8482e127d31c2f3ea4e7ed)(min\_mv, max\_mv, max\_mw) |
| #define | [PDO\_VAR\_MAX\_VOLT\_SHIFT](#acdb43c5ba716e1c8ac98923a99c6c714)   20 /\* 50mV units \*/ |
| #define | [PDO\_VAR\_MIN\_VOLT\_SHIFT](#a718ca0a2cc3f17ff8cf0f4e1ba9ed6a7)   10 /\* 50mV units \*/ |
| #define | [PDO\_VAR\_MAX\_CURR\_SHIFT](#afa16fcdf0864263bbe31d7f6c7370fcb)   0 /\* 10mA units \*/ |
| #define | [PDO\_VAR\_MIN\_VOLT](#a4e1d88119e9b14ffd5ebeafe4a04612a)(mv) |
| #define | [PDO\_VAR\_MAX\_VOLT](#a93d66b588325ac868279a44990623a11)(mv) |
| #define | [PDO\_VAR\_MAX\_CURR](#afdbaa131df861f379c482e0672b97367)(ma) |
| #define | [PDO\_VAR](#a359cf8ce52c69924cd2962b2a766f794)(min\_mv, max\_mv, max\_ma) |
| #define | [APDO\_TYPE\_PPS](#aa48ea0300d5342ef46c5c56ee73bca24)   0 |
| #define | [PDO\_APDO\_TYPE\_SHIFT](#acbed8599e3d5edf52987fde3949a1933)   28 /\* Only valid value currently is 0x0 - PPS \*/ |
| #define | [PDO\_APDO\_TYPE\_MASK](#a4abb13b016cd5d491c0c80495e24d89f)   0x3 |
| #define | [PDO\_APDO\_TYPE](#ad52459e0b7390f0545d38c880128c636)(t) |
| #define | [PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT](#a4582653b731dcaad55436deff9a4ae1f)   17 /\* 100mV units \*/ |
| #define | [PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT](#aaa6c1342446f4fbf7809359b1b59f168)   8 /\* 100mV units \*/ |
| #define | [PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT](#a5c5db3948d197b4611efde32f2374293)   0 /\* 50mA units \*/ |
| #define | [PDO\_PPS\_APDO\_VOLT\_MASK](#a0d66b7f12dd1750b673e9d01d5be70a3)   0xff |
| #define | [PDO\_PPS\_APDO\_CURR\_MASK](#a4d9e457e3c28050906b384bdf0a2f0d9)   0x7f |
| #define | [PDO\_PPS\_APDO\_MIN\_VOLT](#a7c1be180ef537b8104da38724e373e23)(mv) |
| #define | [PDO\_PPS\_APDO\_MAX\_VOLT](#aae9701858816813852e5bff5c814a118)(mv) |
| #define | [PDO\_PPS\_APDO\_MAX\_CURR](#a0eaeee90e4fa809690563a92f829aef2)(ma) |
| #define | [PDO\_PPS\_APDO](#a48f8ae89ab76eae6f27585b389f2b33b)(min\_mv, max\_mv, max\_ma) |

## Macro Definition Documentation

## [◆ ](#aa48ea0300d5342ef46c5c56ee73bca24)APDO\_TYPE\_PPS

| #define APDO\_TYPE\_PPS   0 |
| --- |

## [◆ ](#ad52459e0b7390f0545d38c880128c636)PDO\_APDO\_TYPE

| #define PDO\_APDO\_TYPE | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((t) << [PDO\_APDO\_TYPE\_SHIFT](#acbed8599e3d5edf52987fde3949a1933))

[PDO\_APDO\_TYPE\_SHIFT](#acbed8599e3d5edf52987fde3949a1933)

#define PDO\_APDO\_TYPE\_SHIFT

**Definition** pd.h:70

## [◆ ](#a4abb13b016cd5d491c0c80495e24d89f)PDO\_APDO\_TYPE\_MASK

| #define PDO\_APDO\_TYPE\_MASK   0x3 |
| --- |

## [◆ ](#acbed8599e3d5edf52987fde3949a1933)PDO\_APDO\_TYPE\_SHIFT

| #define PDO\_APDO\_TYPE\_SHIFT   28 /\* Only valid value currently is 0x0 - PPS \*/ |
| --- |

## [◆ ](#a37daa9cc2b8482e127d31c2f3ea4e7ed)PDO\_BATT

| #define PDO\_BATT | ( |  | *min\_mv*, |
| --- | --- | --- | --- |
|  |  |  | *max\_mv*, |
|  |  |  | *max\_mw* ) |

**Value:**

([PDO\_TYPE](#adc26e319ccbe5212476507dd6e70fbd7)([PDO\_TYPE\_BATT](#a45dd0576f017e7c246bafc798ea33b32)) | [PDO\_BATT\_MIN\_VOLT](#add0856842113d1368e4fefc81ed4a268)(min\_mv) | \

PDO\_BATT\_MAX\_VOLT(max\_mv) | [PDO\_BATT\_MAX\_POWER](#a13827f707f980bda4359191ba17e1f43)(max\_mw))

[PDO\_BATT\_MAX\_POWER](#a13827f707f980bda4359191ba17e1f43)

#define PDO\_BATT\_MAX\_POWER(mw)

**Definition** pd.h:50

[PDO\_TYPE\_BATT](#a45dd0576f017e7c246bafc798ea33b32)

#define PDO\_TYPE\_BATT

**Definition** pd.h:13

[PDO\_TYPE](#adc26e319ccbe5212476507dd6e70fbd7)

#define PDO\_TYPE(t)

**Definition** pd.h:20

[PDO\_BATT\_MIN\_VOLT](#add0856842113d1368e4fefc81ed4a268)

#define PDO\_BATT\_MIN\_VOLT(mv)

**Definition** pd.h:48

## [◆ ](#a13827f707f980bda4359191ba17e1f43)PDO\_BATT\_MAX\_POWER

| #define PDO\_BATT\_MAX\_POWER | ( |  | *mw* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mw) / 250) & [PDO\_PWR\_MASK](#a413d2bcbc7bb4748868c665d85f01c79)) << [PDO\_BATT\_MAX\_PWR\_SHIFT](#a055085209166ac4aaf53dd3391f5755d))

[PDO\_BATT\_MAX\_PWR\_SHIFT](#a055085209166ac4aaf53dd3391f5755d)

#define PDO\_BATT\_MAX\_PWR\_SHIFT

**Definition** pd.h:46

[PDO\_PWR\_MASK](#a413d2bcbc7bb4748868c665d85f01c79)

#define PDO\_PWR\_MASK

**Definition** pd.h:24

## [◆ ](#a055085209166ac4aaf53dd3391f5755d)PDO\_BATT\_MAX\_PWR\_SHIFT

| #define PDO\_BATT\_MAX\_PWR\_SHIFT   0 /\* 250mW units \*/ |
| --- |

## [◆ ](#af4d54399ae043b87fd39563aca66ec76)PDO\_BATT\_MAX\_VOLT

| #define PDO\_BATT\_MAX\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 50) & [PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)) << [PDO\_BATT\_MAX\_VOLT\_SHIFT](#a901fc8fe941e77426090cd631f973f58))

[PDO\_BATT\_MAX\_VOLT\_SHIFT](#a901fc8fe941e77426090cd631f973f58)

#define PDO\_BATT\_MAX\_VOLT\_SHIFT

**Definition** pd.h:44

[PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)

#define PDO\_VOLT\_MASK

**Definition** pd.h:22

## [◆ ](#a901fc8fe941e77426090cd631f973f58)PDO\_BATT\_MAX\_VOLT\_SHIFT

| #define PDO\_BATT\_MAX\_VOLT\_SHIFT   20 /\* 50mV units \*/ |
| --- |

## [◆ ](#add0856842113d1368e4fefc81ed4a268)PDO\_BATT\_MIN\_VOLT

| #define PDO\_BATT\_MIN\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 50) & [PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)) << [PDO\_BATT\_MIN\_VOLT\_SHIFT](#ac6cfbddae5f56f963153813597fefe36))

[PDO\_BATT\_MIN\_VOLT\_SHIFT](#ac6cfbddae5f56f963153813597fefe36)

#define PDO\_BATT\_MIN\_VOLT\_SHIFT

**Definition** pd.h:45

## [◆ ](#ac6cfbddae5f56f963153813597fefe36)PDO\_BATT\_MIN\_VOLT\_SHIFT

| #define PDO\_BATT\_MIN\_VOLT\_SHIFT   10 /\* 50mV units \*/ |
| --- |

## [◆ ](#aed2ef8943d23c433e924c51939f3783a)PDO\_CURR\_MASK

| #define PDO\_CURR\_MASK   0x3ff |
| --- |

## [◆ ](#a9fa615ab7f38385c21277d4e9e6a1441)PDO\_FIXED

| #define PDO\_FIXED | ( |  | *mv*, |
| --- | --- | --- | --- |
|  |  |  | *ma*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

**Value:**

([PDO\_TYPE](#adc26e319ccbe5212476507dd6e70fbd7)([PDO\_TYPE\_FIXED](#a6696a76fb9196a66939b81bb7288402d)) | ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) | \

[PDO\_FIXED\_VOLT](#ac084b8a13ba4b179054feb6e4cc806ee)(mv) | [PDO\_FIXED\_CURR](#a565f2b493b29406d391581e23cfe7c55)(ma))

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[PDO\_FIXED\_CURR](#a565f2b493b29406d391581e23cfe7c55)

#define PDO\_FIXED\_CURR(ma)

**Definition** pd.h:36

[PDO\_TYPE\_FIXED](#a6696a76fb9196a66939b81bb7288402d)

#define PDO\_TYPE\_FIXED

**Definition** pd.h:12

[PDO\_FIXED\_VOLT](#ac084b8a13ba4b179054feb6e4cc806ee)

#define PDO\_FIXED\_VOLT(mv)

**Definition** pd.h:35

## [◆ ](#a565f2b493b29406d391581e23cfe7c55)PDO\_FIXED\_CURR

| #define PDO\_FIXED\_CURR | ( |  | *ma* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((ma) / 10) & [PDO\_CURR\_MASK](#aed2ef8943d23c433e924c51939f3783a)) << [PDO\_FIXED\_CURR\_SHIFT](#a40951b7090fb5345b9160ba9bee5ff6f))

[PDO\_FIXED\_CURR\_SHIFT](#a40951b7090fb5345b9160ba9bee5ff6f)

#define PDO\_FIXED\_CURR\_SHIFT

**Definition** pd.h:33

[PDO\_CURR\_MASK](#aed2ef8943d23c433e924c51939f3783a)

#define PDO\_CURR\_MASK

**Definition** pd.h:23

## [◆ ](#a40951b7090fb5345b9160ba9bee5ff6f)PDO\_FIXED\_CURR\_SHIFT

| #define PDO\_FIXED\_CURR\_SHIFT   0 /\* 10mA units \*/ |
| --- |

## [◆ ](#a17760e6fb2761a8d14d41f1f44993c3b)PDO\_FIXED\_DATA\_SWAP

| #define PDO\_FIXED\_DATA\_SWAP   (1 << 25) /\* Data role swap supported \*/ |
| --- |

## [◆ ](#a06df29b5b810f22013ad2135cb0238ea)PDO\_FIXED\_DUAL\_ROLE

| #define PDO\_FIXED\_DUAL\_ROLE   (1 << 29) /\* Power role swap supported \*/ |
| --- |

## [◆ ](#a9e098ecbd9e7b74052fcbf302a0f6a41)PDO\_FIXED\_EXTPOWER

| #define PDO\_FIXED\_EXTPOWER   (1 << 27) /\* Externally powered \*/ |
| --- |

## [◆ ](#ae7692e9c32e7c6ee2cf8e4c84d0752d8)PDO\_FIXED\_HIGHER\_CAP

| #define PDO\_FIXED\_HIGHER\_CAP   (1 << 28) /\* Requires more than vSafe5V (Sink) \*/ |
| --- |

## [◆ ](#a869842bccecddf1941826fba3399f735)PDO\_FIXED\_SUSPEND

| #define PDO\_FIXED\_SUSPEND   (1 << 28) /\* USB Suspend supported (Source) \*/ |
| --- |

## [◆ ](#a398ebc832c89bd8cbccd08b3def758dd)PDO\_FIXED\_USB\_COMM

| #define PDO\_FIXED\_USB\_COMM   (1 << 26) /\* USB communications capable \*/ |
| --- |

## [◆ ](#ac084b8a13ba4b179054feb6e4cc806ee)PDO\_FIXED\_VOLT

| #define PDO\_FIXED\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 50) & [PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)) << [PDO\_FIXED\_VOLT\_SHIFT](#a3742e41a81b5a58bba31237993e1415d))

[PDO\_FIXED\_VOLT\_SHIFT](#a3742e41a81b5a58bba31237993e1415d)

#define PDO\_FIXED\_VOLT\_SHIFT

**Definition** pd.h:32

## [◆ ](#a3742e41a81b5a58bba31237993e1415d)PDO\_FIXED\_VOLT\_SHIFT

| #define PDO\_FIXED\_VOLT\_SHIFT   10 /\* 50mV units \*/ |
| --- |

## [◆ ](#a48f8ae89ab76eae6f27585b389f2b33b)PDO\_PPS\_APDO

| #define PDO\_PPS\_APDO | ( |  | *min\_mv*, |
| --- | --- | --- | --- |
|  |  |  | *max\_mv*, |
|  |  |  | *max\_ma* ) |

**Value:**

([PDO\_TYPE](#adc26e319ccbe5212476507dd6e70fbd7)([PDO\_TYPE\_APDO](#ae34a1d74ce1a88355bdca50ee5ebd5d9)) | [PDO\_APDO\_TYPE](#ad52459e0b7390f0545d38c880128c636)([APDO\_TYPE\_PPS](#aa48ea0300d5342ef46c5c56ee73bca24)) | \

PDO\_PPS\_APDO\_MIN\_VOLT(min\_mv) | [PDO\_PPS\_APDO\_MAX\_VOLT](#aae9701858816813852e5bff5c814a118)(max\_mv) | \

PDO\_PPS\_APDO\_MAX\_CURR(max\_ma))

[APDO\_TYPE\_PPS](#aa48ea0300d5342ef46c5c56ee73bca24)

#define APDO\_TYPE\_PPS

**Definition** pd.h:68

[PDO\_PPS\_APDO\_MAX\_VOLT](#aae9701858816813852e5bff5c814a118)

#define PDO\_PPS\_APDO\_MAX\_VOLT(mv)

**Definition** pd.h:84

[PDO\_APDO\_TYPE](#ad52459e0b7390f0545d38c880128c636)

#define PDO\_APDO\_TYPE(t)

**Definition** pd.h:73

[PDO\_TYPE\_APDO](#ae34a1d74ce1a88355bdca50ee5ebd5d9)

#define PDO\_TYPE\_APDO

**Definition** pd.h:15

## [◆ ](#a4d9e457e3c28050906b384bdf0a2f0d9)PDO\_PPS\_APDO\_CURR\_MASK

| #define PDO\_PPS\_APDO\_CURR\_MASK   0x7f |
| --- |

## [◆ ](#a0eaeee90e4fa809690563a92f829aef2)PDO\_PPS\_APDO\_MAX\_CURR

| #define PDO\_PPS\_APDO\_MAX\_CURR | ( |  | *ma* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((ma) / 50) & [PDO\_PPS\_APDO\_CURR\_MASK](#a4d9e457e3c28050906b384bdf0a2f0d9)) << [PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT](#a5c5db3948d197b4611efde32f2374293))

[PDO\_PPS\_APDO\_CURR\_MASK](#a4d9e457e3c28050906b384bdf0a2f0d9)

#define PDO\_PPS\_APDO\_CURR\_MASK

**Definition** pd.h:80

[PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT](#a5c5db3948d197b4611efde32f2374293)

#define PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT

**Definition** pd.h:77

## [◆ ](#a5c5db3948d197b4611efde32f2374293)PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT

| #define PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT   0 /\* 50mA units \*/ |
| --- |

## [◆ ](#aae9701858816813852e5bff5c814a118)PDO\_PPS\_APDO\_MAX\_VOLT

| #define PDO\_PPS\_APDO\_MAX\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 100) & [PDO\_PPS\_APDO\_VOLT\_MASK](#a0d66b7f12dd1750b673e9d01d5be70a3)) << [PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT](#a4582653b731dcaad55436deff9a4ae1f))

[PDO\_PPS\_APDO\_VOLT\_MASK](#a0d66b7f12dd1750b673e9d01d5be70a3)

#define PDO\_PPS\_APDO\_VOLT\_MASK

**Definition** pd.h:79

[PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT](#a4582653b731dcaad55436deff9a4ae1f)

#define PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT

**Definition** pd.h:75

## [◆ ](#a4582653b731dcaad55436deff9a4ae1f)PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT

| #define PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT   17 /\* 100mV units \*/ |
| --- |

## [◆ ](#a7c1be180ef537b8104da38724e373e23)PDO\_PPS\_APDO\_MIN\_VOLT

| #define PDO\_PPS\_APDO\_MIN\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 100) & [PDO\_PPS\_APDO\_VOLT\_MASK](#a0d66b7f12dd1750b673e9d01d5be70a3)) << [PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT](#aaa6c1342446f4fbf7809359b1b59f168))

[PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT](#aaa6c1342446f4fbf7809359b1b59f168)

#define PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT

**Definition** pd.h:76

## [◆ ](#aaa6c1342446f4fbf7809359b1b59f168)PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT

| #define PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT   8 /\* 100mV units \*/ |
| --- |

## [◆ ](#a0d66b7f12dd1750b673e9d01d5be70a3)PDO\_PPS\_APDO\_VOLT\_MASK

| #define PDO\_PPS\_APDO\_VOLT\_MASK   0xff |
| --- |

## [◆ ](#a413d2bcbc7bb4748868c665d85f01c79)PDO\_PWR\_MASK

| #define PDO\_PWR\_MASK   0x3ff |
| --- |

## [◆ ](#adc26e319ccbe5212476507dd6e70fbd7)PDO\_TYPE

| #define PDO\_TYPE | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((t) << [PDO\_TYPE\_SHIFT](#a194c22d06729436e5e0b9e80db85d157))

[PDO\_TYPE\_SHIFT](#a194c22d06729436e5e0b9e80db85d157)

#define PDO\_TYPE\_SHIFT

**Definition** pd.h:17

## [◆ ](#ae34a1d74ce1a88355bdca50ee5ebd5d9)PDO\_TYPE\_APDO

| #define PDO\_TYPE\_APDO   3 |
| --- |

## [◆ ](#a45dd0576f017e7c246bafc798ea33b32)PDO\_TYPE\_BATT

| #define PDO\_TYPE\_BATT   1 |
| --- |

## [◆ ](#a6696a76fb9196a66939b81bb7288402d)PDO\_TYPE\_FIXED

| #define PDO\_TYPE\_FIXED   0 |
| --- |

## [◆ ](#a1e9f657ac9a2a7bafa774e55ae5eb1b7)PDO\_TYPE\_MASK

| #define PDO\_TYPE\_MASK   0x3 |
| --- |

## [◆ ](#a194c22d06729436e5e0b9e80db85d157)PDO\_TYPE\_SHIFT

| #define PDO\_TYPE\_SHIFT   30 |
| --- |

## [◆ ](#a017a6b931cfbb3bd2a9958f0010fcb3d)PDO\_TYPE\_VAR

| #define PDO\_TYPE\_VAR   2 |
| --- |

## [◆ ](#a359cf8ce52c69924cd2962b2a766f794)PDO\_VAR

| #define PDO\_VAR | ( |  | *min\_mv*, |
| --- | --- | --- | --- |
|  |  |  | *max\_mv*, |
|  |  |  | *max\_ma* ) |

**Value:**

([PDO\_TYPE](#adc26e319ccbe5212476507dd6e70fbd7)([PDO\_TYPE\_VAR](#a017a6b931cfbb3bd2a9958f0010fcb3d)) | [PDO\_VAR\_MIN\_VOLT](#a4e1d88119e9b14ffd5ebeafe4a04612a)(min\_mv) | \

PDO\_VAR\_MAX\_VOLT(max\_mv) | [PDO\_VAR\_MAX\_CURR](#afdbaa131df861f379c482e0672b97367)(max\_ma))

[PDO\_TYPE\_VAR](#a017a6b931cfbb3bd2a9958f0010fcb3d)

#define PDO\_TYPE\_VAR

**Definition** pd.h:14

[PDO\_VAR\_MIN\_VOLT](#a4e1d88119e9b14ffd5ebeafe4a04612a)

#define PDO\_VAR\_MIN\_VOLT(mv)

**Definition** pd.h:60

[PDO\_VAR\_MAX\_CURR](#afdbaa131df861f379c482e0672b97367)

#define PDO\_VAR\_MAX\_CURR(ma)

**Definition** pd.h:62

## [◆ ](#afdbaa131df861f379c482e0672b97367)PDO\_VAR\_MAX\_CURR

| #define PDO\_VAR\_MAX\_CURR | ( |  | *ma* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((ma) / 10) & [PDO\_CURR\_MASK](#aed2ef8943d23c433e924c51939f3783a)) << [PDO\_VAR\_MAX\_CURR\_SHIFT](#afa16fcdf0864263bbe31d7f6c7370fcb))

[PDO\_VAR\_MAX\_CURR\_SHIFT](#afa16fcdf0864263bbe31d7f6c7370fcb)

#define PDO\_VAR\_MAX\_CURR\_SHIFT

**Definition** pd.h:58

## [◆ ](#afa16fcdf0864263bbe31d7f6c7370fcb)PDO\_VAR\_MAX\_CURR\_SHIFT

| #define PDO\_VAR\_MAX\_CURR\_SHIFT   0 /\* 10mA units \*/ |
| --- |

## [◆ ](#a93d66b588325ac868279a44990623a11)PDO\_VAR\_MAX\_VOLT

| #define PDO\_VAR\_MAX\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 50) & [PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)) << [PDO\_VAR\_MAX\_VOLT\_SHIFT](#acdb43c5ba716e1c8ac98923a99c6c714))

[PDO\_VAR\_MAX\_VOLT\_SHIFT](#acdb43c5ba716e1c8ac98923a99c6c714)

#define PDO\_VAR\_MAX\_VOLT\_SHIFT

**Definition** pd.h:56

## [◆ ](#acdb43c5ba716e1c8ac98923a99c6c714)PDO\_VAR\_MAX\_VOLT\_SHIFT

| #define PDO\_VAR\_MAX\_VOLT\_SHIFT   20 /\* 50mV units \*/ |
| --- |

## [◆ ](#a4e1d88119e9b14ffd5ebeafe4a04612a)PDO\_VAR\_MIN\_VOLT

| #define PDO\_VAR\_MIN\_VOLT | ( |  | *mv* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((mv) / 50) & [PDO\_VOLT\_MASK](#ac41dc08efe8dfeeb1a9737e0b187c683)) << [PDO\_VAR\_MIN\_VOLT\_SHIFT](#a718ca0a2cc3f17ff8cf0f4e1ba9ed6a7))

[PDO\_VAR\_MIN\_VOLT\_SHIFT](#a718ca0a2cc3f17ff8cf0f4e1ba9ed6a7)

#define PDO\_VAR\_MIN\_VOLT\_SHIFT

**Definition** pd.h:57

## [◆ ](#a718ca0a2cc3f17ff8cf0f4e1ba9ed6a7)PDO\_VAR\_MIN\_VOLT\_SHIFT

| #define PDO\_VAR\_MIN\_VOLT\_SHIFT   10 /\* 50mV units \*/ |
| --- |

## [◆ ](#ac41dc08efe8dfeeb1a9737e0b187c683)PDO\_VOLT\_MASK

| #define PDO\_VOLT\_MASK   0x3ff |
| --- |

## [◆ ](#ae3c4f39fb7ff5b00bdc25676af3b88f7)VSAFE5V

| #define VSAFE5V   5000 /\* mv units \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [usb-c](dir_0b553f055e45edcd5a3c9c76b7f4ae03.md)
- [pd.h](pd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
