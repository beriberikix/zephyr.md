---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/storage/disk/access.html
original_path: services/storage/disk/access.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Disk Access

## Overview

The disk access API provides access to storage devices.

## SD Card support

Zephyr has support for some SD card controllers and support for interfacing
SD cards via SPI. These drivers use disk driver interface and a file system
can access the SD cards via disk access API.
Both standard and high-capacity SD cards are supported.

Note

The system does not support inserting or removing cards while the
system is running. The cards must be present at boot and must not be
removed. This may be fixed in future releases.

FAT filesystems are not power safe so the filesystem may become
corrupted if power is lost or if the card is removed.

### SD Memory Card subsystem

Zephyr supports SD memory cards via the disk driver API, or via the SDMMC
subsystem. This subsystem can be used transparently via the disk driver API,
but also supports direct block level access to cards. The SDMMC subsystem
interacts with the [sd host controller api](../../../hardware/peripherals/sdhc.md#sdhc-api) to communicate
with attached SD cards.

### SD Card support via SPI

Example devicetree fragment below shows how to add SD card node to `spi1`
interface. Example uses pin `PA27` for chip select, and runs the SPI bus
at 24 MHz once the SD card has been initialized:

```devicetree
&spi1 {
        status = "okay";
        cs-gpios = <&porta 27 GPIO_ACTIVE_LOW>;

        sdhc0: sdhc@0 {
                compatible = "zephyr,sdhc-spi-slot";
                reg = <0>;
                status = "okay";
                mmc {
                    compatible = "zephyr,sdmmc-disk";
                    status = "okay";
                };
                spi-max-frequency = <24000000>;
        };
};
```

The SD card will be automatically detected and initialized by the
filesystem driver when the board boots.

To read and write files and directories, see the [File Systems](../../file_system/index.md#file-system-api) in
[include/zephyr/fs/fs.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/fs/fs.h) such as [`fs_open()`](../../file_system/index.md#c.fs_open "fs_open"),
[`fs_read()`](../../file_system/index.md#c.fs_read "fs_read"), and [`fs_write()`](../../file_system/index.md#c.fs_write "fs_write").

## eMMC Device Support

Zephyr also has support for eMMC devices using the Disk Access API.
MMC in zephyr is implemented using the SD subsystem because the MMC bus
shares a lot of similarity with the SD bus. MMC controllers also use the
SDHC device driver API.

## Emulated block device on flash partition support

Zephyr flashdisk driver makes it possible to use flash memory partition as
a block device. The flashdisk instances are defined in devicetree:

```devicetree
/ {
    msc_disk0 {
        compatible = "zephyr,flash-disk";
        partition = <&storage_partition>;
        disk-name = "NAND";
        cache-size = <4096>;
    };
};
```

The cache size specified in [`zephyr,flash-disk`](../../../build/dts/api/bindings/misc/zephyr%2Cflash-disk.md#std-dtcompatible-zephyr-flash-disk) node should be
equal to backing partition minimum erasable block size.

### NVMe disk support

NVMe disks are also supported

## Disk Access API Configuration Options

Related configuration options:

- [`CONFIG_DISK_ACCESS`](../../../kconfig.md#CONFIG_DISK_ACCESS "CONFIG_DISK_ACCESS")

## API Reference

Related code samples

[File system manipulation](../../../samples/subsys/fs/fs_sample/README.md#fs "Use file system API with various filesystems and storage devices.")
:   Use file system API with various filesystems and storage devices.

*group* disk\_access\_interface
:   Disk Access APIs.

    Functions

    int disk\_access\_init(const char \*pdrv)
    :   perform any initialization

        This call is made by the consumer before doing any IO calls so that the disk or the backing device can do any initialization.

        Parameters:
        :   - **pdrv** – **[in]** Disk name

        Returns:
        :   0 on success, negative errno code on fail

    int disk\_access\_status(const char \*pdrv)
    :   Get the status of disk.

        This call is used to get the status of the disk

        Parameters:
        :   - **pdrv** – **[in]** Disk name

        Returns:
        :   DISK\_STATUS\_OK or other DISK\_STATUS\_\*s

    int disk\_access\_read(const char \*pdrv, uint8\_t \*data\_buf, uint32\_t start\_sector, uint32\_t num\_sector)
    :   read data from disk

        Function to read data from disk to a memory buffer.

        Note: if he disk is of NVMe type, user will need to ensure data\_buf pointer is 4-bytes aligned.

        Parameters:
        :   - **pdrv** – **[in]** Disk name
            - **data\_buf** – **[in]** Pointer to the memory buffer to put data.
            - **start\_sector** – **[in]** Start disk sector to read from
            - **num\_sector** – **[in]** Number of disk sectors to read

        Returns:
        :   0 on success, negative errno code on fail

    int disk\_access\_write(const char \*pdrv, const uint8\_t \*data\_buf, uint32\_t start\_sector, uint32\_t num\_sector)
    :   write data to disk

        Function write data from memory buffer to disk.

        Note: if he disk is of NVMe type, user will need to ensure data\_buf pointer is 4-bytes aligned.

        Parameters:
        :   - **pdrv** – **[in]** Disk name
            - **data\_buf** – **[in]** Pointer to the memory buffer
            - **start\_sector** – **[in]** Start disk sector to write to
            - **num\_sector** – **[in]** Number of disk sectors to write

        Returns:
        :   0 on success, negative errno code on fail

    int disk\_access\_ioctl(const char \*pdrv, uint8\_t cmd, void \*buff)
    :   Get/Configure disk parameters.

        Function to get disk parameters and make any special device requests.

        Parameters:
        :   - **pdrv** – **[in]** Disk name
            - **cmd** – DISK\_IOCTL\_\* code describing the request
            - **buff** – **[in]** Command data buffer

        Returns:
        :   0 on success, negative errno code on fail

## Disk Driver Configuration Options

Related driver configuration options:

- [`CONFIG_DISK_DRIVERS`](../../../kconfig.md#CONFIG_DISK_DRIVERS "CONFIG_DISK_DRIVERS")

## Disk Driver Interface

*group* disk\_driver\_interface
:   Disk Driver Interface.

    Defines

    DISK\_IOCTL\_GET\_SECTOR\_COUNT
    :   Possible Cmd Codes for disk\_ioctl().

        Get the number of sectors in the disk

    DISK\_IOCTL\_GET\_SECTOR\_SIZE
    :   Get the size of a disk SECTOR in bytes.

    DISK\_IOCTL\_RESERVED
    :   reserved.

        It used to be DISK\_IOCTL\_GET\_DISK\_SIZE

    DISK\_IOCTL\_GET\_ERASE\_BLOCK\_SZ
    :   How many sectors constitute a FLASH Erase block.

    DISK\_IOCTL\_CTRL\_SYNC
    :   Commit any cached read/writes to disk.

    DISK\_STATUS\_OK
    :   Possible return bitmasks for disk\_status().

        Disk status okay

    DISK\_STATUS\_UNINIT
    :   Disk status uninitialized.

    DISK\_STATUS\_NOMEDIA
    :   Disk status no media.

    DISK\_STATUS\_WR\_PROTECT
    :   Disk status write protected.

    Functions

    int disk\_access\_register(struct [disk\_info](#c.disk_info) \*disk)
    :   Register disk.

        Parameters:
        :   - **disk** – **[in]** Pointer to the disk info structure

        Returns:
        :   0 on success, negative errno code on fail

    int disk\_access\_unregister(struct [disk\_info](#c.disk_info) \*disk)
    :   Unregister disk.

        Parameters:
        :   - **disk** – **[in]** Pointer to the disk info structure

        Returns:
        :   0 on success, negative errno code on fail

    struct disk\_info
    :   *#include <disk.h>*

        Disk info.

        Public Members

        [sys\_dnode\_t](../../../kernel/data_structures/dlist.md#c.sys_dnode_t "sys_dnode_t") node
        :   Internally used list node.

        char \*name
        :   Disk name.

        const struct [disk\_operations](#c.disk_operations) \*ops
        :   Disk operations.

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev
        :   Device associated to this disk.

    struct disk\_operations
    :   *#include <disk.h>*

        Disk operations.
