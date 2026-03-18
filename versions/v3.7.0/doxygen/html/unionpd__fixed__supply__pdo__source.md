---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unionpd__fixed__supply__pdo__source.html
original_path: doxygen/html/unionpd__fixed__supply__pdo__source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_fixed\_supply\_pdo\_source Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create a Fixed Supply PDO Source value See Table 6-9 Fixed Supply PDO - Source.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_current](#a86664d945f65f19f7b96da1148700640): 10 |  |
|  | Maximum Current in 10mA units. [More...](#a86664d945f65f19f7b96da1148700640) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [voltage](#a66f55e177b6f2bc76b392707e39fa4fe): 10 |  |
|  | Voltage in 50mV units. [More...](#a66f55e177b6f2bc76b392707e39fa4fe) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [peak\_current](#a2c4b27407245da04b67e9524173d39bc): 2 |  |
|  | Peak Current. [More...](#a2c4b27407245da04b67e9524173d39bc) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#a6b0e04acd43c9b18bd1dea80508a8817): 2 |  |
|  | Reserved – Shall be set to zero. [More...](#a6b0e04acd43c9b18bd1dea80508a8817) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unchunked\_ext\_msg\_supported](#a440ff92d2bd533e3ddd6c65f9ac21772): 1 |  |
|  | Unchunked Extended Messages Supported. [More...](#a440ff92d2bd533e3ddd6c65f9ac21772) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [dual\_role\_data](#a7b89666e3753966001caf7602c796147): 1 |  |
|  | Dual-Role Data. [More...](#a7b89666e3753966001caf7602c796147) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_comms\_capable](#a6c1bcf37a1fc9a348cf19e16fbe01dac): 1 |  |
|  | USB Communications Capable. [More...](#a6c1bcf37a1fc9a348cf19e16fbe01dac) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unconstrained\_power](#a9fc10f3ec4126c063f5dd99e8f3e2723): 1 |  |
|  | Unconstrained Power. [More...](#a9fc10f3ec4126c063f5dd99e8f3e2723) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_suspend\_supported](#a55003edba55a920a386cc04cbc7a72a0): 1 |  |
|  | USB Suspend Supported. [More...](#a55003edba55a920a386cc04cbc7a72a0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [dual\_role\_power](#af96673f1ac078436a9eca0973e1bdef9): 1 |  |
|  | Dual-Role Power. [More...](#af96673f1ac078436a9eca0973e1bdef9) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#a111b87e88b4f78e60b78d35dfbcbc307): 2 |  |
|  | Fixed supply. [More...](#a111b87e88b4f78e60b78d35dfbcbc307) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#a9227629f6c97357b71ea20e4e0572cf2) |
|  | Raw PDO value. |

## Detailed Description

Create a Fixed Supply PDO Source value See Table 6-9 Fixed Supply PDO - Source.

## Field Documentation

## [◆ ](#ad74cc67ccc7f6cfeb27fc528dc4a2258)[struct]

| struct { ... } [pd\_fixed\_supply\_pdo\_source](unionpd__fixed__supply__pdo__source.md) |
| --- |

## [◆ ](#a7b89666e3753966001caf7602c796147)dual\_role\_data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::dual\_role\_data |
| --- |

Dual-Role Data.

## [◆ ](#af96673f1ac078436a9eca0973e1bdef9)dual\_role\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::dual\_role\_power |
| --- |

Dual-Role Power.

## [◆ ](#a86664d945f65f19f7b96da1148700640)max\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::max\_current |
| --- |

Maximum Current in 10mA units.

## [◆ ](#a2c4b27407245da04b67e9524173d39bc)peak\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::peak\_current |
| --- |

Peak Current.

## [◆ ](#a9227629f6c97357b71ea20e4e0572cf2)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#a6b0e04acd43c9b18bd1dea80508a8817)reserved0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::reserved0 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#a111b87e88b4f78e60b78d35dfbcbc307)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_fixed\_supply\_pdo\_source::type |
| --- |

Fixed supply.

SET TO PDO\_FIXED

## [◆ ](#a440ff92d2bd533e3ddd6c65f9ac21772)unchunked\_ext\_msg\_supported

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::unchunked\_ext\_msg\_supported |
| --- |

Unchunked Extended Messages Supported.

## [◆ ](#a9fc10f3ec4126c063f5dd99e8f3e2723)unconstrained\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::unconstrained\_power |
| --- |

Unconstrained Power.

## [◆ ](#a6c1bcf37a1fc9a348cf19e16fbe01dac)usb\_comms\_capable

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::usb\_comms\_capable |
| --- |

USB Communications Capable.

## [◆ ](#a55003edba55a920a386cc04cbc7a72a0)usb\_suspend\_supported

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::usb\_suspend\_supported |
| --- |

USB Suspend Supported.

## [◆ ](#a66f55e177b6f2bc76b392707e39fa4fe)voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_source::voltage |
| --- |

Voltage in 50mV units.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_fixed\_supply\_pdo\_source](unionpd__fixed__supply__pdo__source.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
