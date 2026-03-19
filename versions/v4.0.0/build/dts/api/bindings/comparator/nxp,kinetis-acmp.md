---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/comparator/nxp,kinetis-acmp.html
original_path: build/dts/api/bindings/comparator/nxp,kinetis-acmp.html
---

# nxp,kinetis-acmp

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP Kinetis ACMP (Analog CoMParator)

The following example displays the minimum node layout:

  acmp0: acmp@deadbeef {
          compatible = "nxp,kinetis-acmp";
          reg = <0xdeadbeef 0x1000>;
          interrupts = <0 0>;
          clocks = <&scg KINETIS_SCG_BUS_CLK>;
          status = "disabled";
  };

Enabling the comparator node requires setting the minimum default
configuration of the comparator. This includes selecting the
positive and negative inputs, and routing them using pinctrl:

  &pinctrl {
          acmp0_default: acmp0_default {
                  group0 {
                          ...
                  };
          };
  };

  &acmp0 {
          status = "okay";
          pinctrl-0 = <&acmp0_default>;
          pinctrl-names = "default";

          positive-mux-input = "IN0";
          negative-mux-input = "IN1";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `offset-mode` | `string` | Legal values: `'LEVEL0'`, `'LEVEL1'` |
| `hysteresis-mode` | `string` | Legal values: `'LEVEL0'`, `'LEVEL1'`, `'LEVEL2'`, `'LEVEL3'` |
| `enable-high-speed-mode` | `boolean` |  |
| `invert-output` | `boolean` |  |
| `use-unfiltered-output` | `boolean` |  |
| `enable-pin-out` | `boolean` |  |
| `enable-window-mode` | `boolean` |  |
| `positive-mux-input` | `string` | Legal values: `'IN0'`, `'IN1'`, `'IN2'`, `'IN3'`, `'IN4'`, `'IN5'`, `'IN6'`, `'IN7'` |
| `negative-mux-input` | `string` | Legal values: `'IN0'`, `'IN1'`, `'IN2'`, `'IN3'`, `'IN4'`, `'IN5'`, `'IN6'`, `'IN7'` |
| `positive-port-input` | `string` | Legal values: `'DAC'`, `'MUX'` |
| `negative-port-input` | `string` | Legal values: `'DAC'`, `'MUX'` |
| `filter-enable-sample` | `boolean` |  |
| `filter-count` | `int` | ```text Filter sample count (0 to 7). ``` |
| `filter-period` | `int` | ```text Filter sample period in bus clock cycles (0 to 255). ``` |
| `dac-vref-source` | `string` | Legal values: `'VIN1'`, `'VIN2'` |
| `dac-value` | `int` |  |
| `dac-enable` | `boolean` |  |
| `dac-enable-high-speed` | `boolean` |  |
| `discrete-mode-enable-positive-channel` | `boolean` |  |
| `discrete-mode-enable-negative-channel` | `boolean` |  |
| `discrete-mode-enable-resistor-divider` | `boolean` |  |
| `discrete-mode-clock-source` | `string` | Legal values: `'SLOW'`, `'FAST'` |
| `discrete-mode-sample-time` | `string` | Legal values: `'T1'`, `'T2'`, `'T4'`, `'T8'`, `'T16'`, `'T32'`, `'T64'`, `'T256'` |
| `discrete-mode-phase1-time` | `string` | Legal values: `'ALT0'`, `'ALT1'`, `'ALT2'`, `'ALT3'`, `'ALT4'`, `'ALT5'`, `'ALT6'`, `'ALT7'` |
| `discrete-mode-phase2-time` | `string` | Legal values: `'ALT0'`, `'ALT1'`, `'ALT2'`, `'ALT3'`, `'ALT4'`, `'ALT5'`, `'ALT6'`, `'ALT7'` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nxp,enable-output-pin` | `boolean` | ```text Deprecated. Please use enable-pin-out instead ``` |
| `nxp,use-unfiltered-output` | `boolean` | ```text Deprecated. Please use use-unfiltered-output instead ``` |
| `nxp,high-speed-mode` | `boolean` | ```text Deprecated. Please use enable-high-speed-mode instead ``` |
| `nxp,enable-sample` | `boolean` | ```text Deprecated. Please use filter-enable-sample instead ``` |
| `nxp,filter-count` | `int` | ```text Deprecated. Please use filter-count instead ``` |
| `nxp,filter-period` | `int` | ```text Deprecated. Please use filter-period instead ``` |
| `nxp,window-mode` | `boolean` | ```text Deprecated. Please use enable-window-mode instead ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,kinetis-acmp” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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
