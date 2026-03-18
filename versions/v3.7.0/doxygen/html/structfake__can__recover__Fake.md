---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structfake__can__recover__Fake.html
original_path: doxygen/html/structfake__can__recover__Fake.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_recover\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#aee2a6a7afd5670aec8f270b280d1ae19) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a3833492b2003d3936ba0bc1d1d39c50d) [(50u)] |
| [k\_timeout\_t](structk__timeout__t.md) | [arg1\_val](#a6c758d3fa7f15414370ec14b48fe7fbb) |
| [k\_timeout\_t](structk__timeout__t.md) | [arg1\_history](#ac4bf1fbda3be37cee5904b6781e52e8d) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#ac1a96a640a5926afaf31469261a315e4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a40e5bdcbd8380ab47825e958588ee421) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a6b82557dcc63f875b8ffb4c4c78b2166) |
| int | [return\_val](#a6778ba3e919b8dd647dc4328a81ff6f8) |
| int | [return\_val\_seq\_len](#a9e35279a2ab8d7bd3cc318e670a8c8d3) |
| int | [return\_val\_seq\_idx](#a0be06fbc6241b4b8db4d71d464d41154) |
| int \* | [return\_val\_seq](#a3e8d17923c5c84e10d10b2c0664d4362) |
| int | [return\_val\_history](#a4de2d2bc47ad565e1ff029214ea187f2) [(50u)] |
| int | [custom\_fake\_seq\_len](#a3a52b34dfe4804591726d0b0a2e01b3f) |
| int | [custom\_fake\_seq\_idx](#a9c0305c96997dffb3dea8c5e57b16f1e) |
| int(\* | [custom\_fake](#ae44f9c226a12516cf7af55fa58bc7a75) )(const struct [device](structdevice.md) \*, [k\_timeout\_t](structk__timeout__t.md)) |
| int(\*\* | [custom\_fake\_seq](#abec00684cccbd9f19e3bd6981d105a1c) )(const struct [device](structdevice.md) \*, [k\_timeout\_t](structk__timeout__t.md)) |

## Field Documentation

## [◆ ](#a3833492b2003d3936ba0bc1d1d39c50d)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_recover\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#aee2a6a7afd5670aec8f270b280d1ae19)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_recover\_Fake::arg0\_val |
| --- |

## [◆ ](#ac4bf1fbda3be37cee5904b6781e52e8d)arg1\_history

| [k\_timeout\_t](structk__timeout__t.md) fake\_can\_recover\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a6c758d3fa7f15414370ec14b48fe7fbb)arg1\_val

| [k\_timeout\_t](structk__timeout__t.md) fake\_can\_recover\_Fake::arg1\_val |
| --- |

## [◆ ](#a6b82557dcc63f875b8ffb4c4c78b2166)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_recover\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a40e5bdcbd8380ab47825e958588ee421)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_recover\_Fake::arg\_history\_len |
| --- |

## [◆ ](#ac1a96a640a5926afaf31469261a315e4)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_recover\_Fake::call\_count |
| --- |

## [◆ ](#ae44f9c226a12516cf7af55fa58bc7a75)custom\_fake

| int(\* fake\_can\_recover\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [k\_timeout\_t](structk__timeout__t.md)) |
| --- |

## [◆ ](#abec00684cccbd9f19e3bd6981d105a1c)custom\_fake\_seq

| int(\*\* fake\_can\_recover\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [k\_timeout\_t](structk__timeout__t.md)) |
| --- |

## [◆ ](#a9c0305c96997dffb3dea8c5e57b16f1e)custom\_fake\_seq\_idx

| int fake\_can\_recover\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a3a52b34dfe4804591726d0b0a2e01b3f)custom\_fake\_seq\_len

| int fake\_can\_recover\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#a6778ba3e919b8dd647dc4328a81ff6f8)return\_val

| int fake\_can\_recover\_Fake::return\_val |
| --- |

## [◆ ](#a4de2d2bc47ad565e1ff029214ea187f2)return\_val\_history

| int fake\_can\_recover\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a3e8d17923c5c84e10d10b2c0664d4362)return\_val\_seq

| int\* fake\_can\_recover\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a0be06fbc6241b4b8db4d71d464d41154)return\_val\_seq\_idx

| int fake\_can\_recover\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a9e35279a2ab8d7bd3cc318e670a8c8d3)return\_val\_seq\_len

| int fake\_can\_recover\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_recover\_Fake](structfake__can__recover__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
