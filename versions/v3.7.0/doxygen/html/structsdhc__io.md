---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsdhc__io.html
original_path: doxygen/html/structsdhc__io.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc\_io Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SDHC interface](group__sdhc__interface.md)

SD host controller I/O control structure.
[More...](#details)

`#include <[sdhc.h](sdhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [sdhc\_clock\_speed](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539) | [clock](#aaa15197b8f1947a67dcd8522aa62afc5) |
|  | Clock rate. |
| enum [sdhc\_bus\_mode](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8) | [bus\_mode](#a2b4456b108778aada0d42b8c8107b3e9) |
|  | command output mode |
| enum [sdhc\_power](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9) | [power\_mode](#ac503fb9fba7ffdb01695a77780972930) |
|  | SD power supply mode. |
| enum [sdhc\_bus\_width](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448) | [bus\_width](#a904b05c7e73e80bb7326b0bfcb6b7103) |
|  | SD bus width. |
| enum [sdhc\_timing\_mode](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) | [timing](#a85c50f625d8606bb4c07a228c0de24e4) |
|  | SD bus timing. |
| enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) | [driver\_type](#a0c62aaa1a8a7700ebb00a38ce2e57d11) |
|  | SD driver type. |
| enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) | [signal\_voltage](#ade8b8cd4e4f4b21f5fa8e3fb2661917e) |
|  | IO signalling voltage (usually 1.8 or 3.3V). |

## Detailed Description

SD host controller I/O control structure.

Controls I/O settings for the SDHC. Note that only a subset of these settings apply to host controllers in SPI mode. Populate this struct, then call [sdhc\_set\_io](group__sdhc__interface.md#ga0e6d8259cca442bd1356d00f668d35c4 "sdhc_set_io") to apply I/O settings

## Field Documentation

## [◆ ](#a2b4456b108778aada0d42b8c8107b3e9)bus\_mode

| enum [sdhc\_bus\_mode](group__sdhc__interface.md#gaf26909ae9fffdc6ac02abd8094d16dc8) sdhc\_io::bus\_mode |
| --- |

command output mode

## [◆ ](#a904b05c7e73e80bb7326b0bfcb6b7103)bus\_width

| enum [sdhc\_bus\_width](group__sdhc__interface.md#gad8bab66ec505c8356fac7785a8955448) sdhc\_io::bus\_width |
| --- |

SD bus width.

## [◆ ](#aaa15197b8f1947a67dcd8522aa62afc5)clock

| enum [sdhc\_clock\_speed](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539) sdhc\_io::clock |
| --- |

Clock rate.

## [◆ ](#a0c62aaa1a8a7700ebb00a38ce2e57d11)driver\_type

| enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) sdhc\_io::driver\_type |
| --- |

SD driver type.

## [◆ ](#ac503fb9fba7ffdb01695a77780972930)power\_mode

| enum [sdhc\_power](group__sdhc__interface.md#gad63742820bb18ca18cd2f96547e12eb9) sdhc\_io::power\_mode |
| --- |

SD power supply mode.

## [◆ ](#ade8b8cd4e4f4b21f5fa8e3fb2661917e)signal\_voltage

| enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) sdhc\_io::signal\_voltage |
| --- |

IO signalling voltage (usually 1.8 or 3.3V).

## [◆ ](#a85c50f625d8606bb4c07a228c0de24e4)timing

| enum [sdhc\_timing\_mode](group__sdhc__interface.md#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90) sdhc\_io::timing |
| --- |

SD bus timing.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sdhc.h](sdhc_8h_source.md)

- [sdhc\_io](structsdhc__io.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
