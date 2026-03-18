---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/uart.html
original_path: hardware/peripherals/uart.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Universal Asynchronous Receiver-Transmitter (UART)

## Overview

Zephyr provides three different ways to access the UART peripheral. Depending
on the method, different API functions are used according to below sections:

1. [Polling API](#uart-polling-api)
2. [Interrupt-driven API](#uart-interrupt-api)
3. [Asynchronous API](#uart-async-api) using [Direct Memory Access (DMA)](dma.md#dma-api)

Polling is the most basic method to access the UART peripheral. The reading
function, uart\_poll\_in, is a non-blocking function and returns a character
or -1 when no valid data is available. The writing function,
uart\_poll\_out, is a blocking function and the thread waits until the given
character is sent.

With the Interrupt-driven API, possibly slow communication can happen in the
background while the thread continues with other tasks. The Kernel’s
[Data Passing](../../kernel/services/index.md#kernel-data-passing-api) features can be used to communicate between
the thread and the UART driver.

The Asynchronous API allows to read and write data in the background using DMA
without interrupting the MCU at all. However, the setup is more complex
than the other methods.

Warning

Interrupt-driven API and the Asynchronous API should NOT be used at
the same time for the same hardware peripheral, since both APIs require
hardware interrupts to function properly. Using the callbacks for both
APIs would result in interference between each other.
[`CONFIG_UART_EXCLUSIVE_API_CALLBACKS`](../../kconfig.md#CONFIG_UART_EXCLUSIVE_API_CALLBACKS "CONFIG_UART_EXCLUSIVE_API_CALLBACKS") is enabled by default
so that only the callbacks associated with one API is active at a time.

## Configuration Options

Most importantly, the Kconfig options define whether the polling API (default),
the interrupt-driven API or the asynchronous API can be used. Only enable the
features you need in order to minimize memory footprint.

Related configuration options:

- [`CONFIG_SERIAL`](../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL")
- [`CONFIG_UART_INTERRUPT_DRIVEN`](../../kconfig.md#CONFIG_UART_INTERRUPT_DRIVEN "CONFIG_UART_INTERRUPT_DRIVEN")
- [`CONFIG_UART_ASYNC_API`](../../kconfig.md#CONFIG_UART_ASYNC_API "CONFIG_UART_ASYNC_API")
- [`CONFIG_UART_WIDE_DATA`](../../kconfig.md#CONFIG_UART_WIDE_DATA "CONFIG_UART_WIDE_DATA")
- [`CONFIG_UART_USE_RUNTIME_CONFIGURE`](../../kconfig.md#CONFIG_UART_USE_RUNTIME_CONFIGURE "CONFIG_UART_USE_RUNTIME_CONFIGURE")
- [`CONFIG_UART_LINE_CTRL`](../../kconfig.md#CONFIG_UART_LINE_CTRL "CONFIG_UART_LINE_CTRL")
- [`CONFIG_UART_DRV_CMD`](../../kconfig.md#CONFIG_UART_DRV_CMD "CONFIG_UART_DRV_CMD")

## API Reference

Related code samples

[802.15.4 "serial-radio"](../../samples/net/wpan_serial/README.md#wpan-serial "Implement a slip-radio device for Contiki-based border routers.")
:   Implement a slip-radio device for Contiki-based border routers.

[Console over USB CDC ACM](../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")
:   Output "Hello World!" to the console over USB CDC ACM.

[Native TTY UART](../../samples/drivers/uart/native_tty/README.md#uart-native-tty "Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.")
:   Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.

[STM32 single-wire UART](../../samples/boards/stm32/uart/single_wire/README.md#uart-stm32-single-wire "Use single-wire/half-duplex UART functionality of STM32 devices.")
:   Use single-wire/half-duplex UART functionality of STM32 devices.

[UART Passthrough](../../samples/drivers/uart/passthrough/README.md#uart-passthrough "Pass data directly between the console and another UART interface.")
:   Pass data directly between the console and another UART interface.

[UART echo](../../samples/drivers/uart/echo_bot/README.md#uart "Read data from the console and echo it back.")
:   Read data from the console and echo it back.

*group* uart\_interface
:   UART Interface.

    Enums

    enum uart\_line\_ctrl
    :   Line control signals.

        *Values:*

        enumerator UART\_LINE\_CTRL\_BAUD\_RATE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Baud rate.

        enumerator UART\_LINE\_CTRL\_RTS = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Request To Send (RTS).

        enumerator UART\_LINE\_CTRL\_DTR = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Data Terminal Ready (DTR).

        enumerator UART\_LINE\_CTRL\_DCD = [BIT](../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Data Carrier Detect (DCD).

        enumerator UART\_LINE\_CTRL\_DSR = [BIT](../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Data Set Ready (DSR).

    enum uart\_rx\_stop\_reason
    :   Reception stop reasons.

        Values that correspond to events or errors responsible for stopping receiving.

        *Values:*

        enumerator UART\_ERROR\_OVERRUN = (1 << 0)
        :   Overrun error.

        enumerator UART\_ERROR\_PARITY = (1 << 1)
        :   Parity error.

        enumerator UART\_ERROR\_FRAMING = (1 << 2)
        :   Framing error.

        enumerator UART\_BREAK = (1 << 3)
        :   Break interrupt.

            A break interrupt was received. This happens when the serial input is held at a logic ‘0’ state for longer than the sum of start time + data bits + parity + stop bits.

        enumerator UART\_ERROR\_COLLISION = (1 << 4)
        :   Collision error.

            This error is raised when transmitted data does not match received data. Typically this is useful in scenarios where the TX and RX lines maybe connected together such as RS-485 half-duplex. This error is only valid on UARTs that support collision checking.

        enumerator UART\_ERROR\_NOISE = (1 << 5)
        :   Noise error.

    enum uart\_config\_parity
    :   Parity modes.

        *Values:*

        enumerator UART\_CFG\_PARITY\_NONE
        :   No parity.

        enumerator UART\_CFG\_PARITY\_ODD
        :   Odd parity.

        enumerator UART\_CFG\_PARITY\_EVEN
        :   Even parity.

        enumerator UART\_CFG\_PARITY\_MARK
        :   Mark parity.

        enumerator UART\_CFG\_PARITY\_SPACE
        :   Space parity.

    enum uart\_config\_stop\_bits
    :   Number of stop bits.

        *Values:*

        enumerator UART\_CFG\_STOP\_BITS\_0\_5
        :   0.5 stop bit

        enumerator UART\_CFG\_STOP\_BITS\_1
        :   1 stop bit

        enumerator UART\_CFG\_STOP\_BITS\_1\_5
        :   1.5 stop bits

        enumerator UART\_CFG\_STOP\_BITS\_2
        :   2 stop bits

    enum uart\_config\_data\_bits
    :   Number of data bits.

        *Values:*

        enumerator UART\_CFG\_DATA\_BITS\_5
        :   5 data bits

        enumerator UART\_CFG\_DATA\_BITS\_6
        :   6 data bits

        enumerator UART\_CFG\_DATA\_BITS\_7
        :   7 data bits

        enumerator UART\_CFG\_DATA\_BITS\_8
        :   8 data bits

        enumerator UART\_CFG\_DATA\_BITS\_9
        :   9 data bits

    enum uart\_config\_flow\_control
    :   Hardware flow control options.

        With flow control set to none, any operations related to flow control signals can be managed by user with [uart\_line\_ctrl](#group__uart__interface_1ga02552532e171e789efc1b000917a9be0) functions. In other cases, flow control is managed by hardware/driver.

        *Values:*

        enumerator UART\_CFG\_FLOW\_CTRL\_NONE
        :   No flow control.

        enumerator UART\_CFG\_FLOW\_CTRL\_RTS\_CTS
        :   RTS/CTS flow control.

        enumerator UART\_CFG\_FLOW\_CTRL\_DTR\_DSR
        :   DTR/DSR flow control.

        enumerator UART\_CFG\_FLOW\_CTRL\_RS485
        :   RS485 flow control.

    Functions

    int uart\_err\_check(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check whether an error was detected.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **0** – If no error was detected.
            - **err** – Error flags as defined in [uart\_rx\_stop\_reason](#group__uart__interface_1gadeba6c5485e01dfc1c8a6e1c21668a88)
            - **-ENOSYS** – If not implemented.

    int uart\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [uart\_config](#c.uart_config) \*cfg)
    :   Set UART configuration.

        Sets UART configuration using data from \*cfg.

        Parameters:
        :   - **dev** – UART device instance.
            - **cfg** – UART configuration structure.

        Return values:
        :   - **0** – If successful.
            - **-errno** – Negative errno code in case of failure.
            - **-ENOSYS** – If configuration is not supported by device or driver does not support setting configuration in runtime.
            - **-ENOTSUP** – If API is not enabled.

    int uart\_config\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [uart\_config](#c.uart_config) \*cfg)
    :   Get UART configuration.

        Stores current UART configuration to \*cfg, can be used to retrieve initial configuration after device was initialized using data from DTS.

        Parameters:
        :   - **dev** – UART device instance.
            - **cfg** – UART configuration structure.

        Return values:
        :   - **0** – If successful.
            - **-errno** – Negative errno code in case of failure.
            - **-ENOSYS** – If driver does not support getting current configuration.
            - **-ENOTSUP** – If API is not enabled.

    int uart\_line\_ctrl\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t ctrl, uint32\_t val)
    :   Manipulate line control for UART.

        Parameters:
        :   - **dev** – UART device instance.
            - **ctrl** – The line control to manipulate (see enum [uart\_line\_ctrl](#group__uart__interface_1ga02552532e171e789efc1b000917a9be0)).
            - **val** – Value to set to the line control.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.
            - **-errno** – Other negative errno value in case of failure.

    int uart\_line\_ctrl\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t ctrl, uint32\_t \*val)
    :   Retrieve line control for UART.

        Parameters:
        :   - **dev** – UART device instance.
            - **ctrl** – The line control to retrieve (see enum [uart\_line\_ctrl](#group__uart__interface_1ga02552532e171e789efc1b000917a9be0)).
            - **val** – Pointer to variable where to store the line control value.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.
            - **-errno** – Other negative errno value in case of failure.

    int uart\_drv\_cmd(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t cmd, uint32\_t p)
    :   Send extra command to driver.

        Implementation and accepted commands are driver specific. Refer to the drivers for more information.

        Parameters:
        :   - **dev** – UART device instance.
            - **cmd** – Command to driver.
            - **p** – Parameter to the command.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.
            - **-errno** – Other negative errno value in case of failure.

    struct uart\_config
    :   *#include <uart.h>*

        UART controller configuration structure.

        Public Members

        uint32\_t baudrate
        :   Baudrate setting in bps.

        uint8\_t parity
        :   Parity bit, use [uart\_config\_parity](#group__uart__interface_1gab2ab6aacb6e3c43bb26d4274157e5711).

        uint8\_t stop\_bits
        :   Stop bits, use [uart\_config\_stop\_bits](#group__uart__interface_1gafc1aecb863e2456d73b78a49fcbad72e).

        uint8\_t data\_bits
        :   Data bits, use [uart\_config\_data\_bits](#group__uart__interface_1gab9f7de744a68a311330576d7da02c44a).

        uint8\_t flow\_ctrl
        :   Flow control setting, use [uart\_config\_flow\_control](#group__uart__interface_1ga8e2f1b4a8d60d7a6c24835d1b26f99e8).

### Polling API

*group* uart\_polling
:   Functions

    int uart\_poll\_in(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned char \*p\_char)
    :   Read a character from the device for input.

        This routine checks if the receiver has valid data. When the receiver has valid data, it reads a character from the device, stores to the location pointed to by p\_char, and returns 0 to the calling thread. It returns -1, otherwise. This function is a non-blocking call.

        Parameters:
        :   - **dev** – UART device instance.
            - **p\_char** – Pointer to character.

        Return values:
        :   - **0** – If a character arrived.
            - **-1** – If no character was available to read (i.e. the UART input buffer was empty).
            - **-ENOSYS** – If the operation is not implemented.
            - **-EBUSY** – If async reception was enabled using [uart\_rx\_enable](#group__uart__async_1ga902e18c2a727ed2988e1b6caa6a444b8)

    int uart\_poll\_in\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t \*p\_u16)
    :   Read a 16-bit datum from the device for input.

        This routine checks if the receiver has valid data. When the receiver has valid data, it reads a 16-bit datum from the device, stores to the location pointed to by p\_u16, and returns 0 to the calling thread. It returns -1, otherwise. This function is a non-blocking call.

        Parameters:
        :   - **dev** – UART device instance.
            - **p\_u16** – Pointer to 16-bit data.

        Return values:
        :   - **0** – If data arrived.
            - **-1** – If no data was available to read (i.e., the UART input buffer was empty).
            - **-ENOTSUP** – If API is not enabled.
            - **-ENOSYS** – If the function is not implemented.
            - **-EBUSY** – If async reception was enabled using [uart\_rx\_enable](#group__uart__async_1ga902e18c2a727ed2988e1b6caa6a444b8)

    void uart\_poll\_out(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned char out\_char)
    :   Write a character to the device for output.

        This routine checks if the transmitter is full. When the transmitter is not full, it writes a character to the data register. It waits and blocks the calling thread, otherwise. This function is a blocking call.

        To send a character when hardware flow control is enabled, the handshake signal CTS must be asserted.

        Parameters:
        :   - **dev** – UART device instance.
            - **out\_char** – Character to send.

    void uart\_poll\_out\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t out\_u16)
    :   Write a 16-bit datum to the device for output.

        This routine checks if the transmitter is full. When the transmitter is not full, it writes a 16-bit datum to the data register. It waits and blocks the calling thread, otherwise. This function is a blocking call.

        To send a datum when hardware flow control is enabled, the handshake signal CTS must be asserted.

        Parameters:
        :   - **dev** – UART device instance.
            - **out\_u16** – Wide data to send.

### Interrupt-driven API

*group* uart\_interrupt
:   Typedefs

    typedef void (\*uart\_irq\_callback\_user\_data\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, void \*user\_data)
    :   Define the application callback function signature for [uart\_irq\_callback\_user\_data\_set()](#group__uart__interrupt_1gaf469966a56d1fc9f50108201597ee0a0) function.

        Param dev:
        :   UART device instance.

        Param user\_data:
        :   Arbitrary user data.

    typedef void (\*uart\_irq\_config\_func\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   For configuring IRQ on each individual UART device.

        Param dev:
        :   UART device instance.

    Functions

    static inline int uart\_fifo\_fill(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*tx\_data, int size)
    :   Fill FIFO with data.

        This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_tx\_ready()](#group__uart__interrupt_1ga5e126b5f19549eb7f5b785b98ebe7638) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). Likewise, *not* calling this function from an ISR if [uart\_irq\_tx\_ready()](#group__uart__interrupt_1ga5e126b5f19549eb7f5b785b98ebe7638) returns true may lead to undefined behavior, e.g. infinite interrupt loops. It’s mandatory to test return value of this function, as different hardware has different FIFO depth (oftentimes just 1).

        Parameters:
        :   - **dev** – UART device instance.
            - **tx\_data** – Data to transmit.
            - **size** – Number of bytes to send.

        Return values:
        :   - **-ENOSYS** – if this function is not supported
            - **-ENOTSUP** – If API is not enabled.

        Returns:
        :   Number of bytes sent.

    static inline int uart\_fifo\_fill\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t \*tx\_data, int size)
    :   Fill FIFO with wide data.

        This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_tx\_ready()](#group__uart__interrupt_1ga5e126b5f19549eb7f5b785b98ebe7638) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). Likewise, *not* calling this function from an ISR if [uart\_irq\_tx\_ready()](#group__uart__interrupt_1ga5e126b5f19549eb7f5b785b98ebe7638) returns true may lead to undefined behavior, e.g. infinite interrupt loops. It’s mandatory to test return value of this function, as different hardware has different FIFO depth (oftentimes just 1).

        Parameters:
        :   - **dev** – UART device instance.
            - **tx\_data** – Wide data to transmit.
            - **size** – Number of datum to send.

        Return values:
        :   - **-ENOSYS** – If this function is not implemented
            - **-ENOTSUP** – If API is not enabled.

        Returns:
        :   Number of datum sent.

    static inline int uart\_fifo\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*rx\_data, const int size)
    :   Read data from FIFO.

        This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). It’s unspecified whether “RX ready” condition as returned by [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b) is level- or edge- triggered. That means that once [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b) is detected, [uart\_fifo\_read()](#group__uart__interrupt_1gab10942076ac47ecff29e924098049398) must be called until it reads all available data in the FIFO (i.e. until it returns less data than was requested).

        Parameters:
        :   - **dev** – UART device instance.
            - **rx\_data** – Data container.
            - **size** – Container size.

        Return values:
        :   - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

        Returns:
        :   Number of bytes read.

    static inline int uart\_fifo\_read\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t \*rx\_data, const int size)
    :   Read wide data from FIFO.

        This function is expected to be called from UART interrupt handler (ISR), if [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b) returns true. Result of calling this function not from an ISR is undefined (hardware-dependent). It’s unspecified whether “RX ready” condition as returned by [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b) is level- or edge- triggered. That means that once [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b) is detected, [uart\_fifo\_read()](#group__uart__interrupt_1gab10942076ac47ecff29e924098049398) must be called until it reads all available data in the FIFO (i.e. until it returns less data than was requested).

        Parameters:
        :   - **dev** – UART device instance.
            - **rx\_data** – Wide data container.
            - **size** – Container size.

        Return values:
        :   - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

        Returns:
        :   Number of datum read.

    void uart\_irq\_tx\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable TX interrupt in IER.

        Parameters:
        :   - **dev** – UART device instance.

    void uart\_irq\_tx\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable TX interrupt in IER.

        Parameters:
        :   - **dev** – UART device instance.

    static inline int uart\_irq\_tx\_ready(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if UART TX buffer can accept a new char.

        Check if UART TX buffer can accept at least one character for transmission (i.e. [uart\_fifo\_fill()](#group__uart__interrupt_1gafe42e4719eada7e25904bc9ebfe87791) will succeed and return non-zero). This function must be called in a UART interrupt handler, or its result is undefined. Before calling this function in the interrupt handler, [uart\_irq\_update()](#group__uart__interrupt_1gac5241e000d482c40b2a4856c58c106a6) must be called once per the handler invocation.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **1** – If TX interrupt is enabled and at least one char can be written to UART.
            - **0** – If device is not ready to write a new byte.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

    void uart\_irq\_rx\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable RX interrupt.

        Parameters:
        :   - **dev** – UART device instance.

    void uart\_irq\_rx\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable RX interrupt.

        Parameters:
        :   - **dev** – UART device instance.

    static inline int uart\_irq\_tx\_complete(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if UART TX block finished transmission.

        Check if any outgoing data buffered in UART TX block was fully transmitted and TX block is idle. When this condition is true, UART device (or whole system) can be power off. Note that this function is *not* useful to check if UART TX can accept more data, use [uart\_irq\_tx\_ready()](#group__uart__interrupt_1ga5e126b5f19549eb7f5b785b98ebe7638) for that. This function must be called in a UART interrupt handler, or its result is undefined. Before calling this function in the interrupt handler, [uart\_irq\_update()](#group__uart__interrupt_1gac5241e000d482c40b2a4856c58c106a6) must be called once per the handler invocation.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **1** – If nothing remains to be transmitted.
            - **0** – If transmission is not completed.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

    static inline int uart\_irq\_rx\_ready(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if UART RX buffer has a received char.

        Check if UART RX buffer has at least one pending character (i.e. [uart\_fifo\_read()](#group__uart__interrupt_1gab10942076ac47ecff29e924098049398) will succeed and return non-zero). This function must be called in a UART interrupt handler, or its result is undefined. Before calling this function in the interrupt handler, [uart\_irq\_update()](#group__uart__interrupt_1gac5241e000d482c40b2a4856c58c106a6) must be called once per the handler invocation. It’s unspecified whether condition as returned by this function is level- or edge- triggered (i.e. if this function returns true when RX FIFO is non-empty, or when a new char was received since last call to it). See description of [uart\_fifo\_read()](#group__uart__interrupt_1gab10942076ac47ecff29e924098049398) for implication of this.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **1** – If a received char is ready.
            - **0** – If a received char is not ready.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

    void uart\_irq\_err\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable error interrupt.

        Parameters:
        :   - **dev** – UART device instance.

    void uart\_irq\_err\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable error interrupt.

        Parameters:
        :   - **dev** – UART device instance.

    int uart\_irq\_is\_pending(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if any IRQs is pending.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **1** – If an IRQ is pending.
            - **0** – If an IRQ is not pending.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

    int uart\_irq\_update(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Start processing interrupts in ISR.

        This function should be called the first thing in the ISR. Calling [uart\_irq\_rx\_ready()](#group__uart__interrupt_1gad04073b1b8e3de13b43ae1194561377b), [uart\_irq\_tx\_ready()](#group__uart__interrupt_1ga5e126b5f19549eb7f5b785b98ebe7638), [uart\_irq\_tx\_complete()](#group__uart__interrupt_1ga917935a13bf6a5d1e32ef34339e96455) allowed only after this.

        The purpose of this function is:

        - For devices with auto-acknowledge of interrupt status on register read to cache the value of this register (rx\_ready, etc. then use this case).
        - For devices with explicit acknowledgment of interrupts, to ack any pending interrupts and likewise to cache the original value.
        - For devices with implicit acknowledgment, this function will be empty. But the ISR must perform the actions needs to ack the interrupts (usually, call [uart\_fifo\_read()](#group__uart__interrupt_1gab10942076ac47ecff29e924098049398) on rx\_ready, and [uart\_fifo\_fill()](#group__uart__interrupt_1gafe42e4719eada7e25904bc9ebfe87791) on tx\_ready).

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **1** – On success.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

    static inline int uart\_irq\_callback\_user\_data\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [uart\_irq\_callback\_user\_data\_t](#c.uart_irq_callback_user_data_t) cb, void \*user\_data)
    :   Set the IRQ callback function pointer.

        This sets up the callback for IRQ. When an IRQ is triggered, the specified function will be called with specified user data. See description of [uart\_irq\_update()](#group__uart__interrupt_1gac5241e000d482c40b2a4856c58c106a6) for the requirements on ISR.

        Parameters:
        :   - **dev** – UART device instance.
            - **cb** – Pointer to the callback function.
            - **user\_data** – Data to pass to callback function.

        Return values:
        :   - **0** – On success.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

    static inline int uart\_irq\_callback\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [uart\_irq\_callback\_user\_data\_t](#c.uart_irq_callback_user_data_t) cb)
    :   Set the IRQ callback function pointer (legacy).

        This sets up the callback for IRQ. When an IRQ is triggered, the specified function will be called with the device pointer.

        Parameters:
        :   - **dev** – UART device instance.
            - **cb** – Pointer to the callback function.

        Return values:
        :   - **0** – On success.
            - **-ENOSYS** – If this function is not implemented.
            - **-ENOTSUP** – If API is not enabled.

### Asynchronous API

*group* uart\_async
:   Typedefs

    typedef void (\*uart\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [uart\_event](#c.uart_event) \*evt, void \*user\_data)
    :   Define the application callback function signature for [uart\_callback\_set()](#group__uart__async_1gad33e627ed8729409b14e92453e53459c) function.

        Param dev:
        :   UART device instance.

        Param evt:
        :   Pointer to [uart\_event](#structuart__event) instance.

        Param user\_data:
        :   Pointer to data specified by user.

    Enums

    enum uart\_event\_type
    :   Types of events passed to callback in UART\_ASYNC\_API.

        Receiving:

        1. To start receiving, uart\_rx\_enable has to be called with first buffer
        2. When receiving starts to current buffer, [UART\_RX\_BUF\_REQUEST](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) will be generated, in response to that user can either:

           - Provide second buffer using uart\_rx\_buf\_rsp, when first buffer is filled, receiving will automatically start to second buffer.
           - Ignore the event, this way when current buffer is filled [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated and receiving will be stopped.
        3. If some data was received and timeout occurred [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated. It can happen multiples times for the same buffer. RX timeout is counted from last byte received i.e. if no data was received, there won’t be any timeout event.
        4. [UART\_RX\_BUF\_RELEASED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event will be generated when the current buffer is no longer used by the driver. It will immediately follow [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event. Depending on the implementation buffer may be released when it is completely or partially filled.
        5. If there was second buffer provided, it will become current buffer and we start again at point 2. If no second buffer was specified receiving is stopped and [UART\_RX\_DISABLED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event is generated. After that whole process can be repeated.

        Any time during reception [UART\_RX\_STOPPED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) event can occur. if there is any data received, [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated. It will be followed by [UART\_RX\_BUF\_RELEASED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event for every buffer currently passed to driver and finally by [UART\_RX\_DISABLED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event.

        Receiving can be disabled using uart\_rx\_disable, after calling that function, if there is any data received, [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated. [UART\_RX\_BUF\_RELEASED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event will be generated for every buffer currently passed to driver and finally [UART\_RX\_DISABLED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event will occur.

        Transmitting:

        1. Transmitting starts by uart\_tx function.
        2. If whole buffer was transmitted [UART\_TX\_DONE](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) is generated. If timeout occurred [UART\_TX\_ABORTED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) will be generated.

        Transmitting can be aborted using [uart\_tx\_abort](#group__uart__async_1gaa8a26d3ea685fb98030ea03613be6280), after calling that function [UART\_TX\_ABORTED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) event will be generated.

        *Values:*

        enumerator UART\_TX\_DONE
        :   Whole TX buffer was transmitted.

        enumerator UART\_TX\_ABORTED
        :   Transmitting aborted due to timeout or uart\_tx\_abort call.

            When flow control is enabled, there is a possibility that TX transfer won’t finish in the allotted time. Some data may have been transferred, information about it can be found in event data.

        enumerator UART\_RX\_RDY
        :   Received data is ready for processing.

            This event is generated in the following cases:

            - When RX timeout occurred, and data was stored in provided buffer. This can happen multiple times in the same buffer.
            - When provided buffer is full.
            - After [uart\_rx\_disable()](#group__uart__async_1gafd4753bee51b230091a3c6ddb26ea734).
            - After stopping due to external event ([UART\_RX\_STOPPED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)).

        enumerator UART\_RX\_BUF\_REQUEST
        :   Driver requests next buffer for continuous reception.

            This event is triggered when receiving has started for a new buffer, i.e. it’s time to provide a next buffer for a seamless switchover to it. For continuous reliable receiving, user should provide another RX buffer in response to this event, using uart\_rx\_buf\_rsp function

            If uart\_rx\_buf\_rsp is not called before current buffer is filled up, receiving will stop.

        enumerator UART\_RX\_BUF\_RELEASED
        :   Buffer is no longer used by UART driver.

        enumerator UART\_RX\_DISABLED
        :   RX has been disabled and can be reenabled.

            This event is generated whenever receiver has been stopped, disabled or finished its operation and can be enabled again using uart\_rx\_enable

        enumerator UART\_RX\_STOPPED
        :   RX has stopped due to external event.

            Reason is one of [uart\_rx\_stop\_reason](#group__uart__interface_1gadeba6c5485e01dfc1c8a6e1c21668a88).

    Functions

    static inline int uart\_callback\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [uart\_callback\_t](#c.uart_callback_t) callback, void \*user\_data)
    :   Set event handler function.

        Since it is mandatory to set callback to use other asynchronous functions, it can be used to detect if the device supports asynchronous API. Remaining API does not have that detection.

        Parameters:
        :   - **dev** – UART device instance.
            - **callback** – Event handler.
            - **user\_data** – Data to pass to event handler function.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If not supported by the device.
            - **-ENOTSUP** – If API not enabled.

    int uart\_tx(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*buf, size\_t len, int32\_t timeout)
    :   Send given number of bytes from buffer through UART.

        Function returns immediately and event handler, set using [uart\_callback\_set](#group__uart__async_1gad33e627ed8729409b14e92453e53459c), is called after transfer is finished.

        Parameters:
        :   - **dev** – UART device instance.
            - **buf** – Pointer to transmit buffer.
            - **len** – Length of transmit buffer.
            - **timeout** – Timeout in microseconds. Valid only if flow control is enabled. SYS\_FOREVER\_US disables timeout.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EBUSY** – If There is already an ongoing transfer.
            - **-errno** – Other negative errno value in case of failure.

    int uart\_tx\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t \*buf, size\_t len, int32\_t timeout)
    :   Send given number of datum from buffer through UART.

        Function returns immediately and event handler, set using [uart\_callback\_set](#group__uart__async_1gad33e627ed8729409b14e92453e53459c), is called after transfer is finished.

        Parameters:
        :   - **dev** – UART device instance.
            - **buf** – Pointer to wide data transmit buffer.
            - **len** – Length of wide data transmit buffer.
            - **timeout** – Timeout in milliseconds. Valid only if flow control is enabled. SYS\_FOREVER\_MS disables timeout.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EBUSY** – If there is already an ongoing transfer.
            - **-errno** – Other negative errno value in case of failure.

    int uart\_tx\_abort(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Abort current TX transmission.

        [UART\_TX\_DONE](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) event will be generated with amount of data sent.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EFAULT** – There is no active transmission.
            - **-errno** – Other negative errno value in case of failure.

    int uart\_rx\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buf, size\_t len, int32\_t timeout)
    :   Start receiving data through UART.

        Function sets given buffer as first buffer for receiving and returns immediately. After that event handler, set using [uart\_callback\_set](#group__uart__async_1gad33e627ed8729409b14e92453e53459c), is called with [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) or [UART\_RX\_BUF\_REQUEST](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) events.

        Parameters:
        :   - **dev** – UART device instance.
            - **buf** – Pointer to receive buffer.
            - **len** – Buffer length.
            - **timeout** – Inactivity period after receiving at least a byte which triggers [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event. Given in microseconds. SYS\_FOREVER\_US disables timeout. See [uart\_event\_type](#group__uart__async_1gaf0c9513cbafa36d86b4c83f2b6a03dcd) for details.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EBUSY** – RX already in progress.
            - **-errno** – Other negative errno value in case of failure.

    int uart\_rx\_enable\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t \*buf, size\_t len, int32\_t timeout)
    :   Start receiving wide data through UART.

        Function sets given buffer as first buffer for receiving and returns immediately. After that event handler, set using [uart\_callback\_set](#group__uart__async_1gad33e627ed8729409b14e92453e53459c), is called with [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) or [UART\_RX\_BUF\_REQUEST](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) events.

        Parameters:
        :   - **dev** – UART device instance.
            - **buf** – Pointer to wide data receive buffer.
            - **len** – Buffer length.
            - **timeout** – Inactivity period after receiving at least a byte which triggers [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event. Given in milliseconds. SYS\_FOREVER\_MS disables timeout. See [uart\_event\_type](#group__uart__async_1gaf0c9513cbafa36d86b4c83f2b6a03dcd) for details.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EBUSY** – RX already in progress.
            - **-errno** – Other negative errno value in case of failure.

    static inline int uart\_rx\_buf\_rsp(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buf, size\_t len)
    :   Provide receive buffer in response to [UART\_RX\_BUF\_REQUEST](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) event.

        Provide pointer to RX buffer, which will be used when current buffer is filled.

        Note

        Providing buffer that is already in usage by driver leads to undefined behavior. Buffer can be reused when it has been released by driver.

        Parameters:
        :   - **dev** – UART device instance.
            - **buf** – Pointer to receive buffer.
            - **len** – Buffer length.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EBUSY** – Next buffer already set.
            - **-EACCES** – Receiver is already disabled (function called too late?).
            - **-errno** – Other negative errno value in case of failure.

    static inline int uart\_rx\_buf\_rsp\_u16(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t \*buf, size\_t len)
    :   Provide wide data receive buffer in response to [UART\_RX\_BUF\_REQUEST](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) event.

        Provide pointer to RX buffer, which will be used when current buffer is filled.

        Note

        Providing buffer that is already in usage by driver leads to undefined behavior. Buffer can be reused when it has been released by driver.

        Parameters:
        :   - **dev** – UART device instance.
            - **buf** – Pointer to wide data receive buffer.
            - **len** – Buffer length.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled
            - **-EBUSY** – Next buffer already set.
            - **-EACCES** – Receiver is already disabled (function called too late?).
            - **-errno** – Other negative errno value in case of failure.

    int uart\_rx\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable RX.

        [UART\_RX\_BUF\_RELEASED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event will be generated for every buffer scheduled, after that [UART\_RX\_DISABLED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event will be generated. Additionally, if there is any pending received data, the [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event for that data will be generated before the [UART\_RX\_BUF\_RELEASED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) events.

        Parameters:
        :   - **dev** – UART device instance.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If API is not enabled.
            - **-EFAULT** – There is no active reception.
            - **-errno** – Other negative errno value in case of failure.

    struct uart\_event\_tx
    :   *#include <uart.h>*

        UART TX event data.

        Public Members

        const uint8\_t \*buf
        :   Pointer to current buffer.

        size\_t len
        :   Number of bytes sent.

    struct uart\_event\_rx
    :   *#include <uart.h>*

        UART RX event data.

        The data represented by the event is stored in rx.buf[rx.offset] to rx.buf[rx.offset+rx.len]. That is, the length is relative to the offset.

        Public Members

        uint8\_t \*buf
        :   Pointer to current buffer.

        size\_t offset
        :   Currently received data offset in bytes.

        size\_t len
        :   Number of new bytes received.

    struct uart\_event\_rx\_buf
    :   *#include <uart.h>*

        UART RX buffer released event data.

        Public Members

        uint8\_t \*buf
        :   Pointer to buffer that is no longer in use.

    struct uart\_event\_rx\_stop
    :   *#include <uart.h>*

        UART RX stopped data.

        Public Members

        enum [uart\_rx\_stop\_reason](#c.uart_rx_stop_reason) reason
        :   Reason why receiving stopped.

        struct [uart\_event\_rx](#c.uart_event_rx) data
        :   Last received data.

    struct uart\_event
    :   *#include <uart.h>*

        Structure containing information about current event.

        Public Members

        enum [uart\_event\_type](#c.uart_event_type) type
        :   Type of event.

        union uart\_event\_data
        :   *#include <uart.h>*

            Event data.

            Public Members

            struct [uart\_event\_tx](#c.uart_event_tx) tx
            :   [UART\_TX\_DONE](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) and [UART\_TX\_ABORTED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) events data.

            struct [uart\_event\_rx](#c.uart_event_rx) rx
            :   [UART\_RX\_RDY](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event data.

            struct [uart\_event\_rx\_buf](#c.uart_event_rx_buf) rx\_buf
            :   [UART\_RX\_BUF\_RELEASED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event data.

            struct [uart\_event\_rx\_stop](#c.uart_event_rx_stop) rx\_stop
            :   [UART\_RX\_STOPPED](#group__uart__async_1ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) event data.
