---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/mtd/fixed-subpartitions.html
original_path: build/dts/api/bindings/mtd/fixed-subpartitions.html
---

# fixed-subpartitions

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

## Description

```text
Fixed subpartitions of a flash (or other nonvolatile storage) memory.

Here is an example:

  &flash0 {
          partitions {
                  compatible = "fixed-partitions";
                  #address-cells = <1>;
                  #size-cells = <1>;

                  slot0_partition: partition@10000 {
                          compatible = "fixed-subpartitions";
                          label = "image-0";
                          reg = <0x00010000 0x70000>;
                          ranges = <0x0 0x10000 0x70000>;
                          #address-cells = <1>;
                          #size-cells = <1>;

                          slot0_s_partition: partition@0 {
                                  label = "image-0-secure";
                                  reg = <0x00000000 0x40000>;
                          };

                          slot0_ns_partition: partition@40000 {
                                  label = "image-0-nonsecure";
                                  reg = <0x00040000 0x30000>;
                          };
                  };
          };
  };
```

## Properties

### Top level properties

These property descriptions apply to “fixed-subpartitions”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `read-only` | `boolean` | ```text set this property if the partition is read-only ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “fixed-subpartitions” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `label` | `string` | ```text Human readable string describing the flash partition. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text This should be in the format <OFFSET SIZE>, where OFFSET is the offset of the flash partition relative to the base address of the parent memory, and SIZE is the size of the partition in bytes. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text Number of cells required to represent a child node's reg property address. This must be large enough to represent the start offset of each partition. ``` |
| `#size-cells` | `int` | ```text Number of cells required to represent a child node's reg property address. This must be large enough to represent the size of each partition in bytes. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `label` | `string` | ```text Human readable string describing the flash partition. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `read-only` | `boolean` | ```text set this property if the partition is read-only ``` |
| `reg` | `array` | ```text This should be in the format <OFFSET SIZE>, where OFFSET is the offset of the flash partition relative to the base address of the parent memory, and SIZE is the size of the partition in bytes. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
