---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pcie__ep_8h.html
original_path: doxygen/html/pcie__ep_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie\_ep.h File Reference

Public APIs for the PCIe EP drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/init.h](init_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](pcie__ep_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [pcie\_ep\_reset\_callback\_t](#afcde72dd6977ee7de9ebf4146113f912)) (void \*arg) |
|  | Callback API for PCIe reset interrupts. |

| Enumerations | |
| --- | --- |
| enum | [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) { [PCIE\_OB\_ANYMEM](#aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286) , [PCIE\_OB\_LOWMEM](#aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74) , [PCIE\_OB\_HIGHMEM](#aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb) } |
| enum | [pci\_ep\_irq\_type](#aba0e572125869b246d4968ee164f3800) { [PCIE\_EP\_IRQ\_LEGACY](#aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d) , [PCIE\_EP\_IRQ\_MSI](#aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318) , [PCIE\_EP\_IRQ\_MSIX](#aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4) } |
| enum | [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) { [HOST\_TO\_DEVICE](#acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e) , [DEVICE\_TO\_HOST](#acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a) } |
| enum | [pcie\_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd) { [PCIE\_PERST](#a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7) , [PCIE\_PERST\_INB](#a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee) , [PCIE\_FLR](#a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a) , [PCIE\_RESET\_MAX](#a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a) } |

| Functions | |
| --- | --- |
| static int | [pcie\_ep\_conf\_read](#ad35d42579500a959bb3275cd65b04a42) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Read PCIe EP configuration space. |
| static void | [pcie\_ep\_conf\_write](#a8d3f4de13956fbd7ed71acbd387f781a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write PCIe EP configuration space. |
| static int | [pcie\_ep\_map\_addr](#a7bcff5f22fd32e0b2c3c3c509038b2db) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*mapped\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type) |
|  | Map a host memory buffer to PCIe outbound region. |
| static void | [pcie\_ep\_unmap\_addr](#a07ee4ed9ceb42462c95da8bbf3dfc8f7) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr) |
|  | Remove mapping to PCIe outbound region. |
| static int | [pcie\_ep\_raise\_irq](#aec421e689d4d72b0bf8a34fe8303b103) (const struct [device](structdevice.md) \*dev, enum [pci\_ep\_irq\_type](#aba0e572125869b246d4968ee164f3800) irq\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num) |
|  | Raise interrupt to Host. |
| static int | [pcie\_ep\_register\_reset\_cb](#a4e9cc8364703bb58e96642d1250dc410) (const struct [device](structdevice.md) \*dev, enum [pcie\_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd) reset, [pcie\_ep\_reset\_callback\_t](#afcde72dd6977ee7de9ebf4146113f912) cb, void \*arg) |
|  | Register callback function for reset interrupts. |
| static int | [pcie\_ep\_dma\_xfer](#a7c450e4f9d65aade3f912b72b38ed04d) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, const enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) dir) |
|  | Data transfer between mapped Host memory and device memory with "System DMA". |
| int | [pcie\_ep\_xfer\_data\_memcpy](#ac7e46d51c49ce6cb6b0c7ad7f8010292) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type, enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) dir) |
|  | Data transfer using memcpy. |
| int | [pcie\_ep\_xfer\_data\_dma](#acfe495f60e94341e88cc267a879918fc) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size, enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type, enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) dir) |
|  | Data transfer using system DMA. |

## Detailed Description

Public APIs for the PCIe EP drivers.

## Typedef Documentation

## [◆ ](#afcde72dd6977ee7de9ebf4146113f912)pcie\_ep\_reset\_callback\_t

| typedef void(\* pcie\_ep\_reset\_callback\_t) (void \*arg) |
| --- |

Callback API for PCIe reset interrupts.

These callbacks execute in interrupt context. Therefore, use only interrupt-safe APIS. Registration of callbacks is done via *pcie\_ep\_register\_reset\_cb*

Parameters
:   | arg | Pointer provided at registration time, later to be passed back as argument to callback function |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#aba0e572125869b246d4968ee164f3800)pci\_ep\_irq\_type

| enum [pci\_ep\_irq\_type](#aba0e572125869b246d4968ee164f3800) |
| --- |

| Enumerator | |
| --- | --- |
| PCIE\_EP\_IRQ\_LEGACY | Raise Legacy interrupt. |
| PCIE\_EP\_IRQ\_MSI | Raise MSI interrupt. |
| PCIE\_EP\_IRQ\_MSIX | Raise MSIX interrupt. |

## [◆ ](#aa7c51648c5a1663dd4dec689727a510b)pcie\_ob\_mem\_type

| enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) |
| --- |

| Enumerator | |
| --- | --- |
| PCIE\_OB\_ANYMEM | PCIe OB window within any address range. |
| PCIE\_OB\_LOWMEM | PCIe OB window within 32-bit address range. |
| PCIE\_OB\_HIGHMEM | PCIe OB window above 32-bit address range. |

## [◆ ](#a7b0f0f4693b7d11b973bfd62ac1b35cd)pcie\_reset

| enum [pcie\_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd) |
| --- |

| Enumerator | |
| --- | --- |
| PCIE\_PERST | Cold reset. |
| PCIE\_PERST\_INB | Inband hot reset. |
| PCIE\_FLR | Functional Level Reset. |
| PCIE\_RESET\_MAX |  |

## [◆ ](#acd2605f2fb5676ded5f125712681d458)xfer\_direction

| enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) |
| --- |

| Enumerator | |
| --- | --- |
| HOST\_TO\_DEVICE | Read from Host. |
| DEVICE\_TO\_HOST | Write to Host. |

## Function Documentation

## [◆ ](#ad35d42579500a959bb3275cd65b04a42)pcie\_ep\_conf\_read()

| | int pcie\_ep\_conf\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *offset*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Read PCIe EP configuration space.

This API reads EP's own configuration space

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | offset | Offset within configuration space |
    | data | Pointer to data read from the offset |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a8d3f4de13956fbd7ed71acbd387f781a)pcie\_ep\_conf\_write()

| | void pcie\_ep\_conf\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *offset*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Write PCIe EP configuration space.

This API writes EP's own configuration space

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | offset | Offset within configuration space |
    | data | Data to be written at the offset |

## [◆ ](#a7c450e4f9d65aade3f912b72b38ed04d)pcie\_ep\_dma\_xfer()

| | int pcie\_ep\_dma\_xfer | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *mapped\_addr*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *local\_addr*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size*, | |  |  | const enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) | *dir* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Data transfer between mapped Host memory and device memory with "System DMA".

The term "System DMA" is used to clarify that we are not talking about dedicated "PCIe DMA"; rather the one which does not understand PCIe address directly, and uses the mapped Host memory.

If DMA controller is available in the EP device, this API can be used to achieve data transfer between mapped Host memory, i.e. outbound memory and EP device's local memory with DMA

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mapped\_addr | Mapped Host memory address |
    | local\_addr | Device memory address |
    | size | DMA transfer length (bytes) |
    | dir | Direction of DMA transfer |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a7bcff5f22fd32e0b2c3c3c509038b2db)pcie\_ep\_map\_addr()

| | int pcie\_ep\_map\_addr | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *pcie\_addr*, | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *mapped\_addr*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size*, | |  |  | enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) | *ob\_mem\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Map a host memory buffer to PCIe outbound region.

This API maps a host memory buffer to PCIe outbound region, It is left to EP driver to manage multiple mappings through multiple PCIe outbound regions if supported by SoC

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | pcie\_addr | Host memory buffer address to be mapped |
    | mapped\_addr | Mapped PCIe outbound region address |
    | size | Host memory buffer size (bytes) |
    | ob\_mem\_type | Hint if lowmem/highmem outbound region has to be used, this is useful in cases where bus master cannot generate more than 32-bit address; it becomes essential to use lowmem outbound region |

Returns
:   Mapped size : If mapped size is less than requested size, then requester has to call the same API again to map the unmapped host buffer after data transfer is done with mapped size. This situation may arise because of the mapping alignment requirements.
:   Negative errno code if failure.

## [◆ ](#aec421e689d4d72b0bf8a34fe8303b103)pcie\_ep\_raise\_irq()

| | int pcie\_ep\_raise\_irq | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [pci\_ep\_irq\_type](#aba0e572125869b246d4968ee164f3800) | *irq\_type*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq\_num* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Raise interrupt to Host.

This API raises interrupt to Host

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | irq\_type | Type of Interrupt be raised (legacy, MSI or MSI-X) |
    | irq\_num | MSI or MSI-X interrupt number |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a4e9cc8364703bb58e96642d1250dc410)pcie\_ep\_register\_reset\_cb()

| | int pcie\_ep\_register\_reset\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [pcie\_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd) | *reset*, | |  |  | [pcie\_ep\_reset\_callback\_t](#afcde72dd6977ee7de9ebf4146113f912) | *cb*, | |  |  | void \* | *arg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Register callback function for reset interrupts.

If reset interrupts are handled by device, this API can be used to register callback function, which will be executed part of corresponding PCIe reset handler

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | reset | Reset interrupt type |
    | cb | Callback function being registered |
    | arg | Argument to be passed back to callback function |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#a07ee4ed9ceb42462c95da8bbf3dfc8f7)pcie\_ep\_unmap\_addr()

| | void pcie\_ep\_unmap\_addr | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *mapped\_addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Remove mapping to PCIe outbound region.

This API removes mapping to PCIe outbound region. Mapped PCIe outbound region address is given as argument to figure out the outbound region to be unmapped

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mapped\_addr | PCIe outbound region address |

## [◆ ](#acfe495f60e94341e88cc267a879918fc)pcie\_ep\_xfer\_data\_dma()

| int pcie\_ep\_xfer\_data\_dma | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *pcie\_addr*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *local\_addr*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size*, |
|  |  | enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) | *ob\_mem\_type*, |
|  |  | enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) | *dir* ) |

Data transfer using system DMA.

Helper API to achieve data transfer with system DMA through PCIe outbound memory, this API is based off pcie\_ep\_xfer\_data\_memcpy, here we use "system dma" instead of memcpy

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | pcie\_addr | Host memory buffer address |
    | local\_addr | Local memory buffer address |
    | size | Data transfer size (bytes) |
    | ob\_mem\_type | Hint if lowmem/highmem outbound region has to be used (PCIE\_OB\_LOWMEM / PCIE\_OB\_HIGHMEM / PCIE\_OB\_ANYMEM) |
    | dir | Data transfer direction (HOST\_TO\_DEVICE / DEVICE\_TO\_HOST) |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ac7e46d51c49ce6cb6b0c7ad7f8010292)pcie\_ep\_xfer\_data\_memcpy()

| int pcie\_ep\_xfer\_data\_memcpy | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *pcie\_addr*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *local\_addr*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size*, |
|  |  | enum [pcie\_ob\_mem\_type](#aa7c51648c5a1663dd4dec689727a510b) | *ob\_mem\_type*, |
|  |  | enum [xfer\_direction](#acd2605f2fb5676ded5f125712681d458) | *dir* ) |

Data transfer using memcpy.

Helper API to achieve data transfer with memcpy through PCIe outbound memory

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | pcie\_addr | Host memory buffer address |
    | local\_addr | Local memory buffer address |
    | size | Data transfer size (bytes) |
    | ob\_mem\_type | Hint if lowmem/highmem outbound region has to be used (PCIE\_OB\_LOWMEM / PCIE\_OB\_HIGHMEM / PCIE\_OB\_ANYMEM), should be PCIE\_OB\_LOWMEM if bus master cannot generate more than 32-bit address |
    | dir | Data transfer direction (HOST\_TO\_DEVICE / DEVICE\_TO\_HOST) |

Returns
:   0 if successful, negative errno code if failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [endpoint](dir_5013992ccf7d366f81bc518f84f7b0b5.md)
- [pcie\_ep.h](pcie__ep_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
