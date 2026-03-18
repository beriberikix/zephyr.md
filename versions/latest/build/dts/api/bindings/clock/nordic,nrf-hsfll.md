---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/nordic,nrf-hsfll.html
original_path: build/dts/api/bindings/clock/nordic,nrf-hsfll.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nordic,nrf-hsfll

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic nRF HSFLL

The HSFLL mixed-mode IP generates several clock frequencies in the range from
64 MHz to 400 MHz (in steps of 16 MHz).

Usage example:

  hsfll: clock@deadbeef {
      compatible = "nordic,nrf-hsfll";
      reg = <0xdeadbeef 0x1000>;
      clocks = <&fll16m>;
      clock-frequency = <DT_FREQ_M(320)>;
      nordic,ficrs = <&ficr NRF_FICR_TRIM_APPLICATION_HSFLL_TRIM_VSUP>,
                     <&ficr NRF_FICR_TRIM_APPLICATION_HSFLL_TRIM_COARSE_0>,
                     <&ficr NRF_FICR_TRIM_APPLICATION_HSFLL_TRIM_FINE_0>;
      nordic,ficr-names = "vsup", "coarse", "fine";
  };

Required FICR entries are for VSUP, COARSE and FINE trim values.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**.  Legal values: `64000000`, `80000000`, `96000000`, `112000000`, `128000000`, `144000000`, `160000000`, `176000000`, `192000000`, `208000000`, `224000000`, `240000000`, `256000000`, `272000000`, `288000000`, `304000000`, `320000000`, `336000000`, `352000000`, `368000000`, `384000000`, `400000000` |
| `nordic,ficrs` | `phandle-array` | ```text FICR entries, e.g. <&ficr OFFSET>. Available offsets (or FICR entries) are available at <zephyr/dt-bindings/misc/nordic-nrf-ficr-*.h>. ```  This property is **required**. |
| `nordic,ficr-names` | `string-array` | ```text Names of each nordic,ficrs entry. ```  This property is **required**. |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-hsfll” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
