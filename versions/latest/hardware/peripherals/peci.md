---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/peci.html
original_path: hardware/peripherals/peci.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Platform Environment Control Interface (PECI)

## Overview

The Platform Environment Control Interface, abbreviated as PECI,
is a thermal management standard introduced in 2006
with the Intel Core 2 Duo Microprocessors.
The PECI interface allows external devices to read processor temperature,
perform processor manageability functions, and manage processor interface
tuning and diagnostics.
The PECI bus driver APIs enable the interaction between Embedded
Microcontrollers and CPUs.

## Configuration Options

Related configuration options:

- [`CONFIG_PECI`](../../kconfig.md#CONFIG_PECI "CONFIG_PECI")

## API Reference

Related code samples

[PECI interface](../../samples/drivers/peci/README.md#peci "Monitor CPU temperature using PECI.")
:   Monitor CPU temperature using PECI.

*group* peci\_interface
:   PECI Interface 3.0.

    PECI read/write supported responses.

    PECI\_CC\_RSP\_SUCCESS

    PECI\_CC\_RSP\_TIMEOUT

    PECI\_CC\_OUT\_OF\_RESOURCES\_TIMEOUT

    PECI\_CC\_RESOURCES\_LOWPWR\_TIMEOUT

    PECI\_CC\_ILLEGAL\_REQUEST

    Ping command format.

    PECI\_PING\_WR\_LEN

    PECI\_PING\_RD\_LEN

    PECI\_PING\_LEN

    GetDIB command format.

    PECI\_GET\_DIB\_WR\_LEN

    PECI\_GET\_DIB\_RD\_LEN

    PECI\_GET\_DIB\_CMD\_LEN

    PECI\_GET\_DIB\_DEVINFO

    PECI\_GET\_DIB\_REVNUM

    PECI\_GET\_DIB\_DOMAIN\_BIT\_MASK

    PECI\_GET\_DIB\_MAJOR\_REV\_MASK

    PECI\_GET\_DIB\_MINOR\_REV\_MASK

    GetTemp command format.

    PECI\_GET\_TEMP\_WR\_LEN

    PECI\_GET\_TEMP\_RD\_LEN

    PECI\_GET\_TEMP\_CMD\_LEN

    PECI\_GET\_TEMP\_LSB

    PECI\_GET\_TEMP\_MSB

    PECI\_GET\_TEMP\_ERR\_MSB

    PECI\_GET\_TEMP\_ERR\_LSB\_GENERAL

    PECI\_GET\_TEMP\_ERR\_LSB\_RES

    PECI\_GET\_TEMP\_ERR\_LSB\_TEMP\_LO

    PECI\_GET\_TEMP\_ERR\_LSB\_TEMP\_HI

    RdPkgConfig command format.

    PECI\_RD\_PKG\_WR\_LEN

    PECI\_RD\_PKG\_LEN\_BYTE

    PECI\_RD\_PKG\_LEN\_WORD

    PECI\_RD\_PKG\_LEN\_DWORD

    PECI\_RD\_PKG\_CMD\_LEN

    WrPkgConfig command format.

    PECI\_WR\_PKG\_RD\_LEN

    PECI\_WR\_PKG\_LEN\_BYTE

    PECI\_WR\_PKG\_LEN\_WORD

    PECI\_WR\_PKG\_LEN\_DWORD

    PECI\_WR\_PKG\_CMD\_LEN

    RdIAMSR command format.

    PECI\_RD\_IAMSR\_WR\_LEN

    PECI\_RD\_IAMSR\_LEN\_BYTE

    PECI\_RD\_IAMSR\_LEN\_WORD

    PECI\_RD\_IAMSR\_LEN\_DWORD

    PECI\_RD\_IAMSR\_LEN\_QWORD

    PECI\_RD\_IAMSR\_CMD\_LEN

    WrIAMSR command format.

    PECI\_WR\_IAMSR\_RD\_LEN

    PECI\_WR\_IAMSR\_LEN\_BYTE

    PECI\_WR\_IAMSR\_LEN\_WORD

    PECI\_WR\_IAMSR\_LEN\_DWORD

    PECI\_WR\_IAMSR\_LEN\_QWORD

    PECI\_WR\_IAMSR\_CMD\_LEN

    RdPCIConfig command format.

    PECI\_RD\_PCICFG\_WR\_LEN

    PECI\_RD\_PCICFG\_LEN\_BYTE

    PECI\_RD\_PCICFG\_LEN\_WORD

    PECI\_RD\_PCICFG\_LEN\_DWORD

    PECI\_RD\_PCICFG\_CMD\_LEN

    WrPCIConfig command format.

    PECI\_WR\_PCICFG\_RD\_LEN

    PECI\_WR\_PCICFG\_LEN\_BYTE

    PECI\_WR\_PCICFG\_LEN\_WORD

    PECI\_WR\_PCICFG\_LEN\_DWORD

    PECI\_WR\_PCICFG\_CMD\_LEN

    RdPCIConfigLocal command format.

    PECI\_RD\_PCICFGL\_WR\_LEN

    PECI\_RD\_PCICFGL\_RD\_LEN\_BYTE

    PECI\_RD\_PCICFGL\_RD\_LEN\_WORD

    PECI\_RD\_PCICFGL\_RD\_LEN\_DWORD

    PECI\_RD\_PCICFGL\_CMD\_LEN

    WrPCIConfigLocal command format.

    PECI\_WR\_PCICFGL\_RD\_LEN

    PECI\_WR\_PCICFGL\_WR\_LEN\_BYTE

    PECI\_WR\_PCICFGL\_WR\_LEN\_WORD

    PECI\_WR\_PCICFGL\_WR\_LEN\_DWORD

    PECI\_WR\_PCICFGL\_CMD\_LEN

    Enums

    enum peci\_error\_code
    :   PECI error codes.

        *Values:*

        enumerator PECI\_GENERAL\_SENSOR\_ERROR = 0x8000

        enumerator PECI\_UNDERFLOW\_SENSOR\_ERROR = 0x8002

        enumerator PECI\_OVERFLOW\_SENSOR\_ERROR = 0x8003

    enum peci\_command\_code
    :   PECI commands.

        *Values:*

        enumerator PECI\_CMD\_PING = 0x00

        enumerator PECI\_CMD\_GET\_TEMP0 = 0x01

        enumerator PECI\_CMD\_GET\_TEMP1 = 0x02

        enumerator PECI\_CMD\_RD\_PCI\_CFG0 = 0x61

        enumerator PECI\_CMD\_RD\_PCI\_CFG1 = 0x62

        enumerator PECI\_CMD\_WR\_PCI\_CFG0 = 0x65

        enumerator PECI\_CMD\_WR\_PCI\_CFG1 = 0x66

        enumerator PECI\_CMD\_RD\_PKG\_CFG0 = 0xA1

        enumerator PECI\_CMD\_RD\_PKG\_CFG1 = 0xA

        enumerator PECI\_CMD\_WR\_PKG\_CFG0 = 0xA5

        enumerator PECI\_CMD\_WR\_PKG\_CFG1 = 0xA6

        enumerator PECI\_CMD\_RD\_IAMSR0 = 0xB1

        enumerator PECI\_CMD\_RD\_IAMSR1 = 0xB2

        enumerator PECI\_CMD\_WR\_IAMSR0 = 0xB5

        enumerator PECI\_CMD\_WR\_IAMSR1 = 0xB6

        enumerator PECI\_CMD\_RD\_PCI\_CFG\_LOCAL0 = 0xE1

        enumerator PECI\_CMD\_RD\_PCI\_CFG\_LOCAL1 = 0xE2

        enumerator PECI\_CMD\_WR\_PCI\_CFG\_LOCAL0 = 0xE5

        enumerator PECI\_CMD\_WR\_PCI\_CFG\_LOCAL1 = 0xE6

        enumerator PECI\_CMD\_GET\_DIB = 0xF7

    Functions

    int peci\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t bitrate)
    :   Configures the PECI interface.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **bitrate** – the selected bitrate expressed in Kbps.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int peci\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable PECI interface.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int peci\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable PECI interface.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int peci\_transfer(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [peci\_msg](#c.peci_msg) \*msg)
    :   Performs a PECI transaction.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **msg** – Structure representing a PECI transaction.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    struct peci\_buf
    :   *#include <peci.h>*

        PECI buffer structure.

        Public Members

        uint8\_t \*buf
        :   Valid pointer on a data buffer, or NULL otherwise.

        size\_t len
        :   Length of the data buffer expected to be received without considering the frame check sequence byte.

            Note

            Frame check sequence byte is added into rx buffer: need to allocate an additional byte for this in rx buffer.

    struct peci\_msg
    :   *#include <peci.h>*

        PECI transaction packet format.

        Public Members

        uint8\_t addr
        :   Client address.

        enum [peci\_command\_code](#c.peci_command_code) cmd\_code
        :   Command code.

        struct [peci\_buf](#c.peci_buf) tx\_buffer
        :   Pointer to buffer of write data.

        struct [peci\_buf](#c.peci_buf) rx\_buffer
        :   Pointer to buffer of read data.

        uint8\_t flags
        :   PECI msg flags.
