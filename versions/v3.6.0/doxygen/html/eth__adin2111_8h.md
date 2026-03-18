---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/eth__adin2111_8h.html
original_path: doxygen/html/eth__adin2111_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_adin2111.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](eth__adin2111_8h_source.md)

| Functions | |
| --- | --- |
| int | [eth\_adin2111\_lock](#a54e88cd118466a1a44ef02197fe2b59d) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Locks device access. |
| int | [eth\_adin2111\_unlock](#a72b5466138f087ac4e788bc878781c3e) (const struct [device](structdevice.md) \*dev) |
|  | Unlocks device access. |
| int | [eth\_adin2111\_reg\_write](#ac768d3625f30e4a90903a3070347f38c) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Writes host MAC interface register over SPI. |
| int | [eth\_adin2111\_reg\_read](#a06e40561475a7f997e706da388717414) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Reads host MAC interface register over SPI. |

## Function Documentation

## [◆ ](#a54e88cd118466a1a44ef02197fe2b59d)eth\_adin2111\_lock()

| int eth\_adin2111\_lock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

Locks device access.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | timeout | Waiting period to lock the device, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Device locked. |
    | --- | --- |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#a06e40561475a7f997e706da388717414)eth\_adin2111\_reg\_read()

| int eth\_adin2111\_reg\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *val* ) |

Reads host MAC interface register over SPI.

Note
:   The caller is responsible for device lock. Shall not be called from ISR.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | reg | Register address. |
    | [out] | val | Read value output. |

Return values
:   | 0 | Successful write. |
    | --- | --- |
    | <0 | Error, a negative errno code. |

## [◆ ](#ac768d3625f30e4a90903a3070347f38c)eth\_adin2111\_reg\_write()

| int eth\_adin2111\_reg\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

Writes host MAC interface register over SPI.

Note
:   The caller is responsible for device lock. Shall not be called from ISR.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | reg | Register address. |
    |  | val | Value to write. |

Return values
:   | 0 | Successful write. |
    | --- | --- |
    | <0 | Error, a negative errno code. |

## [◆ ](#a72b5466138f087ac4e788bc878781c3e)eth\_adin2111\_unlock()

| int eth\_adin2111\_unlock | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Unlocks device access.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |

Return values
:   | 0 | Device unlocked. |
    | --- | --- |
    | -EPERM | The current thread does not own the device lock. |
    | -EINVAL | The device is not locked. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_adin2111.h](eth__adin2111_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
