---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/wifi/infineon,airoc-wifi.html
original_path: build/dts/api/bindings/wifi/infineon,airoc-wifi.html
---

# infineon,airoc-wifi

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/wifi/infineon/airoc\_wifi.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/infineon/airoc_wifi.c).

## Description

```text
AIROC Wi-Fi Connectivity.

Example of enabling AIROC Wi-Fi device (for SDIO):
  &sdhc0 {
    status = "okay";

    /* SDIO pins */
    pinctrl-0 = <&p2_4_sdio_cmd &p2_5_sdio_clk &p2_0_sdio_data0
          &p2_1_sdio_data1 &p2_2_sdio_data2 &p2_3_sdio_data3>;
    pinctrl-names = "default";

    /* Wifi configuration */
    airoc-wifi {
      status = "okay";
      compatible = "infineon,airoc-wifi-sdio";

      /* Wi-Fi control gpios */
      wifi-reg-on-gpios    = <&gpio_prt2 6 GPIO_ACTIVE_HIGH>;
      wifi-host-wake-gpios = <&gpio_prt0 4 GPIO_ACTIVE_HIGH>;
    };
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `wifi-reg-on-gpios` | `phandle-array` | ```text Power-up/down gpio to control the internal regulators used by the WiFi section of AIROC Wi-Fi device. ``` |
| `wifi-host-wake-gpios` | `phandle-array` | ```text Host wake-up gpio. Signal from the AIROC Wi-Fi device to the host indicating that the device requires attention. ``` |
| `wifi-dev-wake-gpios` | `phandle-array` | ```text WiFi device wake-up gpio. Signal from the host to the AIROC Wi-Fi device indicating that the host requires attention. ``` |
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
may apply to the “infineon,airoc-wifi” compatible.

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
