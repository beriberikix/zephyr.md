---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/xlnx,ps-gpio-bank.html
original_path: build/dts/api/bindings/gpio/xlnx,ps-gpio-bank.html
---

# xlnx,ps-gpio-bank

Vendor: [Xilinx](../../bindings.md#dt-vendor-xlnx)

Note

An implementation of a driver matching this compatible is available in
[drivers/gpio/gpio\_xlnx\_ps\_bank.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_xlnx_ps_bank.c).

## Description

```text
Xilinx Zynq-7000/ZynqMP MIO/EMIO GPIO controller bank node.

Each node of this type specified in the devicetree represents
a bank of the MIO/EMIO GPIO controller integrated in the Processor
System.
```

## Properties

### Top level properties

These property descriptions apply to “xlnx,ps-gpio-bank”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**.  Constant value: `2` |
| `ngpios` | `int` | ```text This property indicates the number of in-use slots of available slots for GPIOs. The typical example is something like this: the hardware register is 32 bits wide, but only 18 of the bits have a physical counterpart. The driver is generally written so that all 32 bits can be used, but the IP block is reused in a lot of designs, some using all 32 bits, some using 18 and some using 12. In this case, setting "ngpios = <18>;" informs the driver that only the first 18 GPIOs, at local offset 0 .. 17, are in use.  For cases in which there might be holes in the slot range, this value should be the max slot number+1. ```  This property is **required**.  Default value: `32` |
| `gpio-controller` | `boolean` | ```text Convey's this node is a GPIO controller ```  This property is **required**. |
| `gpio-reserved-ranges` | `array` | ```text If not all the GPIOs at offsets 0...N-1 are usable for ngpios = <N>, then this property contains an additional set of tuples which specify which GPIOs are unusable. This property indicates the start and size of the GPIOs that can't be used.  For example, setting "gpio-reserved-ranges = <3 2>, <10 1>;" means that GPIO offsets 3, 4, and 10 are not usable, even if ngpios = <18>. ``` |
| `gpio-line-names` | `string-array` | ```text This is an array of strings defining the names of the GPIO lines going out of the GPIO controller ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “xlnx,ps-gpio-bank” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `gpio-hog` | `boolean` | ```text Conveys this node is a GPIO hog. ```  This property is **required**. |
| `gpios` | `array` | ```text This is an array of GPIO specifiers (e.g. pin, flags) to be hogged. The number of array entries must be an integer multiple of the number of GPIO specifier cells for the parent GPIO controller. ```  This property is **required**. |
| `input` | `boolean` | ```text If this property is set, the GPIO is configured as an input. This property takes precedence over the output-low and output-high properties. ``` |
| `output-low` | `boolean` | ```text If this property is set, the GPIO is configured as an output set to logical low. This property takes precedence over the output-high property. ``` |
| `output-high` | `boolean` | ```text If this property is set, the GPIO is configured as an output set to logical high. ``` |
| `line-name` | `string` | ```text Optional GPIO line name. ``` |

## Specifier cell names

- gpio cells: pin, flags
