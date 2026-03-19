---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/comparator/nordic,nrf-comp.html
original_path: build/dts/api/bindings/comparator/nordic,nrf-comp.html
---

# nordic,nrf-comp

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

Note

An implementation of a driver matching this compatible is available in
[drivers/comparator/comparator\_nrf\_comp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_nrf_comp.c).

## Description

```text
Nordic nRF COMP (analog COMParator)

This comparator has varying configurations which require varying
properties be set in the devicetree.

The following example displays the minimum node layout:

  comp: comp@deadbeef {
          compatible = "nordic,nrf-comp";
          reg = <0xdeadbeef 0x1000>;
          interrupts = <0 NRF_DEFAULT_IRQ_PRIORITY>;
          status = "disabled";
  };

Enabling the comparator node requires setting the default
configuration of the comparator.

The following example displays enabling the comparator in
single-ended mode, selecting an internal reference:

  &comp {
          status = "okay";
          main-mode = "SE";
          psel = "AIN0";
          refsel = "INT_1V2";
          sp-mode = "NORMAL";
          th-up = <36>;
          th-down = <30>;
          isource = "OFF";
  };

To select an external reference, select the "AREF"
reference and add the external reference:

  &comp {
          ...
          refsel = "AREF";
          extrefsel = "AIN1";
          ...
  };

The following example displays enabling the comparator
in differential mode:

  &comp {
          status = "okay";
          main-mode = "DIFF";
          psel = "AIN0";
          extrefsel = "AIN1";
          sp-mode = "NORMAL";
          hyst = "50MV";
          isource = "OFF";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `main-mode` | `string` | Legal values: `'SE'`, `'DIFF'` |
| `psel` | `string` | Legal values: `'AIN0'`, `'AIN1'`, `'AIN2'`, `'AIN3'`, `'AIN4'`, `'AIN5'`, `'AIN6'`, `'AIN7'`, `'VDD_DIV2'`, `'VDDH_DIV5'` |
| `extrefsel` | `string` | Legal values: `'AIN0'`, `'AIN1'`, `'AIN2'`, `'AIN3'`, `'AIN4'`, `'AIN5'`, `'AIN6'`, `'AIN7'` |
| `refsel` | `string` | Legal values: `'INT_1V2'`, `'INT_1V8'`, `'INT_2V4'`, `'AVDDAO1V8'`, `'VDD'`, `'AREF'` |
| `enable-hyst` | `boolean` |  |
| `sp-mode` | `string` | Legal values: `'LOW'`, `'NORMAL'`, `'HIGH'` |
| `th-up` | `int` |  |
| `th-down` | `int` |  |
| `isource` | `string` | Legal values: `'DISABLED'`, `'2UA5'`, `'5UA'`, `'10UA'` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-comp” compatible.

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
