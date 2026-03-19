---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/memory-controllers/renesas,ra-sdram.html
original_path: build/dts/api/bindings/memory-controllers/renesas,ra-sdram.html
---

# renesas,ra-sdram

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

Note

An implementation of a driver matching this compatible is available in
[drivers/memc/memc\_renesas\_ra\_sdram.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_renesas_ra_sdram.c).

## Description

```text
Renesas RA SDRAM controller.
sdram {
    pinctrl-0 = <&sdram_default>;
    pinctrl-names = "default";
    status = "okay";
    auto-refresh-interval = <10>;
    auto-refresh-count = <8>;
    precharge-cycle-count = <3>;
    multiplex-addr-shift = "10-bit";
    edian-mode = "little-endian";
    continuous-access;
    bus-width = "16-bit";
    bank@0 {
      reg = <0>;
      renesas,ra-sdram-timing = <RENESAS_RA_SDRAM_TRAS_6CYCLES
                RENESAS_RA_SDRAM_TRCD_3CYCLES
                RENESAS_RA_SDRAM_TRP_3CYCLES
                RENESAS_RA_SDRAM_TWR_2CYCLES
                RENESAS_RA_SDRAM_TCL_3CYCLES
                937
                RENESAS_RA_SDRAM_TREFW_8CYCLES>;
    };

Note that you will find definitions for the renesas,ra-sdram-control field at
dt-bindings/memory-controller/renesas,ra-sdram.h. This file is already included
in the SoC DeviceTree files.

Finally, in order to make the memory available you will need to define new
memory device/s in DeviceTree:

sdram1: sdram@68000000 {
    compatible = "zephyr,memory-region", "mmio-sram";
    device_type = "memory";
    reg = <0x68000000 DT_SIZE_M(X)>;
    zephyr,memory-region = "SDRAM";
};
```

## Properties

### Top level properties

These property descriptions apply to “renesas,ra-sdram”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `auto-refresh-interval` | `int` | ```text Number of auto-refresh-interval. ```  Default value: `10` |
| `auto-refresh-count` | `int` | ```text Number of auto-refresh-count. ```  Default value: `8` |
| `precharge-cycle-count` | `int` | ```text Number of precharge-cycle-count. ```  Default value: `3` |
| `multiplex-addr-shift` | `string` | ```text Select the size of the shift towards the lower half of the row address in row address/column address multiplexing. ```  Default value: `10-bit`  Legal values: `'8-bit'`, `'9-bit'`, `'10-bit'`, `'11-bit'` |
| `edian-mode` | `string` | ```text Specifies the endianness for the SDRAM address space. ```  Default value: `little-endian`  Legal values: `'little-endian'`, `'big-endian'` |
| `continuous-access` | `boolean` | ```text Enables or disables continuous access to the SDRAM access space. ``` |
| `bus-width` | `string` | ```text Specify the data bus width for SDRAM ```  Default value: `16-bit`  Legal values: `'16-bit'`, `'32-bit'`, `'8-bit'` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “renesas,ra-sdram” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ```  This property is **required**. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `int` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `renesas,ra-sdram-timing` | `array` | ```text SDRAM timing configuration. Expected fields, in order, are,  - TRAS: Row active interval. The effective value from 1 to 7 cycles - TRCD: Row column latency. The effective value from 1 to 4 cycles - TRP: Row precharge interval. The effective value from 1 to 8 cycles - TWR: Write recovery interval. The effective value from 1 to 2 cycles - TCL: Column latency. The effective value from 1 to 3 cycles - TRFC: Auto-Refresh Request Interval Setting. - TREFW: Auto-Refresh Cycle/Self-Refresh Clearing Cycle Count Setting.   The effective value from 1 to 16 cycles ```  This property is **required**. |
