---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/mtd/fixed-partitions.html
original_path: build/dts/api/bindings/mtd/fixed-partitions.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# fixed-partitions

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
This binding is used to describe fixed partitions of a flash (or
other nonvolatile storage) memory.

Here is an example:

  &flash0 {
          partitions {
                  compatible = "fixed-partitions";
                  #address-cells = <1>;
                  #size-cells = <1>;

                  boot_partition: partition@0 {
                          label = "mcuboot";
                          reg = <0x00000000 0x0000C000>;
                  };
                  slot0_partition: partition@c000 {
                          label = "image-0";
                          reg = <0x0000C000 0x00076000>;
                  };
                  slot1_partition: partition@82000 {
                          label = "image-1";
                          reg = <0x00082000 0x00076000>;
                  };

                  /*
                   * The flash starting at 0x000f8000 and ending at
                   * 0x000fffff is reserved for use by the application.
                   */

                  /*
                   * Storage partition will be used by FCB/LittleFS/NVS
                   * if enabled.
                   */
                  storage_partition: partition@f8000 {
                          label = "storage";
                          reg = <0x000f8000 0x00008000>;
                  };
          };
  };

Note that the usual name for this node is 'partitions'.
The fixed-partitions node should be a child of the flash
memory node. Note also that the flash memory node is usually
different from the node representing the flash controller
IP block.

Above, slot0_partition's register address 0xc000 means that
the partition begins at that offset from the parent flash
memory flash0's base address. That is, partition addresses
are relative; physical addresses must be calculated by adding
the start address of flash0 in memory to each partition's
reg address.
```

## Properties

### Top level properties

These property descriptions apply to “fixed-partitions”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “fixed-partitions” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text Number of cells required to represent a child node's reg property address. This must be large enough to represent the start offset of each partition. ``` |
| `#size-cells` | `int` | ```text Number of cells required to represent a child node's reg property address. This must be large enough to represent the size of each partition in bytes. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `label` | `string` | ```text Human readable string describing the flash partition. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `read-only` | `boolean` | ```text set this property if the partition is read-only ``` |
| `reg` | `array` | ```text This should be in the format <OFFSET SIZE>, where OFFSET is the offset of the flash partition relative to the base address of the parent memory, and SIZE is the size of the partition in bytes. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
