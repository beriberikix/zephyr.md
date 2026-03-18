---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/misc/zephyr,swdp-gpio.html
original_path: build/dts/api/bindings/misc/zephyr,swdp-gpio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# zephyr,swdp-gpio

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
This is a representation of the Serial Wire Debug Port interface
implementation by GPIO bit-banging.

Schematic using dual-supply bus transceiver and separate dout and dnoe pins

       VCC_3V3                      VCC_REF
          ^                           ^
          |       +-------------+     |
          +-------|vcca     vccb|-----+
                  |             |
 clk-gpios -------|a           b|-------------- SWD CLK
                  |             |
 noe-gpios -------|dir       gnd|-----+
                  +-------------+     |
                   74LVC1T45          v
                                     GND

       VCC_3V3                      VCC_REF
          ^                           ^
          |       +-------------+     |
          +-------|vcca     vccb|-----+
                  |             |
 dio-gpios -------|a           b|------------*- SWD DIO
                  |             |            |
          +-------|dir       gnd|-----+      |
          |       +-------------+     |      |
          v        74LVC1T45          v      |
         GND                         GND     |
                                             |
                                             |
       VCC_3V3                      VCC_REF  |
          ^                           ^      |
          |       +-------------+     |      |
          +-------|vcca     vccb|-----+      |
                  |             |            |
dout-gpios -------|a           b|------------+
                  |             |
dnoe-gpios -------|dir       gnd|-----+
                  +-------------+     |
                   74LVC1T45          v
                                     GND

Direct connection using only dio pin for SWD DIO.

 clk-gpios ------------------------------------ SWD CLK

 dio-gpios ------------------------------------ SWD DIO

Of course, bidirectional bus transceiver between dio and SWD DIO can also be
used together with noe pin to enable/disable transceivers.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clk-gpios` | `phandle-array` | ```text GPIO pin used for SWCLK output ```  This property is **required**. |
| `dio-gpios` | `phandle-array` | ```text GPIO pin used for SWDIO input. This pin is also used for the SWDIO output if separate output pin is not defined. ```  This property is **required**. |
| `dout-gpios` | `phandle-array` | ```text Optional GPIO pin used for SWDIO output. ``` |
| `dnoe-gpios` | `phandle-array` | ```text GPIO pin used to disable the SWDIO output buffer behind optional pin dout-gpios. ``` |
| `noe-gpios` | `phandle-array` | ```text Optional pin to disable all bus transceivers if any are present. ``` |
| `reset-gpios` | `phandle-array` | ```text Optional GPIO pin used for RESET output. ``` |
| `port-write-cycles` | `int` | ```text Number of processor cycles for I/O Port write operations.For example, the GPIO clock may be different from the CPU clock. This can usually be found in the SoC documentation. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,swdp-gpio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
