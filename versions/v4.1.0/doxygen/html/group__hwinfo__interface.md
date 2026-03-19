---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__hwinfo__interface.html
original_path: doxygen/html/group__hwinfo__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hardware Info Interface

[Device Driver APIs](group__io__interfaces.md)

Hardware Information Interface.
[More...](#details)

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [hwinfo\_get\_device\_id](#ga197b58d995c77aae423527d0f8d9ff31) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Copy the device id to a buffer. |
| int | [hwinfo\_get\_device\_eui64](#ga0f5ab222b4f7e75a3e9d3650e954a036) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer) |
|  | Copy the device EUI64 to a buffer. |
| int | [hwinfo\_get\_reset\_cause](#ga390c1c29088813ace17856ffa97d97b5) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cause) |
|  | Retrieve cause of device reset. |
| int | [hwinfo\_clear\_reset\_cause](#gaeaa23e68c53eb6a2b56f06c74b83e613) (void) |
|  | Clear cause of device reset. |
| int | [hwinfo\_get\_supported\_reset\_cause](#gaf0d345653c4fbb5f38a78aba766a6bb8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*supported) |
|  | Get supported reset cause flags. |

| Reset cause flags | |
| --- | --- |
|  | |
| #define | [RESET\_PIN](#ga08bca59db4b190eaaea4d47b7562869c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | External pin. |
| #define | [RESET\_SOFTWARE](#ga737ea2c652086e38a9b895cc42593908)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Software reset. |
| #define | [RESET\_BROWNOUT](#gac9dc9b22ba1fc551a3d68810155a640e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Brownout (drop in voltage). |
| #define | [RESET\_POR](#ga21fa7b8a5ec2e1c077dbc453ca3a4265)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Power-on reset (POR). |
| #define | [RESET\_WATCHDOG](#ga112ab452e5015120edcb88b9a6de3de0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Watchdog timer expiration. |
| #define | [RESET\_DEBUG](#ga031454a8ff535f8cf66ddbdbc2acba5e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Debug event. |
| #define | [RESET\_SECURITY](#ga846cce95f808d3c1a5b48376f8de3612)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Security violation. |
| #define | [RESET\_LOW\_POWER\_WAKE](#ga3ce47e00b35b155416a3d48dd5c477ac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Waking up from low power mode. |
| #define | [RESET\_CPU\_LOCKUP](#gad6721dc841941ccdca349999ce655e83)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | CPU lock-up detected. |
| #define | [RESET\_PARITY](#gac32af4272b5356a498cb3d4ce6fb87e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Parity error. |
| #define | [RESET\_PLL](#gaed16942e0487d525c79c539b385e6f31)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | PLL error. |
| #define | [RESET\_CLOCK](#ga9bb4063cded0167c496b834d642fd73c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Clock error. |
| #define | [RESET\_HARDWARE](#gaf9659a85b05447ef9267606182bf568a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Hardware reset. |
| #define | [RESET\_USER](#ga5aa032c5d8560a4bb351ca29d1464939)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | User reset. |
| #define | [RESET\_TEMPERATURE](#gade167088d6c99163f5af385bcac93f58)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Temperature reset. |

## Detailed Description

Hardware Information Interface.

Since
:   1.14

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#gac9dc9b22ba1fc551a3d68810155a640e)RESET\_BROWNOUT

| #define RESET\_BROWNOUT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Brownout (drop in voltage).

## [◆ ](#ga9bb4063cded0167c496b834d642fd73c)RESET\_CLOCK

| #define RESET\_CLOCK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Clock error.

## [◆ ](#gad6721dc841941ccdca349999ce655e83)RESET\_CPU\_LOCKUP

| #define RESET\_CPU\_LOCKUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

CPU lock-up detected.

## [◆ ](#ga031454a8ff535f8cf66ddbdbc2acba5e)RESET\_DEBUG

| #define RESET\_DEBUG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Debug event.

## [◆ ](#gaf9659a85b05447ef9267606182bf568a)RESET\_HARDWARE

| #define RESET\_HARDWARE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Hardware reset.

## [◆ ](#ga3ce47e00b35b155416a3d48dd5c477ac)RESET\_LOW\_POWER\_WAKE

| #define RESET\_LOW\_POWER\_WAKE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Waking up from low power mode.

## [◆ ](#gac32af4272b5356a498cb3d4ce6fb87e7)RESET\_PARITY

| #define RESET\_PARITY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Parity error.

## [◆ ](#ga08bca59db4b190eaaea4d47b7562869c)RESET\_PIN

| #define RESET\_PIN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

External pin.

## [◆ ](#gaed16942e0487d525c79c539b385e6f31)RESET\_PLL

| #define RESET\_PLL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

PLL error.

## [◆ ](#ga21fa7b8a5ec2e1c077dbc453ca3a4265)RESET\_POR

| #define RESET\_POR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Power-on reset (POR).

## [◆ ](#ga846cce95f808d3c1a5b48376f8de3612)RESET\_SECURITY

| #define RESET\_SECURITY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Security violation.

## [◆ ](#ga737ea2c652086e38a9b895cc42593908)RESET\_SOFTWARE

| #define RESET\_SOFTWARE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Software reset.

## [◆ ](#gade167088d6c99163f5af385bcac93f58)RESET\_TEMPERATURE

| #define RESET\_TEMPERATURE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Temperature reset.

## [◆ ](#ga5aa032c5d8560a4bb351ca29d1464939)RESET\_USER

| #define RESET\_USER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

User reset.

## [◆ ](#ga112ab452e5015120edcb88b9a6de3de0)RESET\_WATCHDOG

| #define RESET\_WATCHDOG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Watchdog timer expiration.

## Function Documentation

## [◆ ](#gaeaa23e68c53eb6a2b56f06c74b83e613)hwinfo\_clear\_reset\_cause()

| int hwinfo\_clear\_reset\_cause | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Clear cause of device reset.

Clears reset cause flags.

Return values
:   | zero | if successful. |
    | --- | --- |
    | -ENOSYS | if there is no implementation for the particular device. |
    | any | negative value on driver specific errors. |

## [◆ ](#ga0f5ab222b4f7e75a3e9d3650e954a036)hwinfo\_get\_device\_eui64()

| int hwinfo\_get\_device\_eui64 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Copy the device EUI64 to a buffer.

This routine copies the device EUI64 (8 bytes) to the buffer. The EUI64 depends on the hardware and is guaranteed unique.

Parameters
:   | buffer | Buffer of 8 bytes to write the ID to. |
    | --- | --- |

Return values
:   | zero | if successful. |
    | --- | --- |
    | -ENOSYS | if there is no implementation for the particular device. |
    | any | negative value on driver specific errors. |

## [◆ ](#ga197b58d995c77aae423527d0f8d9ff31)hwinfo\_get\_device\_id()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) hwinfo\_get\_device\_id | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Copy the device id to a buffer.

This routine copies "length" number of bytes of the device ID to the buffer. If the device ID is smaller than length, the rest of the buffer is left unchanged. The ID depends on the hardware and is not guaranteed unique.

Drivers are responsible for ensuring that the ID data structure is a sequence of bytes. The returned ID value is not supposed to be interpreted based on vendor-specific assumptions of byte order. It should express the identifier as a raw byte sequence, doing any endian conversion necessary so that a hex representation of the bytes produces the intended serial number.

Parameters
:   | buffer | Buffer to write the ID to. |
    | --- | --- |
    | length | Max length of the buffer. |

Return values
:   | size | of the device ID copied. |
    | --- | --- |
    | -ENOSYS | if there is no implementation for the particular device. |
    | any | negative value on driver specific errors. |

## [◆ ](#ga390c1c29088813ace17856ffa97d97b5)hwinfo\_get\_reset\_cause()

| int hwinfo\_get\_reset\_cause | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *cause* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Retrieve cause of device reset.

Parameters
:   | cause | OR'd [reset cause](#reset_cause) flags |
    | --- | --- |

This routine retrieves the flags that indicate why the device was reset.

On some platforms the reset cause flags accumulate between successive resets and this routine may return multiple flags indicating all reset causes since the device was powered on. If you need to retrieve the cause only for the most recent reset call [hwinfo\_clear\_reset\_cause](#gaeaa23e68c53eb6a2b56f06c74b83e613) after calling this routine to clear the hardware flags before the next reset event.

Successive calls to this routine will return the same value, unless [hwinfo\_clear\_reset\_cause](#gaeaa23e68c53eb6a2b56f06c74b83e613) has been called.

Return values
:   | zero | if successful. |
    | --- | --- |
    | -ENOSYS | if there is no implementation for the particular device. |
    | any | negative value on driver specific errors. |

## [◆ ](#gaf0d345653c4fbb5f38a78aba766a6bb8)hwinfo\_get\_supported\_reset\_cause()

| int hwinfo\_get\_supported\_reset\_cause | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *supported* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hwinfo.h](hwinfo_8h.md)>`

Get supported reset cause flags.

Parameters
:   | supported | OR'd [reset cause](#reset_cause) flags that are supported |
    | --- | --- |

Retrieves all reset\_cause flags that are supported by this device.

Return values
:   | zero | if successful. |
    | --- | --- |
    | -ENOSYS | if there is no implementation for the particular device. |
    | any | negative value on driver specific errors. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
