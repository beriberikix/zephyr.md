---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfake__can__remove__rx__filter__Fake.html
original_path: doxygen/html/structfake__can__remove__rx__filter__Fake.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_remove\_rx\_filter\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#ab0e2060727803583d9f6e809e82e6655) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a56275f173f6ae79a2baa2b5fd6f53335) [(50u)] |
| int | [arg1\_val](#ad37cc173abf16fd381935e090766eefa) |
| int | [arg1\_history](#a5eb3c0e60321e69b60156b746377e5d2) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#af7dcfa56f44a8409853a68ec50e400a4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a558bafd009b860c1b36d0bdf49044826) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#ae5f621c8c579bc1e4a37c45520bd2322) |
| int | [custom\_fake\_seq\_len](#ab69617f5fd720f3a619aacd5900fb8ea) |
| int | [custom\_fake\_seq\_idx](#aacb8c8744b9dca2fb121f55b87023f75) |
| void(\* | [custom\_fake](#a74db5a0a96e662194c8864a16d223d26) )(const struct [device](structdevice.md) \*, int) |
| void(\*\* | [custom\_fake\_seq](#a0f2a8c4aaf5536523f45a5fca36bef2a) )(const struct [device](structdevice.md) \*, int) |

## Field Documentation

## [◆ ](#a56275f173f6ae79a2baa2b5fd6f53335)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_remove\_rx\_filter\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#ab0e2060727803583d9f6e809e82e6655)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_remove\_rx\_filter\_Fake::arg0\_val |
| --- |

## [◆ ](#a5eb3c0e60321e69b60156b746377e5d2)arg1\_history

| int fake\_can\_remove\_rx\_filter\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#ad37cc173abf16fd381935e090766eefa)arg1\_val

| int fake\_can\_remove\_rx\_filter\_Fake::arg1\_val |
| --- |

## [◆ ](#ae5f621c8c579bc1e4a37c45520bd2322)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_remove\_rx\_filter\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a558bafd009b860c1b36d0bdf49044826)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_remove\_rx\_filter\_Fake::arg\_history\_len |
| --- |

## [◆ ](#af7dcfa56f44a8409853a68ec50e400a4)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_remove\_rx\_filter\_Fake::call\_count |
| --- |

## [◆ ](#a74db5a0a96e662194c8864a16d223d26)custom\_fake

| void(\* fake\_can\_remove\_rx\_filter\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, int) |
| --- |

## [◆ ](#a0f2a8c4aaf5536523f45a5fca36bef2a)custom\_fake\_seq

| void(\*\* fake\_can\_remove\_rx\_filter\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, int) |
| --- |

## [◆ ](#aacb8c8744b9dca2fb121f55b87023f75)custom\_fake\_seq\_idx

| int fake\_can\_remove\_rx\_filter\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#ab69617f5fd720f3a619aacd5900fb8ea)custom\_fake\_seq\_len

| int fake\_can\_remove\_rx\_filter\_Fake::custom\_fake\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_remove\_rx\_filter\_Fake](structfake__can__remove__rx__filter__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
