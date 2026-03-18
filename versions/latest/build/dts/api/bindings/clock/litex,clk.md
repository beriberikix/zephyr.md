---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/litex,clk.html
original_path: build/dts/api/bindings/clock/litex,clk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# litex,clk

Vendor: [LiteX SoC builder](../../bindings.md#dt-vendor-litex)

## Description

```text
LiteX Mixed Mode Clock Manager
Common clock driver with MMCM unit for dynamic reconfiguration
of up to 7 clock outputs with ability to change frequency, duty
cycle and phase offset
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `1` |
| `clock-output-names` | `string-array` | ```text List of strings of clock output signal names indexed by the first cell in the clock specifier. ```  This property is **required**. |
| `litex,lock-timeout` | `int` | ```text Number of ms to wait for MMCM to assert LOCK signal ```  This property is **required**. |
| `litex,drdy-timeout` | `int` | ```text Number of ms to wait for MMCM to assert DRDY signal ```  This property is **required**. |
| `litex,sys-clock-frequency` | `int` | ```text System clock frequency ```  This property is **required**. |
| `litex,divclk-divide-min` | `int` | ```text minimal global divider ```  This property is **required**. |
| `litex,divclk-divide-max` | `int` | ```text maximal global divider ```  This property is **required**. |
| `litex,clkfbout-mult-min` | `int` | ```text minimal global multiplier ```  This property is **required**. |
| `litex,clkfbout-mult-max` | `int` | ```text maximal global multiplier ```  This property is **required**. |
| `litex,vco-freq-min` | `int` | ```text minimal frequency after global divider and multiplier ```  This property is **required**. |
| `litex,vco-freq-max` | `int` | ```text maximal frequency after global divider and multiplier ```  This property is **required**. |
| `litex,clkout-divide-min` | `int` | ```text minimal clock output divider ```  This property is **required**. |
| `litex,clkout-divide-max` | `int` | ```text maximal clock output divider ```  This property is **required**. |
| `litex,vco-margin` | `int` | ```text tolerancy for vco frequency ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “litex,clk” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Base address and lengths of the register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

## Specifier cell names

- clock cells: id
