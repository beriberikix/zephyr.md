---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/led_strip/worldsemi,ws2812-rpi_pico-pio.html
original_path: build/dts/api/bindings/led_strip/worldsemi,ws2812-rpi_pico-pio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# worldsemi,ws2812-rpi\_pico-pio

Vendor: [Worldsemi Co., Limited](../../bindings.md#dt-vendor-worldsemi)

## Description

```text
The pio node configured for ws2812.
```

## Properties

### Top level properties

These property descriptions apply to “worldsemi,ws2812-rpi\_pico-pio”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `bit-waveform` | `array` | ```text This property defines the waveform for sending 1-bit data. The program uses the first three elements of the array. The T0 is equal to T0H in the datasheet. The T2 is equal to T1L in the datasheet. The T1 is equal to (T1H-T0H) or (T0L-T1L) in the datasheet.  Code-0    +------+                 +---    |      |                 |    |  T0  |      T1+T2      |    |      |                 | ---+      +-----------------+  Code-1    +---------------+        +---    |               |        |    |     T0+T1     |   T2   |    |               |        | ---+               +--------+   The frequency determines the wave period. The T0～T2 means ratio in one period.  For example, T0=3, T1=3, T2=4 and the frequency is 800kHz case, T0H is   (1 / 800kHz) * (3/10) = 375ns T0L is   (1 / 800kHz) * ((4+3)/10) = 875ns ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “worldsemi,ws2812-rpi\_pico-pio” compatible.

(None)

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `chain-length` | `int` | ```text The number of devices in the daisy-chain. ```  This property is **required**. |
| `color-mapping` | `array` | ```text Channel to color mapping (or pixel order).  For example a GRB channel to color mapping would be     color-mapping = <LED_COLOR_ID_GREEN                     LED_COLOR_ID_RED                     LED_COLOR_ID_BLUE>; ```  This property is **required**. |
| `reset-delay` | `int` | ```text Minimum delay to wait (in microseconds) to make sure that the strip has latched the signal. If omitted, a default value of 8 microseconds is used. This default is good for the WS2812 controllers. Note that despite the WS2812 datasheet states that a 50 microseconds delay is required, it seems 6 microseconds is enough. The default is set to 8 microseconds just to be safe. ```  Default value: `8` |
| `gpios` | `phandle-array` | ```text Inherited from ws2812-gpio.yaml.  Note: This driver does not configure the output pin. You need to configure the pin with pinctrl that is in the parent node configuration for use by PIO. This property only uses the GPIO pin number and ignores flags. ```  This property is **required**. |
| `frequency` | `int` | ```text Specify the number of times a waveform representing 1 bit is transmitted per second. It is same meaning as bit-per-seconds. WS2812 works with 800000. Set the value 400000 if use with WS2811. ``` |
