---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/fs/zephyr,fstab,littlefs.html
original_path: build/dts/api/bindings/fs/zephyr,fstab,littlefs.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# zephyr,fstab,littlefs

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
Description of pre-defined file systems.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `mount-point` | `string` | ```text The absolute path used as the file system mount point. ```  This property is **required**. |
| `partition` | `phandle` | ```text A reference to the file system's partition. ```  This property is **required**. |
| `automount` | `boolean` | ```text Mount file system on boot if present.  During initialization the file system driver will attempt to mount this partition. ``` |
| `read-only` | `boolean` | ```text Mount file system read-only if present.  This adds the FS_MOUNT_FLAG_READ_ONLY option to be set in the mount descriptor generated for the file system. ``` |
| `no-format` | `boolean` | ```text Do not format file system if mount fails.  This causes the FS_MOUNT_FLAG_NO_FORMAT option to be set in the mount descriptor generated for the file system. ``` |
| `disk-access` | `boolean` | ```text Use disk-access for accessing storage media.  This causes the FS_MOUNT_FLAG_USE_DISK_ACCESS option to be set in the mount descriptor generated for the file system. ``` |
| `read-size` | `int` | ```text The size of file system read operations, in bytes.  All read operations will be a multiple of this value.  A reasonable default is 16.  This corresponds to CONFIG_FS_LITTLEFS_READ_SIZE. ```  This property is **required**. |
| `prog-size` | `int` | ```text The size of file system program (write) operations, in bytes.  All program operations will be a multiple of this value.  A reasonable default is 16.  This corresponds to CONFIG_FS_LITTLEFS_PROG_SIZE. ```  This property is **required**. |
| `cache-size` | `int` | ```text The size of block caches, in bytes.  Each cache buffers a portion of a block in RAM.  The littlefs needs a read cache, a program cache, and one additional cache per file. Larger caches can improve performance by storing more data and reducing the number of disk accesses. Must be a multiple of the read and program sizes of the underlying flash device, and a factor of the block size.  A reasonable default is 64.  This corresponds to CONFIG_FS_LITTLEFS_CACHE_SIZE. ```  This property is **required**. |
| `lookahead-size` | `int` | ```text The size of the lookahead buffer, in bytes.  A larger lookahead buffer increases the number of blocks found during an allocation pass. The lookahead buffer is stored as a compact bitmap, so each byte of RAM can track 8 blocks. Must be a multiple of 8.  A reasonable default is 32.  This corresponds to CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE. ```  This property is **required**. |
| `block-cycles` | `int` | ```text The number of erase cycles before moving data to another block.  For dynamic wear leveling, the number of erase cycles before data is moved to another block.  Set to a non-positive value to disable leveling.  This corresponds to CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,fstab,littlefs” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
