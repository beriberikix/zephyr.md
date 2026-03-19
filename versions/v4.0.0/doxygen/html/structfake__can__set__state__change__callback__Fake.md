---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfake__can__set__state__change__callback__Fake.html
original_path: doxygen/html/structfake__can__set__state__change__callback__Fake.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_set\_state\_change\_callback\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#abffb5229e088812b05d40c7a4ba64200) |
| const struct [device](structdevice.md) \* | [arg0\_history](#ab38acb1d5b28cdbdb091354f0831adb1) [(50u)] |
| [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) | [arg1\_val](#adc0c50863c1e2c4a0596b02b6f8fe095) |
| [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) | [arg1\_history](#a57eebc27313a2232297514e411168e7d) [(50u)] |
| void \* | [arg2\_val](#a877ef95c441bdcf8b23150f25f54e8d9) |
| void \* | [arg2\_history](#a26561def01144c85b9dadffe06b1cb02) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#aeea4d8cbe60185f2871acd99cedf31e2) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a665ffac5d8c9f9224acfb4359cc6d7c1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a265b73064807e6f3b69595118ea17011) |
| int | [custom\_fake\_seq\_len](#a18bad3283e5b731a46b14b0e37d8fcb7) |
| int | [custom\_fake\_seq\_idx](#ad6bb6a36efba89f0c461cb7a50f290e8) |
| void(\* | [custom\_fake](#abe6a7fc6c7f0fccf0c5096bc463b9a2f) )(const struct [device](structdevice.md) \*, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d), void \*) |
| void(\*\* | [custom\_fake\_seq](#a1bb52f289114151a9e842d6a9de00330) )(const struct [device](structdevice.md) \*, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d), void \*) |

## Field Documentation

## [◆ ](#ab38acb1d5b28cdbdb091354f0831adb1)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_set\_state\_change\_callback\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#abffb5229e088812b05d40c7a4ba64200)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_set\_state\_change\_callback\_Fake::arg0\_val |
| --- |

## [◆ ](#a57eebc27313a2232297514e411168e7d)arg1\_history

| [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) fake\_can\_set\_state\_change\_callback\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#adc0c50863c1e2c4a0596b02b6f8fe095)arg1\_val

| [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) fake\_can\_set\_state\_change\_callback\_Fake::arg1\_val |
| --- |

## [◆ ](#a26561def01144c85b9dadffe06b1cb02)arg2\_history

| void\* fake\_can\_set\_state\_change\_callback\_Fake::arg2\_history[(50u)] |
| --- |

## [◆ ](#a877ef95c441bdcf8b23150f25f54e8d9)arg2\_val

| void\* fake\_can\_set\_state\_change\_callback\_Fake::arg2\_val |
| --- |

## [◆ ](#a265b73064807e6f3b69595118ea17011)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_state\_change\_callback\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a665ffac5d8c9f9224acfb4359cc6d7c1)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_state\_change\_callback\_Fake::arg\_history\_len |
| --- |

## [◆ ](#aeea4d8cbe60185f2871acd99cedf31e2)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_set\_state\_change\_callback\_Fake::call\_count |
| --- |

## [◆ ](#abe6a7fc6c7f0fccf0c5096bc463b9a2f)custom\_fake

| void(\* fake\_can\_set\_state\_change\_callback\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d), void \*) |
| --- |

## [◆ ](#a1bb52f289114151a9e842d6a9de00330)custom\_fake\_seq

| void(\*\* fake\_can\_set\_state\_change\_callback\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d), void \*) |
| --- |

## [◆ ](#ad6bb6a36efba89f0c461cb7a50f290e8)custom\_fake\_seq\_idx

| int fake\_can\_set\_state\_change\_callback\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a18bad3283e5b731a46b14b0e37d8fcb7)custom\_fake\_seq\_len

| int fake\_can\_set\_state\_change\_callback\_Fake::custom\_fake\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_set\_state\_change\_callback\_Fake](structfake__can__set__state__change__callback__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
