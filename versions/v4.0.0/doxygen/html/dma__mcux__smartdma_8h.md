---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dma__mcux__smartdma_8h.html
original_path: doxygen/html/dma__mcux__smartdma_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_smartdma.h File Reference

[Go to the source code of this file.](dma__mcux__smartdma_8h_source.md)

| Functions | |
| --- | --- |
| void | [dma\_smartdma\_install\_fw](#a72c469e163fc727135224893adbf757e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*firmware, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | install SMARTDMA firmware |

## Function Documentation

## [◆ ](#a72c469e163fc727135224893adbf757e)dma\_smartdma\_install\_fw()

| void dma\_smartdma\_install\_fw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *firmware*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

install SMARTDMA firmware

Install a custom firmware for the smartDMA. This function allows the user to install a custom firmware into the smartDMA, which implements different API functions than the standard MCUX SDK firmware.

Parameters
:   | dev | smartDMA device |
    | --- | --- |
    | firmware | address of buffer containing smartDMA firmware |
    | len | length of firmware buffer |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_smartdma.h](dma__mcux__smartdma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
