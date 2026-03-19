---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/gpio/nordic,nrf-gpio-forwarder.html
original_path: build/dts/api/bindings/gpio/nordic,nrf-gpio-forwarder.html
---

# nordic,nrf-gpio-forwarder

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
This is an abstract device responsible for forwarding pins between cores.

In nRF53 family of SoCs, GPIO pins must be explicitly forwarded by
the application core to the network core if the latter should drive them.
The purpose of this abstract device is to represent all GPIO pins that the
nRF53 application core should forward to the nRF53 network core.

Once the control over selected GPIO pins is forwarded to it, the network
core is responsible for configuring the pins and driving them as needed.

Here is an example of how a nrf-gpio-forwarder can be used with a nRF5340
combined with a nRF21540 Front-End module. Consider the following node
present in DTS file targeted for the nRF5340 network core, which defines
the details of the nRF21540 Front-End module's interface:

nrf_radio_fem: nrf21540 {
  compatible = "nordic,nrf21540-fem";
  tx-en-gpios = <&gpio0 30 GPIO_ACTIVE_HIGH>;
  rx-en-gpios = <&gpio1 11 GPIO_ACTIVE_HIGH>;
  pdn-gpios   = <&gpio1 10 GPIO_ACTIVE_HIGH>;
  mode-gpios  = <&gpio1 12 GPIO_ACTIVE_HIGH>;
};

Since the nRF21540 Front-End module should be controlled by the nRF5340
network core, all the GPIO pins used to control it must be forwarded by
the nRF5340 application core to the network core. Consider the following
nrf-gpio-forwarder node defined in DTS file targeted for the nRF5340
application core:

gpio_fwd: nrf-gpio-forwarder {
  compatible = "nordic,nrf-gpio-forwarder";
  nrf21540-gpio-if {
    gpios = <&gpio0 30 0>, <&gpio1 11 0>, <&gpio1 10 0>, <&gpio1 12 0>;
  };
};

In the above example, the nrf-gpio-forwarder node is configured to forward
control over the following GPIO pins to the network core:

  - P0.30 (matching `tx-en-gpios`)
  - P1.11 (matching `rx-en-gpios`)
  - P1.10 (matching `pdn-gpios`)
  - P1.12 (matching `mode-gpios`)

Please note that the GPIO flags provided for child nodes of the forwarder
are ignored. In order to configure the GPIOs passed to the forwarder, their
GPIO flags must be set in the matching node that these GPIOs are forwarded
to. In the above example, the GPIO flags must be set in the nrf21540 node.
They are set to 0 in the nrf-gpio-forwarder node as they are ignored anyway.

Child nodes for the forwarder can be defined independently by multiple DTS
files. They are merged into a single node with multiple child nodes when
processing devicetree for an application build. However, in order for that
to happen, names of the child nodes must be unique in the scope of a single
nrf-gpio-forwarder instance.
```

## Properties

### Top level properties

These property descriptions apply to “nordic,nrf-gpio-forwarder”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-gpio-forwarder” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `gpios` | `phandle-array` | ```text Array of GPIOs to be forwarded. Note that GPIO flags provided for elements of this array are ignored. In order to configure the GPIOs from this array, their GPIO flags must be set in the matching node that these GPIOs are forwarded to. ```  This property is **required**. |
