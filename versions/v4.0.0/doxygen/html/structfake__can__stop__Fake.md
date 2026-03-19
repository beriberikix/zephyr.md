---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfake__can__stop__Fake.html
original_path: doxygen/html/structfake__can__stop__Fake.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_stop\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a93954796bac5b7d43868a4faf4486abb) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a8ed74f448aeee4b7c9527b6352184587) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#ac9003fca681b56ed821d7fb5647221c5) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#aeae352bcb02853ec7815af75859ffb53) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a095753248ea5a5fb5aa4b5e82e208b5e) |
| int | [return\_val](#aef0161a1aab2a5e7870099254531cf07) |
| int | [return\_val\_seq\_len](#ab4428aead11059d34ef1472a1f6bcf5a) |
| int | [return\_val\_seq\_idx](#acbb09bb97a40ed6dc70d193b75804b27) |
| int \* | [return\_val\_seq](#a3a45bce3e49c40f8244d5956a10c61bc) |
| int | [return\_val\_history](#ab3052ac8b6b069376ddc0e65febc9b06) [(50u)] |
| int | [custom\_fake\_seq\_len](#a5ad9940a17bdf0e14083218ec9100cac) |
| int | [custom\_fake\_seq\_idx](#a150d4566a528221bb28d7debf25339c2) |
| int(\* | [custom\_fake](#aa7ba4c8f92aca6c92256b7f20dd4cabc) )(const struct [device](structdevice.md) \*) |
| int(\*\* | [custom\_fake\_seq](#a49382fa10fcc9e85e14b035dd5ddae0e) )(const struct [device](structdevice.md) \*) |

## Field Documentation

## [◆ ](#a8ed74f448aeee4b7c9527b6352184587)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_stop\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a93954796bac5b7d43868a4faf4486abb)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_stop\_Fake::arg0\_val |
| --- |

## [◆ ](#a095753248ea5a5fb5aa4b5e82e208b5e)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_stop\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#aeae352bcb02853ec7815af75859ffb53)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_stop\_Fake::arg\_history\_len |
| --- |

## [◆ ](#ac9003fca681b56ed821d7fb5647221c5)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_stop\_Fake::call\_count |
| --- |

## [◆ ](#aa7ba4c8f92aca6c92256b7f20dd4cabc)custom\_fake

| int(\* fake\_can\_stop\_Fake::custom\_fake) (const struct [device](structdevice.md) \*) |
| --- |

## [◆ ](#a49382fa10fcc9e85e14b035dd5ddae0e)custom\_fake\_seq

| int(\*\* fake\_can\_stop\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*) |
| --- |

## [◆ ](#a150d4566a528221bb28d7debf25339c2)custom\_fake\_seq\_idx

| int fake\_can\_stop\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a5ad9940a17bdf0e14083218ec9100cac)custom\_fake\_seq\_len

| int fake\_can\_stop\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#aef0161a1aab2a5e7870099254531cf07)return\_val

| int fake\_can\_stop\_Fake::return\_val |
| --- |

## [◆ ](#ab3052ac8b6b069376ddc0e65febc9b06)return\_val\_history

| int fake\_can\_stop\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a3a45bce3e49c40f8244d5956a10c61bc)return\_val\_seq

| int\* fake\_can\_stop\_Fake::return\_val\_seq |
| --- |

## [◆ ](#acbb09bb97a40ed6dc70d193b75804b27)return\_val\_seq\_idx

| int fake\_can\_stop\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#ab4428aead11059d34ef1472a1f6bcf5a)return\_val\_seq\_len

| int fake\_can\_stop\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_stop\_Fake](structfake__can__stop__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
