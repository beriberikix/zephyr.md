---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/gpio/ambiq,gpio.html
original_path: build/dts/api/bindings/gpio/ambiq,gpio.html
---

# ambiq,gpio

Vendor: [Ambiq Micro, Inc.](../../bindings.md#dt-vendor-ambiq)

## Description

```text
Ambiq GPIO provides the GPIO pin mapping for GPIO child nodes.

The Ambiq Apollo4x soc designs a single GPIO port with 128 pins.
It uses 128 continuous 32-bit registers to configure the GPIO pins.
This binding provides a pin mapping to solve the limitation of the maximum
32 pins handling in GPIO driver API.

The Ambiq Apollo4x soc should define one "ambiq,gpio" parent node in soc
devicetree and some child nodes which are compatible with "ambiq,gpio-bank"
under this parent node.

Here is an example of how a "ambiq,gpio" node can be used with the combined
gpio child nodes:

gpio: gpio@40010000 {
  compatible = "ambiq,gpio";
  gpio-map-mask = <0xffffffe0 0xffffffc0>;
  gpio-map-pass-thru = <0x1f 0x3f>;
  gpio-map = <
    0x00 0x0 &gpio0_31 0x0 0x0
    0x20 0x0 &gpio32_63 0x0 0x0
    0x40 0x0 &gpio64_95 0x0 0x0
    0x60 0x0 &gpio96_127 0x0 0x0
  >;
  reg = <0x40010000>;
  #gpio-cells = <2>;
  #address-cells = <1>;
  #size-cells = <0>;
  ranges;

  gpio0_31: gpio0_31@0 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0>;
    interrupts = <56 0>;
    status = "disabled";
  };

  gpio32_63: gpio32_63@80 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0x80>;
    interrupts = <57 0>;
    status = "disabled";
  };

  gpio64_95: gpio64_95@100 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0x100>;
    interrupts = <58 0>;
    status = "disabled";
  };

  gpio96_127: gpio96_127@180 {
    compatible = "ambiq,gpio-bank";
    gpio-controller;
    #gpio-cells = <2>;
    reg = <0x180>;
    interrupts = <59 0>;
    status = "disabled";
  };
};

In the above example, the gpio@40010000 is a "ambiq,gpio" parent node which
provides the base register address 0x40010000. It has four "ambiq,gpio-bank"
child nodes. Each of them covers 32 pins (the default value of "ngpios"
property is 32). The "reg" property of child nodes defines the register
address offset. The register address of pin described in gpio-cells can be
obtained by: base address + child address offset + (pin << 2). For example:
the address of pin 20 of gpio32_63@80 node is (0x40010000 + 0x80 + (20 << 2))
= 0x400100D0 and the real GPIO pin number of this pin in soc is (20 + 32)
= 52.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpio-map` | `compound` | This property is **required**. |
| `gpio-map-mask` | `compound` |  |
| `gpio-map-pass-thru` | `compound` |  |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ambiq,gpio” compatible.

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
