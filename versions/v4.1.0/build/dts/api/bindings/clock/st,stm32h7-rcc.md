---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/clock/st,stm32h7-rcc.html
original_path: build/dts/api/bindings/clock/st,stm32h7-rcc.html
---

# st,stm32h7-rcc

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32H7 RCC (Reset and Clock controller).

This node is in charge of system clock ('SYSCLK') source selection and
System Clock Generation.

Configuring STM32 Reset and Clock controller node:

System clock source should be selected amongst the clock nodes available in "clocks"
node (typically 'clk_hse, clk_csi', 'pll', ...).
As part of this node configuration, SYSCLK frequency should also be defined, using
"clock-frequency" property.
Last, bus clocks (typically HCLK, PCLK1, PCLK2) should be configured using matching
prescaler properties.
Here is an example of correctly configured rcc node:
&rcc {
         clocks = <&pll>;  /* Set pll as SYSCLK source */
         clock-frequency = <DT_FREQ_M(480)>; /* SYSCLK runs at 480MHz */
         d1cpre = <1>;
         hpre = <1>;
         d1ppre = <1>;
         d2ppre1 = <1>;
         d2ppre2 = <1>;
         d3ppre = <1>;
}

Confere st,stm32-rcc binding for information about domain clocks configuration.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `2` |
| `clock-frequency` | `int` | ```text default frequency in Hz for clock output ```  This property is **required**. |
| `d1cpre` | `int` | ```text D1 Domain, CPU1 clock prescaler. Sets a HCLK frequency (feeding Cortex-M Systick) lower than SYSCLK frequency (actual core frequency). Zephyr doesn't make a difference today between these two clocks. Changing this prescaler is not allowed until it is made possible to use them independently in Zephyr clock subsystem. ```  This property is **required**.  Legal values: `1` |
| `hpre` | `int` | ```text D2 domain, CPU2 core clock and AHB(1/2/3/4) peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16`, `64`, `128`, `256`, `512` |
| `d1ppre` | `int` | ```text D1 domain, APB3 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `d2ppre1` | `int` | ```text D2 domain, APB1 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `d2ppre2` | `int` | ```text D2 domain, APB2 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `d3ppre` | `int` | ```text D3 domain, APB4 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32h7-rcc” compatible.

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

## Specifier cell names

- clock cells: bus, bits
