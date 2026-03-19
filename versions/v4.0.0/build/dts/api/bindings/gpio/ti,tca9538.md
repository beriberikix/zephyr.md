---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/ti,tca9538.html
original_path: build/dts/api/bindings/gpio/ti,tca9538.html
---

# ti,tca9538 (on i2c bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/gpio/gpio\_pca953x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_pca953x.c).

## Description

```text
TCA9538 GPIO node
```

## Properties

### Top level properties

These property descriptions apply to “ti,tca9538”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**.  Constant value: `2` |
| `ngpios` | `int` | ```text Number of GPIOs available on port expander. ```  This property is **required**.  Default value: `32`  Constant value: `8` |
| `nint-gpios` | `phandle-array` | ```text Connection for the NINT signal. This signal is active-low when produced by tca9538 GPIO node. ``` |
| `input-latch` | `int` | ```text Input latch register bit is 0 by default and the input pin state is not latched. When input latch register bit is 1 and the input pin state is latched. ``` |
| `interrupt-mask` | `int` | ```text Interrupt mask register is set to logic 1 by default without enabling interrupts. Setting corresponding mask bits to logic 0 to enable the interrupts. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `gpio-controller` | `boolean` | ```text Convey's this node is a GPIO controller ```  This property is **required**. |
| `gpio-reserved-ranges` | `array` | ```text If not all the GPIOs at offsets 0...N-1 are usable for ngpios = <N>, then this property contains an additional set of tuples which specify which GPIOs are unusable. This property indicates the start and size of the GPIOs that can't be used.  For example, setting "gpio-reserved-ranges = <3 2>, <10 1>;" means that GPIO offsets 3, 4, and 10 are not usable, even if ngpios = <18>. ``` |
| `gpio-line-names` | `string-array` | ```text This is an array of strings defining the names of the GPIO lines going out of the GPIO controller ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,tca9538” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text device address on i2c bus ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
