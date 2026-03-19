---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/wifi/nordic,nrf7000-qspi.html
original_path: build/dts/api/bindings/wifi/nordic,nrf7000-qspi.html
---

# nordic,nrf7000-qspi (on qspi bus)

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
This is a representation of the nRF7002 Wi-Fi chip with QSPI interface.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `qspi-frequency` | `int` | ```text Maximum clock speed (in Hz) supported by the device. ```  This property is **required**. |
| `qspi-quad-mode` | `boolean` | ```text If specified, Use QSPI in quad mode (4 IO lines) otherwise in SPI mode (2 IO lines - MOSI & MISO). ``` |
| `qspi-rx-delay` | `int` | ```text Number of clock cycles from the rising edge of the SPI clock until the input serial data is sampled. ``` |
| `qspi-cpha` | `boolean` | ```text Set to indicate phase starts with asserted half-phase (CPHA=1). The driver using this property must also use `cpol`. ``` |
| `qspi-cpol` | `boolean` | ```text Set to indicate that the clock leading edge is falling (CPOL=1). The driver using this property requires also use `cpha`. ``` |
| `iovdd-ctrl-gpios` | `phandle-array` | ```text GPIO of the SoC controlling IO_VDD Control pin of the nRF70 ```  This property is **required**. |
| `bucken-gpios` | `phandle-array` | ```text GPIO of the SoC controlling BUCK_EN pin of the nRF70 ```  This property is **required**. |
| `host-irq-gpios` | `phandle-array` | ```text GPIO of the SoC controlling the HOST_IRQ pin of the nRF70 ```  This property is **required**. |
| `srrf-switch-gpios` | `phandle-array` | ```text GPIO of the RF Switch to control SR RF output to either SR Antenna or shared Antenna with Wi-Fi ``` |
| `wifi-max-tx-pwr-2g-dsss` | `int` | ```text Maximum transmit power allowed in 2.4GHz band for DSSS/CCK rates ```  This property is **required**. |
| `wifi-max-tx-pwr-2g-mcs0` | `int` | ```text Maximum transmit power allowed in 2.4GHz band for MCS0 ```  This property is **required**. |
| `wifi-max-tx-pwr-2g-mcs7` | `int` | ```text Maximum transmit power allowed in 2.4GHz band for MCS7 ```  This property is **required**. |
| `wifi-max-tx-pwr-5g-low-mcs0` | `int` | ```text Maximum transmit power allowed in 5GHz band MCS0 low sub-band ```  This property is **required**. |
| `wifi-max-tx-pwr-5g-low-mcs7` | `int` | ```text Maximum transmit power allowed in 5GHz band MCS7 low sub-band ```  This property is **required**. |
| `wifi-max-tx-pwr-5g-mid-mcs0` | `int` | ```text Maximum transmit power allowed in 5GHz band MCS0 mid sub-band ```  This property is **required**. |
| `wifi-max-tx-pwr-5g-mid-mcs7` | `int` | ```text Maximum transmit power allowed in 5GHz band MCS7 mid sub-band ```  This property is **required**. |
| `wifi-max-tx-pwr-5g-high-mcs0` | `int` | ```text Maximum transmit power allowed in 5GHz band MCS0 high sub-band ```  This property is **required**. |
| `wifi-max-tx-pwr-5g-high-mcs7` | `int` | ```text Maximum transmit power allowed in 5GHz band MCS7 high sub-band ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf7000-qspi” compatible.

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
