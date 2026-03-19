---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/mtd/ti,cc23x0-ccfg-flash.html
original_path: build/dts/api/bindings/mtd/ti,cc23x0-ccfg-flash.html
---

# ti,cc23x0-ccfg-flash

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

## Description

```text
This binding describes the TI CC23X0 flash CCFG (custom configuration)
area content.

Notes:
  The flash CCFG sector node (e.g. flash1) should have both
  "ti,cc23x0-ccfg-flash" and the "soc-nv-flash" compatibles.
  The latter is used from mcuboot and other modules to identify
  the flash area.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `ti,bldr-vtor-flash` | `int` | ```text Bootloader entry point when a boot from flash is selected. Valid range: 0 - 0x0effffff Default is 0, which is the standard initial configuration. ``` |
| `ti,serial-io-cfg-index` | `int` | ```text Index of which I/O mapping to use for UART/SPI. Valid range: 0 - 2 Default is 0, which is the standard initial configuration. Other values can be used depending on I/O availability. ``` |
| `ti,pin-trigger` | `boolean` | ```text If not present, then bootloader unconditionally triggers. Else normal pin trigger check is performed. ``` |
| `ti,pin-trigger-dio` | `int` | ```text Index of DIO pin to use for pin trigger check. Valid range: 0 - 25 Default is 0, which is the standard initial configuration. Other values can be used depending on DIO availability. ``` |
| `ti,pin-trigger-level-hi` | `boolean` | ```text If not present, then the level on trigger pin that triggers bootloader is low. Else level that triggers bootloader is high. ``` |
| `ti,debug-port` | `boolean` | ```text If not present, then the SWD port is disabled altogether at a certain point in boot before invoking either bootloader or application. ``` |
| `ti,energy-trace` | `boolean` | ```text Allows using EnergyTrace power analyzer tool. EnergyTrace software is an energy-based code analysis tool that measures and displays the energy profile of an application and helps optimize it for ultra-low-power consumption. ``` |
| `ti,flash-verify` | `boolean` | ```text Determines whether flash verifying SACI commands are allowed. These commands only check integrity against a provided CRC32 value, never return any flash contents. Flash verify commands are always allowed after a chip erase and until the first reset after the CCFG sector has been programmed. ``` |
| `ti,flash-program` | `boolean` | ```text Determines whether flash programming SACI commands are allowed. Reset to allowed after a chip erase. ``` |
| `ti,chip-erase` | `boolean` | ```text Determines whether chip erasing SACI commands are allowed. ``` |
| `ti,ret-to-factory` | `boolean` | ```text Allows return-to-factory procedure by SACI. To do full failure analysis including flash, a return to factory procedure is supported. ``` |
| `ti,wr-er-prot-sect0-31` | `int` | ```text Bitmask for write/erase protection of individual sectors in sector range [0, 31]. Controls whether flash programming is allowed through SACI. The same mechanism controls whether the application is allowed to program these sectors. 0 = protected. Valid range: 0 - 0xffffffff Default is 0xffffffff to allow programming these sectors. ```  Default value: `4294967295` |
| `ti,wr-er-prot-sect32-255` | `int` | ```text Bitmask for write/erase protection of groups of 8 sectors, in sector range [32, 255]. Bit i protects sectors [32 + 8i, 39 + 8i]. 0 = protected. Valid range: 0 - 0xffffffff Default is 0xffffffff to allow programming these sectors. ```  Default value: `4294967295` |
| `ti,wr-er-prot-ccfg-sect` | `int` | ```text Bitmask for write/erase protection of CCFG sectors. Valid range: 0 - 0xffffffff Default is 0 to prevent from mistakenly programming these sectors. ``` |
| `ti,wr-er-prot-fcfg-sect` | `int` | ```text Bitmask for write/erase protection of FCFG sectors. Valid range: 0 - 0xffffffff Default is 0 to prevent from mistakenly programming these sectors. ``` |
| `ti,wr-er-prot-engr-sect` | `int` | ```text Bitmask for write/erase protection of ENGR sectors. Valid range: 0 - 0xffffffff Default is 0 to prevent from mistakenly programming these sectors. ``` |
| `ti,chip-er-retain-sect0-31` | `int` | ```text Bitmask for chip erase protection of individual sectors in sector range [0, 31]. Controls whether a chip erase affects a sector or not. The mechanism is intended to allow flash sectors devoted to logging or runtime state/configuration to survive the chip erase during a FW update. 0 = protected. Valid range: 0 - 0xffffffff Default is 0 to prevent from mistakenly programming these sectors. ``` |
| `ti,chip-er-retain-sect32-255` | `int` | ```text Bitmask for chip erase protection of groups of 8 sectors, in sector range [32, 255]. Bit i protects sectors [32 + 8i, 39 + 8i]. 0 = protected. Valid range: 0 - 0xffffffff Default is 0 to prevent from mistakenly programming these sectors. ``` |
| `erase-block-size` | `int` | ```text address alignment required by flash erase operations ``` |
| `write-block-size` | `int` | ```text address alignment required by flash write operations ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,cc23x0-ccfg-flash” compatible.

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
