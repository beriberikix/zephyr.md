---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bindesc_8h.html
original_path: doxygen/html/bindesc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bindesc.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](bindesc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bindesc\_entry](structbindesc__entry.md) |
| struct | [bindesc\_handle](structbindesc__handle.md) |

| Macros | |
| --- | --- |
| #define | [BINDESC\_MAGIC](#a8e7d54173280f72eb5f031d752c19197)   0xb9863e5a7ea46046 |
| #define | [BINDESC\_ALIGNMENT](#a674bcf8c1d881131b5e82d5dec48ee33)   4 |
| #define | [BINDESC\_TYPE\_UINT](#adac0fea8ab54ea428c533f509058b910)   0x0 |
| #define | [BINDESC\_TYPE\_STR](#a68acc09b5e324134e5c83eeaa064fc41)   0x1 |
| #define | [BINDESC\_TYPE\_BYTES](#a24e6723b552f65cc1f143bcb7f66f125)   0x2 |
| #define | [BINDESC\_TYPE\_DESCRIPTORS\_END](#ac98ab7042b1b3f6654e910fa4d0c2d40)   0xf |
| #define | [BINDESC\_ENTRY\_HEADER\_SIZE](#a3327af407c3d5a7c05e9fd5c3c53380a)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [bindesc\_entry](structbindesc__entry.md))) |
| #define | [BINDESC\_ID\_APP\_VERSION\_STRING](group__bindesc__define.md#ga8521a2005ed6ad5bdbd6ad27a0e26cfc)   0x800 |
|  | The app version string such as "1.2.3". |
| #define | [BINDESC\_ID\_APP\_VERSION\_MAJOR](group__bindesc__define.md#ga94f405178c0139626718b143e6f22734)   0x801 |
|  | The app version major such as 1. |
| #define | [BINDESC\_ID\_APP\_VERSION\_MINOR](group__bindesc__define.md#gaab4f7cdf7ea4f766be1fa7779eef1bdb)   0x802 |
|  | The app version minor such as 2. |
| #define | [BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL](group__bindesc__define.md#ga90eb8f252c3484103eee18dbb1aabdc6)   0x803 |
|  | The app version patchlevel such as 3. |
| #define | [BINDESC\_ID\_APP\_VERSION\_NUMBER](group__bindesc__define.md#ga66b25585ff23de9906814ddecb4ac4ea)   0x804 |
|  | The app version number such as 0x10203. |
| #define | [BINDESC\_ID\_APP\_BUILD\_VERSION](group__bindesc__define.md#gadde3e821958da17070aa91dc82c51265)   0x805 |
|  | The app git reference such as "v3.3.0-18-g2c85d9224fca". |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_STRING](group__bindesc__define.md#ga35fdf13eb11dd4eeca1bf2dc57782777)   0x900 |
|  | The kernel version string such as "3.4.0". |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_MAJOR](group__bindesc__define.md#gabd5e9193c56495faa19f299371a02fd0)   0x901 |
|  | The kernel version major such as 3. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_MINOR](group__bindesc__define.md#ga9ab56a8cef01c648a313bb4e5b7983e4)   0x902 |
|  | The kernel version minor such as 4. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL](group__bindesc__define.md#ga2ef91c2cd49d61c9f3e95ac5292e6983)   0x903 |
|  | The kernel version patchlevel such as 0. |
| #define | [BINDESC\_ID\_KERNEL\_VERSION\_NUMBER](group__bindesc__define.md#gad2c5489eaa1a191a49ffd409462b1af4)   0x904 |
|  | The kernel version number such as 0x30400. |
| #define | [BINDESC\_ID\_KERNEL\_BUILD\_VERSION](group__bindesc__define.md#gaf7b25978649c3d9339e13ecaa1090c74)   0x905 |
|  | The kernel git reference such as "v3.3.0-18-g2c85d9224fca". |
| #define | [BINDESC\_ID\_BUILD\_TIME\_YEAR](group__bindesc__define.md#ga21fbd3ff6a408febdaf0f1a1f19f0fa3)   0xa00 |
|  | The year the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_MONTH](group__bindesc__define.md#ga8e68f8226d05415c040f6fb74bada6fc)   0xa01 |
|  | The month of the year the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_DAY](group__bindesc__define.md#ga5710e218f4f10e5049d039b17a376d0b)   0xa02 |
|  | The day of the month the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_HOUR](group__bindesc__define.md#gaeed1651e0d025ff74092a88b6d57e408)   0xa03 |
|  | The hour of the day the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_MINUTE](group__bindesc__define.md#ga67f679968aeea5517e02da6e5e67d73e)   0xa04 |
|  | The minute the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_SECOND](group__bindesc__define.md#gacdff70f58c8098e23611327c1264a7dd)   0xa05 |
|  | The second the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_TIME\_UNIX](group__bindesc__define.md#gab0eefe2d83294d6ebe4ca6299f05d785)   0xa06 |
|  | The UNIX time (seconds since midnight of 1970/01/01) the image was compiled in. |
| #define | [BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING](group__bindesc__define.md#gad8803e832ed0a42fd7033e277f8d8362)   0xa07 |
|  | The date and time of compilation such as "2023/02/05 00:07:04". |
| #define | [BINDESC\_ID\_BUILD\_DATE\_STRING](group__bindesc__define.md#ga8bf6d98fb9495f2cca6b0403dffd0752)   0xa08 |
|  | The date of compilation such as "2023/02/05". |
| #define | [BINDESC\_ID\_BUILD\_TIME\_STRING](group__bindesc__define.md#gac4f75b876a81072e14bb39e3fb1c1f8a)   0xa09 |
|  | The time of compilation such as "00:07:04". |
| #define | [BINDESC\_ID\_HOST\_NAME](group__bindesc__define.md#ga4cc66094d33709d9738b49e181a6eec3)   0xb00 |
|  | The name of the host that compiled the image. |
| #define | [BINDESC\_ID\_C\_COMPILER\_NAME](group__bindesc__define.md#ga51b3fdd47d3dd94101134523c4dca144)   0xb01 |
|  | The C compiler name. |
| #define | [BINDESC\_ID\_C\_COMPILER\_VERSION](group__bindesc__define.md#gac4c6c9576b31cb2c26b085537648552b)   0xb02 |
|  | The C compiler version. |
| #define | [BINDESC\_ID\_CXX\_COMPILER\_NAME](group__bindesc__define.md#ga6f198590afdb2524b587e0194598b8eb)   0xb03 |
|  | The C++ compiler name. |
| #define | [BINDESC\_ID\_CXX\_COMPILER\_VERSION](group__bindesc__define.md#ga7ec0430daae1f99bdeeae6a636a263d8)   0xb04 |
|  | The C++ compiler version. |
| #define | [BINDESC\_TAG\_DESCRIPTORS\_END](group__bindesc__define.md#gac12b3cbf6d132fb54bbf702fd581373f)   BINDESC\_TAG(DESCRIPTORS\_END, 0x0fff) |
| #define | [BINDESC\_STR\_DEFINE](group__bindesc__define.md#gacfba0fe843c53a86271e685394078b22)(name, id, value) |
|  | Define a binary descriptor of type string. |
| #define | [BINDESC\_UINT\_DEFINE](group__bindesc__define.md#gac603068b1abdac72d5f668fea3b3cdff)(name, id, value) |
|  | Define a binary descriptor of type uint. |
| #define | [BINDESC\_BYTES\_DEFINE](group__bindesc__define.md#ga137cc1f8fcc0e36e71c8ea4b8c0e8885)(name, id, value) |
|  | Define a binary descriptor of type bytes. |
| #define | [BINDESC\_GET\_STR](group__bindesc__define.md#gaf7628498209bc6729a6abf36a92d0cbd)(name) |
|  | Get the value of a string binary descriptor. |
| #define | [BINDESC\_GET\_UINT](group__bindesc__define.md#ga8f738fd9f99f52f0c7ce81011c8e7b98)(name) |
|  | Get the value of a uint binary descriptor. |
| #define | [BINDESC\_GET\_BYTES](group__bindesc__define.md#ga1fbf08f04e66c250aecdd70045242a37)(name) |
|  | Get the value of a bytes binary descriptor. |
| #define | [BINDESC\_GET\_SIZE](group__bindesc__define.md#gace8f89f0a8d25a12503c1b337f74dd30)(name) |
|  | Get the size of a binary descriptor. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bindesc\_callback\_t](group__bindesc__read.md#ga6f02f63064e53a0d85150982cc529519)) (const struct [bindesc\_entry](structbindesc__entry.md) \*entry, void \*user\_data) |
|  | Callback type to be called on descriptors found during a walk. |

| Functions | |
| --- | --- |
| int | [bindesc\_open\_memory\_mapped\_flash](group__bindesc__read.md#ga3ed93a855c2ee2981f2ca76450c57d99) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Open an image's binary descriptors for reading, from a memory mapped flash. |
| int | [bindesc\_open\_ram](group__bindesc__read.md#gadec0f4f828c1e4cdcef63b67c0fbafcf) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*address, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_size) |
|  | Open an image's binary descriptors for reading, from RAM. |
| int | [bindesc\_open\_flash](group__bindesc__read.md#ga724d940fecd648523c3d3bd840785498) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const struct [device](structdevice.md) \*flash\_device) |
|  | Open an image's binary descriptors for reading, from flash. |
| int | [bindesc\_foreach](group__bindesc__read.md#ga8d7f293d620a80b49797d4c1d6d2998f) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [bindesc\_callback\_t](group__bindesc__read.md#ga6f02f63064e53a0d85150982cc529519) callback, void \*user\_data) |
|  | Walk the binary descriptors and run a user defined callback on each of them. |
| int | [bindesc\_find\_str](group__bindesc__read.md#ga422708cc9ffb1a911b4990eff0270e76) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const char \*\*result) |
|  | Find a specific descriptor of type string. |
| int | [bindesc\_find\_uint](group__bindesc__read.md#gad3ae2bde011c2115a33c836caff37811) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*\*result) |
|  | Find a specific descriptor of type uint. |
| int | [bindesc\_find\_bytes](group__bindesc__read.md#gaf8b8b3a883f5c835d5a0581768d801d4) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*result, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result\_size) |
|  | Find a specific descriptor of type bytes. |
| int | [bindesc\_get\_size](group__bindesc__read.md#ga7df52ef12aa9572d3a2ff4245529d8fd) (struct [bindesc\_handle](structbindesc__handle.md) \*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
|  | Get the size of an image's binary descriptors. |

| Variables | |
| --- | --- |
| Incorrect memory | [layout](#af8174bbae9567135fe17f1e55621f641) |

## Macro Definition Documentation

## [◆ ](#a674bcf8c1d881131b5e82d5dec48ee33)BINDESC\_ALIGNMENT

| #define BINDESC\_ALIGNMENT   4 |
| --- |

## [◆ ](#a3327af407c3d5a7c05e9fd5c3c53380a)BINDESC\_ENTRY\_HEADER\_SIZE

| #define BINDESC\_ENTRY\_HEADER\_SIZE   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [bindesc\_entry](structbindesc__entry.md))) |
| --- |

## [◆ ](#a8e7d54173280f72eb5f031d752c19197)BINDESC\_MAGIC

| #define BINDESC\_MAGIC   0xb9863e5a7ea46046 |
| --- |

## [◆ ](#a24e6723b552f65cc1f143bcb7f66f125)BINDESC\_TYPE\_BYTES

| #define BINDESC\_TYPE\_BYTES   0x2 |
| --- |

## [◆ ](#ac98ab7042b1b3f6654e910fa4d0c2d40)BINDESC\_TYPE\_DESCRIPTORS\_END

| #define BINDESC\_TYPE\_DESCRIPTORS\_END   0xf |
| --- |

## [◆ ](#a68acc09b5e324134e5c83eeaa064fc41)BINDESC\_TYPE\_STR

| #define BINDESC\_TYPE\_STR   0x1 |
| --- |

## [◆ ](#adac0fea8ab54ea428c533f509058b910)BINDESC\_TYPE\_UINT

| #define BINDESC\_TYPE\_UINT   0x0 |
| --- |

## Variable Documentation

## [◆ ](#af8174bbae9567135fe17f1e55621f641)layout

| Incorrect memory layout |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bindesc.h](bindesc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
