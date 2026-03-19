---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfake__can__get__max__filters__Fake.html
original_path: doxygen/html/structfake__can__get__max__filters__Fake.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_get\_max\_filters\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#af40b1b22072b32296af68ee2412eedb1) |
| const struct [device](structdevice.md) \* | [arg0\_history](#aeafbc134795c08a0da417352a78f32d7) [(50u)] |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arg1\_val](#aed473df95baf56f79478994231dd76af) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arg1\_history](#a23f9c766494bd5202774cdd2cc75c6a1) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#a6df96b03a3d58a273e845f950074d368) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#abc3ac21861e378d216b46fe26d19a8f0) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a5ef346d34d652561570acf959212025a) |
| int | [return\_val](#a3a5e67adb4614f3042dc88cfad66c558) |
| int | [return\_val\_seq\_len](#a9a104d57ac7e841337aa913128a14fea) |
| int | [return\_val\_seq\_idx](#a924a678272adcda0e35dfd7f455e4f7b) |
| int \* | [return\_val\_seq](#a32aec789ce9120a066ac51f4b740735d) |
| int | [return\_val\_history](#aa093a15796241b9ad9ac817bf5f35435) [(50u)] |
| int | [custom\_fake\_seq\_len](#a7fb6f096602d71966f39666a469d5936) |
| int | [custom\_fake\_seq\_idx](#a36ab564ce87e9724f2424c3ab75aebd8) |
| int(\* | [custom\_fake](#ace3b8f00a6ece545a069b0e853ec6f5d) )(const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |
| int(\*\* | [custom\_fake\_seq](#a37938ce95e68871b2d686c47758ad1aa) )(const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |

## Field Documentation

## [◆ ](#aeafbc134795c08a0da417352a78f32d7)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_get\_max\_filters\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#af40b1b22072b32296af68ee2412eedb1)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_get\_max\_filters\_Fake::arg0\_val |
| --- |

## [◆ ](#a23f9c766494bd5202774cdd2cc75c6a1)arg1\_history

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fake\_can\_get\_max\_filters\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#aed473df95baf56f79478994231dd76af)arg1\_val

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fake\_can\_get\_max\_filters\_Fake::arg1\_val |
| --- |

## [◆ ](#a5ef346d34d652561570acf959212025a)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_max\_filters\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#abc3ac21861e378d216b46fe26d19a8f0)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_max\_filters\_Fake::arg\_history\_len |
| --- |

## [◆ ](#a6df96b03a3d58a273e845f950074d368)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_max\_filters\_Fake::call\_count |
| --- |

## [◆ ](#ace3b8f00a6ece545a069b0e853ec6f5d)custom\_fake

| int(\* fake\_can\_get\_max\_filters\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |
| --- |

## [◆ ](#a37938ce95e68871b2d686c47758ad1aa)custom\_fake\_seq

| int(\*\* fake\_can\_get\_max\_filters\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |
| --- |

## [◆ ](#a36ab564ce87e9724f2424c3ab75aebd8)custom\_fake\_seq\_idx

| int fake\_can\_get\_max\_filters\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a7fb6f096602d71966f39666a469d5936)custom\_fake\_seq\_len

| int fake\_can\_get\_max\_filters\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#a3a5e67adb4614f3042dc88cfad66c558)return\_val

| int fake\_can\_get\_max\_filters\_Fake::return\_val |
| --- |

## [◆ ](#aa093a15796241b9ad9ac817bf5f35435)return\_val\_history

| int fake\_can\_get\_max\_filters\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a32aec789ce9120a066ac51f4b740735d)return\_val\_seq

| int\* fake\_can\_get\_max\_filters\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a924a678272adcda0e35dfd7f455e4f7b)return\_val\_seq\_idx

| int fake\_can\_get\_max\_filters\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a9a104d57ac7e841337aa913128a14fea)return\_val\_seq\_len

| int fake\_can\_get\_max\_filters\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_get\_max\_filters\_Fake](structfake__can__get__max__filters__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
