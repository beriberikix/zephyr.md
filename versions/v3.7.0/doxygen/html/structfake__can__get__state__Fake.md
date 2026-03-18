---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structfake__can__get__state__Fake.html
original_path: doxygen/html/structfake__can__get__state__Fake.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_get\_state\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a93bbc7bfdc30a157004fddcfdf7094a6) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a5c405d3ba0cd766e745103a6e8065239) [(50u)] |
| enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \* | [arg1\_val](#a8bec740c46caf4bd4b2b8b79bfc19364) |
| enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \* | [arg1\_history](#a6920bd0ad00e3f4eb0765e6035d2f9b2) [(50u)] |
| struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \* | [arg2\_val](#a8d39a3a2e910d31b3c1b31c997157f7e) |
| struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \* | [arg2\_history](#a8ab48d1bc94d252a85765262d637a18b) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#ae9b67b7798f1b8da5126e2c175d06c81) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a54b23d388d2a92f5fd5354471bf68eb1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a2d5fdb64a74af8f75869f0a5f0a02e39) |
| int | [return\_val](#a2a2be13c24ca311959f2b11803d45d52) |
| int | [return\_val\_seq\_len](#a22053b6779e2bd18302d952bb9fc1d92) |
| int | [return\_val\_seq\_idx](#a647e4d0ca61879f8537a0b4b352e76fb) |
| int \* | [return\_val\_seq](#a3832b7339306493da20cdc4afa6c1658) |
| int | [return\_val\_history](#a0411ce13aa7a745dee640980b7332adf) [(50u)] |
| int | [custom\_fake\_seq\_len](#a8157a5d7466eadc122a6d0ac71c81f62) |
| int | [custom\_fake\_seq\_idx](#ac657f4181e012f36f762bbea32e7d87c) |
| int(\* | [custom\_fake](#ae06f67dc970fb49c239e4ca2b971d120) )(const struct [device](structdevice.md) \*, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*, struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*) |
| int(\*\* | [custom\_fake\_seq](#ab5e9bbd5d636b71ab3d0905750d5c34b) )(const struct [device](structdevice.md) \*, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*, struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*) |

## Field Documentation

## [◆ ](#a5c405d3ba0cd766e745103a6e8065239)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_get\_state\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a93bbc7bfdc30a157004fddcfdf7094a6)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_get\_state\_Fake::arg0\_val |
| --- |

## [◆ ](#a6920bd0ad00e3f4eb0765e6035d2f9b2)arg1\_history

| enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)\* fake\_can\_get\_state\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a8bec740c46caf4bd4b2b8b79bfc19364)arg1\_val

| enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)\* fake\_can\_get\_state\_Fake::arg1\_val |
| --- |

## [◆ ](#a8ab48d1bc94d252a85765262d637a18b)arg2\_history

| struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md)\* fake\_can\_get\_state\_Fake::arg2\_history[(50u)] |
| --- |

## [◆ ](#a8d39a3a2e910d31b3c1b31c997157f7e)arg2\_val

| struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md)\* fake\_can\_get\_state\_Fake::arg2\_val |
| --- |

## [◆ ](#a2d5fdb64a74af8f75869f0a5f0a02e39)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_state\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a54b23d388d2a92f5fd5354471bf68eb1)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_state\_Fake::arg\_history\_len |
| --- |

## [◆ ](#ae9b67b7798f1b8da5126e2c175d06c81)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_state\_Fake::call\_count |
| --- |

## [◆ ](#ae06f67dc970fb49c239e4ca2b971d120)custom\_fake

| int(\* fake\_can\_get\_state\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*, struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*) |
| --- |

## [◆ ](#ab5e9bbd5d636b71ab3d0905750d5c34b)custom\_fake\_seq

| int(\*\* fake\_can\_get\_state\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*, struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*) |
| --- |

## [◆ ](#ac657f4181e012f36f762bbea32e7d87c)custom\_fake\_seq\_idx

| int fake\_can\_get\_state\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a8157a5d7466eadc122a6d0ac71c81f62)custom\_fake\_seq\_len

| int fake\_can\_get\_state\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#a2a2be13c24ca311959f2b11803d45d52)return\_val

| int fake\_can\_get\_state\_Fake::return\_val |
| --- |

## [◆ ](#a0411ce13aa7a745dee640980b7332adf)return\_val\_history

| int fake\_can\_get\_state\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a3832b7339306493da20cdc4afa6c1658)return\_val\_seq

| int\* fake\_can\_get\_state\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a647e4d0ca61879f8537a0b4b352e76fb)return\_val\_seq\_idx

| int fake\_can\_get\_state\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a22053b6779e2bd18302d952bb9fc1d92)return\_val\_seq\_len

| int fake\_can\_get\_state\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_get\_state\_Fake](structfake__can__get__state__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
