---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/pinctrl/microchip,xec-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/microchip,xec-pinctrl.html
---

# microchip,xec-pinctrl

Vendor: [Microchip Technology Inc.](../../bindings.md#dt-vendor-microchip)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_mchp\_xec.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_mchp_xec.c).

## Description

```text
Microchip XEC Pin controller Node
Based on pincfg-node.yaml binding.
The MCHP XEC pin controller is a singleton node responsible for controlling
pin function selection and pin properties. For example, you can use this
node to select peripheral pin functions.

The node has the 'pinctrl' node label set in your SoC's devicetree,
so you can modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the
'pinctrl' node, as in the spi0 example shown at the end:

A group can also specify shared pin properties common to all the specified
pins, such as the 'bias-pull-up' property in group 2. Here is a list of
supported standard pin properties:

- bias-disable: Disable pull-up/down (default behavior, not required).
- bias-pull-down: Enable pull-down resistor.
- bias-pull-up: Enable pull-up resistor.
- drive-push-pull: Output driver is push-pull (default, not required).
- drive-open-drain: Output driver is open-drain.
- output-high: Set output state high when pin configured.
- output-low: Set output state low when pin configured.

Custom pin properties for drive strength and slew rate are available:
- drive-strength
- slew-rate

Driver strength and slew rate hardware defaults vary by SoC and pin.

An example for MEC172x family, include the chip level pinctrl
DTSI file in the board level DTS:

  #include <microchip/mec172x/mec172xnsz-pinctrl.dtsi>

We want to use the shared SPI port of the MEC172x QMSPI controller
and want the chip select 0 to be open-drain.

To change a pin's pinctrl default properties add a reference to the
pin in the board's DTS file and set the properties.

  &spi0 {
    pinctrl-0 = < &shd_cs0_n_gpio055
                  &shd_clk_gpio056
                  &shd_io0_gpio223
                  &shd_io1_gpio224
                  &shd_io3_gpio016 >;
    pinctrl-names = "default";
  }

  &shd_cs0_n_gpio055 {
    drive-open-drain;
  };
```

## Properties

### Top level properties

These property descriptions apply to “microchip,xec-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “microchip,xec-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `int` | ```text Pinmux selection ```  This property is **required**. |
| `slew-rate` | `string` | ```text Pin speed. The default value of slew-rate is the SoC power-on-reset value. Please refer to the data sheet as a small number of pins may have a different default and some pins do not implement slew rate adjustment. ```  Default value: `no-change`  Legal values: `'no-change'`, `'low-speed'`, `'high-speed'` |
| `drive-strength` | `string` | ```text Pin output drive strength for PIO and PIO-24 pin types. Default is "1x" for most pins. PIO pins are 2, 4, 8, or 12 mA. PIO-24 pins are 4, 8, 16, or 24 mA. Please refer to the data sheet for each pin's PIO type and default drive strength. ```  Default value: `no-change`  Legal values: `'no-change'`, `'1x'`, `'2x'`, `'4x'`, `'6x'` |
| `microchip,output-func-invert` | `boolean` | ```text Invert polarity of an output alternate function. Input functions are not affected. ``` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `low-power-enable` | `boolean` | ```text enable low power mode ``` |
| `output-disable` | `boolean` | ```text disable output on a pin (e.g. disable an output buffer) ``` |
| `output-enable` | `boolean` | ```text enable output on a pin without actively driving it (e.g. enable an output buffer) ``` |
| `output-low` | `boolean` | ```text set the pin to output mode with low level ``` |
| `output-high` | `boolean` | ```text set the pin to output mode with high level ``` |
