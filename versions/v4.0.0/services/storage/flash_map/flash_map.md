---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/storage/flash_map/flash_map.html
original_path: services/storage/flash_map/flash_map.html
---

# Flash map

The `<zephyr/storage/flash_map.h>` API allows accessing information about device
flash partitions via [`flash_area`](../../../doxygen/html/structflash__area.md) structures.

Each [`flash_area`](../../../doxygen/html/structflash__area.md) describes a flash partition. The API provides access
to a “flash map”, which contains predefined flash areas accessible via globally
unique ID numbers. The map is created from “fixed-partition” compatible entries
in DTS file. Users may also create [`flash_area`](../../../doxygen/html/structflash__area.md) objects at runtime
for application-specific purposes.

This documentation uses “flash area” when referencing single “fixed-partition”
entities.

The [`flash_area`](../../../doxygen/html/structflash__area.md) contains a pointer to a [`device`](../../../doxygen/html/structdevice.md),
which can be used to access the flash device an area is placed on directly
with the [flash API](../../../hardware/peripherals/flash.md#flash-api).
Each flash area is characterized by a device it is placed on, offset
from the beginning of the device and size on the device.
An additional identifier parameter is used by the [`flash_area_open()`](../../../doxygen/html/group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7)
function to find flash area in flash map.

The flash\_map.h API provides functions for operating on a [`flash_area`](../../../doxygen/html/structflash__area.md).
The main examples are [`flash_area_read()`](../../../doxygen/html/group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127) and [`flash_area_write()`](../../../doxygen/html/group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8).
These functions are basically wrappers around the flash API with additional
offset and size checks, to limit flash operations to a predefined area.

Most `<zephyr/storage/flash_map.h>` API functions require a [`flash_area`](../../../doxygen/html/structflash__area.md) object pointer
characterizing the flash area they will be working on. There are two possible
methods to obtain such a pointer:

> - obtain it using [`flash_area_open()`](../../../doxygen/html/group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7);
> - defining a [`flash_area`](../../../doxygen/html/structflash__area.md) type object, which requires providing
>   a valid [`device`](../../../doxygen/html/structdevice.md) object pointer with offset and size of the area
>   within the flash device.

[`flash_area_open()`](../../../doxygen/html/group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7) uses numeric identifiers to search flash map for
[`flash_area`](../../../doxygen/html/structflash__area.md) objects and returns, if found, a pointer to an object
representing area with given ID.
The ID number for a flash area can be obtained from a fixed-partition
DTS node label using [`FIXED_PARTITION_ID()`](../../../doxygen/html/group__flash__area__api.md#ga60d5298007e2ee261b915a110389e76a); these labels are obtained
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
[`FIXED_PARTITION_ID()`](../../../doxygen/html/group__flash__area__api.md#ga60d5298007e2ee261b915a110389e76a); for example to obtain ID number
for `slot0_partition`, user would invoke `FIXED_PARTITION_ID(slot0_partition)`.

All `FIXED_PARTITION_*` macros take DTS node labels as partition
identifiers.

Users do not have to obtain a [`flash_area`](../../../doxygen/html/structflash__area.md) object pointer
using `flash_map_open()` to get information on flash area size, offset
or device, if such area is defined in DTS file. Knowing the DTS node label
of an area, users may use [`FIXED_PARTITION_OFFSET()`](../../../doxygen/html/group__flash__area__api.md#ga9229bc06458c19baf093ced063a9494b),
[`FIXED_PARTITION_SIZE()`](../../../doxygen/html/group__flash__area__api.md#ga2dbc50d9f80d7f7c597c75cbd536cd50) or [`FIXED_PARTITION_DEVICE()`](../../../doxygen/html/group__flash__area__api.md#ga3c92b6797feb183da38b8b57e77f2d17)
respectively to obtain such information directly from DTS node definition.
For example to obtain offset of `storage_partition` it is enough to
invoke `FIXED_PARTITION_OFFSET(storage_partition)`.

Below example shows how to obtain a [`flash_area`](../../../doxygen/html/structflash__area.md) object pointer
using [`flash_area_open()`](../../../doxygen/html/group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7) and DTS node label:

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

[flash area Interface](../../../doxygen/html/group__flash__area__api.md)

Related code samples

- [LittleFS filesystem](../../../samples/subsys/fs/littlefs/README.md#littlefs "Use file system API over LittleFS.")Use file system API over LittleFS.
- [nRF SoC Internal Storage](../../../samples/drivers/soc_flash_nrf/README.md#soc-flash-nrf "Use the flash API to interact with the SoC flash.")Use the flash API to interact with the SoC flash.
