---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfake__can__set__timing__Fake.html
original_path: doxygen/html/structfake__can__set__timing__Fake.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_set\_timing\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a7de46773faeadeece1b74604a4041a0b) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a688e98a0b933b87bc6294636e509252c) [(50u)] |
| const struct [can\_timing](structcan__timing.md) \* | [arg1\_val](#a1745c5d00bf3f6bc06157c14bd6d4892) |
| const struct [can\_timing](structcan__timing.md) \* | [arg1\_history](#a6b8a9f5f0252913cf7ddd1d853ea85cd) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#a7a1ecd4865b4f6cd99b6eae0518e1dc1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#aa55f26cd013da19bf650f25b66784321) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#af15aad2f982ba7b8c7d7c0771196f66c) |
| int | [return\_val](#adeb6c8042e8c5081ac79f4eafde66e85) |
| int | [return\_val\_seq\_len](#a85a6badda893dba34adf3e83a0094c23) |
| int | [return\_val\_seq\_idx](#a9559dc2354e86d0d86e85df9f97a4b73) |
| int \* | [return\_val\_seq](#a1878daa553d3d044ddcea05910918dcf) |
| int | [return\_val\_history](#a9d99aeb5fdd823a8938b4da2de5cb12f) [(50u)] |
| int | [custom\_fake\_seq\_len](#a08fb2b1ad985eb33c11abec86430cda4) |
| int | [custom\_fake\_seq\_idx](#a33309b35978aa0fd7568a3b88e09e45f) |
| int(\* | [custom\_fake](#ad2ef1b960af2e0784a2c91ef50c95b98) )(const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |
| int(\*\* | [custom\_fake\_seq](#afd6e1fbe7d036196de54ee173ae7467a) )(const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |

## Field Documentation

## [◆ ](#a688e98a0b933b87bc6294636e509252c)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_set\_timing\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a7de46773faeadeece1b74604a4041a0b)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_set\_timing\_Fake::arg0\_val |
| --- |

## [◆ ](#a6b8a9f5f0252913cf7ddd1d853ea85cd)arg1\_history

| const struct [can\_timing](structcan__timing.md)\* fake\_can\_set\_timing\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a1745c5d00bf3f6bc06157c14bd6d4892)arg1\_val

| const struct [can\_timing](structcan__timing.md)\* fake\_can\_set\_timing\_Fake::arg1\_val |
| --- |

## [◆ ](#af15aad2f982ba7b8c7d7c0771196f66c)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_timing\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#aa55f26cd013da19bf650f25b66784321)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_timing\_Fake::arg\_history\_len |
| --- |

## [◆ ](#a7a1ecd4865b4f6cd99b6eae0518e1dc1)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_timing\_Fake::call\_count |
| --- |

## [◆ ](#ad2ef1b960af2e0784a2c91ef50c95b98)custom\_fake

| int(\* fake\_can\_set\_timing\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |
| --- |

## [◆ ](#afd6e1fbe7d036196de54ee173ae7467a)custom\_fake\_seq

| int(\*\* fake\_can\_set\_timing\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |
| --- |

## [◆ ](#a33309b35978aa0fd7568a3b88e09e45f)custom\_fake\_seq\_idx

| int fake\_can\_set\_timing\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a08fb2b1ad985eb33c11abec86430cda4)custom\_fake\_seq\_len

| int fake\_can\_set\_timing\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#adeb6c8042e8c5081ac79f4eafde66e85)return\_val

| int fake\_can\_set\_timing\_Fake::return\_val |
| --- |

## [◆ ](#a9d99aeb5fdd823a8938b4da2de5cb12f)return\_val\_history

| int fake\_can\_set\_timing\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a1878daa553d3d044ddcea05910918dcf)return\_val\_seq

| int\* fake\_can\_set\_timing\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a9559dc2354e86d0d86e85df9f97a4b73)return\_val\_seq\_idx

| int fake\_can\_set\_timing\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a85a6badda893dba34adf3e83a0094c23)return\_val\_seq\_len

| int fake\_can\_set\_timing\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_set\_timing\_Fake](structfake__can__set__timing__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
