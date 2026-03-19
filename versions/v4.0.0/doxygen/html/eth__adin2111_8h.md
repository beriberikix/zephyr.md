---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/eth__adin2111_8h.html
original_path: doxygen/html/eth__adin2111_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_adin2111.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
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
| int | [eth\_adin2111\_reg\_update](#ab2a247e4ee0c3ff778a972768ee5bc51) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Update host MAC interface register over SPI. |
| int | [eth\_adin2111\_sw\_reset](#a340b4d3786807c7feb423b36d6533a87) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) delay) |
|  | Reset both the MAC and PHY. |
| int | [eth\_adin2111\_mac\_reset](#ad737f44a16702f4c8ce3f8a8ae994364) (const struct [device](structdevice.md) \*dev) |
|  | Reset the MAC device. |
| int | [eth\_adin2111\_broadcast\_filter](#a9752b1a6a75880af069af1b00ce43928) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable the forwarding (to host) of broadcast frames. |
| struct [net\_if](structnet__if.md) \* | [eth\_adin2111\_get\_iface](#a86de61f524a1837ff8f701c5af969d1b) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port\_idx) |
|  | Get the port-related [net\_if](structnet__if.md "Network Interface structure.") reference. |

## Function Documentation

## [◆ ](#a9752b1a6a75880af069af1b00ce43928)eth\_adin2111\_broadcast\_filter()

| int eth\_adin2111\_broadcast\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

Enable/disable the forwarding (to host) of broadcast frames.

Frames who's DA doesn't match are dropped.

Note
:   The caller is responsible for device lock. Shall not be called from ISR.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | enable | Set to 0 to disable and to nonzero to enable. |

Return values
:   | 0 | Successful write. |
    | --- | --- |
    | <0 | Error, a negative errno code. |

## [◆ ](#a86de61f524a1837ff8f701c5af969d1b)eth\_adin2111\_get\_iface()

| struct [net\_if](structnet__if.md) \* eth\_adin2111\_get\_iface | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *port\_idx* ) |

Get the port-related [net\_if](structnet__if.md "Network Interface structure.") reference.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | port\_idx | Port index. |

Return values
:   | a | struct [net\_if](structnet__if.md "Network Interface structure.") pointer, or NULL on error. |
    | --- | --- |

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

## [◆ ](#ad737f44a16702f4c8ce3f8a8ae994364)eth\_adin2111\_mac\_reset()

| int eth\_adin2111\_mac\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Reset the MAC device.

Note that PHY 1 must be out of software power-down for the MAC subsystem reset to take effect.

Note
:   The caller is responsible for device lock. Shall not be called from ISR.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |

Return values
:   | 0 | Successful write. |
    | --- | --- |
    | <0 | Error, a negative errno code. |

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

## [◆ ](#ab2a247e4ee0c3ff778a972768ee5bc51)eth\_adin2111\_reg\_update()

| int eth\_adin2111\_reg\_update | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mask*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) |

Update host MAC interface register over SPI.

Note
:   The caller is responsible for device lock. Shall not be called from ISR.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | reg | Register address. |
    |  | mask | Bitmask for bits that may be modified. |
    |  | data | Data to apply in the masked range. |

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

## [◆ ](#a340b4d3786807c7feb423b36d6533a87)eth\_adin2111\_sw\_reset()

| int eth\_adin2111\_sw\_reset | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *delay* ) |

Reset both the MAC and PHY.

Parameters
:   | [in] | dev | ADIN2111 device. |
    | --- | --- | --- |
    |  | delay | Delay in milliseconds. |

Note
:   The caller is responsible for device lock. Shall not be called from ISR.

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
