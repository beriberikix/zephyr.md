---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/retention/zephyr,retention.html
original_path: build/dts/api/bindings/retention/zephyr,retention.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# zephyr,retention

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
Retention subsystem area, which has a retained memory parent. Example
64-byte area with 2-byte prefix and 1-byte checksum with 61 usable bytes
for user storage:

sram@2003FFC0 {
  compatible = "zephyr,memory-region", "mmio-sram";
  reg = <0x2003FFC0 64>;
  zephyr,memory-region = "RetainedMem";
  status = "okay";

  retainedmem {
    compatible = "zephyr,retained-ram";
    status = "okay";
    #address-cells = <1>;
    #size-cells = <1>;

    retention0: retention@0 {
      compatible = "zephyr,retention";
      status = "okay";
      reg = <0x0 0x40>;
      prefix = [04 fa];
      checksum = <1>;
    };
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `prefix` | `uint8-array` | ```text An optional magic prefix, which indicates that the data has been set (applies to the header of the data, reduces the available user data size). ``` |
| `checksum` | `int` | ```text An optional data verification checksum, which indicates that the data is valid (appended to the footer of the data, reduces the available user data size). Value is size in bytes (0 for none, 1 for 8-bit CRC, 2 for 16-bit CRC, 4 for 32-bit CRC). Default is to not use a checksum. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,retention” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text Address reg cell is for the offset of the area in parent node, can be increased if multiple retention partitions are used or parts are reserved. ```  Constant value: `1` |
| `#size-cells` | `int` | ```text Size reg cell is for the size of the area, which includes sizes of prefix and checksum (if enabled). ```  Constant value: `1` |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
