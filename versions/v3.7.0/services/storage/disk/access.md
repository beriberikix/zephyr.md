---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/storage/disk/access.html
original_path: services/storage/disk/access.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Disk Access

## Overview

The disk access API provides access to storage devices.

## Initializing Disks

Since many disk devices (such as SD cards) are hotpluggable, the disk access
API provides IOCTLs to initialize and de-initialize the disk. They are
as follows:

- [`DISK_IOCTL_CTRL_INIT`](#c.DISK_IOCTL_CTRL_INIT): Initialize the disk. Must be called before
  additional I/O operations can be run on the disk device. Equivalent to
  calling the legacy function [`disk_access_init()`](#c.disk_access_init).
- [`DISK_IOCTL_CTRL_DEINIT`](#c.DISK_IOCTL_CTRL_DEINIT): De-initialize the disk. Once this IOCTL
  is issued, the [`DISK_IOCTL_CTRL_INIT`](#c.DISK_IOCTL_CTRL_INIT) must be issued before
  the disk can be used for addition I/O operations.

Init/deinit IOCTL calls are balanced, so a disk will not de-initialize until
an equal number of deinit IOCTLs have been issued as init IOCTLs.

It is also possible to force a disk de-initialization by passing a
pointer to a boolean set to `true` as a parameter to the
[`DISK_IOCTL_CTRL_DEINIT`](#c.DISK_IOCTL_CTRL_DEINIT) IOCTL. This is an unsafe operation which
each disk driver may handle differently, but it will always return
a value indicating success.

Note that de-initializing a disk is a low level operation- typically the
de-initialization and initialization calls should be left to the filesystem
implementation, and the user application should not need to manually
de-initialize the disk and can instead call [`fs_unmount()`](../../file_system/index.md#c.fs_unmount "fs_unmount")

## SD Card support

Zephyr has support for some SD card controllers and support for interfacing
SD cards via SPI. These drivers use disk driver interface and a file system
can access the SD cards via disk access API.
Both standard and high-capacity SD cards are supported.

Note

FAT filesystems are not power safe so the filesystem may become
corrupted if power is lost or if the card is removed without unmounting
the filesystem

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

*group* Disk Access Interface
:   Disk Access APIs.

    Functions

    int disk\_access\_init(const char \*pdrv)
    :   perform any initialization

        This call is made by the consumer before doing any IO calls so that the disk or the backing device can do any initialization. Although still supported for legacy compatibility, users should instead call [disk\_access\_ioctl](#group__disk__access__interface_1ga152d85821d73644fea7ffde27b7c953c) with the IOCTL [DISK\_IOCTL\_CTRL\_INIT](#group__disk__driver__interface_1ga9def34b23915a3ce6c9a8a746d3d1372).

        Disk initialization is reference counted, so only the first successful call to initialize a uninitialized (or previously de-initialized) disk will actually initialize the disk

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

*group* Disk Driver Interface
:   Disk Driver Interface.

    **Since**
    :   1.6

    **Version**
    :   1.0.0

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

    DISK\_IOCTL\_CTRL\_INIT
    :   Initialize the disk.

        This IOCTL must be issued before the disk can be used for I/O. It is reference counted, so only the first successful invocation of this macro on an uninitialized disk will initialize the IO device

    DISK\_IOCTL\_CTRL\_DEINIT
    :   Deinitialize the disk.

        This IOCTL can be used to de-initialize the disk, enabling it to be removed from the system if the disk is hot-pluggable. Disk usage is reference counted, so for a given disk the `[DISK_IOCTL_CTRL_DEINIT](#group__disk__driver__interface_1gaf13b377592baace863070fee450bd5be)` IOCTL must be issued as many times as the `[DISK_IOCTL_CTRL_INIT](#group__disk__driver__interface_1ga9def34b23915a3ce6c9a8a746d3d1372)` IOCTL was issued in order to de-initialize it.

        This macro optionally accepts a pointer to a boolean as the `buf` parameter, which if true indicates the disk should be forcibly stopped, ignoring all reference counts. The disk driver must report success if a forced stop is requested, but this operation is inherently unsafe.

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

        const char \*name
        :   Disk name.

        const struct [disk\_operations](#c.disk_operations) \*ops
        :   Disk operations.

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev
        :   Device associated to this disk.

        uint16\_t refcnt
        :   Internally used disk reference count.

    struct disk\_operations
    :   *#include <disk.h>*

        Disk operations.
