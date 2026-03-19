---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmic__privacy__api__funcs.html
original_path: doxygen/html/structmic__privacy__api__funcs.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mic\_privacy\_api\_funcs Struct Reference

`#include <[mic_privacy.h](mic__privacy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [enable\_fw\_managed\_irq](#a67548968f088126881ef11f7317e5036) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf), const void \*fn) |
| void(\* | [clear\_fw\_managed\_irq](#a294e4cd3bb23ccb23f7143b6a9e4dba5) )() |
| void(\* | [enable\_dmic\_irq](#afc87beb092fa02c06dcd84125ccc305a) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf), const void \*fn) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [get\_dmic\_irq\_status](#a8cd74fd6817c3f5bfa0fc7697765d357) )(void) |
| void(\* | [clear\_dmic\_irq\_status](#ae68b97acf6ec4f5812275ee682bdf96d) )(void) |
| enum [mic\_privacy\_policy](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931)(\* | [get\_policy](#a558346b619a67f3f05b20cf62a7993ef) )() |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_privacy\_policy\_register\_raw\_value](#ad03e41de9d08b1cdd77abd6d40f14baf) )() |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_dma\_data\_zeroing\_wait\_time](#a1ee80c505a6a7d7bdf34c228acfc3b87) )() |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_dma\_data\_zeroing\_link\_select](#a73ea5882b8af5f4a738913c1c16a3aaf) )() |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_dmic\_mic\_disable\_status](#a3e365ecf294cf653d0439d5d6d7d6ed5) )(void) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_fw\_managed\_mic\_disable\_status](#abedb0ba2dbb1d9ba639aab636308747f) )() |
| void(\* | [set\_fw\_managed\_mode](#a9b827a1b6b817d5e5ec19ffa94b531f0) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_fw\_managed\_enabled) |
| void(\* | [set\_fw\_mic\_disable\_status](#a6f21bade6b6041322cba6995f9140d6b) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fw\_mic\_disable\_status) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_fw\_mic\_disable\_status](#ac60beb8b72089feab7267c265d4bfe5d) )() |

## Field Documentation

## [◆ ](#ae68b97acf6ec4f5812275ee682bdf96d)clear\_dmic\_irq\_status

| void(\* mic\_privacy\_api\_funcs::clear\_dmic\_irq\_status) (void) |
| --- |

## [◆ ](#a294e4cd3bb23ccb23f7143b6a9e4dba5)clear\_fw\_managed\_irq

| void(\* mic\_privacy\_api\_funcs::clear\_fw\_managed\_irq) () |
| --- |

## [◆ ](#afc87beb092fa02c06dcd84125ccc305a)enable\_dmic\_irq

| void(\* mic\_privacy\_api\_funcs::enable\_dmic\_irq) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf), const void \*fn) |
| --- |

## [◆ ](#a67548968f088126881ef11f7317e5036)enable\_fw\_managed\_irq

| void(\* mic\_privacy\_api\_funcs::enable\_fw\_managed\_irq) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf), const void \*fn) |
| --- |

## [◆ ](#a73ea5882b8af5f4a738913c1c16a3aaf)get\_dma\_data\_zeroing\_link\_select

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mic\_privacy\_api\_funcs::get\_dma\_data\_zeroing\_link\_select) () |
| --- |

## [◆ ](#a1ee80c505a6a7d7bdf34c228acfc3b87)get\_dma\_data\_zeroing\_wait\_time

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mic\_privacy\_api\_funcs::get\_dma\_data\_zeroing\_wait\_time) () |
| --- |

## [◆ ](#a8cd74fd6817c3f5bfa0fc7697765d357)get\_dmic\_irq\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* mic\_privacy\_api\_funcs::get\_dmic\_irq\_status) (void) |
| --- |

## [◆ ](#a3e365ecf294cf653d0439d5d6d7d6ed5)get\_dmic\_mic\_disable\_status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mic\_privacy\_api\_funcs::get\_dmic\_mic\_disable\_status) (void) |
| --- |

## [◆ ](#abedb0ba2dbb1d9ba639aab636308747f)get\_fw\_managed\_mic\_disable\_status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mic\_privacy\_api\_funcs::get\_fw\_managed\_mic\_disable\_status) () |
| --- |

## [◆ ](#ac60beb8b72089feab7267c265d4bfe5d)get\_fw\_mic\_disable\_status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mic\_privacy\_api\_funcs::get\_fw\_mic\_disable\_status) () |
| --- |

## [◆ ](#a558346b619a67f3f05b20cf62a7993ef)get\_policy

| enum [mic\_privacy\_policy](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931)(\* mic\_privacy\_api\_funcs::get\_policy) () |
| --- |

## [◆ ](#ad03e41de9d08b1cdd77abd6d40f14baf)get\_privacy\_policy\_register\_raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mic\_privacy\_api\_funcs::get\_privacy\_policy\_register\_raw\_value) () |
| --- |

## [◆ ](#a9b827a1b6b817d5e5ec19ffa94b531f0)set\_fw\_managed\_mode

| void(\* mic\_privacy\_api\_funcs::set\_fw\_managed\_mode) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_fw\_managed\_enabled) |
| --- |

## [◆ ](#a6f21bade6b6041322cba6995f9140d6b)set\_fw\_mic\_disable\_status

| void(\* mic\_privacy\_api\_funcs::set\_fw\_mic\_disable\_status) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fw\_mic\_disable\_status) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/mic\_privacy/intel/[mic\_privacy.h](mic__privacy_8h_source.md)

- [mic\_privacy\_api\_funcs](structmic__privacy__api__funcs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
