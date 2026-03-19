---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__addr.html
original_path: doxygen/html/group__bt__addr.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Device Address

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth device address definitions and utilities.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_addr\_t](structbt__addr__t.md) |
|  | Bluetooth Device Address. [More...](structbt__addr__t.md#details) |
| struct | [bt\_addr\_le\_t](structbt__addr__le__t.md) |
|  | Bluetooth LE Device Address. [More...](structbt__addr__le__t.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_ADDR\_LE\_PUBLIC](#ga1717d2b4e61b28637be8a5f78685a3c4)   0x00 |
| #define | [BT\_ADDR\_LE\_RANDOM](#ga6e81e967527b5418ee6cbc6d72c5aef9)   0x01 |
| #define | [BT\_ADDR\_LE\_PUBLIC\_ID](#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)   0x02 |
| #define | [BT\_ADDR\_LE\_RANDOM\_ID](#gafdf2572991427d95bb44d1a5ee2ad85a)   0x03 |
| #define | [BT\_ADDR\_LE\_UNRESOLVED](#gad02c40564a140300efda28ecb15674be) |
| #define | [BT\_ADDR\_LE\_ANONYMOUS](#gab2ddd85c5972a53da0aee3974edc0258) |
| #define | [BT\_ADDR\_SIZE](#ga6b6f56325b5136d2719f02eecc780d49)   6 |
|  | Length in bytes of a standard Bluetooth address. |
| #define | [BT\_ADDR\_LE\_SIZE](#ga2656b9a936bf8cb9f1cc86668fca6108)   7 |
|  | Length in bytes of an LE Bluetooth address. |
| #define | [BT\_ADDR\_ANY](#ga40ddc9769e38b7537bbb4e8002de592a)   (&[bt\_addr\_any](#gadd64afda1a14cbc2740f205e90169152)) |
|  | Bluetooth device "any" address, not a valid address. |
| #define | [BT\_ADDR\_NONE](#gacb24d83ded350176fc96dfc0f5dde6be)   (&[bt\_addr\_none](#ga0b2f611fbd28b066d261b81303c4b93f)) |
|  | Bluetooth device "none" address, not a valid address. |
| #define | [BT\_ADDR\_LE\_ANY](#ga17e9efacd50c682b2f709c217e920d48)   (&[bt\_addr\_le\_any](#ga40c282f720d13b5d24a2dd62bfdceb73)) |
|  | Bluetooth LE device "any" address, not a valid address. |
| #define | [BT\_ADDR\_LE\_NONE](#gadfcc0281e453cba990b623631c26f80b)   (&[bt\_addr\_le\_none](#gaefa17a553b6f8e9ad599e8db7538e1b8)) |
|  | Bluetooth LE device "none" address, not a valid address. |
| #define | [BT\_ADDR\_IS\_RPA](#ga32abc1a2e827542efea5b9cb05a57fbc)(a) |
|  | Check if a Bluetooth LE random address is resolvable private address. |
| #define | [BT\_ADDR\_IS\_NRPA](#gaa8745bff73c42a693cb76e42755b2bf9)(a) |
|  | Check if a Bluetooth LE random address is a non-resolvable private address. |
| #define | [BT\_ADDR\_IS\_STATIC](#ga0cb3aa4d48cf41d8485b570ef0e7447a)(a) |
|  | Check if a Bluetooth LE random address is a static address. |
| #define | [BT\_ADDR\_SET\_RPA](#ga52a0bd596e726dff39b247dfbc58406d)(a) |
|  | Set a Bluetooth LE random address as a resolvable private address. |
| #define | [BT\_ADDR\_SET\_NRPA](#ga6b23035316e9bdd071e10ecc803fcdbc)(a) |
|  | Set a Bluetooth LE random address as a non-resolvable private address. |
| #define | [BT\_ADDR\_SET\_STATIC](#gaa6261bf0b96099b58f0a0c3674ce5713)(a) |
|  | Set a Bluetooth LE random address as a static address. |
| #define | [BT\_ADDR\_STR\_LEN](#ga8097c3b80a5647b0b951d29aa30a397d)   18 |
|  | Recommended length of user string buffer for Bluetooth address. |
| #define | [BT\_ADDR\_LE\_STR\_LEN](#gae0df0067c55eb4388625bb62f3d7e235)   30 |
|  | Recommended length of user string buffer for Bluetooth LE address. |

| Functions | |
| --- | --- |
| static int | [bt\_addr\_cmp](#ga41ff9419098728f037c3e97d29c30ba9) (const [bt\_addr\_t](structbt__addr__t.md) \*a, const [bt\_addr\_t](structbt__addr__t.md) \*b) |
|  | Compare Bluetooth device addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_eq](#gadecf8fe8e183a11a4ff569bc0d673ec1) (const [bt\_addr\_t](structbt__addr__t.md) \*a, const [bt\_addr\_t](structbt__addr__t.md) \*b) |
|  | Determine equality of two Bluetooth device addresses. |
| static int | [bt\_addr\_le\_cmp](#ga588d392f51372ff2951c3ff39da22f12) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*a, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*b) |
|  | Compare Bluetooth LE device addresses. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_le\_eq](#ga8644e77108f029088adb203e5392016b) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*a, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*b) |
|  | Determine equality of two Bluetooth LE device addresses. |
| static void | [bt\_addr\_copy](#ga5a8284cf34d0835d725dab31d710ea4c) ([bt\_addr\_t](structbt__addr__t.md) \*dst, const [bt\_addr\_t](structbt__addr__t.md) \*src) |
|  | Copy Bluetooth device address. |
| static void | [bt\_addr\_le\_copy](#gac6c9b20f17936efaa082fe63aedc2138) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*dst, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*src) |
|  | Copy Bluetooth LE device address. |
| int | [bt\_addr\_le\_create\_nrpa](#gaf2d38888131c9e8bdbc820b415c14082) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Create a Bluetooth LE random non-resolvable private address. |
| int | [bt\_addr\_le\_create\_static](#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Create a Bluetooth LE random static address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_le\_is\_rpa](#ga42bcee6b5aadde7ccdbe243df25043bc) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Check if a Bluetooth LE address is a random private resolvable address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_addr\_le\_is\_identity](#ga7a6acc7a9267ae2645aeee38e553b8b3) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Check if a Bluetooth LE address is valid identity address. |
| static int | [bt\_addr\_to\_str](#ga151bdd0ada8635acfebd60f0e203cde2) (const [bt\_addr\_t](structbt__addr__t.md) \*addr, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Converts binary Bluetooth address to string. |
| static int | [bt\_addr\_le\_to\_str](#ga74a644cd3de081a353a281d80b32b91e) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Converts binary LE Bluetooth address to string. |
| int | [bt\_addr\_from\_str](#gad93410d0161ca84939f4bf983da29c14) (const char \*str, [bt\_addr\_t](structbt__addr__t.md) \*addr) |
|  | Convert Bluetooth address from string to binary. |
| int | [bt\_addr\_le\_from\_str](#ga2539a1ac8774587fb75702aac66f8e19) (const char \*str, const char \*type, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Convert LE Bluetooth address from string to binary. |

| Variables | |
| --- | --- |
| const [bt\_addr\_t](structbt__addr__t.md) | [bt\_addr\_any](#gadd64afda1a14cbc2740f205e90169152) |
| const [bt\_addr\_t](structbt__addr__t.md) | [bt\_addr\_none](#ga0b2f611fbd28b066d261b81303c4b93f) |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) | [bt\_addr\_le\_any](#ga40c282f720d13b5d24a2dd62bfdceb73) |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) | [bt\_addr\_le\_none](#gaefa17a553b6f8e9ad599e8db7538e1b8) |

## Detailed Description

Bluetooth device address definitions and utilities.

## Macro Definition Documentation

## [◆ ](#ga40ddc9769e38b7537bbb4e8002de592a)BT\_ADDR\_ANY

| #define BT\_ADDR\_ANY   (&[bt\_addr\_any](#gadd64afda1a14cbc2740f205e90169152)) |
| --- |

`#include <[addr.h](addr_8h.md)>`

Bluetooth device "any" address, not a valid address.

## [◆ ](#gaa8745bff73c42a693cb76e42755b2bf9)BT\_ADDR\_IS\_NRPA

| #define BT\_ADDR\_IS\_NRPA | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

(((a)->val[5] & 0xc0) == 0x00)

Check if a Bluetooth LE random address is a non-resolvable private address.

## [◆ ](#ga32abc1a2e827542efea5b9cb05a57fbc)BT\_ADDR\_IS\_RPA

| #define BT\_ADDR\_IS\_RPA | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

(((a)->val[5] & 0xc0) == 0x40)

Check if a Bluetooth LE random address is resolvable private address.

## [◆ ](#ga0cb3aa4d48cf41d8485b570ef0e7447a)BT\_ADDR\_IS\_STATIC

| #define BT\_ADDR\_IS\_STATIC | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

(((a)->val[5] & 0xc0) == 0xc0)

Check if a Bluetooth LE random address is a static address.

## [◆ ](#gab2ddd85c5972a53da0aee3974edc0258)BT\_ADDR\_LE\_ANONYMOUS

| #define BT\_ADDR\_LE\_ANONYMOUS |
| --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

0xFF /\* No address provided

\* (anonymous advertisement)

\*/

## [◆ ](#ga17e9efacd50c682b2f709c217e920d48)BT\_ADDR\_LE\_ANY

| #define BT\_ADDR\_LE\_ANY   (&[bt\_addr\_le\_any](#ga40c282f720d13b5d24a2dd62bfdceb73)) |
| --- |

`#include <[addr.h](addr_8h.md)>`

Bluetooth LE device "any" address, not a valid address.

## [◆ ](#gadfcc0281e453cba990b623631c26f80b)BT\_ADDR\_LE\_NONE

| #define BT\_ADDR\_LE\_NONE   (&[bt\_addr\_le\_none](#gaefa17a553b6f8e9ad599e8db7538e1b8)) |
| --- |

`#include <[addr.h](addr_8h.md)>`

Bluetooth LE device "none" address, not a valid address.

## [◆ ](#ga1717d2b4e61b28637be8a5f78685a3c4)BT\_ADDR\_LE\_PUBLIC

| #define BT\_ADDR\_LE\_PUBLIC   0x00 |
| --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)BT\_ADDR\_LE\_PUBLIC\_ID

| #define BT\_ADDR\_LE\_PUBLIC\_ID   0x02 |
| --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#ga6e81e967527b5418ee6cbc6d72c5aef9)BT\_ADDR\_LE\_RANDOM

| #define BT\_ADDR\_LE\_RANDOM   0x01 |
| --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#gafdf2572991427d95bb44d1a5ee2ad85a)BT\_ADDR\_LE\_RANDOM\_ID

| #define BT\_ADDR\_LE\_RANDOM\_ID   0x03 |
| --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#ga2656b9a936bf8cb9f1cc86668fca6108)BT\_ADDR\_LE\_SIZE

| #define BT\_ADDR\_LE\_SIZE   7 |
| --- |

`#include <[addr.h](addr_8h.md)>`

Length in bytes of an LE Bluetooth address.

Not packed, so no [sizeof()](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)

## [◆ ](#gae0df0067c55eb4388625bb62f3d7e235)BT\_ADDR\_LE\_STR\_LEN

| #define BT\_ADDR\_LE\_STR\_LEN   30 |
| --- |

`#include <[addr.h](addr_8h.md)>`

Recommended length of user string buffer for Bluetooth LE address.

The recommended length guarantee the output of address conversion will not lose valuable information about address being processed.

## [◆ ](#gad02c40564a140300efda28ecb15674be)BT\_ADDR\_LE\_UNRESOLVED

| #define BT\_ADDR\_LE\_UNRESOLVED |
| --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

0xFE /\* Resolvable Private Address

\* (Controller unable to resolve)

\*/

## [◆ ](#gacb24d83ded350176fc96dfc0f5dde6be)BT\_ADDR\_NONE

| #define BT\_ADDR\_NONE   (&[bt\_addr\_none](#ga0b2f611fbd28b066d261b81303c4b93f)) |
| --- |

`#include <[addr.h](addr_8h.md)>`

Bluetooth device "none" address, not a valid address.

## [◆ ](#ga6b23035316e9bdd071e10ecc803fcdbc)BT\_ADDR\_SET\_NRPA

| #define BT\_ADDR\_SET\_NRPA | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

((a)->val[5] &= 0x3f)

Set a Bluetooth LE random address as a non-resolvable private address.

## [◆ ](#ga52a0bd596e726dff39b247dfbc58406d)BT\_ADDR\_SET\_RPA

| #define BT\_ADDR\_SET\_RPA | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

((a)->val[5] = (((a)->val[5] & 0x3f) | 0x40))

Set a Bluetooth LE random address as a resolvable private address.

## [◆ ](#gaa6261bf0b96099b58f0a0c3674ce5713)BT\_ADDR\_SET\_STATIC

| #define BT\_ADDR\_SET\_STATIC | ( |  | *a* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

**Value:**

((a)->val[5] |= 0xc0)

Set a Bluetooth LE random address as a static address.

## [◆ ](#ga6b6f56325b5136d2719f02eecc780d49)BT\_ADDR\_SIZE

| #define BT\_ADDR\_SIZE   6 |
| --- |

`#include <[addr.h](addr_8h.md)>`

Length in bytes of a standard Bluetooth address.

## [◆ ](#ga8097c3b80a5647b0b951d29aa30a397d)BT\_ADDR\_STR\_LEN

| #define BT\_ADDR\_STR\_LEN   18 |
| --- |

`#include <[addr.h](addr_8h.md)>`

Recommended length of user string buffer for Bluetooth address.

The recommended length guarantee the output of address conversion will not lose valuable information about address being processed.

## Function Documentation

## [◆ ](#ga41ff9419098728f037c3e97d29c30ba9)bt\_addr\_cmp()

| | int bt\_addr\_cmp | ( | const [bt\_addr\_t](structbt__addr__t.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const [bt\_addr\_t](structbt__addr__t.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Compare Bluetooth device addresses.

Parameters
:   | a | First Bluetooth device address to compare |
    | --- | --- |
    | b | Second Bluetooth device address to compare |

Returns
:   negative value if *a* < *b*, 0 if *a* == *b*, else positive

## [◆ ](#ga5a8284cf34d0835d725dab31d710ea4c)bt\_addr\_copy()

| | void bt\_addr\_copy | ( | [bt\_addr\_t](structbt__addr__t.md) \* | *dst*, | | --- | --- | --- | --- | |  |  | const [bt\_addr\_t](structbt__addr__t.md) \* | *src* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Copy Bluetooth device address.

Parameters
:   | dst | Bluetooth device address destination buffer. |
    | --- | --- |
    | src | Bluetooth device address source buffer. |

## [◆ ](#gadecf8fe8e183a11a4ff569bc0d673ec1)bt\_addr\_eq()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_addr\_eq | ( | const [bt\_addr\_t](structbt__addr__t.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const [bt\_addr\_t](structbt__addr__t.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Determine equality of two Bluetooth device addresses.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the two addresses are equal |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise |

## [◆ ](#gad93410d0161ca84939f4bf983da29c14)bt\_addr\_from\_str()

| int bt\_addr\_from\_str | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [bt\_addr\_t](structbt__addr__t.md) \* | *addr* ) |

`#include <[addr.h](addr_8h.md)>`

Convert Bluetooth address from string to binary.

Parameters
:   | [in] | str | The string representation of a Bluetooth address. |
    | --- | --- | --- |
    | [out] | addr | Address of buffer to store the Bluetooth address |

Return values
:   | 0 | Success. The parsed address is stored in `addr`. |
    | --- | --- |

Returns
:   -EINVAL Invalid address string. `str` is not a well-formed Bluetooth address.

## [◆ ](#ga588d392f51372ff2951c3ff39da22f12)bt\_addr\_le\_cmp()

| | int bt\_addr\_le\_cmp | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Compare Bluetooth LE device addresses.

Parameters
:   | a | First Bluetooth LE device address to compare |
    | --- | --- |
    | b | Second Bluetooth LE device address to compare |

Returns
:   negative value if *a* < *b*, 0 if *a* == *b*, else positive

See also
:   [bt\_addr\_le\_eq](#ga8644e77108f029088adb203e5392016b)

## [◆ ](#gac6c9b20f17936efaa082fe63aedc2138)bt\_addr\_le\_copy()

| | void bt\_addr\_le\_copy | ( | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *dst*, | | --- | --- | --- | --- | |  |  | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *src* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Copy Bluetooth LE device address.

Parameters
:   | dst | Bluetooth LE device address destination buffer. |
    | --- | --- |
    | src | Bluetooth LE device address source buffer. |

## [◆ ](#gaf2d38888131c9e8bdbc820b415c14082)bt\_addr\_le\_create\_nrpa()

| int bt\_addr\_le\_create\_nrpa | ( | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Create a Bluetooth LE random non-resolvable private address.

## [◆ ](#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)bt\_addr\_le\_create\_static()

| int bt\_addr\_le\_create\_static | ( | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Create a Bluetooth LE random static address.

## [◆ ](#ga8644e77108f029088adb203e5392016b)bt\_addr\_le\_eq()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_addr\_le\_eq | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *a*, | | --- | --- | --- | --- | |  |  | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *b* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Determine equality of two Bluetooth LE device addresses.

The Bluetooth LE addresses are equal if and only if both the types and the 48-bit addresses are numerically equal.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the two addresses are equal |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise |

## [◆ ](#ga2539a1ac8774587fb75702aac66f8e19)bt\_addr\_le\_from\_str()

| int bt\_addr\_le\_from\_str | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | const char \* | *type*, |
|  |  | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* ) |

`#include <[addr.h](addr_8h.md)>`

Convert LE Bluetooth address from string to binary.

Parameters
:   | [in] | str | The string representation of an LE Bluetooth address. |
    | --- | --- | --- |
    | [in] | type | The string representation of the LE Bluetooth address type. |
    | [out] | addr | Address of buffer to store the LE Bluetooth address |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga7a6acc7a9267ae2645aeee38e553b8b3)bt\_addr\_le\_is\_identity()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_addr\_le\_is\_identity | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Check if a Bluetooth LE address is valid identity address.

Valid Bluetooth LE identity addresses are either public address or random static address.

Parameters
:   | addr | Bluetooth LE device address. |
    | --- | --- |

Returns
:   true if address is a valid identity address.

## [◆ ](#ga42bcee6b5aadde7ccdbe243df25043bc)bt\_addr\_le\_is\_rpa()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_addr\_le\_is\_rpa | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Check if a Bluetooth LE address is a random private resolvable address.

Parameters
:   | addr | Bluetooth LE device address. |
    | --- | --- |

Returns
:   true if address is a random private resolvable address.

## [◆ ](#ga74a644cd3de081a353a281d80b32b91e)bt\_addr\_le\_to\_str()

| | int bt\_addr\_le\_to\_str | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | char \* | *str*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Converts binary LE Bluetooth address to string.

Parameters
:   | addr | Address of buffer containing binary LE Bluetooth address. |
    | --- | --- |
    | str | Address of user buffer with enough room to store formatted string containing binary LE address. |
    | len | Length of data to be copied to user string buffer. Refer to BT\_ADDR\_LE\_STR\_LEN about recommended value. |

Returns
:   Number of successfully formatted bytes from binary address.

## [◆ ](#ga151bdd0ada8635acfebd60f0e203cde2)bt\_addr\_to\_str()

| | int bt\_addr\_to\_str | ( | const [bt\_addr\_t](structbt__addr__t.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | char \* | *str*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

Converts binary Bluetooth address to string.

Parameters
:   | addr | Address of buffer containing binary Bluetooth address. |
    | --- | --- |
    | str | Address of user buffer with enough room to store formatted string containing binary address. |
    | len | Length of data to be copied to user string buffer. Refer to BT\_ADDR\_STR\_LEN about recommended value. |

Returns
:   Number of successfully formatted bytes from binary address.

## Variable Documentation

## [◆ ](#gadd64afda1a14cbc2740f205e90169152)bt\_addr\_any

| | const [bt\_addr\_t](structbt__addr__t.md) bt\_addr\_any | | --- | | extern |
| --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#ga40c282f720d13b5d24a2dd62bfdceb73)bt\_addr\_le\_any

| | const [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_addr\_le\_any | | --- | | extern |
| --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#gaefa17a553b6f8e9ad599e8db7538e1b8)bt\_addr\_le\_none

| | const [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_addr\_le\_none | | --- | | extern |
| --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

## [◆ ](#ga0b2f611fbd28b066d261b81303c4b93f)bt\_addr\_none

| | const [bt\_addr\_t](structbt__addr__t.md) bt\_addr\_none | | --- | | extern |
| --- | --- | --- |

`#include <[addr.h](addr_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
