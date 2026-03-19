---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfake__can__set__timing__data__Fake.html
original_path: doxygen/html/structfake__can__set__timing__data__Fake.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_set\_timing\_data\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a222b9dd263e0678699f8ed5f0734d9d8) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a34f4146ceabf0e70469bf7bde574e95a) [(50u)] |
| const struct [can\_timing](structcan__timing.md) \* | [arg1\_val](#a2df927faec6f4d81333e892f37ad8d7d) |
| const struct [can\_timing](structcan__timing.md) \* | [arg1\_history](#a72683050fd32ae66b6766c86a5ad8f9e) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#ad560561595ff68b2c89a52a0560f2584) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#aff821fda6a3a93f182c190691ed5db58) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a59cf453641e0294978049af949346944) |
| int | [return\_val](#ab4ac6387bec3f79fbc80b6da7bcf55f8) |
| int | [return\_val\_seq\_len](#ab13fcb385432a4280c65086d6275a025) |
| int | [return\_val\_seq\_idx](#aaca6acd6654cb57512e46e337fbbb39a) |
| int \* | [return\_val\_seq](#a38fb5182480d73fb2959d79564a121ac) |
| int | [return\_val\_history](#ab716431869ea6aece52380e4c4af341c) [(50u)] |
| int | [custom\_fake\_seq\_len](#a8a43210bc766be3bed7bc534a5d11269) |
| int | [custom\_fake\_seq\_idx](#a6bb13daed22a444130aa4052f6a29dc7) |
| int(\* | [custom\_fake](#a364237dec0ef6bcd9b7754dc2fb7ad7c) )(const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |
| int(\*\* | [custom\_fake\_seq](#a74bcf6146705fe89f844b3d4aceb2998) )(const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |

## Field Documentation

## [◆ ](#a34f4146ceabf0e70469bf7bde574e95a)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_set\_timing\_data\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a222b9dd263e0678699f8ed5f0734d9d8)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_set\_timing\_data\_Fake::arg0\_val |
| --- |

## [◆ ](#a72683050fd32ae66b6766c86a5ad8f9e)arg1\_history

| const struct [can\_timing](structcan__timing.md)\* fake\_can\_set\_timing\_data\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a2df927faec6f4d81333e892f37ad8d7d)arg1\_val

| const struct [can\_timing](structcan__timing.md)\* fake\_can\_set\_timing\_data\_Fake::arg1\_val |
| --- |

## [◆ ](#a59cf453641e0294978049af949346944)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_timing\_data\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#aff821fda6a3a93f182c190691ed5db58)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_timing\_data\_Fake::arg\_history\_len |
| --- |

## [◆ ](#ad560561595ff68b2c89a52a0560f2584)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_timing\_data\_Fake::call\_count |
| --- |

## [◆ ](#a364237dec0ef6bcd9b7754dc2fb7ad7c)custom\_fake

| int(\* fake\_can\_set\_timing\_data\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |
| --- |

## [◆ ](#a74bcf6146705fe89f844b3d4aceb2998)custom\_fake\_seq

| int(\*\* fake\_can\_set\_timing\_data\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*) |
| --- |

## [◆ ](#a6bb13daed22a444130aa4052f6a29dc7)custom\_fake\_seq\_idx

| int fake\_can\_set\_timing\_data\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a8a43210bc766be3bed7bc534a5d11269)custom\_fake\_seq\_len

| int fake\_can\_set\_timing\_data\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#ab4ac6387bec3f79fbc80b6da7bcf55f8)return\_val

| int fake\_can\_set\_timing\_data\_Fake::return\_val |
| --- |

## [◆ ](#ab716431869ea6aece52380e4c4af341c)return\_val\_history

| int fake\_can\_set\_timing\_data\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a38fb5182480d73fb2959d79564a121ac)return\_val\_seq

| int\* fake\_can\_set\_timing\_data\_Fake::return\_val\_seq |
| --- |

## [◆ ](#aaca6acd6654cb57512e46e337fbbb39a)return\_val\_seq\_idx

| int fake\_can\_set\_timing\_data\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#ab13fcb385432a4280c65086d6275a025)return\_val\_seq\_len

| int fake\_can\_set\_timing\_data\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_set\_timing\_data\_Fake](structfake__can__set__timing__data__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
