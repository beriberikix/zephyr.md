---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/flash.html
original_path: hardware/peripherals/flash.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Flash

## Overview

**Flash offset concept**

Offsets used by the user API are expressed in relation to
the flash memory beginning address. This rule shall be applied to
all flash controller regular memory that layout is accessible via
API for retrieving the layout of pages (see [`CONFIG_FLASH_PAGE_LAYOUT`](../../kconfig.md#CONFIG_FLASH_PAGE_LAYOUT "CONFIG_FLASH_PAGE_LAYOUT")).

An exception from the rule may be applied to a vendor-specific flash
dedicated-purpose region (such a region obviously can’t be covered under
API for retrieving the layout of pages).

## User API Reference

Related code samples

[AT45 DataFlash driver](../../samples/drivers/spi_flash_at45/README.md#spi-flash-at45 "Use the AT45 family DataFlash driver to interact with the flash memory over SPI.")
:   Use the AT45 family DataFlash driver to interact with the flash memory over SPI.

[ESP32 Flash Memory-Mapped](../../samples/boards/esp32/flash_memory_mapped/README.md#esp32-flash-memory-mapped "Write data into scratch area and read it using flash API and memory-mapped pointer.")
:   Write data into scratch area and read it using flash API and memory-mapped pointer.

[Flash shell](../../samples/drivers/flash_shell/README.md#flash-shell "Explore a flash device using shell commands.")
:   Explore a flash device using shell commands.

[JEDEC SPI-NOR flash](../../samples/drivers/spi_flash/README.md#spi-nor "Use the flash API to interact with an SPI NOR serial flash memory device.")
:   Use the flash API to interact with an SPI NOR serial flash memory device.

[JESD216 flash](../../samples/drivers/jesd216/README.md#jesd216 "Use the JESD216 flash API to extract information from a compatible serial memory device.")
:   Use the JESD216 flash API to extract information from a compatible serial memory device.

[nRF SoC flash](../../samples/drivers/soc_flash_nrf/README.md#soc-flash-nrf "Use the flash API to interact with the SoC flash.")
:   Use the flash API to interact with the SoC flash.

*group* flash\_interface
:   FLASH Interface.

    Defines

    FLASH\_EX\_OP\_VENDOR\_BASE

    FLASH\_EX\_OP\_IS\_VENDOR(c)

    Typedefs

    typedef bool (\*flash\_page\_cb)(const struct [flash\_pages\_info](#c.flash_pages_info) \*info, void \*data)
    :   Callback type for iterating over flash pages present on a device.

        The callback should return true to continue iterating, and false to halt.

        See also

        [flash\_page\_foreach()](#group__flash__interface_1ga275f2346e88b5e4d050dae426f0953fe)

        Param info:
        :   Information for current page

        Param data:
        :   Private data for callback

        Return:
        :   True to continue iteration, false to halt iteration.

    Enums

    enum flash\_ex\_op\_types
    :   Enumeration for extra flash operations.

        *Values:*

        enumerator FLASH\_EX\_OP\_RESET = 0

    Functions

    int flash\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, void \*data, size\_t len)
    :   Read data from flash.

        All flash drivers support reads without alignment restrictions on the read offset, the read size, or the destination address.

        Parameters:
        :   - **dev** – : flash dev
            - **offset** – : Offset (byte aligned) to read
            - **data** – : Buffer to store read data
            - **len** – : Number of bytes to read.

        Returns:
        :   0 on success, negative errno code on fail.

    int flash\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, const void \*data, size\_t len)
    :   Write buffer into flash memory.

        All flash drivers support a source buffer located either in RAM or SoC flash, without alignment restrictions on the source address. Write size and offset must be multiples of the minimum write block size supported by the driver.

        Any necessary write protection management is performed by the driver write implementation itself.

        Parameters:
        :   - **dev** – : flash device
            - **offset** – : starting offset for the write
            - **data** – : data to write
            - **len** – : Number of bytes to write

        Returns:
        :   0 on success, negative errno code on fail.

    int flash\_erase(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, size\_t size)
    :   Erase part or all of a flash memory.

        Acceptable values of erase size and offset are subject to hardware-specific multiples of page size and offset. Please check the API implemented by the underlying sub driver, for example by using [flash\_get\_page\_info\_by\_offs()](#group__flash__interface_1gafc959b0363eb27d6a3237e4288d60979) if that is supported by your flash driver.

        Any necessary erase protection management is performed by the driver erase implementation itself.

        See also

        [flash\_get\_page\_info\_by\_offs()](#group__flash__interface_1gafc959b0363eb27d6a3237e4288d60979)

        See also

        [flash\_get\_page\_info\_by\_idx()](#group__flash__interface_1gaae733082fa92f80261d5895d3f81a98b)

        Parameters:
        :   - **dev** – : flash device
            - **offset** – : erase area starting offset
            - **size** – : size of area to be erased

        Returns:
        :   0 on success, negative errno code on fail.

    int flash\_get\_page\_info\_by\_offs(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, struct [flash\_pages\_info](#c.flash_pages_info) \*info)
    :   Get the size and start offset of flash page at certain flash offset.

        Parameters:
        :   - **dev** – flash device
            - **offset** – Offset within the page
            - **info** – Page Info structure to be filled

        Returns:
        :   0 on success, -EINVAL if page of the offset doesn’t exist.

    int flash\_get\_page\_info\_by\_idx(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t page\_index, struct [flash\_pages\_info](#c.flash_pages_info) \*info)
    :   Get the size and start offset of flash page of certain index.

        Parameters:
        :   - **dev** – flash device
            - **page\_index** – Index of the page. Index are counted from 0.
            - **info** – Page Info structure to be filled

        Returns:
        :   0 on success, -EINVAL if page of the index doesn’t exist.

    size\_t flash\_get\_page\_count(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the total number of flash pages.

        Parameters:
        :   - **dev** – flash device

        Returns:
        :   Number of flash pages.

    void flash\_page\_foreach(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [flash\_page\_cb](#c.flash_page_cb) cb, void \*data)
    :   Iterate over all flash pages on a device.

        This routine iterates over all flash pages on the given device, ordered by increasing start offset. For each page, it invokes the given callback, passing it the page’s information and a private data object.

        Parameters:
        :   - **dev** – Device whose pages to iterate over
            - **cb** – Callback to invoke for each flash page
            - **data** – Private data for callback function

    int flash\_sfdp\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, void \*data, size\_t len)
    :   Read data from Serial Flash Discoverable Parameters.

        This routine reads data from a serial flash device compatible with the JEDEC JESD216 standard for encoding flash memory characteristics.

        Availability of this API is conditional on selecting `CONFIG_FLASH_JESD216_API` and support of that functionality in the driver underlying `dev`.

        Parameters:
        :   - **dev** – device from which parameters will be read
            - **offset** – address within the SFDP region containing data of interest
            - **data** – where the data to be read will be placed
            - **len** – the number of bytes of data to be read

        Return values:
        :   - **0** – on success
            - **-ENOTSUP** – if the flash driver does not support SFDP access
            - **negative** – values for other errors.

    int flash\_read\_jedec\_id(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*id)
    :   Read the JEDEC ID from a compatible flash device.

        Parameters:
        :   - **dev** – device from which id will be read
            - **id** – pointer to a buffer of at least 3 bytes into which id will be stored

        Return values:
        :   - **0** – on successful store of 3-byte JEDEC id
            - **-ENOTSUP** – if flash driver doesn’t support this function
            - **negative** – values for other errors

    size\_t flash\_get\_write\_block\_size(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the minimum write block size supported by the driver.

        The write block size supported by the driver might differ from the write block size of memory used because the driver might implements write-modify algorithm.

        Parameters:
        :   - **dev** – flash device

        Returns:
        :   write block size in bytes.

    const struct [flash\_parameters](#c.flash_parameters) \*flash\_get\_parameters(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get pointer to [flash\_parameters](#structflash__parameters) structure.

        Returned pointer points to a structure that should be considered constant through a runtime, regardless if it is defined in RAM or Flash. Developer is free to cache the structure pointer or copy its contents.

        Returns:
        :   pointer to [flash\_parameters](#structflash__parameters) structure characteristic for the device.

    int flash\_ex\_op(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t code, const uintptr\_t in, void \*out)
    :   Execute flash extended operation on given device.

        Besides of standard flash operations like write or erase, flash controllers also support additional features like write protection or readout protection. These features are not available in every flash controller, what’s more controllers can implement it in a different way.

        It doesn’t make sense to add a separate flash API function for every flash controller feature, because it could be unique (supported on small number of flash controllers) or the API won’t be able to represent the same feature on every flash controller.

        Parameters:
        :   - **dev** – Flash device
            - **code** – Operation which will be executed on the device.
            - **in** – Pointer to input data used by operation. If operation doesn’t need any input data it could be NULL.
            - **out** – Pointer to operation output data. If operation doesn’t produce any output it could be NULL.

        Return values:
        :   - **0** – on success.
            - **-ENOTSUP** – if given device doesn’t support extended operation.
            - **-ENOSYS** – if support for extended operations is not enabled in Kconfig
            - **negative** – value on extended operation errors.

    struct flash\_parameters
    :   *#include <flash.h>*

        Flash memory parameters.

        Contents of this structure suppose to be filled in during flash device initialization and stay constant through a runtime.

    struct flash\_pages\_info
    :   *#include <flash.h>*

## Implementation interface API Reference

*group* flash\_internal\_interface
:   FLASH internal Interface.

    Typedefs

    typedef int (\*flash\_api\_read)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, void \*data, size\_t len)

    typedef int (\*flash\_api\_write)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, const void \*data, size\_t len)
    :   Flash write implementation handler type.

        Note

        Any necessary write protection management must be performed by the driver, with the driver responsible for ensuring the “write-protect” after the operation completes (successfully or not) matches the write-protect state when the operation was started.

    typedef int (\*flash\_api\_erase)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, size\_t size)
    :   Flash erase implementation handler type.

        Note

        Any necessary erase protection management must be performed by the driver, with the driver responsible for ensuring the “erase-protect” after the operation completes (successfully or not) matches the erase-protect state when the operation was started.

    typedef const struct [flash\_parameters](#c.flash_parameters) \*(\*flash\_api\_get\_parameters)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef void (\*flash\_api\_pages\_layout)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [flash\_pages\_layout](#c.flash_pages_layout) \*\*layout, size\_t \*layout\_size)
    :   Retrieve a flash device’s layout.

        A flash device layout is a run-length encoded description of the pages on the device. (Here, “page” means the smallest erasable area on the flash device.)

        For flash memories which have uniform page sizes, this routine returns an array of length 1, which specifies the page size and number of pages in the memory.

        Layouts for flash memories with nonuniform page sizes will be returned as an array with multiple elements, each of which describes a group of pages that all have the same size. In this case, the sequence of array elements specifies the order in which these groups occur on the device.

        Param dev:
        :   Flash device whose layout to retrieve.

        Param layout:
        :   The flash layout will be returned in this argument.

        Param layout\_size:
        :   The number of elements in the returned layout.

    typedef int (\*flash\_api\_sfdp\_read)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, void \*data, size\_t len)

    typedef int (\*flash\_api\_read\_jedec\_id)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*id)

    typedef int (\*flash\_api\_ex\_op)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t code, const uintptr\_t in, void \*out)

    struct flash\_pages\_layout
    :   *#include <flash.h>*

    struct flash\_driver\_api
    :   *#include <flash.h>*
