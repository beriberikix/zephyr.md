---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structfake__can__set__mode__Fake.html
original_path: doxygen/html/structfake__can__set__mode__Fake.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_set\_mode\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a9928da668bcfbba6bda0bc14e9806529) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a4c6b9383a5b18f4910daac77b0b551f4) [(50u)] |
| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | [arg1\_val](#aa93922d5a25c05d79b951e943e732d99) |
| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | [arg1\_history](#a55c7132af00a33b4d75ead611cf6504b) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#aa07f5a7a7e0ede26d1c9c285c27b82d9) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#aa01b199e2a8c1873f27bb8da2ded5c7c) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#adc0c33d124baf7c1310d4c5fae9539f8) |
| int | [return\_val](#a9d95a945f598654895e36d0451d0cde8) |
| int | [return\_val\_seq\_len](#a8d398f423c7a4c31c10420b24fb8d752) |
| int | [return\_val\_seq\_idx](#a0edd30a604d0b6806e7a62f4eed2de8b) |
| int \* | [return\_val\_seq](#a3ca85751d75707075aabfe2d6644d276) |
| int | [return\_val\_history](#a31caf1937935c8e4cb3d6e11307f5efe) [(50u)] |
| int | [custom\_fake\_seq\_len](#a2fceb073073a0db8727919928fa8c06a) |
| int | [custom\_fake\_seq\_idx](#aa4d5c1662240e320ade9bde0f32b772b) |
| int(\* | [custom\_fake](#a1af80f4fe410a6983bdb9baf54284400) )(const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)) |
| int(\*\* | [custom\_fake\_seq](#a829824ba39f43781fdbc14c99111c170) )(const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)) |

## Field Documentation

## [◆ ](#a4c6b9383a5b18f4910daac77b0b551f4)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_set\_mode\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a9928da668bcfbba6bda0bc14e9806529)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_set\_mode\_Fake::arg0\_val |
| --- |

## [◆ ](#a55c7132af00a33b4d75ead611cf6504b)arg1\_history

| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) fake\_can\_set\_mode\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#aa93922d5a25c05d79b951e943e732d99)arg1\_val

| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) fake\_can\_set\_mode\_Fake::arg1\_val |
| --- |

## [◆ ](#adc0c33d124baf7c1310d4c5fae9539f8)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_mode\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#aa01b199e2a8c1873f27bb8da2ded5c7c)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_mode\_Fake::arg\_history\_len |
| --- |

## [◆ ](#aa07f5a7a7e0ede26d1c9c285c27b82d9)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_mode\_Fake::call\_count |
| --- |

## [◆ ](#a1af80f4fe410a6983bdb9baf54284400)custom\_fake

| int(\* fake\_can\_set\_mode\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)) |
| --- |

## [◆ ](#a829824ba39f43781fdbc14c99111c170)custom\_fake\_seq

| int(\*\* fake\_can\_set\_mode\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)) |
| --- |

## [◆ ](#aa4d5c1662240e320ade9bde0f32b772b)custom\_fake\_seq\_idx

| int fake\_can\_set\_mode\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a2fceb073073a0db8727919928fa8c06a)custom\_fake\_seq\_len

| int fake\_can\_set\_mode\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#a9d95a945f598654895e36d0451d0cde8)return\_val

| int fake\_can\_set\_mode\_Fake::return\_val |
| --- |

## [◆ ](#a31caf1937935c8e4cb3d6e11307f5efe)return\_val\_history

| int fake\_can\_set\_mode\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a3ca85751d75707075aabfe2d6644d276)return\_val\_seq

| int\* fake\_can\_set\_mode\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a0edd30a604d0b6806e7a62f4eed2de8b)return\_val\_seq\_idx

| int fake\_can\_set\_mode\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a8d398f423c7a4c31c10420b24fb8d752)return\_val\_seq\_len

| int fake\_can\_set\_mode\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_set\_mode\_Fake](structfake__can__set__mode__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
