---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__uart__interface.html
original_path: doxygen/html/group__uart__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

UART Interface

[Device Driver APIs](group__io__interfaces.md)

UART Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Async UART API](group__uart__async.md) |
|  |  |
|  | [Interrupt-driven UART API](group__uart__interrupt.md) |
|  |  |
|  | [Polling UART API](group__uart__polling.md) |

| Data Structures | |
| --- | --- |
| struct | [uart\_config](structuart__config.md) |
|  | UART controller configuration structure. [More...](structuart__config.md#details) |

| Enumerations | |
| --- | --- |
| enum | [uart\_line\_ctrl](#ga02552532e171e789efc1b000917a9be0) {     [UART\_LINE\_CTRL\_BAUD\_RATE](#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) = BIT(0) , [UART\_LINE\_CTRL\_RTS](#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) = BIT(1) , [UART\_LINE\_CTRL\_DTR](#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) = BIT(2) , [UART\_LINE\_CTRL\_DCD](#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) = BIT(3) ,     [UART\_LINE\_CTRL\_DSR](#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) = BIT(4)   } |
|  | Line control signals. [More...](#ga02552532e171e789efc1b000917a9be0) |
| enum | [uart\_rx\_stop\_reason](#gadeba6c5485e01dfc1c8a6e1c21668a88) {     [UART\_ERROR\_OVERRUN](#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) = (1 << 0) , [UART\_ERROR\_PARITY](#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) = (1 << 1) , [UART\_ERROR\_FRAMING](#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) = (1 << 2) , [UART\_BREAK](#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) = (1 << 3) ,     [UART\_ERROR\_COLLISION](#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) = (1 << 4) , [UART\_ERROR\_NOISE](#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) = (1 << 5)   } |
|  | Reception stop reasons. [More...](#gadeba6c5485e01dfc1c8a6e1c21668a88) |
| enum | [uart\_config\_parity](#gab2ab6aacb6e3c43bb26d4274157e5711) {     [UART\_CFG\_PARITY\_NONE](#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d) , [UART\_CFG\_PARITY\_ODD](#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed) , [UART\_CFG\_PARITY\_EVEN](#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba) , [UART\_CFG\_PARITY\_MARK](#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca) ,     [UART\_CFG\_PARITY\_SPACE](#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)   } |
|  | Parity modes. [More...](#gab2ab6aacb6e3c43bb26d4274157e5711) |
| enum | [uart\_config\_stop\_bits](#gafc1aecb863e2456d73b78a49fcbad72e) { [UART\_CFG\_STOP\_BITS\_0\_5](#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af) , [UART\_CFG\_STOP\_BITS\_1](#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58) , [UART\_CFG\_STOP\_BITS\_1\_5](#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad) , [UART\_CFG\_STOP\_BITS\_2](#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6) } |
|  | Number of stop bits. [More...](#gafc1aecb863e2456d73b78a49fcbad72e) |
| enum | [uart\_config\_data\_bits](#gab9f7de744a68a311330576d7da02c44a) {     [UART\_CFG\_DATA\_BITS\_5](#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27) , [UART\_CFG\_DATA\_BITS\_6](#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4) , [UART\_CFG\_DATA\_BITS\_7](#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913) , [UART\_CFG\_DATA\_BITS\_8](#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97) ,     [UART\_CFG\_DATA\_BITS\_9](#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)   } |
|  | Number of data bits. [More...](#gab9f7de744a68a311330576d7da02c44a) |
| enum | [uart\_config\_flow\_control](#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) { [UART\_CFG\_FLOW\_CTRL\_NONE](#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973) , [UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86) , [UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f) , [UART\_CFG\_FLOW\_CTRL\_RS485](#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c) } |
|  | Hardware flow control options. [More...](#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) |

| Functions | |
| --- | --- |
| int | [uart\_err\_check](#ga22ea20fd8e07153b3b71cc9416f5462f) (const struct [device](structdevice.md) \*dev) |
|  | Check whether an error was detected. |
| int | [uart\_configure](#gaa0b75777b879af10543f7e8f463ff9a2) (const struct [device](structdevice.md) \*dev, const struct [uart\_config](structuart__config.md) \*cfg) |
|  | Set UART configuration. |
| int | [uart\_config\_get](#ga81dfc5f2134de8e4acb5f063512cf703) (const struct [device](structdevice.md) \*dev, struct [uart\_config](structuart__config.md) \*cfg) |
|  | Get UART configuration. |
| int | [uart\_line\_ctrl\_set](#gab039414b41145dc8d31349836da91263) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Manipulate line control for UART. |
| int | [uart\_line\_ctrl\_get](#gafda8a550284a54c8e1d6b6638de978e5) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Retrieve line control for UART. |
| int | [uart\_drv\_cmd](#gaa8683398e5d709b513509d08841ed51b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p) |
|  | Send extra command to driver. |

## Detailed Description

UART Interface.

Since
:   1.0

Version
:   1.0.0

## Enumeration Type Documentation

## [◆ ](#gab9f7de744a68a311330576d7da02c44a)uart\_config\_data\_bits

| enum [uart\_config\_data\_bits](#gab9f7de744a68a311330576d7da02c44a) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Number of data bits.

| Enumerator | |
| --- | --- |
| UART\_CFG\_DATA\_BITS\_5 | 5 data bits |
| UART\_CFG\_DATA\_BITS\_6 | 6 data bits |
| UART\_CFG\_DATA\_BITS\_7 | 7 data bits |
| UART\_CFG\_DATA\_BITS\_8 | 8 data bits |
| UART\_CFG\_DATA\_BITS\_9 | 9 data bits |

## [◆ ](#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)uart\_config\_flow\_control

| enum [uart\_config\_flow\_control](#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Hardware flow control options.

With flow control set to none, any operations related to flow control signals can be managed by user with [uart\_line\_ctrl](#ga02552532e171e789efc1b000917a9be0) functions. In other cases, flow control is managed by hardware/driver.

| Enumerator | |
| --- | --- |
| UART\_CFG\_FLOW\_CTRL\_NONE | No flow control. |
| UART\_CFG\_FLOW\_CTRL\_RTS\_CTS | RTS/CTS flow control. |
| UART\_CFG\_FLOW\_CTRL\_DTR\_DSR | DTR/DSR flow control. |
| UART\_CFG\_FLOW\_CTRL\_RS485 | RS485 flow control. |

## [◆ ](#gab2ab6aacb6e3c43bb26d4274157e5711)uart\_config\_parity

| enum [uart\_config\_parity](#gab2ab6aacb6e3c43bb26d4274157e5711) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Parity modes.

| Enumerator | |
| --- | --- |
| UART\_CFG\_PARITY\_NONE | No parity. |
| UART\_CFG\_PARITY\_ODD | Odd parity. |
| UART\_CFG\_PARITY\_EVEN | Even parity. |
| UART\_CFG\_PARITY\_MARK | Mark parity. |
| UART\_CFG\_PARITY\_SPACE | Space parity. |

## [◆ ](#gafc1aecb863e2456d73b78a49fcbad72e)uart\_config\_stop\_bits

| enum [uart\_config\_stop\_bits](#gafc1aecb863e2456d73b78a49fcbad72e) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Number of stop bits.

| Enumerator | |
| --- | --- |
| UART\_CFG\_STOP\_BITS\_0\_5 | 0.5 stop bit |
| UART\_CFG\_STOP\_BITS\_1 | 1 stop bit |
| UART\_CFG\_STOP\_BITS\_1\_5 | 1.5 stop bits |
| UART\_CFG\_STOP\_BITS\_2 | 2 stop bits |

## [◆ ](#ga02552532e171e789efc1b000917a9be0)uart\_line\_ctrl

| enum [uart\_line\_ctrl](#ga02552532e171e789efc1b000917a9be0) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Line control signals.

| Enumerator | |
| --- | --- |
| UART\_LINE\_CTRL\_BAUD\_RATE | Baud rate. |
| UART\_LINE\_CTRL\_RTS | Request To Send (RTS). |
| UART\_LINE\_CTRL\_DTR | Data Terminal Ready (DTR). |
| UART\_LINE\_CTRL\_DCD | Data Carrier Detect (DCD). |
| UART\_LINE\_CTRL\_DSR | Data Set Ready (DSR). |

## [◆ ](#gadeba6c5485e01dfc1c8a6e1c21668a88)uart\_rx\_stop\_reason

| enum [uart\_rx\_stop\_reason](#gadeba6c5485e01dfc1c8a6e1c21668a88) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Reception stop reasons.

Values that correspond to events or errors responsible for stopping receiving.

| Enumerator | |
| --- | --- |
| UART\_ERROR\_OVERRUN | Overrun error. |
| UART\_ERROR\_PARITY | Parity error. |
| UART\_ERROR\_FRAMING | Framing error. |
| UART\_BREAK | Break interrupt.  A break interrupt was received. This happens when the serial input is held at a logic '0' state for longer than the sum of start time + data bits + parity + stop bits. |
| UART\_ERROR\_COLLISION | Collision error.  This error is raised when transmitted data does not match received data. Typically this is useful in scenarios where the TX and RX lines maybe connected together such as RS-485 half-duplex. This error is only valid on UARTs that support collision checking. |
| UART\_ERROR\_NOISE | Noise error. |

## Function Documentation

## [◆ ](#ga81dfc5f2134de8e4acb5f063512cf703)uart\_config\_get()

| int uart\_config\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [uart\_config](structuart__config.md) \* | *cfg* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Get UART configuration.

Stores current UART configuration to \*cfg, can be used to retrieve initial configuration after device was initialized using data from DTS.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | cfg | UART configuration structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative errno code in case of failure. |
    | -ENOSYS | If driver does not support getting current configuration. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaa0b75777b879af10543f7e8f463ff9a2)uart\_configure()

| int uart\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [uart\_config](structuart__config.md) \* | *cfg* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Set UART configuration.

Sets UART configuration using data from \*cfg.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | cfg | UART configuration structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative errno code in case of failure. |
    | -ENOSYS | If configuration is not supported by device or driver does not support setting configuration in runtime. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaa8683398e5d709b513509d08841ed51b)uart\_drv\_cmd()

| int uart\_drv\_cmd | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cmd*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *p* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Send extra command to driver.

Implementation and accepted commands are driver specific. Refer to the drivers for more information.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command to driver. |
    | p | Parameter to the command. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#ga22ea20fd8e07153b3b71cc9416f5462f)uart\_err\_check()

| int uart\_err\_check | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Check whether an error was detected.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 0 | If no error was detected. |
    | --- | --- |
    | err | Error flags as defined in [uart\_rx\_stop\_reason](#gadeba6c5485e01dfc1c8a6e1c21668a88) |
    | -ENOSYS | If not implemented. |

## [◆ ](#gafda8a550284a54c8e1d6b6638de978e5)uart\_line\_ctrl\_get()

| int uart\_line\_ctrl\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ctrl*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *val* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Retrieve line control for UART.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | ctrl | The line control to retrieve (see enum [uart\_line\_ctrl](#ga02552532e171e789efc1b000917a9be0)). |
    | val | Pointer to variable where to store the line control value. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#gab039414b41145dc8d31349836da91263)uart\_line\_ctrl\_set()

| int uart\_line\_ctrl\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ctrl*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Manipulate line control for UART.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | ctrl | The line control to manipulate (see enum [uart\_line\_ctrl](#ga02552532e171e789efc1b000917a9be0)). |
    | val | Value to set to the line control. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |
    | -errno | Other negative errno value in case of failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
