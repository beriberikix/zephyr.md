---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/mtd/nordic,owned-partitions.html
original_path: build/dts/api/bindings/mtd/nordic,owned-partitions.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
          perm-read;
          perm-execute;
          #address-cells = <1>;
          #size-cells = <1>;

          slot0_partition: partition@c0000 {
              label = "image-0";
              reg = <0xc0000 0x40000>;
          };
      };

      rw-partitions {
          compatible = "nordic,owned-partitions";
          perm-read;
          perm-write;
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
| `owner-id` | `int` | ```text Owner ID of the domain that will own this memory region. If not defined, the ownership will default to the domain being compiled.  Note: owner ID is not the same as domain ID; see the product specification for details. ``` |
| `perm-read` | `boolean` | ```text Owner has read access to the region. ``` |
| `perm-write` | `boolean` | ```text Owner has write access to the region. ``` |
| `perm-execute` | `boolean` | ```text Owner can execute code from the region. ``` |
| `perm-secure` | `boolean` | ```text Owner has secure-only access to the region. ``` |
| `non-secure-callable` | `boolean` | ```text Memory region is used for non-secure-callable code. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,owned-partitions” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**. |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
