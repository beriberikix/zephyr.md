---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/mtd/atmel,sam-flash.html
original_path: build/dts/api/bindings/mtd/atmel,sam-flash.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# atmel,sam-flash

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

## Description

```text
This binding describes the Atmel SAM flash area layout.

The Atmel SAM flash area varies in write-block-size, memory area,
and the layout of erase-blocks.

E.g. the flash area layout of the ATSAM4E16C:

  |--------------------|
  | 8 Kbytes           |  erase block size = 2048
  |--------------------|
  | 8 Kbytes           |  erase block size = 2048
  |--------------------|
  | 48 Kbytes          |  erase block size = 4096
  |--------------------|
  | 64 Kbytes          |  erase block size = 4096
  |--------------------|
  | ...                |

The ATSAM4E16C has a flash area which is 1000Kbytes
(1024 * 1024 bytes) with a write-block-size of 8 bytes. The first
16 Kbytes can be erased in blocks of 2048 bytes
(8 blocks of 2048 bytes), the remaining flash area is erasable
in blocks of 4096 bytes (252 blocks of 4096 bytes).

This flash area layout would described as:

  / {
    soc {
      eefc: flash-controller@400e0a00 {
      compatible = "atmel,sam-flash-controller";
      reg = <0x400e0a00 0x200>;
      clocks = <&pmc PMC_TYPE_PERIPHERAL 6>;
      status = "okay";

      #address-cells = <1>;
      #size-cells = <1>;
      #erase-block-cells = <2>;

      flash0: flash@400000 {
        compatible = "atmel,sam-flash", "soc-nv-flash";
        reg = <0x400000 0x100000>;
        write-block-size = <8>;
        erase-block-size = <4096>;
        erase-blocks = <&eefc 8 2048>, <&eefc 252 4096>;
      };
    };
  };

Notes:
  The flash area layout node flash0 should have both this
  compatible, "atmel,sam-flash", and the "soc-nv-flash"
  compatible. The latter is used from mcuboot and other
  modules to identify the flash area.

  If partitions are used, remember that their addresses are
  offsets relative to the flash area address.  E.g. using
  mcuboot and a allocating a storage partition:

    &flash0 {
      partitions {
        compatible = "fixed-partitions";
        #address-cells = <1>;
        #size-cells = <1>;

        boot_partition: partition@0 {
          label = "mcuboot";
          reg = <0x0 0x10000>;
        };

        slot0_partition: partition@10000 {
          label = "slot0";
          reg = <0x10000 0x70000>;
        };

        slot1_partition: partition@80000 {
          label = "slot1";
          reg = <0x80000 0x70000>;
        };

        storage_partition: partition@f0000 {
          label = "storage";
          reg = <0xf0000 0x100000>;
        };
      };
    };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `write-block-size` | `int` | ```text The flash controller is limited by hardware to writing blocks of this size, aligned to this size, in bytes, to previously erased flash, within the flash memory area. ``` |
| `erase-block-size` | `int` | ```text The flash controller is limited by hardware to erase whole blocks of flash at a time. This property describes the largest erase block size in erase-blocks. ``` |
| `erase-blocks` | `phandle-array` | ```text The flash controller is limited by hardware to erase whole blocks of flash at a time. This property describes the layout of the erase-blocks, which can vary in size within the flash memory area. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel,sam-flash” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
