---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/mtd/nordic,owned-partitions.html
original_path: build/dts/api/bindings/mtd/nordic,owned-partitions.html
---

# nordic,owned-partitions

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic Owned Partitions

Memory partition table with permission attributes common to its partitions.
This is a special case of the Nordic Owned Memory binding.

Every compatible node is expected to be a child of a memory node, where the
listed partitions belong.

A single memory node can contain multiple partition tables, each with a
different set of permissions. For each such table, the smallest memory region
spanning the contained partitions will be recorded in the UICR. These regions
are allowed to contain gaps between the partitions, but this is discouraged.

Example:

  mram1x: mram@e000000 {
      compatible = "nordic,mram";
      reg = <0xe000000 0x200000>;
      ...

      rx-partitions {
          compatible = "nordic,owned-partitions";
          nordic,access = <NRF_OWNER_ID_APPLICATION NRF_PERM_RX>;
          #address-cells = <1>;
          #size-cells = <1>;

          slot0_partition: partition@c0000 {
              label = "image-0";
              reg = <0xc0000 0x40000>;
          };
      };

      rw-partitions {
          compatible = "nordic,owned-partitions";
          nordic,access = <NRF_OWNER_ID_APPLICATION NRF_PERM_RW>;
          #address-cells = <1>;
          #size-cells = <1>;

          slot1_partition: partition@100000 {
              label = "image-1";
              reg = <0x100000 0x50000>;
          };
          storage_partition: partition@150000 {
              label = "storage";
              reg = <0x150000 0x6000>;
          };
      };
  };

From this example, two memory regions will be inferred:

  - 0x0E0C0000--0x0E100000, with read & execute permissions, containing the
    partition labeled "image-0".
  - 0x0E100000--0x0E156000, with read & write permissions, containing the
    partitions labeled "image-1" and "storage".
```

## Properties

### Top level properties

These property descriptions apply to “nordic,owned-partitions”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nordic,access` | `array` | ```text Array of (owner-id, permission-flags) pairs, where:  - Owner ID represents the domain that will have access to this memory.   Valid values can be found in dts/common/nordic/<soc>.dtsi,   where they are defined as NRF_OWNER_ID_*  - Permissions are encoded as a 32-bit bitfield, using the flags found in   include/zephyr/dt-bindings/reserved-memory/nordic-owned-memory.h,   where they are defined as NRF_PERM_*    The same file defines all possible permission flag combinations.   For example, one can use:     <NRF_OWNER_ID_APPLICATION NRF_PERM_RWX>    as a shorthand for:     <NRF_OWNER_ID_APPLICATION (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X)> ``` |
| `zephyr,memory-region` | `string` | ```text Signify that this node should result in a dedicated linker script memory region in the final executable. The region address and size is taken from the <reg> property, while the name is the value of this property. ``` |
| `zephyr,memory-attr` | `int` | ```text Attribute or set of attributes (bitmask) for the memory region. See 'include/zephyr/dt-bindings/memory-attr/memory-attr.h' for a comprehensive list with description of possible values. ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `owner-id` | `int` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner ID of the domain that will own this memory region. If not defined, the ownership will default to the domain being compiled.  Note: owner ID is not the same as domain ID; see the product specification for details. ``` |
| `perm-read` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner has read access to the region. ``` |
| `perm-write` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner has write access to the region. ``` |
| `perm-execute` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner can execute code from the region. ``` |
| `perm-secure` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner has secure-only access to the region. ``` |
| `non-secure-callable` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Memory region is used for non-secure-callable code. ``` |
| `zephyr,memory-region-mpu` | `string` | ```text Signify that this node should result in a dedicated MPU region. Deprecated in favor of 'zephyr,memory-attr'. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,owned-partitions” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**. |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
