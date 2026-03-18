---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structfake__can__get__core__clock__Fake.html
original_path: doxygen/html/structfake__can__get__core__clock__Fake.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_get\_core\_clock\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#aabc10869c39d8a43999a270758da250e) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a977411871f80bf3660c56ca95aafec4f) [(50u)] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [arg1\_val](#adba579c74856f304de97dbc051ce43df) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [arg1\_history](#abb94cd7772bcc939eaf2ece23fea38b1) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#ae71380fc3213ccfe491fee94509dd314) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a289f41f54261be87b774c35769498321) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#aadcac948228154253f906f88dddb629a) |
| int | [return\_val](#a0077caeea20680ee962f8f3cdda0886b) |
| int | [return\_val\_seq\_len](#a2f4fabada292d26278d7dadb278d8572) |
| int | [return\_val\_seq\_idx](#ad532049854f837183677bd1db5c8bcb3) |
| int \* | [return\_val\_seq](#a0db77d0d10b0c0e36af0e90687b6baef) |
| int | [return\_val\_history](#a8f90656ee3873349cd5ba1c71cdc85ea) [(50u)] |
| int | [custom\_fake\_seq\_len](#a0bee30d975d73f0cfabf401686eb4ff2) |
| int | [custom\_fake\_seq\_idx](#ae8e575eedb9e5587f5050032dda11435) |
| int(\* | [custom\_fake](#a4085e3ca3bfe3d7d2ce0902b89047741) )(const struct [device](structdevice.md) \*, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*) |
| int(\*\* | [custom\_fake\_seq](#a0004e9c61f5fcddaa7e21e2124eb2a0a) )(const struct [device](structdevice.md) \*, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*) |

## Field Documentation

## [◆ ](#a977411871f80bf3660c56ca95aafec4f)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_get\_core\_clock\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#aabc10869c39d8a43999a270758da250e)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_get\_core\_clock\_Fake::arg0\_val |
| --- |

## [◆ ](#abb94cd7772bcc939eaf2ece23fea38b1)arg1\_history

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* fake\_can\_get\_core\_clock\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#adba579c74856f304de97dbc051ce43df)arg1\_val

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* fake\_can\_get\_core\_clock\_Fake::arg1\_val |
| --- |

## [◆ ](#aadcac948228154253f906f88dddb629a)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_core\_clock\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a289f41f54261be87b774c35769498321)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_core\_clock\_Fake::arg\_history\_len |
| --- |

## [◆ ](#ae71380fc3213ccfe491fee94509dd314)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_get\_core\_clock\_Fake::call\_count |
| --- |

## [◆ ](#a4085e3ca3bfe3d7d2ce0902b89047741)custom\_fake

| int(\* fake\_can\_get\_core\_clock\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*) |
| --- |

## [◆ ](#a0004e9c61f5fcddaa7e21e2124eb2a0a)custom\_fake\_seq

| int(\*\* fake\_can\_get\_core\_clock\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*) |
| --- |

## [◆ ](#ae8e575eedb9e5587f5050032dda11435)custom\_fake\_seq\_idx

| int fake\_can\_get\_core\_clock\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a0bee30d975d73f0cfabf401686eb4ff2)custom\_fake\_seq\_len

| int fake\_can\_get\_core\_clock\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#a0077caeea20680ee962f8f3cdda0886b)return\_val

| int fake\_can\_get\_core\_clock\_Fake::return\_val |
| --- |

## [◆ ](#a8f90656ee3873349cd5ba1c71cdc85ea)return\_val\_history

| int fake\_can\_get\_core\_clock\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a0db77d0d10b0c0e36af0e90687b6baef)return\_val\_seq

| int\* fake\_can\_get\_core\_clock\_Fake::return\_val\_seq |
| --- |

## [◆ ](#ad532049854f837183677bd1db5c8bcb3)return\_val\_seq\_idx

| int fake\_can\_get\_core\_clock\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a2f4fabada292d26278d7dadb278d8572)return\_val\_seq\_len

| int fake\_can\_get\_core\_clock\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_get\_core\_clock\_Fake](structfake__can__get__core__clock__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
