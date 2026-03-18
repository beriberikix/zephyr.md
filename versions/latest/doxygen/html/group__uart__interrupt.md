---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__uart__interrupt.html
original_path: doxygen/html/group__uart__interrupt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Interrupt-driven UART API

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_irq\_callback\_user\_data\_t](#gad7a26b1a1d6212d7d39c05c8ad4ec926)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Define the application callback function signature for [uart\_irq\_callback\_user\_data\_set()](#gaf469966a56d1fc9f50108201597ee0a0) function. |
| typedef void(\* | [uart\_irq\_config\_func\_t](#ga6750414923953c84fb1e19177ec74ae0)) (const struct [device](structdevice.md) \*dev) |
|  | For configuring IRQ on each individual UART device. |

| Functions | |
| --- | --- |
| static int | [uart\_fifo\_fill](#gafe42e4719eada7e25904bc9ebfe87791) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data, int size) |
|  | Fill FIFO with data. |
| static int | [uart\_fifo\_fill\_u16](#gaa89f58818d8428ad6a11abf692c54c0d) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data, int size) |
|  | Fill FIFO with wide data. |
| static int | [uart\_fifo\_read](#gab10942076ac47ecff29e924098049398) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data, const int size) |
|  | Read data from FIFO. |
| static int | [uart\_fifo\_read\_u16](#ga4a3c25dad2290f1f40e4b847e3b83f64) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data, const int size) |
|  | Read wide data from FIFO. |
| void | [uart\_irq\_tx\_enable](#ga9cbd6e33dce6a5b06233cf10077e19cc) (const struct [device](structdevice.md) \*dev) |
|  | Enable TX interrupt in IER. |
| void | [uart\_irq\_tx\_disable](#gaf8a5bc26cd7c32e7bc6516c6f873c45a) (const struct [device](structdevice.md) \*dev) |
|  | Disable TX interrupt in IER. |
| static int | [uart\_irq\_tx\_ready](#ga5e126b5f19549eb7f5b785b98ebe7638) (const struct [device](structdevice.md) \*dev) |
|  | Check if UART TX buffer can accept a new char. |
| void | [uart\_irq\_rx\_enable](#ga4ec3ae3974da2b3ab94ae7b835d17bad) (const struct [device](structdevice.md) \*dev) |
|  | Enable RX interrupt. |
| void | [uart\_irq\_rx\_disable](#gaa759d7935fdd9ab6ca0761f161389a29) (const struct [device](structdevice.md) \*dev) |
|  | Disable RX interrupt. |
| static int | [uart\_irq\_tx\_complete](#ga917935a13bf6a5d1e32ef34339e96455) (const struct [device](structdevice.md) \*dev) |
|  | Check if UART TX block finished transmission. |
| static int | [uart\_irq\_rx\_ready](#gad04073b1b8e3de13b43ae1194561377b) (const struct [device](structdevice.md) \*dev) |
|  | Check if UART RX buffer has a received char. |
| void | [uart\_irq\_err\_enable](#ga7c24daae3326bc2959ea13a2be79969f) (const struct [device](structdevice.md) \*dev) |
|  | Enable error interrupt. |
| void | [uart\_irq\_err\_disable](#gaaf8a88361807e204f7227fbd1d0e75b2) (const struct [device](structdevice.md) \*dev) |
|  | Disable error interrupt. |
| int | [uart\_irq\_is\_pending](#ga11ccae917c8b5fd76aaabdb047125f6a) (const struct [device](structdevice.md) \*dev) |
|  | Check if any IRQs is pending. |
| int | [uart\_irq\_update](#gac5241e000d482c40b2a4856c58c106a6) (const struct [device](structdevice.md) \*dev) |
|  | Start processing interrupts in ISR. |
| static int | [uart\_irq\_callback\_user\_data\_set](#gaf469966a56d1fc9f50108201597ee0a0) (const struct [device](structdevice.md) \*dev, [uart\_irq\_callback\_user\_data\_t](#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb, void \*user\_data) |
|  | Set the IRQ callback function pointer. |
| static int | [uart\_irq\_callback\_set](#ga5f7af3f7f0d9155349ea3b4fad78956c) (const struct [device](structdevice.md) \*dev, [uart\_irq\_callback\_user\_data\_t](#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb) |
|  | Set the IRQ callback function pointer (legacy). |

## Detailed Description

## Typedef Documentation

## [◆ ](#gad7a26b1a1d6212d7d39c05c8ad4ec926)uart\_irq\_callback\_user\_data\_t

| typedef void(\* uart\_irq\_callback\_user\_data\_t) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Define the application callback function signature for [uart\_irq\_callback\_user\_data\_set()](#gaf469966a56d1fc9f50108201597ee0a0) function.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | user\_data | Arbitrary user data. |

## [◆ ](#ga6750414923953c84fb1e19177ec74ae0)uart\_irq\_config\_func\_t

| typedef void(\* uart\_irq\_config\_func\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

For configuring IRQ on each individual UART device.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#gafe42e4719eada7e25904bc9ebfe87791)uart\_fifo\_fill()

| | int uart\_fifo\_fill | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *tx\_data*, | |  |  | int | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Fill FIFO with data.

This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_tx\_ready()](#ga5e126b5f19549eb7f5b785b98ebe7638) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). Likewise, *not* calling this function from an ISR if [uart\_irq\_tx\_ready()](#ga5e126b5f19549eb7f5b785b98ebe7638) returns true may lead to undefined behavior, e.g. infinite interrupt loops. It's mandatory to test return value of this function, as different hardware has different FIFO depth (oftentimes just 1).

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | tx\_data | Data to transmit. |
    | size | Number of bytes to send. |

Returns
:   Number of bytes sent.

Return values
:   | -ENOSYS | if this function is not supported |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaa89f58818d8428ad6a11abf692c54c0d)uart\_fifo\_fill\_u16()

| | int uart\_fifo\_fill\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *tx\_data*, | |  |  | int | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Fill FIFO with wide data.

This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_tx\_ready()](#ga5e126b5f19549eb7f5b785b98ebe7638) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). Likewise, *not* calling this function from an ISR if [uart\_irq\_tx\_ready()](#ga5e126b5f19549eb7f5b785b98ebe7638) returns true may lead to undefined behavior, e.g. infinite interrupt loops. It's mandatory to test return value of this function, as different hardware has different FIFO depth (oftentimes just 1).

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | tx\_data | Wide data to transmit. |
    | size | Number of datum to send. |

Returns
:   Number of datum sent.

Return values
:   | -ENOSYS | If this function is not implemented |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gab10942076ac47ecff29e924098049398)uart\_fifo\_read()

| | int uart\_fifo\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rx\_data*, | |  |  | const int | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Read data from FIFO.

This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). It's unspecified whether "RX ready" condition as returned by [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b) is level- or edge- triggered. That means that once [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b) is detected, [uart\_fifo\_read()](#gab10942076ac47ecff29e924098049398) must be called until it reads all available data in the FIFO (i.e. until it returns less data than was requested).

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | rx\_data | Data container. |
    | size | Container size. |

Returns
:   Number of bytes read.

Return values
:   | -ENOSYS | If this function is not implemented. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#ga4a3c25dad2290f1f40e4b847e3b83f64)uart\_fifo\_read\_u16()

| | int uart\_fifo\_read\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *rx\_data*, | |  |  | const int | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Read wide data from FIFO.

This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). It's unspecified whether "RX ready" condition as returned by [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b) is level- or edge- triggered. That means that once [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b) is detected, [uart\_fifo\_read()](#gab10942076ac47ecff29e924098049398) must be called until it reads all available data in the FIFO (i.e. until it returns less data than was requested).

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | rx\_data | Wide data container. |
    | size | Container size. |

Returns
:   Number of datum read.

Return values
:   | -ENOSYS | If this function is not implemented. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#ga5f7af3f7f0d9155349ea3b4fad78956c)uart\_irq\_callback\_set()

| | int uart\_irq\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uart\_irq\_callback\_user\_data\_t](#gad7a26b1a1d6212d7d39c05c8ad4ec926) | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Set the IRQ callback function pointer (legacy).

This sets up the callback for IRQ. When an IRQ is triggered, the specified function will be called with the device pointer.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | cb | Pointer to the callback function. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaf469966a56d1fc9f50108201597ee0a0)uart\_irq\_callback\_user\_data\_set()

| | int uart\_irq\_callback\_user\_data\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uart\_irq\_callback\_user\_data\_t](#gad7a26b1a1d6212d7d39c05c8ad4ec926) | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Set the IRQ callback function pointer.

This sets up the callback for IRQ. When an IRQ is triggered, the specified function will be called with specified user data. See description of [uart\_irq\_update()](#gac5241e000d482c40b2a4856c58c106a6) for the requirements on ISR.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | cb | Pointer to the callback function. |
    | user\_data | Data to pass to callback function. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaaf8a88361807e204f7227fbd1d0e75b2)uart\_irq\_err\_disable()

| void uart\_irq\_err\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Disable error interrupt.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## [◆ ](#ga7c24daae3326bc2959ea13a2be79969f)uart\_irq\_err\_enable()

| void uart\_irq\_err\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Enable error interrupt.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## [◆ ](#ga11ccae917c8b5fd76aaabdb047125f6a)uart\_irq\_is\_pending()

| int uart\_irq\_is\_pending | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Check if any IRQs is pending.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 1 | If an IRQ is pending. |
    | --- | --- |
    | 0 | If an IRQ is not pending. |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaa759d7935fdd9ab6ca0761f161389a29)uart\_irq\_rx\_disable()

| void uart\_irq\_rx\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Disable RX interrupt.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## [◆ ](#ga4ec3ae3974da2b3ab94ae7b835d17bad)uart\_irq\_rx\_enable()

| void uart\_irq\_rx\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Enable RX interrupt.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## [◆ ](#gad04073b1b8e3de13b43ae1194561377b)uart\_irq\_rx\_ready()

| | int uart\_irq\_rx\_ready | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Check if UART RX buffer has a received char.

Check if UART RX buffer has at least one pending character (i.e. [uart\_fifo\_read()](#gab10942076ac47ecff29e924098049398) will succeed and return non-zero). This function must be called in a UART interrupt handler, or its result is undefined. Before calling this function in the interrupt handler, [uart\_irq\_update()](#gac5241e000d482c40b2a4856c58c106a6) must be called once per the handler invocation. It's unspecified whether condition as returned by this function is level- or edge- triggered (i.e. if this function returns true when RX FIFO is non-empty, or when a new char was received since last call to it). See description of [uart\_fifo\_read()](#gab10942076ac47ecff29e924098049398) for implication of this.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 1 | If a received char is ready. |
    | --- | --- |
    | 0 | If a received char is not ready. |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#ga917935a13bf6a5d1e32ef34339e96455)uart\_irq\_tx\_complete()

| | int uart\_irq\_tx\_complete | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Check if UART TX block finished transmission.

Check if any outgoing data buffered in UART TX block was fully transmitted and TX block is idle. When this condition is true, UART device (or whole system) can be power off. Note that this function is *not* useful to check if UART TX can accept more data, use [uart\_irq\_tx\_ready()](#ga5e126b5f19549eb7f5b785b98ebe7638) for that. This function must be called in a UART interrupt handler, or its result is undefined. Before calling this function in the interrupt handler, [uart\_irq\_update()](#gac5241e000d482c40b2a4856c58c106a6) must be called once per the handler invocation.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 1 | If nothing remains to be transmitted. |
    | --- | --- |
    | 0 | If transmission is not completed. |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gaf8a5bc26cd7c32e7bc6516c6f873c45a)uart\_irq\_tx\_disable()

| void uart\_irq\_tx\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Disable TX interrupt in IER.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## [◆ ](#ga9cbd6e33dce6a5b06233cf10077e19cc)uart\_irq\_tx\_enable()

| void uart\_irq\_tx\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Enable TX interrupt in IER.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

## [◆ ](#ga5e126b5f19549eb7f5b785b98ebe7638)uart\_irq\_tx\_ready()

| | int uart\_irq\_tx\_ready | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Check if UART TX buffer can accept a new char.

Check if UART TX buffer can accept at least one character for transmission (i.e. [uart\_fifo\_fill()](#gafe42e4719eada7e25904bc9ebfe87791) will succeed and return non-zero). This function must be called in a UART interrupt handler, or its result is undefined. Before calling this function in the interrupt handler, [uart\_irq\_update()](#gac5241e000d482c40b2a4856c58c106a6) must be called once per the handler invocation.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 1 | If TX interrupt is enabled and at least one char can be written to UART. |
    | --- | --- |
    | 0 | If device is not ready to write a new byte. |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

## [◆ ](#gac5241e000d482c40b2a4856c58c106a6)uart\_irq\_update()

| int uart\_irq\_update | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Start processing interrupts in ISR.

This function should be called the first thing in the ISR. Calling [uart\_irq\_rx\_ready()](#gad04073b1b8e3de13b43ae1194561377b), [uart\_irq\_tx\_ready()](#ga5e126b5f19549eb7f5b785b98ebe7638), [uart\_irq\_tx\_complete()](#ga917935a13bf6a5d1e32ef34339e96455) allowed only after this.

The purpose of this function is:

- For devices with auto-acknowledge of interrupt status on register read to cache the value of this register (rx\_ready, etc. then use this case).
- For devices with explicit acknowledgment of interrupts, to ack any pending interrupts and likewise to cache the original value.
- For devices with implicit acknowledgment, this function will be empty. But the ISR must perform the actions needs to ack the interrupts (usually, call [uart\_fifo\_read()](#gab10942076ac47ecff29e924098049398) on rx\_ready, and [uart\_fifo\_fill()](#gafe42e4719eada7e25904bc9ebfe87791) on tx\_ready).

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 1 | On success. |
    | --- | --- |
    | -ENOSYS | If this function is not implemented. |
    | -ENOTSUP | If API is not enabled. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
