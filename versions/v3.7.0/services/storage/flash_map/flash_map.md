---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/storage/flash_map/flash_map.html
original_path: services/storage/flash_map/flash_map.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Flash map

The `<zephyr/storage/flash_map.h>` API allows accessing information about device
flash partitions via [`flash_area`](#c.flash_area) structures.

Each [`flash_area`](#c.flash_area) describes a flash partition. The API provides access
to a “flash map”, which contains predefined flash areas accessible via globally
unique ID numbers. The map is created from “fixed-partition” compatible entries
in DTS file. Users may also create [`flash_area`](#c.flash_area) objects at runtime
for application-specific purposes.

This documentation uses “flash area” when referencing single “fixed-partition”
entities.

The [`flash_area`](#c.flash_area) contains a pointer to a [`device`](../../../kernel/drivers/index.md#c.device "device"),
which can be used to access the flash device an area is placed on directly
with the [flash API](../../../hardware/peripherals/flash.md#flash-api).
Each flash area is characterized by a device it is placed on, offset
from the beginning of the device and size on the device.
An additional identifier parameter is used by the [`flash_area_open()`](#c.flash_area_open)
function to find flash area in flash map.

The flash\_map.h API provides functions for operating on a [`flash_area`](#c.flash_area).
The main examples are [`flash_area_read()`](#c.flash_area_read) and [`flash_area_write()`](#c.flash_area_write).
These functions are basically wrappers around the flash API with additional
offset and size checks, to limit flash operations to a predefined area.

Most `<zephyr/storage/flash_map.h>` API functions require a [`flash_area`](#c.flash_area) object pointer
characterizing the flash area they will be working on. There are two possible
methods to obtain such a pointer:

> - obtain it using flash\_area\_open;
> - defining a [`flash_area`](#c.flash_area) type object, which requires providing
>   a valid [`device`](../../../kernel/drivers/index.md#c.device "device") object pointer with offset and size of the area
>   within the flash device.

[`flash_area_open()`](#c.flash_area_open) uses numeric identifiers to search flash map for
[`flash_area`](#c.flash_area) objects and returns, if found, a pointer to an object
representing area with given ID.
The ID number for a flash area can be obtained from a fixed-partition
DTS node label using [`FIXED_PARTITION_ID()`](#c.FIXED_PARTITION_ID); these labels are obtained
from the devicetree as described below.

## Relationship with Devicetree

The flash\_map.h API uses data generated from the [Devicetree API](../../../build/dts/api/api.md#devicetree-api), in
particular its [Fixed flash partitions](../../../build/dts/api/api.md#devicetree-flash-api). Zephyr additionally has some
partitioning conventions used for [Device Firmware Upgrade](../../device_mgmt/dfu.md#dfu) via the MCUboot bootloader, as
well as defining partitions usable by [file systems](../../file_system/index.md#file-system-api) or
other nonvolatile [storage](../index.md#storage-reference).

Here is an example devicetree fragment which uses fixed flash partitions for
both MCUboot and a storage partition. Some details were left out for clarity.

```dts
/ {
	soc {
		flashctrl: flash-controller@deadbeef {
			flash0: flash@0 {
				compatible = "soc-nv-flash";
				reg = <0x0 0x100000>;

				partitions {
					compatible = "fixed-partitions";
					#address-cells = <0x1>;
					#size-cells = <0x1>;

					boot_partition: partition@0 {
						reg = <0x0 0x10000>;
						read-only;
					};
					storage_partition: partition@1e000 {
						reg = <0x1e000 0x2000>;
					};
					slot0_partition: partition@20000 {
						reg = <0x20000 0x60000>;
					};
					slot1_partition: partition@80000 {
						reg = <0x80000 0x60000>;
					};
					scratch_partition: partition@e0000 {
						reg = <0xe0000 0x20000>;
					};
				};
			};
		};
	};
};
```

Partition offset shall be expressed in relation to the flash memory beginning
address, to which the partition belongs to.

The `boot_partition`, `slot0_partition`, `slot1_partition`, and
`scratch_partition` node labels are defined for MCUboot, though not all MCUboot
configurations require all of them to be defined. See the [MCUboot
documentation](https://docs.mcuboot.com) for more details.

The `storage_partition` node is defined for use by a file system or other
nonvolatile storage API.

Numeric flash area ID is obtained by passing DTS node label to
[`FIXED_PARTITION_ID()`](#c.FIXED_PARTITION_ID); for example to obtain ID number
for `slot0_partition`, user would invoke `FIXED_PARTITION_ID(slot0_partition)`.

All `FIXED_PARTITION_` macros take DTS node labels as partition
identifiers.

Users do not have to obtain a [`flash_area`](#c.flash_area) object pointer
using `flash_map_open()` to get information on flash area size, offset
or device, if such area is defined in DTS file. Knowing the DTS node label
of an area, users may use [`FIXED_PARTITION_OFFSET()`](#c.FIXED_PARTITION_OFFSET),
[`FIXED_PARTITION_SIZE()`](#c.FIXED_PARTITION_SIZE) or [`FIXED_PARTITION_DEVICE()`](#c.FIXED_PARTITION_DEVICE)
respectively to obtain such information directly from DTS node definition.
For example to obtain offset of `storage_partition` it is enough to
invoke `FIXED_PARTITION_OFFSET(storage_partition)`.

Below example shows how to obtain a [`flash_area`](#c.flash_area) object pointer
using [`flash_area_open()`](#c.flash_area_open) and DTS node label:

```c
const struct flash_area *my_area;
int err = flash_area_open(FIXED_PARTITION_ID(slot0_partition), &my_area);

if (err != 0) {
     handle_the_error(err);
} else {
     flash_area_read(my_area, ...);
}
```

## API Reference

Related code samples

[LittleFS filesystem](../../../samples/subsys/fs/littlefs/README.md#littlefs "Use file system API over LittleFS.")
:   Use file system API over LittleFS.

[nRF SoC Internal Storage](../../../samples/drivers/soc_flash_nrf/README.md#soc-flash-nrf "Use the flash API to interact with the SoC flash.")
:   Use the flash API to interact with the SoC flash.

*group* flash area Interface
:   Abstraction over flash partitions/areas and their drivers.

    **Since**
    :   1.11

    **Version**
    :   1.0.0

    Defines

    SOC\_FLASH\_0\_ID
    :   Provided for compatibility with MCUboot.

    SPI\_FLASH\_0\_ID
    :   Provided for compatibility with MCUboot.

    FIXED\_PARTITION\_EXISTS(label)
    :   Returns non-0 value if fixed-partition of given DTS node label exists.

        Parameters:
        :   - **label** – DTS node label

        Returns:
        :   non-0 if fixed-partition node exists and is enabled; 0 if node does not exist, is not enabled or is not fixed-partition.

    FIXED\_PARTITION\_ID(label)
    :   Get flash area ID from fixed-partition DTS node label.

        Parameters:
        :   - **label** – DTS node label of a partition

        Returns:
        :   flash area ID

    FIXED\_PARTITION\_OFFSET(label)
    :   Get fixed-partition offset from DTS node label.

        Parameters:
        :   - **label** – DTS node label of a partition

        Returns:
        :   fixed-partition offset, as defined for the partition in DTS.

    FIXED\_PARTITION\_NODE\_OFFSET(node)
    :   Get fixed-partition offset from DTS node.

        Parameters:
        :   - **node** – DTS node of a partition

        Returns:
        :   fixed-partition offset, as defined for the partition in DTS.

    FIXED\_PARTITION\_SIZE(label)
    :   Get fixed-partition size for DTS node label.

        Parameters:
        :   - **label** – DTS node label

        Returns:
        :   fixed-partition offset, as defined for the partition in DTS.

    FIXED\_PARTITION\_NODE\_SIZE(node)
    :   Get fixed-partition size for DTS node.

        Parameters:
        :   - **node** – DTS node of a partition

        Returns:
        :   fixed-partition size, as defined for the partition in DTS.

    FLASH\_AREA\_DEVICE(label)
    :   Get device pointer for device the area/partition resides on.

        Parameters:
        :   - **label** – DTS node label of a partition

        Returns:
        :   const struct device type pointer

    FIXED\_PARTITION\_DEVICE(label)
    :   Get device pointer for device the area/partition resides on.

        Parameters:
        :   - **label** – DTS node label of a partition

        Returns:
        :   Pointer to a device.

    FIXED\_PARTITION\_NODE\_DEVICE(node)
    :   Get device pointer for device the area/partition resides on.

        Parameters:
        :   - **node** – DTS node of a partition

        Returns:
        :   Pointer to a device.

    Typedefs

    typedef void (\*flash\_area\_cb\_t)(const struct [flash\_area](#c.flash_area) \*fa, void \*user\_data)
    :   Flash map iteration callback.

        Param fa:
        :   flash area

        Param user\_data:
        :   User supplied data

    Functions

    int flash\_area\_open(uint8\_t id, const struct [flash\_area](#c.flash_area) \*\*fa)
    :   Retrieve partitions flash area from the flash\_map.

        Function Retrieves [flash\_area](#structflash__area) from flash\_map for given partition.

        Parameters:
        :   - **id** – **[in]** ID of the flash partition.
            - **fa** – **[out]** Pointer which has to reference [flash\_area](#structflash__area). If `ID` is unknown, it will be NULL on output.

        Returns:
        :   0 on success, -EACCES if the flash\_map is not available , -ENOENT if `ID` is unknown, -ENODEV if there is no driver attached to the area.

    void flash\_area\_close(const struct [flash\_area](#c.flash_area) \*fa)
    :   Close [flash\_area](#structflash__area).

        Reserved for future usage and external projects compatibility reason. Currently is NOP.

        Parameters:
        :   - **fa** – **[in]** Flash area to be closed.

    int flash\_area\_read(const struct [flash\_area](#c.flash_area) \*fa, off\_t off, void \*dst, size\_t len)
    :   Read flash area data.

        Read data from flash area. Area readout boundaries are asserted before read request. API has the same limitation regard read-block alignment and size as wrapped flash driver.

        Parameters:
        :   - **fa** – **[in]** Flash area
            - **off** – Offset relative from beginning of flash area to read
            - **dst** – **[out]** Buffer to store read data
            - **len** – **[in]** Number of bytes to read

        Returns:
        :   0 on success, negative errno code on fail.

    int flash\_area\_write(const struct [flash\_area](#c.flash_area) \*fa, off\_t off, const void \*src, size\_t len)
    :   Write data to flash area.

        Write data to flash area. Area write boundaries are asserted before write request. API has the same limitation regard write-block alignment and size as wrapped flash driver.

        Parameters:
        :   - **fa** – **[in]** Flash area
            - **off** – Offset relative from beginning of flash area to write
            - **src** – **[in]** Buffer with data to be written
            - **len** – **[in]** Number of bytes to write

        Returns:
        :   0 on success, negative errno code on fail.

    int flash\_area\_erase(const struct [flash\_area](#c.flash_area) \*fa, off\_t off, size\_t len)
    :   Erase flash area.

        Erase given flash area range. Area boundaries are asserted before erase request. API has the same limitation regard erase-block alignment and size as wrapped flash driver.

        Parameters:
        :   - **fa** – **[in]** Flash area
            - **off** – Offset relative from beginning of flash area.
            - **len** – **[in]** Number of bytes to be erase

        Returns:
        :   0 on success, negative errno code on fail.

    int flash\_area\_flatten(const struct [flash\_area](#c.flash_area) \*fa, off\_t off, size\_t len)
    :   Erase flash area or fill with erase-value.

        On program-erase devices this function behaves exactly like flash\_area\_erase. On RAM non-volatile device it will call erase, if driver provides such callback, or will fill given range with erase-value defined by driver. This function should be only used by code that has not been written to directly support devices that do not require erase and rely on device being erased prior to some operations. Note that emulated erase, on devices that do not require, is done via write, which affects endurance of device.

        See also

        [flash\_area\_erase()](#group__flash__area__api_1gacc5cbff19d23773115f3334f862814d2)

        See also

        [flash\_flatten()](../../../hardware/peripherals/flash.md#group__flash__interface_1ga11eda0cdc7be12636a90d2e8c7264e4a)

        Parameters:
        :   - **fa** – **[in]** Flash area
            - **off** – Offset relative from beginning of flash area.
            - **len** – **[in]** Number of bytes to be erase

        Returns:
        :   0 on success, negative errno code on fail.

    uint32\_t flash\_area\_align(const struct [flash\_area](#c.flash_area) \*fa)
    :   Get write block size of the flash area.

        Currently write block size might be treated as read block size, although most of drivers supports unaligned readout.

        Parameters:
        :   - **fa** – **[in]** Flash area

        Returns:
        :   Alignment restriction for flash writes in [B].

    int flash\_area\_get\_sectors(int fa\_id, uint32\_t \*count, struct [flash\_sector](#c.flash_sector) \*sectors)
    :   Retrieve info about sectors within the area.

        Parameters:
        :   - **fa\_id** – **[in]** Given flash area ID
            - **sectors** – **[out]** buffer for sectors data
            - **count** – **[inout]** On input Capacity of `sectors`, on output number of sectors Retrieved.

        Returns:
        :   0 on success, negative errno code on fail. Especially returns -ENOMEM if There are too many flash pages on the [flash\_area](#structflash__area) to fit in the array.

    void flash\_area\_foreach([flash\_area\_cb\_t](#c.flash_area_cb_t) user\_cb, void \*user\_data)
    :   Iterate over flash map.

        Parameters:
        :   - **user\_cb** – User callback
            - **user\_data** – User supplied data

    int flash\_area\_has\_driver(const struct [flash\_area](#c.flash_area) \*fa)
    :   Check whether given flash area has supporting flash driver in the system.

        Parameters:
        :   - **fa** – **[in]** Flash area.

        Returns:
        :   1 On success. -ENODEV if no driver match.

    const struct [device](../../../kernel/drivers/index.md#c.device "device") \*flash\_area\_get\_device(const struct [flash\_area](#c.flash_area) \*fa)
    :   Get driver for given flash area.

        Parameters:
        :   - **fa** – **[in]** Flash area.

        Returns:
        :   device driver.

    uint8\_t flash\_area\_erased\_val(const struct [flash\_area](#c.flash_area) \*fa)
    :   Get the value expected to be read when accessing any erased flash byte.

        This API is compatible with the MCUBoot’s porting layer.

        Parameters:
        :   - **fa** – Flash area.

        Returns:
        :   Byte value of erase memory.

    struct flash\_area
    :   *#include <flash\_map.h>*

        Flash partition.

        This structure represents a fixed-size partition on a flash device. Each partition contains one or more flash sectors.

        Public Members

        uint8\_t fa\_id
        :   ID number.

        off\_t fa\_off
        :   Start offset from the beginning of the flash device.

        size\_t fa\_size
        :   Total size.

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*fa\_dev
        :   Backing flash device.

    struct flash\_sector
    :   *#include <flash\_map.h>*

        Structure for transfer flash sector boundaries.

        This template is used for presentation of flash memory structure. It consumes much less RAM than [flash\_area](#structflash__area)

        Public Members

        off\_t fs\_off
        :   Sector offset from the beginning of the flash device.

        size\_t fs\_size
        :   Sector size in bytes.
