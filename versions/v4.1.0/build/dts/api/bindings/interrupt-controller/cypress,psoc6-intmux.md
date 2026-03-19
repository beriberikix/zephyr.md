---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/interrupt-controller/cypress,psoc6-intmux.html
original_path: build/dts/api/bindings/interrupt-controller/cypress,psoc6-intmux.html
---

# cypress,psoc6-intmux

Vendor: [Cypress Semiconductor Corporation](../../bindings.md#dt-vendor-cypress)

## Description

```text
Cypress Interrupt Multiplex

The PSOC 6 Cortex-M0+ NVIC can handle up to 32 interrupts. This means that
user can select up to 32 interrupts sources from the 240 possible vectors
to be processed in the Cortex-M0+ CPU.

At CPU Sub System (CPUSS) there are 8 special registers (intmux[0~7]) to
configure the 32 NVIC lines for Cortex-M0+ CPU. Each register handles up to
4 interrupt sources by grouping intmux channels. These means that each byte
from intmux[0~7] store a 'vector number' which selects the peripheral
interrupt source in the multiplexer. The multiplexer is placed before
Cortex-M0+ NVIC controller. Note that Cortex-M4 have all interrupt sources
directly connected to NVIC and doesn't require any special configuration.

On a general view, the below represents the Interrupt Multiplexer
configuration and how the Cortex-M0+ NVIC sources are organized. Each
channel chX represents a Cortex-M0+ NVIC line and it stores a vector number.
The vector number selects the PSOC 6 peripheral interrupt source for the
Cortex-M0+ NVIC controller line.

intmux[0] = {ch03, ch02, ch01, ch00}
intmux[1] = {ch07, ch06, ch05, ch04}
...
intmux[7] = {ch31, ch30, ch29, ch28}

In practical terms, the Cortex-M0+ requires user to define all NVIC interrupt
sources and the proper NVIC interrupt order. With that, the system configures
the Cortex-M0+ Interrupt Multiplexer and interrupts can be processed.
More information about it at PSOC 6 Architecture Technical Reference Manual,
section CPU Sub System (CPUSS) Registers.

The below fragment configure the GPIO Port 0 to generate an interrupt at
Cortex-M0+ NVIC:

At psoc6.dtsi file the gpio_prt0 peripheral had the interrupt source 2:

gpio_prt0: gpio@40320100 {
  interrupts = <2 1>;
};

In order to enable gpio_prt0 interrupt at Cortex-M0+ an interrupt parent
must be defined at gpio_prt0 node selecting the Interrupt Multiplex Channel.
This can be defined at <board>_m0.dts file:

&gpio_prt0 {
  interrupt-parent = <&intmux_ch20>;
};

The translation of these two definitions is:
       CH   REGS  INT NUM    CH   CH/REG
intmux[20 mod 8] |= 0x02 << (20 mod 4);

These results in Cortex-M0+ NVIC line 20 handling PSOC 6 interrupt source 2.
The interrupt can be enabled/disabled at NVIC at line 20 as usual.

Notes:
1) Multiple definitions will generate multiple interrupts
2) The interrupt sources are shared between Cortex-M0+/M4. This means, they
   can trigger actions in parallel on both processors.
3) User can change priority at Cortex-M0+ NVIC by changing interrupt channels
   at interrupt-parent properties.
4) Only the peripherals used by Cortex-M0+ should be configured.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “cypress,psoc6-intmux” compatible.

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
