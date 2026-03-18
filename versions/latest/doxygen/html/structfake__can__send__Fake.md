---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structfake__can__send__Fake.html
original_path: doxygen/html/structfake__can__send__Fake.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_send\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#aa3dbf1075324f019f5127ddbd3e08c11) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a3537b8b901274f1bbdb508e52a180f95) [(50u)] |
| const struct [can\_frame](structcan__frame.md) \* | [arg1\_val](#a976958722e013359afcd94ce554fe652) |
| const struct [can\_frame](structcan__frame.md) \* | [arg1\_history](#a1aa63a3a414eb9d731937b5ba7f790f0) [(50u)] |
| [k\_timeout\_t](structk__timeout__t.md) | [arg2\_val](#a65483a432f087241c05a35e0f6d55189) |
| [k\_timeout\_t](structk__timeout__t.md) | [arg2\_history](#ac0aa1946dbca3efb1256756124a594cd) [(50u)] |
| [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) | [arg3\_val](#afe78e6d75712abd6113ce1a7bc259404) |
| [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) | [arg3\_history](#a271db15349005a658faf23983b8fef93) [(50u)] |
| void \* | [arg4\_val](#aac0a0cb0a511dd54276fe822c87ac145) |
| void \* | [arg4\_history](#a1fb146928dc3d81650228ef4bb77ff0a) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#a82af086bf0a90278d0a1aba1ec4d9599) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a70d2168170574d8d2f2a238690537bfd) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#ac5fe8ae37315e3117373589e27192791) |
| int | [return\_val](#a5020bfced94d0f32b6e04908fcdd77e9) |
| int | [return\_val\_seq\_len](#aedb4b4d3fd13abbbe076d1c39863925e) |
| int | [return\_val\_seq\_idx](#a96166f1712546e7e06cea495a5f17162) |
| int \* | [return\_val\_seq](#ac547fa6437beba801329ff2227f66767) |
| int | [return\_val\_history](#a859b16340124dbf98582a897a732403b) [(50u)] |
| int | [custom\_fake\_seq\_len](#a200b5a0fa237c09ed77556be826de8b9) |
| int | [custom\_fake\_seq\_idx](#a32a3912960a04b4ea2f9f83e0dfe2fd1) |
| int(\* | [custom\_fake](#a97777eec2acfebebd1e5ee2339e57fa9) )(const struct [device](structdevice.md) \*, const struct [can\_frame](structcan__frame.md) \*, [k\_timeout\_t](structk__timeout__t.md), [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca), void \*) |
| int(\*\* | [custom\_fake\_seq](#a24dd4e6a13652da8992281f9b1dbf340) )(const struct [device](structdevice.md) \*, const struct [can\_frame](structcan__frame.md) \*, [k\_timeout\_t](structk__timeout__t.md), [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca), void \*) |

## Field Documentation

## [◆ ](#a3537b8b901274f1bbdb508e52a180f95)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_send\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#aa3dbf1075324f019f5127ddbd3e08c11)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_send\_Fake::arg0\_val |
| --- |

## [◆ ](#a1aa63a3a414eb9d731937b5ba7f790f0)arg1\_history

| const struct [can\_frame](structcan__frame.md)\* fake\_can\_send\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a976958722e013359afcd94ce554fe652)arg1\_val

| const struct [can\_frame](structcan__frame.md)\* fake\_can\_send\_Fake::arg1\_val |
| --- |

## [◆ ](#ac0aa1946dbca3efb1256756124a594cd)arg2\_history

| [k\_timeout\_t](structk__timeout__t.md) fake\_can\_send\_Fake::arg2\_history[(50u)] |
| --- |

## [◆ ](#a65483a432f087241c05a35e0f6d55189)arg2\_val

| [k\_timeout\_t](structk__timeout__t.md) fake\_can\_send\_Fake::arg2\_val |
| --- |

## [◆ ](#a271db15349005a658faf23983b8fef93)arg3\_history

| [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) fake\_can\_send\_Fake::arg3\_history[(50u)] |
| --- |

## [◆ ](#afe78e6d75712abd6113ce1a7bc259404)arg3\_val

| [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) fake\_can\_send\_Fake::arg3\_val |
| --- |

## [◆ ](#a1fb146928dc3d81650228ef4bb77ff0a)arg4\_history

| void\* fake\_can\_send\_Fake::arg4\_history[(50u)] |
| --- |

## [◆ ](#aac0a0cb0a511dd54276fe822c87ac145)arg4\_val

| void\* fake\_can\_send\_Fake::arg4\_val |
| --- |

## [◆ ](#ac5fe8ae37315e3117373589e27192791)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_send\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a70d2168170574d8d2f2a238690537bfd)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_send\_Fake::arg\_history\_len |
| --- |

## [◆ ](#a82af086bf0a90278d0a1aba1ec4d9599)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_send\_Fake::call\_count |
| --- |

## [◆ ](#a97777eec2acfebebd1e5ee2339e57fa9)custom\_fake

| int(\* fake\_can\_send\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, const struct [can\_frame](structcan__frame.md) \*, [k\_timeout\_t](structk__timeout__t.md), [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca), void \*) |
| --- |

## [◆ ](#a24dd4e6a13652da8992281f9b1dbf340)custom\_fake\_seq

| int(\*\* fake\_can\_send\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, const struct [can\_frame](structcan__frame.md) \*, [k\_timeout\_t](structk__timeout__t.md), [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca), void \*) |
| --- |

## [◆ ](#a32a3912960a04b4ea2f9f83e0dfe2fd1)custom\_fake\_seq\_idx

| int fake\_can\_send\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a200b5a0fa237c09ed77556be826de8b9)custom\_fake\_seq\_len

| int fake\_can\_send\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#a5020bfced94d0f32b6e04908fcdd77e9)return\_val

| int fake\_can\_send\_Fake::return\_val |
| --- |

## [◆ ](#a859b16340124dbf98582a897a732403b)return\_val\_history

| int fake\_can\_send\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#ac547fa6437beba801329ff2227f66767)return\_val\_seq

| int\* fake\_can\_send\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a96166f1712546e7e06cea495a5f17162)return\_val\_seq\_idx

| int fake\_can\_send\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#aedb4b4d3fd13abbbe076d1c39863925e)return\_val\_seq\_len

| int fake\_can\_send\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_send\_Fake](structfake__can__send__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
