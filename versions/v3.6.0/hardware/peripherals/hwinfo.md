---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/hwinfo.html
original_path: hardware/peripherals/hwinfo.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Hardware Information

## Overview

The HW Info API provides access to hardware information such as device
identifiers and reset cause flags.

Reset cause flags can be used to determine why the device was reset; for
example due to a watchdog timeout or due to power cycling. Different devices
support different subset of flags. Use
[`hwinfo_get_supported_reset_cause()`](#c.hwinfo_get_supported_reset_cause) to retrieve the flags that are
supported by that device.

## Configuration Options

Related configuration options:

- [`CONFIG_HWINFO`](../../kconfig.md#CONFIG_HWINFO "CONFIG_HWINFO")

## API Reference

*group* hwinfo\_interface
:   Hardware Information Interface.

    Reset cause flags

    RESET\_PIN
    :   External pin.

    RESET\_SOFTWARE
    :   Software reset.

    RESET\_BROWNOUT
    :   Brownout (drop in voltage).

    RESET\_POR
    :   Power-on reset (POR).

    RESET\_WATCHDOG
    :   Watchdog timer expiration.

    RESET\_DEBUG
    :   Debug event.

    RESET\_SECURITY
    :   Security violation.

    RESET\_LOW\_POWER\_WAKE
    :   Waking up from low power mode.

    RESET\_CPU\_LOCKUP
    :   CPU lock-up detected.

    RESET\_PARITY
    :   Parity error.

    RESET\_PLL
    :   PLL error.

    RESET\_CLOCK
    :   Clock error.

    RESET\_HARDWARE
    :   Hardware reset.

    RESET\_USER
    :   User reset.

    RESET\_TEMPERATURE
    :   Temperature reset.

    Functions

    ssize\_t hwinfo\_get\_device\_id(uint8\_t \*buffer, size\_t length)
    :   Copy the device id to a buffer.

        This routine copies “length” number of bytes of the device ID to the buffer. If the device ID is smaller then length, the rest of the buffer is left unchanged. The ID depends on the hardware and is not guaranteed unique.

        Drivers are responsible for ensuring that the ID data structure is a sequence of bytes. The returned ID value is not supposed to be interpreted based on vendor-specific assumptions of byte order. It should express the identifier as a raw byte sequence, doing any endian conversion necessary so that a hex representation of the bytes produces the intended serial number.

        Parameters:
        :   - **buffer** – Buffer to write the ID to.
            - **length** – Max length of the buffer.

        Return values:
        :   - **size** – of the device ID copied.
            - **-ENOSYS** – if there is no implementation for the particular device.
            - **any** – negative value on driver specific errors.

    int hwinfo\_get\_reset\_cause(uint32\_t \*cause)
    :   Retrieve cause of device reset.

        This routine retrieves the flags that indicate why the device was reset.

        On some platforms the reset cause flags accumulate between successive resets and this routine may return multiple flags indicating all reset causes since the device was powered on. If you need to retrieve the cause only for the most recent reset call `[hwinfo_clear_reset_cause](#group__hwinfo__interface_1gaeaa23e68c53eb6a2b56f06c74b83e613)` after calling this routine to clear the hardware flags before the next reset event.

        Successive calls to this routine will return the same value, unless `[hwinfo_clear_reset_cause](#group__hwinfo__interface_1gaeaa23e68c53eb6a2b56f06c74b83e613)` has been called.

        Parameters:
        :   - **cause** – OR’d [reset cause](#group__hwinfo__interface_1reset_cause) flags

        Return values:
        :   - **zero** – if successful.
            - **-ENOSYS** – if there is no implementation for the particular device.
            - **any** – negative value on driver specific errors.

    int hwinfo\_clear\_reset\_cause(void)
    :   Clear cause of device reset.

        Clears reset cause flags.

        Return values:
        :   - **zero** – if successful.
            - **-ENOSYS** – if there is no implementation for the particular device.
            - **any** – negative value on driver specific errors.

    int hwinfo\_get\_supported\_reset\_cause(uint32\_t \*supported)
    :   Get supported reset cause flags.

        Retrieves all `reset_cause` flags that are supported by this device.

        Parameters:
        :   - **supported** – OR’d [reset cause](#group__hwinfo__interface_1reset_cause) flags that are supported

        Return values:
        :   - **zero** – if successful.
            - **-ENOSYS** – if there is no implementation for the particular device.
            - **any** – negative value on driver specific errors.
