---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/fs/zephyr,fstab,littlefs.html
original_path: build/dts/api/bindings/fs/zephyr,fstab,littlefs.html
---

# zephyr,fstab,littlefs

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[subsys/fs/littlefs\_fs.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/littlefs_fs.c).

## Description

```text
Description of pre-defined file systems.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `read-size` | `int` | ```text The size of file system read operations, in bytes.  All read operations will be a multiple of this value.  A reasonable default is 16.  This corresponds to CONFIG_FS_LITTLEFS_READ_SIZE. ```  This property is **required**. |
| `prog-size` | `int` | ```text The size of file system program (write) operations, in bytes.  All program operations will be a multiple of this value.  A reasonable default is 16.  This corresponds to CONFIG_FS_LITTLEFS_PROG_SIZE. ```  This property is **required**. |
| `cache-size` | `int` | ```text The size of block caches, in bytes.  Each cache buffers a portion of a block in RAM.  The littlefs needs a read cache, a program cache, and one additional cache per file. Larger caches can improve performance by storing more data and reducing the number of disk accesses. Must be a multiple of the read and program sizes of the underlying flash device, and a factor of the block size.  A reasonable default is 64.  This corresponds to CONFIG_FS_LITTLEFS_CACHE_SIZE. ```  This property is **required**. |
| `lookahead-size` | `int` | ```text The size of the lookahead buffer, in bytes.  A larger lookahead buffer increases the number of blocks found during an allocation pass. The lookahead buffer is stored as a compact bitmap, so each byte of RAM can track 8 blocks. Must be a multiple of 8.  A reasonable default is 32.  This corresponds to CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE. ```  This property is **required**. |
| `block-cycles` | `int` | ```text The number of erase cycles before moving data to another block.  For dynamic wear leveling, the number of erase cycles before data is moved to another block.  Set to a non-positive value to disable leveling.  This corresponds to CONFIG_FS_LITTLEFS_BLOCK_CYCLES. ```  This property is **required**. |
| `disk-version` | `int` | ```text The littlefs disk version.  To maintain backward compatibility with existing littlefs with the same major disk version.  The default version is LFS_DISK_VERSION. ``` |
| `mount-point` | `string` | ```text The absolute path used as the file system mount point. ```  This property is **required**. |
| `partition` | `phandle` | ```text A reference to the file system's partition. ```  This property is **required**. |
| `automount` | `boolean` | ```text Mount file system on boot if present.  During initialization the file system driver will attempt to mount this partition. ``` |
| `read-only` | `boolean` | ```text Mount file system read-only if present.  This adds the FS_MOUNT_FLAG_READ_ONLY option to be set in the mount descriptor generated for the file system. ``` |
| `no-format` | `boolean` | ```text Do not format file system if mount fails.  This causes the FS_MOUNT_FLAG_NO_FORMAT option to be set in the mount descriptor generated for the file system. ``` |
| `disk-access` | `boolean` | ```text Use disk-access for accessing storage media.  This causes the FS_MOUNT_FLAG_USE_DISK_ACCESS option to be set in the mount descriptor generated for the file system. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,fstab,littlefs” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
