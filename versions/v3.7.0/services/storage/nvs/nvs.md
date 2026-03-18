---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/storage/nvs/nvs.html
original_path: services/storage/nvs/nvs.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Non-Volatile Storage (NVS)

Elements, represented as id-data pairs, are stored in flash using a
FIFO-managed circular buffer. The flash area is divided into sectors. Elements
are appended to a sector until storage space in the sector is exhausted. Then a
new sector in the flash area is prepared for use (erased). Before erasing the
sector it is checked that identifier - data pairs exist in the sectors in use,
if not the id-data pair is copied.

The id is a 16-bit unsigned number. NVS ensures that for each used id there is
at least one id-data pair stored in flash at all time.

NVS allows storage of binary blobs, strings, integers, longs, and any
combination of these.

Each element is stored in flash as metadata (8 byte) and data. The metadata is
written in a table starting from the end of a nvs sector, the data is
written one after the other from the start of the sector. The metadata consists
of: id, data offset in sector, data length, part (unused), and a CRC. This CRC is
only calculated over the metadata and only ensures that a write has been
completed. The actual data of the element can be protected by a different (and optional)
CRC-32. Use the [`CONFIG_NVS_DATA_CRC`](../../../kconfig.md#CONFIG_NVS_DATA_CRC "CONFIG_NVS_DATA_CRC") configuration item to enable
the data part CRC.

Note

The data CRC is checked only when the whole data of the element is read.
The data CRC is not checked for a partial read, as it is stored at the end of the
element data area.

Note

Enabling the data CRC feature on a previously existing NVS content without
data CRC will make all existing data invalid.

A write of data to nvs always starts with writing the data, followed by a write
of the metadata. Data that is written in flash without metadata is ignored
during initialization.

During initialization NVS will verify the data stored in flash, if it
encounters an error it will ignore any data with missing/incorrect metadata.

NVS checks the id-data pair before writing data to flash. If the id-data pair
is unchanged no write to flash is performed.

To protect the flash area against frequent erases it is important that there is
sufficient free space. NVS has a protection mechanism to avoid getting in a
endless loop of flash page erases when there is limited free space. When such
a loop is detected NVS returns that there is no more space available.

For NVS the file system is declared as:

```c
static struct nvs_fs fs = {
.flash_device = NVS_FLASH_DEVICE,
.sector_size = NVS_SECTOR_SIZE,
.sector_count = NVS_SECTOR_COUNT,
.offset = NVS_STORAGE_OFFSET,
};
```

where

- `NVS_FLASH_DEVICE` is a reference to the flash device that will be used. The
  device needs to be operational.
- `NVS_SECTOR_SIZE` is the sector size, it has to be a multiple of
  the flash erase page size and a power of 2.
- `NVS_SECTOR_COUNT` is the number of sectors, it is at least 2, one
  sector is always kept empty to allow copying of existing data.
- `NVS_STORAGE_OFFSET` is the offset of the storage area in flash.

## Flash wear

When writing data to flash a study of the flash wear is important. Flash has a
limited life which is determined by the number of times flash can be erased.
Flash is erased one page at a time and the pagesize is determined by the
hardware. As an example a nRF51822 device has a pagesize of 1024 bytes and each
page can be erased about 20,000 times.

### Calculating expected device lifetime

Suppose we use a 4 bytes state variable that is changed every minute and
needs to be restored after reboot. NVS has been defined with a sector\_size
equal to the pagesize (1024 bytes) and 2 sectors have been defined.

Each write of the state variable requires 12 bytes of flash storage: 8 bytes
for the metadata and 4 bytes for the data. When storing the data the
first sector will be full after 1024/12 = 85.33 minutes. After another 85.33
minutes, the second sector is full. When this happens, because we’re using
only two sectors, the first sector will be used for storage and will be erased
after 171 minutes of system time. With the expected device life of 20,000
writes, with two sectors writing every 171 minutes, the device should last
about 171 \* 20,000 minutes, or about 6.5 years.

More generally then, with

- `NS` as the number of storage requests per minute,
- `DS` as the data size in bytes,
- `SECTOR_SIZE` in bytes, and
- `PAGE_ERASES` as the number of times the page can be erased,

the expected device life (in minutes) can be calculated as:

```text
SECTOR_COUNT * SECTOR_SIZE * PAGE_ERASES / (NS * (DS+8)) minutes
```

From this formula it is also clear what to do in case the expected life is too
short: increase `SECTOR_COUNT` or `SECTOR_SIZE`.

## Flash write block size migration

It is possible that during a DFU process, the flash driver used by the NVS
changes the supported minimal write block size.
The NVS in-flash image will stay compatible unless the
physical ATE size changes.
Especially, migration between 1,2,4,8-bytes write block sizes is allowed.

## Sample

A sample of how NVS can be used is supplied in `samples/subsys/nvs`.

## Troubleshooting

MPU fault while using NVS, or `-ETIMEDOUT` error returned
:   NVS can use the internal flash of the SoC. While the MPU is enabled,
    the flash driver requires MPU RWX access to flash memory, configured
    using [`CONFIG_MPU_ALLOW_FLASH_WRITE`](../../../kconfig.md#CONFIG_MPU_ALLOW_FLASH_WRITE "CONFIG_MPU_ALLOW_FLASH_WRITE"). If this option is
    disabled, the NVS application will get an MPU fault if it references
    the internal SoC flash and it’s the only thread running. In a
    multi-threaded application, another thread might intercept the fault
    and the NVS API will return an `-ETIMEDOUT` error.

## API Reference

The NVS subsystem APIs are provided by `nvs.h`:

*group* Non-volatile Storage Data Structures
:   Non-volatile Storage Data Structures.

    struct nvs\_fs
    :   *#include <nvs.h>*

        Non-volatile Storage File system structure.

        Public Members

        off\_t offset
        :   File system offset in flash.

        uint32\_t ate\_wra
        :   Allocation table entry write address.

            Addresses are stored as uint32\_t:

            - high 2 bytes correspond to the sector
            - low 2 bytes are the offset in the sector

        uint32\_t data\_wra
        :   Data write address.

        uint16\_t sector\_size
        :   File system is split into sectors, each sector must be multiple of erase-block-size.

        uint16\_t sector\_count
        :   Number of sectors in the file system.

        bool ready
        :   Flag indicating if the file system is initialized.

        struct [k\_mutex](../../../kernel/services/synchronization/mutexes.md#c.k_mutex "k_mutex") nvs\_lock
        :   Mutex.

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*flash\_device
        :   Flash device runtime structure.

        const struct [flash\_parameters](#c.nvs_fs.flash_parameters) \*flash\_parameters
        :   Flash memory parameters structure.

Related code samples

[Non-Volatile Storage (NVS)](../../../samples/subsys/nvs/README.md#nvs "Store and retrieve data from flash using the NVS API.")
:   Store and retrieve data from flash using the NVS API.

*group* Non-volatile Storage APIs
:   Non-volatile Storage APIs.

    Functions

    int nvs\_mount(struct [nvs\_fs](#c.nvs_fs) \*fs)
    :   Mount an NVS file system onto the flash device specified in `fs`.

        Parameters:
        :   - **fs** – Pointer to file system

        Return values:
        :   - **0** – Success
            - **-ERRNO** – errno code if error

    int nvs\_clear(struct [nvs\_fs](#c.nvs_fs) \*fs)
    :   Clear the NVS file system from flash.

        Parameters:
        :   - **fs** – Pointer to file system

        Return values:
        :   - **0** – Success
            - **-ERRNO** – errno code if error

    ssize\_t nvs\_write(struct [nvs\_fs](#c.nvs_fs) \*fs, uint16\_t id, const void \*data, size\_t len)
    :   Write an entry to the file system.

        Note

        When `len` parameter is equal to `0` then entry is effectively removed (it is equivalent to calling of nvs\_delete). Any calls to nvs\_read for entries with data of length `0`

        will return error.

        It is not possible to distinguish between deleted entry and entry with data of length 0.

        Parameters:
        :   - **fs** – Pointer to file system
            - **id** – Id of the entry to be written
            - **data** – Pointer to the data to be written
            - **len** – Number of bytes to be written

        Returns:
        :   Number of bytes written. On success, it will be equal to the number of bytes requested to be written. When a rewrite of the same data already stored is attempted, nothing is written to flash, thus 0 is returned. On error, returns negative value of errno.h defined error codes.

    int nvs\_delete(struct [nvs\_fs](#c.nvs_fs) \*fs, uint16\_t id)
    :   Delete an entry from the file system.

        Parameters:
        :   - **fs** – Pointer to file system
            - **id** – Id of the entry to be deleted

        Return values:
        :   - **0** – Success
            - **-ERRNO** – errno code if error

    ssize\_t nvs\_read(struct [nvs\_fs](#c.nvs_fs) \*fs, uint16\_t id, void \*data, size\_t len)
    :   Read an entry from the file system.

        Parameters:
        :   - **fs** – Pointer to file system
            - **id** – Id of the entry to be read
            - **data** – Pointer to data buffer
            - **len** – Number of bytes to be read

        Returns:
        :   Number of bytes read. On success, it will be equal to the number of bytes requested to be read. When the return value is larger than the number of bytes requested to read this indicates not all bytes were read, and more data is available. On error, returns negative value of errno.h defined error codes.

    ssize\_t nvs\_read\_hist(struct [nvs\_fs](#c.nvs_fs) \*fs, uint16\_t id, void \*data, size\_t len, uint16\_t cnt)
    :   Read a history entry from the file system.

        Parameters:
        :   - **fs** – Pointer to file system
            - **id** – Id of the entry to be read
            - **data** – Pointer to data buffer
            - **len** – Number of bytes to be read
            - **cnt** – History counter: 0: latest entry, 1: one before latest …

        Returns:
        :   Number of bytes read. On success, it will be equal to the number of bytes requested to be read. When the return value is larger than the number of bytes requested to read this indicates not all bytes were read, and more data is available. On error, returns negative value of errno.h defined error codes.

    ssize\_t nvs\_calc\_free\_space(struct [nvs\_fs](#c.nvs_fs) \*fs)
    :   Calculate the available free space in the file system.

        Parameters:
        :   - **fs** – Pointer to file system

        Returns:
        :   Number of bytes free. On success, it will be equal to the number of bytes that can still be written to the file system. Calculating the free space is a time consuming operation, especially on spi flash. On error, returns negative value of errno.h defined error codes.
