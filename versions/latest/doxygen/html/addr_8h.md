---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/addr_8h.html
original_path: doxygen/html/addr_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

addr.h File Reference

Bluetooth device address definitions and utilities.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/sys/printk.h](printk_8h_source.md)>`

[Go to the source code of this file.](addr_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_addr\_t](structbt__addr__t.md) |
|  | Bluetooth Device Address. [More...](structbt__addr__t.md#details) |
| struct | [bt\_addr\_le\_t](structbt__addr__le__t.md) |
|  | Bluetooth LE Device Address. [More...](structbt__addr__le__t.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_ADDR\_LE\_PUBLIC](group__bt__addr.md#ga1717d2b4e61b28637be8a5f78685a3c4)   0x00 |
| #define | [BT\_ADDR\_LE\_RANDOM](group__bt__addr.md#ga6e81e967527b5418ee6cbc6d72c5aef9)   0x01 |
| #define | [BT\_ADDR\_LE\_PUBLIC\_ID](group__bt__addr.md#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)   0x02 |
| #define | [BT\_ADDR\_LE\_RANDOM\_ID](group__bt__addr.md#gafdf2572991427d95bb44d1a5ee2ad85a)   0x03 |
| #define | [BT\_ADDR\_LE\_UNRESOLVED](group__bt__addr.md#gad02c40564a140300efda28ecb15674be) |
| #define | [BT\_ADDR\_LE\_ANONYMOUS](group__bt__addr.md#gab2ddd85c5972a53da0aee3974edc0258) |
| #define | [BT\_ADDR\_SIZE](group__bt__addr.md#ga6b6f56325b5136d2719f02eecc780d49)   6 |
|  | Length in bytes of a standard Bluetooth address. |
| #define | [BT\_ADDR\_LE\_SIZE](group__bt__addr.md#ga2656b9a936bf8cb9f1cc86668fca6108)   7 |
|  | Length in bytes of an LE Bluetooth address. |
| #define | [BT\_ADDR\_ANY](group__bt__addr.md#ga40ddc9769e38b7537bbb4e8002de592a)   (&[bt\_addr\_any](group__bt__addr.md#gadd64afda1a14cbc2740f205e90169152)) |
|  | Bluetooth device "any" address, not a valid address. |
| #define | [BT\_ADDR\_NONE](group__bt__addr.md#gacb24d83ded350176fc96dfc0f5dde6be)   (&[bt\_addr\_none](group__bt__addr.md#ga0b2f611fbd28b066d261b81303c4b93f)) |
|  | Bluetooth device "none" address, not a valid address. |
| #define | [BT\_ADDR\_LE\_ANY](group__bt__addr.md#ga17e9efacd50c682b2f709c217e920d48)   (&[bt\_addr\_le\_any](group__bt__addr.md#ga40c282f720d13b5d24a2dd62bfdceb73)) |
|  | Bluetooth LE device "any" address, not a valid address. |
| #define | [BT\_ADDR\_LE\_NONE](group__bt__addr.md#gadfcc0281e453cba990b623631c26f80b)   (&[bt\_addr\_le\_none](group__bt__addr.md#gaefa17a553b6f8e9ad599e8db7538e1b8)) |
|  | Bluetooth LE device "none" address, not a valid address. |
| #define | [BT\_ADDR\_IS\_RPA](group__bt__addr.md#ga32abc1a2e827542efea5b9cb05a57fbc)(a) |
|  | Check if a Bluetooth LE random address is resolvable private address. |
| #define | [BT\_ADDR\_IS\_NRPA](group__bt__addr.md#gaa8745bff73c42a693cb76e42755b2bf9)(a) |
|  | Check if a Bluetooth LE random address is a non-resolvable private address. |
| #define | [BT\_ADDR\_IS\_STATIC](group__bt__addr.md#ga0cb3aa4d48cf41d8485b570ef0e7447a)(a) |
|  | Check if a Bluetooth LE random address is a static address. |
| #define | [BT\_ADDR\_SET\_RPA](group__bt__addr.md#ga52a0bd596e726dff39b247dfbc58406d)(a) |
|  | Set a Bluetooth LE random address as a resolvable private address. |
| #define | [BT\_ADDR\_SET\_NRPA](group__bt__addr.md#ga6b23035316e9bdd071e10ecc803fcdbc)(a) |
|  | Set a Bluetooth LE random address as a non-resolvable private address. |
| #define | [BT\_ADDR\_SET\_STATIC](group__bt__addr.md#gaa6261bf0b96099b58f0a0c3674ce5713)(a) |
|  | Set a Bluetooth LE random address as a static address. |
| #define | [BT\_ADDR\_STR\_LEN](group__bt__addr.md#ga8097c3b80a5647b0b951d29aa30a397d)   18 |
|  | Recommended length of user string buffer for Bluetooth address. |
| #define | [BT\_ADDR\_LE\_STR\_LEN](group__bt__addr.md#gae0df0067c55eb4388625bb62f3d7e235)   30 |
|  | Recommended length of user string buffer for Bluetooth LE address. |

| Functions | |
| --- | --- |
| static int | [bt\_addr\_cmp](group__bt__addr.md#ga41ff9419098728f037c3e97d29c30ba9) (const [bt\_addr\_t](structbt__addr__t.md) \*a, const [bt\_addr\_t](structbt__addr__t.md) \*b) |
|  | Compare Bluetooth device addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_eq](group__bt__addr.md#gadecf8fe8e183a11a4ff569bc0d673ec1) (const [bt\_addr\_t](structbt__addr__t.md) \*a, const [bt\_addr\_t](structbt__addr__t.md) \*b) |
|  | Determine equality of two Bluetooth device addresses. |
| static int | [bt\_addr\_le\_cmp](group__bt__addr.md#ga588d392f51372ff2951c3ff39da22f12) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*a, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*b) |
|  | Compare Bluetooth LE device addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_le\_eq](group__bt__addr.md#ga8644e77108f029088adb203e5392016b) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*a, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*b) |
|  | Determine equality of two Bluetooth LE device addresses. |
| static void | [bt\_addr\_copy](group__bt__addr.md#ga5a8284cf34d0835d725dab31d710ea4c) ([bt\_addr\_t](structbt__addr__t.md) \*dst, const [bt\_addr\_t](structbt__addr__t.md) \*src) |
|  | Copy Bluetooth device address. |
| static void | [bt\_addr\_le\_copy](group__bt__addr.md#gac6c9b20f17936efaa082fe63aedc2138) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*dst, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*src) |
|  | Copy Bluetooth LE device address. |
| int | [bt\_addr\_le\_create\_nrpa](group__bt__addr.md#gaf2d38888131c9e8bdbc820b415c14082) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Create a Bluetooth LE random non-resolvable private address. |
| int | [bt\_addr\_le\_create\_static](group__bt__addr.md#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Create a Bluetooth LE random static address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_le\_is\_rpa](group__bt__addr.md#ga42bcee6b5aadde7ccdbe243df25043bc) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Check if a Bluetooth LE address is a random private resolvable address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_le\_is\_identity](group__bt__addr.md#ga7a6acc7a9267ae2645aeee38e553b8b3) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Check if a Bluetooth LE address is valid identity address. |
| static int | [bt\_addr\_to\_str](group__bt__addr.md#ga151bdd0ada8635acfebd60f0e203cde2) (const [bt\_addr\_t](structbt__addr__t.md) \*addr, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Converts binary Bluetooth address to string. |
| static int | [bt\_addr\_le\_to\_str](group__bt__addr.md#ga74a644cd3de081a353a281d80b32b91e) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Converts binary LE Bluetooth address to string. |
| int | [bt\_addr\_from\_str](group__bt__addr.md#gad93410d0161ca84939f4bf983da29c14) (const char \*str, [bt\_addr\_t](structbt__addr__t.md) \*addr) |
|  | Convert Bluetooth address from string to binary. |
| int | [bt\_addr\_le\_from\_str](group__bt__addr.md#ga2539a1ac8774587fb75702aac66f8e19) (const char \*str, const char \*type, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Convert LE Bluetooth address from string to binary. |

| Variables | |
| --- | --- |
| const [bt\_addr\_t](structbt__addr__t.md) | [bt\_addr\_any](group__bt__addr.md#gadd64afda1a14cbc2740f205e90169152) |
| const [bt\_addr\_t](structbt__addr__t.md) | [bt\_addr\_none](group__bt__addr.md#ga0b2f611fbd28b066d261b81303c4b93f) |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) | [bt\_addr\_le\_any](group__bt__addr.md#ga40c282f720d13b5d24a2dd62bfdceb73) |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) | [bt\_addr\_le\_none](group__bt__addr.md#gaefa17a553b6f8e9ad599e8db7538e1b8) |

## Detailed Description

Bluetooth device address definitions and utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [addr.h](addr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
