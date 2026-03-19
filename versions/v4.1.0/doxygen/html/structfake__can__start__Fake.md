---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfake__can__start__Fake.html
original_path: doxygen/html/structfake__can__start__Fake.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_start\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#af83d2ccd63409fdc9e6e8625f7869f49) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a074da35cf170f2c4c4e85c79d23bca68) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#aeb3cbdf997078f55285397be3da60ead) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a27cf1e156c7a1c38535645e8b54a615e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a27249cafd98f3097ba5f294804ca5ed9) |
| int | [return\_val](#aeab853bf65ade0096f3d4363ef3ce7e5) |
| int | [return\_val\_seq\_len](#a56e8c63657230e5f8a2eda50dfbd5407) |
| int | [return\_val\_seq\_idx](#acdee1b7ba9e0252edba1cd21d5cd8ccb) |
| int \* | [return\_val\_seq](#a146929f1f8c575cc71a05c64d8e2fc27) |
| int | [return\_val\_history](#af2d9d456a2efb6d7ae44aeb9255bf6ee) [(50u)] |
| int | [custom\_fake\_seq\_len](#a91d8e1dc7c8f6013ba94be463132519a) |
| int | [custom\_fake\_seq\_idx](#aae41ca09c7b22416c58eddebdc0f522d) |
| int(\* | [custom\_fake](#ac28ac5b198ef45c109fb51af3f06ed92) )(const struct [device](structdevice.md) \*) |
| int(\*\* | [custom\_fake\_seq](#a652954893672294994628a3f31ca0c71) )(const struct [device](structdevice.md) \*) |

## Field Documentation

## [◆ ](#a074da35cf170f2c4c4e85c79d23bca68)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_start\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#af83d2ccd63409fdc9e6e8625f7869f49)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_start\_Fake::arg0\_val |
| --- |

## [◆ ](#a27249cafd98f3097ba5f294804ca5ed9)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_start\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a27cf1e156c7a1c38535645e8b54a615e)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_start\_Fake::arg\_history\_len |
| --- |

## [◆ ](#aeb3cbdf997078f55285397be3da60ead)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_start\_Fake::call\_count |
| --- |

## [◆ ](#ac28ac5b198ef45c109fb51af3f06ed92)custom\_fake

| int(\* fake\_can\_start\_Fake::custom\_fake) (const struct [device](structdevice.md) \*) |
| --- |

## [◆ ](#a652954893672294994628a3f31ca0c71)custom\_fake\_seq

| int(\*\* fake\_can\_start\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*) |
| --- |

## [◆ ](#aae41ca09c7b22416c58eddebdc0f522d)custom\_fake\_seq\_idx

| int fake\_can\_start\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a91d8e1dc7c8f6013ba94be463132519a)custom\_fake\_seq\_len

| int fake\_can\_start\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#aeab853bf65ade0096f3d4363ef3ce7e5)return\_val

| int fake\_can\_start\_Fake::return\_val |
| --- |

## [◆ ](#af2d9d456a2efb6d7ae44aeb9255bf6ee)return\_val\_history

| int fake\_can\_start\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a146929f1f8c575cc71a05c64d8e2fc27)return\_val\_seq

| int\* fake\_can\_start\_Fake::return\_val\_seq |
| --- |

## [◆ ](#acdee1b7ba9e0252edba1cd21d5cd8ccb)return\_val\_seq\_idx

| int fake\_can\_start\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a56e8c63657230e5f8a2eda50dfbd5407)return\_val\_seq\_len

| int fake\_can\_start\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_start\_Fake](structfake__can__start__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
