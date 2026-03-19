---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/gpio/nordic,npm6001-gpio.html
original_path: build/dts/api/bindings/gpio/nordic,npm6001-gpio.html
---

# nordic,npm6001-gpio

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

Note

An implementation of a driver matching this compatible is available in
[drivers/gpio/gpio\_npm6001.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_npm6001.c).

## Description

```text
nPM6001 GPIO Controller
```

## Properties

### Top level properties

These property descriptions apply to “nordic,npm6001-gpio”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `gpio-controller` | `boolean` | ```text Convey's this node is a GPIO controller ```  This property is **required**. |
| `#gpio-cells` | `int` | ```text Number of items to expect in a GPIO specifier ```  This property is **required**. |
| `ngpios` | `int` | ```text This property indicates the number of in-use slots of available slots for GPIOs. The typical example is something like this: the hardware register is 32 bits wide, but only 18 of the bits have a physical counterpart. The driver is generally written so that all 32 bits can be used, but the IP block is reused in a lot of designs, some using all 32 bits, some using 18 and some using 12. In this case, setting "ngpios = <18>;" informs the driver that only the first 18 GPIOs, at local offset 0 .. 17, are in use.  For cases in which there might be holes in the slot range, this value should be the max slot number+1. ```  Default value: `32` |
| `gpio-reserved-ranges` | `array` | ```text If not all the GPIOs at offsets 0...N-1 are usable for ngpios = <N>, then this property contains an additional set of tuples which specify which GPIOs are unusable. This property indicates the start and size of the GPIOs that can't be used.  For example, setting "gpio-reserved-ranges = <3 2>, <10 1>;" means that GPIO offsets 3, 4, and 10 are not usable, even if ngpios = <18>. ``` |
| `gpio-line-names` | `string-array` | ```text This is an array of strings defining the names of the GPIO lines going out of the GPIO controller ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,npm6001-gpio” compatible.

(None)

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
