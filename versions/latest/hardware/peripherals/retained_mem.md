---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/retained_mem.html
original_path: hardware/peripherals/retained_mem.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Retained Memory

## Overview

The retained memory driver API provides a way of reading from/writing to memory
areas whereby the contents of the memory is retained whilst the device is
powered (data may be lost in low power modes).

## Configuration Options

Related configuration options:

- [`CONFIG_RETAINED_MEM`](../../kconfig.md#CONFIG_RETAINED_MEM "CONFIG_RETAINED_MEM")
- [`CONFIG_RETAINED_MEM_INIT_PRIORITY`](../../kconfig.md#CONFIG_RETAINED_MEM_INIT_PRIORITY "CONFIG_RETAINED_MEM_INIT_PRIORITY")
- [`CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE`](../../kconfig.md#CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE "CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE")

## Mutex protection

Mutex protection of retained memory drivers is enabled by default when
applications are compiled with multithreading support. This means that
different threads can safely call the retained memory functions without
clashing with other concurrent thread function usage, but means that retained
memory functions cannot be used from ISRs. It is possible to disable mutex
protection globally on all retained memory drivers by enabling
[`CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE`](../../kconfig.md#CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE "CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE") - users are then
responsible for ensuring that the function calls do not conflict with each
other.

## API Reference

*group* retained\_mem\_interface
:   Retained memory driver interface.

    Typedefs

    typedef ssize\_t (\*retained\_mem\_size\_api)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to get size of retained memory area.

        See [retained\_mem\_size()](#group__retained__mem__interface_1gaa0b4b6db4c96054a709f803880f3091a) for argument description.

    typedef int (\*retained\_mem\_read\_api)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, uint8\_t \*buffer, size\_t size)
    :   Callback API to read from retained memory area.

        See [retained\_mem\_read()](#group__retained__mem__interface_1ga47fba21400c1f7019e7bd0e8f10662b3) for argument description.

    typedef int (\*retained\_mem\_write\_api)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, const uint8\_t \*buffer, size\_t size)
    :   Callback API to write to retained memory area.

        See [retained\_mem\_write()](#group__retained__mem__interface_1ga1976ac945eb7c09b8dd6121926af0c6a) for argument description.

    typedef int (\*retained\_mem\_clear\_api)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to clear retained memory area (reset all data to 0x00).

        See [retained\_mem\_clear()](#group__retained__mem__interface_1ga5962d863c21cd91e259bf47abf2154d7) for argument description.

    Functions

    ssize\_t retained\_mem\_size(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Returns the size of the retained memory area.

        Parameters:
        :   - **dev** – Retained memory device to use.

        Return values:
        :   **Positive** – value indicating size in bytes on success, else negative errno code.

    int retained\_mem\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, uint8\_t \*buffer, size\_t size)
    :   Reads data from the Retained memory area.

        Parameters:
        :   - **dev** – Retained memory device to use.
            - **offset** – Offset to read data from.
            - **buffer** – Buffer to store read data in.
            - **size** – Size of data to read.

        Return values:
        :   **0** – on success else negative errno code.

    int retained\_mem\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, const uint8\_t \*buffer, size\_t size)
    :   Writes data to the Retained memory area - underlying data does not need to be cleared prior to writing.

        Parameters:
        :   - **dev** – Retained memory device to use.
            - **offset** – Offset to write data to.
            - **buffer** – Data to write.
            - **size** – Size of data to be written.

        Return values:
        :   **0** – on success else negative errno code.

    int retained\_mem\_clear(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clears data in the retained memory area by setting it to 0x00.

        Parameters:
        :   - **dev** – Retained memory device to use.

        Return values:
        :   **0** – on success else negative errno code.

    struct retained\_mem\_driver\_api
    :   *#include <retained\_mem.h>*

        Retained memory driver API API which can be used by a device to store data in a retained memory area.

        Retained memory is memory that is retained while the device is powered but is lost when power to the device is lost (note that low power modes in some devices may clear the data also). This may be in a non-initialised RAM region, or in specific registers, but is not reset when a different application begins execution or the device is rebooted (without power loss). It must support byte-level reading and writing without a need to erase data before writing.

        Note that drivers must implement all functions, none of the functions are optional.
