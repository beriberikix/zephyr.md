---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodbus__user__callbacks.html
original_path: doxygen/html/structmodbus__user__callbacks.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus\_user\_callbacks Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MODBUS](group__modbus.md)

Modbus Server User Callback structure.
[More...](#details)

`#include <[modbus.h](modbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [coil\_rd](#a3353b3aa0ec073fb9031a5c151e9995b) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Coil read callback. |
| int(\* | [coil\_wr](#a0dad31490d8b5d454f06a8b7805a09fd) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Coil write callback. |
| int(\* | [discrete\_input\_rd](#aa6fd8fc2663c6a982ec17a162ae56961) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Discrete Input read callback. |
| int(\* | [input\_reg\_rd](#a91a9270bd945935b74c6f5e021429d42) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*reg) |
|  | Input Register read callback. |
| int(\* | [input\_reg\_rd\_fp](#ae315e76c3ceefbd65ef8cea500b43df5) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float \*reg) |
|  | Floating Point Input Register read callback. |
| int(\* | [holding\_reg\_rd](#acf5fe90fab9765bd83d1ab2075d073a2) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*reg) |
|  | Holding Register read callback. |
| int(\* | [holding\_reg\_wr](#a4ca1ed4bfc93b36d939f847d7ac9f8da) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg) |
|  | Holding Register write callback. |
| int(\* | [holding\_reg\_rd\_fp](#a821e0aacd7c90eff5e7c0047cc88a855) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float \*reg) |
|  | Floating Point Holding Register read callback. |
| int(\* | [holding\_reg\_wr\_fp](#a333b5781c35e781e7021f53d5a357482) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float reg) |
|  | Floating Point Holding Register write callback. |

## Detailed Description

Modbus Server User Callback structure.

## Field Documentation

## [◆ ](#a3353b3aa0ec073fb9031a5c151e9995b)coil\_rd

| int(\* modbus\_user\_callbacks::coil\_rd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Coil read callback.

## [◆ ](#a0dad31490d8b5d454f06a8b7805a09fd)coil\_wr

| int(\* modbus\_user\_callbacks::coil\_wr) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Coil write callback.

## [◆ ](#aa6fd8fc2663c6a982ec17a162ae56961)discrete\_input\_rd

| int(\* modbus\_user\_callbacks::discrete\_input\_rd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Discrete Input read callback.

## [◆ ](#acf5fe90fab9765bd83d1ab2075d073a2)holding\_reg\_rd

| int(\* modbus\_user\_callbacks::holding\_reg\_rd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*reg) |
| --- |

Holding Register read callback.

## [◆ ](#a821e0aacd7c90eff5e7c0047cc88a855)holding\_reg\_rd\_fp

| int(\* modbus\_user\_callbacks::holding\_reg\_rd\_fp) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float \*reg) |
| --- |

Floating Point Holding Register read callback.

## [◆ ](#a4ca1ed4bfc93b36d939f847d7ac9f8da)holding\_reg\_wr

| int(\* modbus\_user\_callbacks::holding\_reg\_wr) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg) |
| --- |

Holding Register write callback.

## [◆ ](#a333b5781c35e781e7021f53d5a357482)holding\_reg\_wr\_fp

| int(\* modbus\_user\_callbacks::holding\_reg\_wr\_fp) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float reg) |
| --- |

Floating Point Holding Register write callback.

## [◆ ](#a91a9270bd945935b74c6f5e021429d42)input\_reg\_rd

| int(\* modbus\_user\_callbacks::input\_reg\_rd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*reg) |
| --- |

Input Register read callback.

## [◆ ](#ae315e76c3ceefbd65ef8cea500b43df5)input\_reg\_rd\_fp

| int(\* modbus\_user\_callbacks::input\_reg\_rd\_fp) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, float \*reg) |
| --- |

Floating Point Input Register read callback.

---

The documentation for this struct was generated from the following file:

- zephyr/modbus/[modbus.h](modbus_8h_source.md)

- [modbus\_user\_callbacks](structmodbus__user__callbacks.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
