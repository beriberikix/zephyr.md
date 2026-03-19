---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/nuvoton,numaker-scc.html
original_path: build/dts/api/bindings/clock/nuvoton,numaker-scc.html
---

# nuvoton,numaker-scc

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

Note

An implementation of a driver matching this compatible is available in
[drivers/clock\_control/clock\_control\_numaker\_scc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_numaker_scc.c).

## Description

```text
Nuvoton NuMaker System Clock Controller (SCC)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `hxt` | `string` | ```text Enable/disable 4~24 MHz external crystal oscillator (HXT) ```  Legal values: `'untouched'`, `'enable'`, `'disable'` |
| `lxt` | `string` | ```text Enable/disable 32.768 kHz low-speed external crystal oscillator (LXT) ```  Legal values: `'untouched'`, `'enable'`, `'disable'` |
| `hirc48m` | `string` | ```text Enable/disable 48 MHz high-speed internal RC oscillator (HIRC48) ```  Legal values: `'untouched'`, `'enable'`, `'disable'` |
| `clk-pclkdiv` | `int` | ```text Configure APB Clock Divider register ``` |
| `core-clock` | `int` | ```text Configure core clock (HCLK) ``` |
| `powerdown-mode` | `int` | ```text Configure power down mode, please choose one of NUMAKER_CLK_PMUCTL_PDMSEL_XXX from numaker_xxx_clock.h ``` |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,numaker-scc” compatible.

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
