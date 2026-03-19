---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/cpu/espressif,riscv.html
original_path: build/dts/api/bindings/cpu/espressif,riscv.html
---

# espressif,riscv

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

## Description

```text
Espressif RISC-V CPU
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-source` | `int` | ```text Defines the CPU clock source, each corresponding to different frequencies: - 0: ESP32_CPU_CLK_SRC_XTAL - Uses the external crystal clock typically at 40 MHz. - 1: ESP32_CPU_CLK_SRC_PLL - Utilizes an internal PLL which operates at either 320 MHz or 480 MHz. - 2: ESP32_CPU_CLK_SRC_RC_FAST - Employs an internal fast RC oscillator with frequency of 17.5 MHz. ```  This property is **required**.  Legal values: `0`, `1`, `2` |
| `xtal-freq` | `int` | ```text Value of the external XTAL connected to ESP32. This is typically 40 MHz. ```  This property is **required**.  Legal values: `26000000`, `32000000`, `40000000` |
| `mmu-type` | `string` | ```text Memory Management Unit (MMU) ```  Legal values: `'riscv,sv32'`, `'riscv,sv39'`, `'riscv,sv48'`, `'riscv,none'` |
| `riscv,isa` | `string` | ```text RISC-V instruction set architecture ```  This property is **required**. |
| `clock-frequency` | `int` | ```text Clock frequency in Hz ``` |
| `cpu-power-states` | `phandles` | ```text List of power management states supported by this cpu ``` |
| `i-cache-line-size` | `int` | ```text i-cache line size ``` |
| `d-cache-line-size` | `int` | ```text d-cache line size ``` |
| `enable-method` | `string` | ```text Enable method for cpu, either it is "psci" or "spin-table" ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,riscv” compatible.

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
