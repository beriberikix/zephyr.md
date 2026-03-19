---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2interrupt__controller_2intel__vtd_8h.html
original_path: doxygen/html/drivers_2interrupt__controller_2intel__vtd_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel\_vtd.h File Reference

`#include <[zephyr/drivers/pcie/msi.h](msi_8h_source.md)>`

[Go to the source code of this file.](drivers_2interrupt__controller_2intel__vtd_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [vtd\_driver\_api](structvtd__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [vtd\_alloc\_entries\_f](#a3bded96a42bec41476ff6bc9f75676b4)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_entries) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [vtd\_remap\_msi\_f](#aadb69e257884026693109510e20dc2b4)) (const struct [device](structdevice.md) \*dev, [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector) |
| typedef int(\* | [vtd\_remap\_f](#afefa59b2064053d90445127da9b64bfb)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_id) |
| typedef int(\* | [vtd\_set\_irte\_vector\_f](#a06190d6273d0adeb92e9e4e4fa79d9b4)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| typedef int(\* | [vtd\_get\_irte\_by\_vector\_f](#a944bfa2dc643fd3ff182eee12d836ae5)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [vtd\_get\_irte\_vector\_f](#af3ddf5e22fcb4956e4887e1982fae28e)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx) |
| typedef int(\* | [vtd\_set\_irte\_irq\_f](#a63733309814847ba4204776e8ace9a85)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| typedef int(\* | [vtd\_get\_irte\_by\_irq\_f](#a0a2e483fe9159a46d6265b257841f43a)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| typedef void(\* | [vtd\_set\_irte\_msi\_f](#a0118f224100f721a508ce00c3ae99698)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) msi) |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [vtd\_irte\_is\_msi\_f](#a622083e8841c3899ca7b7156f526581f)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx) |

| Functions | |
| --- | --- |
| static int | [vtd\_allocate\_entries](#a87b1cea7c86d724da0c379bfd3742879) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_entries) |
|  | Allocate contiguous IRTEs. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vtd\_remap\_msi](#ab7b8ad9dbee740c9e97021853f1131fc) (const struct [device](structdevice.md) \*dev, [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector) |
|  | Generate the MSI Message Address data for the given vector. |
| static int | [vtd\_remap](#a3cc5ff5183e80aeb18115d8b5a541546) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_id) |
|  | Remap the given vector. |
| static int | [vtd\_set\_irte\_vector](#a342e4745949ed1bd50b4d51de482be57) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
|  | Set the vector on the allocated irte. |
| static int | [vtd\_get\_irte\_by\_vector](#a4645558c4f9e461e86e6d0caf96311ad) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
|  | Get the irte allocated for the given vector. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vtd\_get\_irte\_vector](#a76d5a655a925c9ec9536e6c906c2192e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx) |
|  | Get the vector given to the IRTE. |
| static int | [vtd\_set\_irte\_irq](#ab067e306959a0774ee5e896eafab2132) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Set the irq on the allocated irte. |
| static int | [vtd\_get\_irte\_by\_irq](#a214bd683e7331adbe5afbca41e3a6bc9) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Get the irte allocated for the given irq. |
| static void | [vtd\_set\_irte\_msi](#ae81918a2c81e03cc4e02603781e8ca21) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) msi) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [vtd\_irte\_is\_msi](#a82018e41e5bbb12f98c16b0d416596fe) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx) |

## Typedef Documentation

## [◆ ](#a3bded96a42bec41476ff6bc9f75676b4)vtd\_alloc\_entries\_f

| typedef int(\* vtd\_alloc\_entries\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_entries) |
| --- |

## [◆ ](#a0a2e483fe9159a46d6265b257841f43a)vtd\_get\_irte\_by\_irq\_f

| typedef int(\* vtd\_get\_irte\_by\_irq\_f) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| --- |

## [◆ ](#a944bfa2dc643fd3ff182eee12d836ae5)vtd\_get\_irte\_by\_vector\_f

| typedef int(\* vtd\_get\_irte\_by\_vector\_f) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| --- |

## [◆ ](#af3ddf5e22fcb4956e4887e1982fae28e)vtd\_get\_irte\_vector\_f

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* vtd\_get\_irte\_vector\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx) |
| --- |

## [◆ ](#a622083e8841c3899ca7b7156f526581f)vtd\_irte\_is\_msi\_f

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* vtd\_irte\_is\_msi\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx) |
| --- |

## [◆ ](#afefa59b2064053d90445127da9b64bfb)vtd\_remap\_f

| typedef int(\* vtd\_remap\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_id) |
| --- |

## [◆ ](#aadb69e257884026693109510e20dc2b4)vtd\_remap\_msi\_f

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* vtd\_remap\_msi\_f) (const struct [device](structdevice.md) \*dev, [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector) |
| --- |

## [◆ ](#a63733309814847ba4204776e8ace9a85)vtd\_set\_irte\_irq\_f

| typedef int(\* vtd\_set\_irte\_irq\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| --- |

## [◆ ](#a0118f224100f721a508ce00c3ae99698)vtd\_set\_irte\_msi\_f

| typedef void(\* vtd\_set\_irte\_msi\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) msi) |
| --- |

## [◆ ](#a06190d6273d0adeb92e9e4e4fa79d9b4)vtd\_set\_irte\_vector\_f

| typedef int(\* vtd\_set\_irte\_vector\_f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| --- |

## Function Documentation

## [◆ ](#a87b1cea7c86d724da0c379bfd3742879)vtd\_allocate\_entries()

| | int vtd\_allocate\_entries | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *n\_entries* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Allocate contiguous IRTEs.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | n\_entries | How many IRTE to allocate |

Note: It will try to allocate all, or it will fail.

Returns
:   The first allocated IRTE index, or -EBUSY on failure

## [◆ ](#a214bd683e7331adbe5afbca41e3a6bc9)vtd\_get\_irte\_by\_irq()

| | int vtd\_get\_irte\_by\_irq | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Get the irte allocated for the given irq.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | irq | A valid IRQ number |

Returns
:   0 or positive value on success, a negative errno otherwise

## [◆ ](#a4645558c4f9e461e86e6d0caf96311ad)vtd\_get\_irte\_by\_vector()

| | int vtd\_get\_irte\_by\_vector | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vector* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Get the irte allocated for the given vector.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | vector | An allocated interrupt vector |

Returns
:   0 or positive value on success, a negative errno otherwise

## [◆ ](#a76d5a655a925c9ec9536e6c906c2192e)vtd\_get\_irte\_vector()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vtd\_get\_irte\_vector | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irte\_idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Get the vector given to the IRTE.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | irte\_idx | A previously allocated irte entry index number |

Returns
:   the vector set to this IRTE

## [◆ ](#a82018e41e5bbb12f98c16b0d416596fe)vtd\_irte\_is\_msi()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) vtd\_irte\_is\_msi | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irte\_idx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3cc5ff5183e80aeb18115d8b5a541546)vtd\_remap()

| | int vtd\_remap | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irte\_idx*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vector*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *src\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Remap the given vector.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | irte\_idx | A previously allocated irte entry index number |
    | vector | An allocated interrupt vector |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | interrupt flags |
    | src\_id | a valid source ID or USHRT\_MAX if none |

Returns
:   0 on success, a negative errno otherwise

## [◆ ](#ab7b8ad9dbee740c9e97021853f1131fc)vtd\_remap\_msi()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vtd\_remap\_msi | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \* | *vector*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *n\_vector* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Generate the MSI Message Address data for the given vector.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | vector | A valid allocated MSI vector array |
    | n\_vector | the size of the vector array |

Returns
:   The MSI Message Address value

## [◆ ](#ab067e306959a0774ee5e896eafab2132)vtd\_set\_irte\_irq()

| | int vtd\_set\_irte\_irq | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irte\_idx*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the irq on the allocated irte.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | irte\_idx | A previously allocated irte entry index number |
    | irq | A valid IRQ number |

Returns
:   0, a negative errno otherwise

## [◆ ](#ae81918a2c81e03cc4e02603781e8ca21)vtd\_set\_irte\_msi()

| | void vtd\_set\_irte\_msi | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irte\_idx*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *msi* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a342e4745949ed1bd50b4d51de482be57)vtd\_set\_irte\_vector()

| | int vtd\_set\_irte\_vector | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irte\_idx*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vector* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the vector on the allocated irte.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | irte\_idx | A previously allocated irte entry index number |
    | vector | An allocated interrupt vector |

Returns
:   0, a negative errno otherwise

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intel\_vtd.h](drivers_2interrupt__controller_2intel__vtd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
