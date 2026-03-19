---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/led_strip/worldsemi,ws2812-gpio.html
original_path: build/dts/api/bindings/led_strip/worldsemi,ws2812-gpio.html
---

# worldsemi,ws2812-gpio

Vendor: [Worldsemi Co., Limited](../../bindings.md#dt-vendor-worldsemi)

Note

An implementation of a driver matching this compatible is available in
[drivers/led\_strip/ws2812\_gpio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/ws2812_gpio.c).

## Description

```text
Worldsemi WS2812 LED strip, GPIO binding

Driver bindings for bit-banging a WS2812 or compatible LED strip.

The CPU driver uses inline assembly, and isn't available for all
boards. The timing is automatically derived from the CPU clock frequency,
or can be provided by setting the delay-txx properties in the device
tree, or can be manually provided by the Kconfig settings DELAY_Txx.

The four delays provided (calculated based on the clock frequency,
provided by a dts, or Kconfig file) determine the delays as depicted
below. The exact timings of the LED strip data line might vary on the
type of LEDs used, consult the data-sheet for the precise timings.

0 code
   +-------+                 +---
   |       |                 |
   |  T0H  |       T0L       |
   |       |                 |
---+       +-----------------+

1 code
   +---------------+         +---
   |               |         |
   |      T1H      |   T1L   |
   |               |         |
---+               +---------+

Example dts file:
/ {
      cpus {
          cpu@0 {
              clock-frequency = <64000000>;
          };
      };

      rgb_led: ws2812 {
          compatible = "worldsemi,ws2812-gpio";
          chain-length = <1>;
          color-mapping = <LED_COLOR_ID_GREEN
                           LED_COLOR_ID_RED
                           LED_COLOR_ID_BLUE>;
          gpios = <&gpio0 16 0>;
      };
};

Example dts file:
/ {
      chosen {
          zephyr,led-strip = &rgb_led;
      };

      rgb_led: ws2812 {
          compatible = "worldsemi,ws2812-gpio";
          chain-length = <1>;
          color-mapping = <LED_COLOR_ID_GREEN
                           LED_COLOR_ID_RED
                           LED_COLOR_ID_BLUE>;
          reset-delay = <50>;
          gpios = <&gpio0 16 0>;
          delay-t1h = <48>;
          delay-t1l = <32>;
          delay-t0h = <16>;
          delay-t0l = <32>;
      };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `delay-t1h` | `int` | ```text Number of NOP assembly operations to create a delay for a 1 bit, high voltage period (default 700 nsec) ``` |
| `delay-t1l` | `int` | ```text Number of NOP assembly operations to create a delay for a 1 bit, low voltage period (default 600 nsec) ``` |
| `delay-t0h` | `int` | ```text Number of NOP assembly operations to create a delay for a 0 bit, high voltage period (default 350 nsec) ``` |
| `delay-t0l` | `int` | ```text Number of NOP assembly operations to create a delay for a 0 bit, low voltage period (default 800 nsec) ``` |
| `gpios` | `phandle-array` | ```text GPIO phandle and specifier for the pin connected to the led-strip. Exactly one pin should be given. ```  This property is **required**. |
| `reset-delay` | `int` | ```text Minimum delay to wait (in microseconds) to make sure that the strip has latched the signal. If omitted, a default value of 8 microseconds is used. This default is good for the WS2812 controllers. Note that despite the WS2812 datasheet states that a 50 microseconds delay is required, it seems 6 microseconds is enough. The default is set to 8 microseconds just to be safe. ```  Default value: `8` |
| `chain-length` | `int` | ```text The number of devices in the daisy-chain. ```  This property is **required**. |
| `color-mapping` | `array` | ```text Channel to color mapping (or pixel order).  For example a GRB channel to color mapping would be     color-mapping = <LED_COLOR_ID_GREEN                     LED_COLOR_ID_RED                     LED_COLOR_ID_BLUE>; ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “worldsemi,ws2812-gpio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
