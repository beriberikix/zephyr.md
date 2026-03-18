---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structfake__can__get__capabilities__Fake.html
original_path: doxygen/html/structfake__can__get__capabilities__Fake.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_get\_capabilities\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a4e878d672c24276eea068c02bf4697f8) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a6b17d900a403bc6f9b937a334deda02a) [(50u)] |
| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \* | [arg1\_val](#a4c8f706be4cf95f03d41e191b3f61205) |
| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \* | [arg1\_history](#ad0956c317d73e8267f1263a9dc3ef828) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#abb20f4fe70df3288e5ca6efd72f8ab23) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a8a817c61d4554aa835db9fb2609b9042) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a15786c39c175a417e5d2b75c66cb56c0) |
| int | [return\_val](#aca3d756eb1b917184e5bc8cd3781b1bc) |
| int | [return\_val\_seq\_len](#a9bc5d7e5e803c79aa347e37fa0e13a8a) |
| int | [return\_val\_seq\_idx](#a905a01ef2ddaff051006ac522d73e578) |
| int \* | [return\_val\_seq](#a6588957ff231c50878e724e4e429d0f7) |
| int | [return\_val\_history](#aaf172191419d29e41ff6e0f9f02160b5) [(50u)] |
| int | [custom\_fake\_seq\_len](#ac942f32b3e67d0589496ee9d7d4d1932) |
| int | [custom\_fake\_seq\_idx](#a6fe347b819783f7814f5832843ec1291) |
| int(\* | [custom\_fake](#a04304e4e638aa8f2aab7b7d9ec9b3b10) )(const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*) |
| int(\*\* | [custom\_fake\_seq](#aefdb36f8575a64349fbec558fc793469) )(const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*) |

## Field Documentation

## [◆ ](#a6b17d900a403bc6f9b937a334deda02a)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_get\_capabilities\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a4e878d672c24276eea068c02bf4697f8)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_get\_capabilities\_Fake::arg0\_val |
| --- |

## [◆ ](#ad0956c317d73e8267f1263a9dc3ef828)arg1\_history

| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)\* fake\_can\_get\_capabilities\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a4c8f706be4cf95f03d41e191b3f61205)arg1\_val

| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)\* fake\_can\_get\_capabilities\_Fake::arg1\_val |
| --- |

## [◆ ](#a15786c39c175a417e5d2b75c66cb56c0)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_capabilities\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a8a817c61d4554aa835db9fb2609b9042)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_capabilities\_Fake::arg\_history\_len |
| --- |

## [◆ ](#abb20f4fe70df3288e5ca6efd72f8ab23)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_capabilities\_Fake::call\_count |
| --- |

## [◆ ](#a04304e4e638aa8f2aab7b7d9ec9b3b10)custom\_fake

| int(\* fake\_can\_get\_capabilities\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*) |
| --- |

## [◆ ](#aefdb36f8575a64349fbec558fc793469)custom\_fake\_seq

| int(\*\* fake\_can\_get\_capabilities\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*) |
| --- |

## [◆ ](#a6fe347b819783f7814f5832843ec1291)custom\_fake\_seq\_idx

| int fake\_can\_get\_capabilities\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#ac942f32b3e67d0589496ee9d7d4d1932)custom\_fake\_seq\_len

| int fake\_can\_get\_capabilities\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#aca3d756eb1b917184e5bc8cd3781b1bc)return\_val

| int fake\_can\_get\_capabilities\_Fake::return\_val |
| --- |

## [◆ ](#aaf172191419d29e41ff6e0f9f02160b5)return\_val\_history

| int fake\_can\_get\_capabilities\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a6588957ff231c50878e724e4e429d0f7)return\_val\_seq

| int\* fake\_can\_get\_capabilities\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a905a01ef2ddaff051006ac522d73e578)return\_val\_seq\_idx

| int fake\_can\_get\_capabilities\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a9bc5d7e5e803c79aa347e37fa0e13a8a)return\_val\_seq\_len

| int fake\_can\_get\_capabilities\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_get\_capabilities\_Fake](structfake__can__get__capabilities__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
