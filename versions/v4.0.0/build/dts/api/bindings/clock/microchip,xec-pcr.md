---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/microchip,xec-pcr.html
original_path: build/dts/api/bindings/clock/microchip,xec-pcr.html
---

# microchip,xec-pcr

Vendor: [Microchip Technology Inc.](../../bindings.md#dt-vendor-microchip)

Note

An implementation of a driver matching this compatible is available in
[drivers/clock\_control/clock\_control\_mchp\_xec.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_mchp_xec.c).

## Description

```text
Microchip XEC Power Clock Reset and VBAT register (PCR)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `core-clock-div` | `int` | ```text Divide 96 MHz PLL clock to produce Cortex-M4 core clock ```  This property is **required**. |
| `slow-clock-div` | `int` | ```text PWM and TACH clock domain divided down from 48 MHz AHB clock. The default value is 480 for 100 kHz. ``` |
| `pll-32k-src` | `int` | ```text 32 KHz clock source for PLL ```  This property is **required**. |
| `periph-32k-src` | `int` | ```text 32 KHz clock source for peripherals ```  This property is **required**. |
| `xtal-single-ended` | `boolean` | ```text Use single ended crystal connection to XTAL2 pin. ``` |
| `clk32kmon-period-min` | `int` | ```text 32KHz clock monitor minimum valid 32KHz period in 48MHz units ```  This property is **required**. |
| `clk32kmon-period-max` | `int` | ```text 32KHz clock monitor maximum valid 32KHz period in 48MHz units ```  This property is **required**. |
| `clk32kmon-duty-cycle-var-max` | `int` | ```text Maximum duty cycle variation. Difference in units of 48HMz between the measured 32KHz high and low pulse widths. ```  This property is **required**. |
| `clk32kmon-valid-min` | `int` | ```text Minimum number of consecutive 32KHz pulses that pass all monitor tests ```  This property is **required**. |
| `xtal-enable-delay-ms` | `int` | ```text Delay in milliseconds after crystal is enabled and clock monitor is started. ```  This property is **required**.  Default value: `300` |
| `pll-lock-timeout-ms` | `int` | ```text Timeout in milliseconds waiting for PLL to lock to new clock source. ```  This property is **required**.  Default value: `30` |
| `clkmon-bypass` | `boolean` | ```text Bypass clkmon check of crystal or XTAL2 single-ended clock. ``` |
| `internal-osc-disable` | `boolean` | ```text If the internal silicon 32KHz oscillator is not chosen as the source for PLL and Periheral devices then disable the internal 32KHz oscillator to save power. ``` |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `3` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “microchip,xec-pcr” compatible.

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

## Specifier cell names

- clock cells: regidx, bitpos, domain
