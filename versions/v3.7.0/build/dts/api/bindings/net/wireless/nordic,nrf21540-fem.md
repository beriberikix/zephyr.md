---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/net/wireless/nordic,nrf21540-fem.html
original_path: build/dts/api/bindings/net/wireless/nordic,nrf21540-fem.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf21540-fem

Vendor: [Nordic Semiconductor](../../../bindings.md#dt-vendor-nordic)

## Description

```text
This is a representation of the nRF21540 Radio Front-End module.

See the "nordic,nrf21540-fem-spi" binding to configure the SPI
interface. The SPI interface should be configured as a child node
of the SPI bus you have connected to the FEM. Then you "connect"
the FEM and SPI configurations using the spi-if property.

Here is an example nRF21540 configuration with a SPI interface
selected, using the SPIM0 peripheral found on several nRF5 SoCs:

  &spi0 {
          compatible = "nordic,nrf-spim";
          status = "okay";
          cs-gpios = <&gpio1 3 GPIO_ACTIVE_LOW>;
          /* ... MISO/MOSI/SCK pin configuration goes here ... */

          my_spi_if: nrf21540-spi@0 {
                  compatible = "nordic,nrf21540-fem-spi";
                  reg = <0>;
                  spi-max-frequency = <8000000>;
          };
  };

  nrf_radio_fem: nrf21540 {
          compatible = "nordic,nrf21540-fem";
          tx-en-gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
          rx-en-gpios = <&gpio0 5 GPIO_ACTIVE_HIGH>;
          spi-if = <&my_spi_if>;
          pdn-gpios = <...>;
          ant-sel-gpios = <...>;
          mode-gpios = <...>;
          /* ... other nRF21540 properties go here ... */
  };

  &radio {
          fem = <&nrf_radio_fem>;
  };

In the above example, the nRF21540 is configured for use with:

  - TX_EN on P0.2 (from 'tx-en-gpios')
  - RX_EN on P0.5 (from 'rx-en-gpios')
  - SPI communication via SPIM0 (the bus, or parent node, of
    the 'my_spi_if' node
  - CSN on P1.3 (from index 0 in the bus node's 'cs-gpios' property)

You must perform any additional required SPI pin configuration
(nRF21540 MISO, MOSI, and SCK pins) within the SPI bus node
('spi0' in the above example). See your SPI node's binding for
details on these pin mux properties. You can use any SPI node
available in your SoC's devicetree.

Configure any other nRF21540 pins as needed using 'pdn-gpios',
'ant-sel-gpios', and 'mode-gpios' properties. If unsure about the
format, use 'tx-en-gpios' as an example.

Finally, the nRF5 SoC's radio peripheral is set up for use with
the nRF21540 via the 'fem' property in the 'radio' node.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `tx-en-gpios` | `phandle-array` | ```text GPIO of the SOC controlling TX_EN pin of the nRF21540 ``` |
| `rx-en-gpios` | `phandle-array` | ```text GPIO of the SOC controlling RX_EN pin of the nRF21540 ``` |
| `pdn-gpios` | `phandle-array` | ```text GPIO of the SOC controlling PDN pin of the nRF21540 ``` |
| `ant-sel-gpios` | `phandle-array` | ```text GPIO of the SOC controlling ANT-SEL pin of the nRF21540 ``` |
| `mode-gpios` | `phandle-array` | ```text GPIO of the SOC controlling MODE pin of the nRF21540 ``` |
| `spi-if` | `phandle` | ```text Reference to the nordic,nrf21540-fem-spi SPI bus interface.  This must be present to support SPI control of the FEM. ``` |
| `tx-en-settle-time-us` | `int` | ```text Settling time in microseconds from state PG to TX.  Default value is based on Table 6 of the nRF21540 Product Specification (v1.0), and can be overridden for tuned configurations. ```  Default value: `11` |
| `rx-en-settle-time-us` | `int` | ```text Settling time in microseconds from state PG to RX.  Default value is based on Table 6 of the nRF21540 Product Specification (v1.0), and can be overridden for tuned configurations. ```  Default value: `11` |
| `pdn-settle-time-us` | `int` | ```text Settling time in microseconds from state PD to PG.  Default value is based on Table 6 of the nRF21540 Product Specification (v1.0), and can be overridden for tuned configurations. ```  Default value: `18` |
| `trx-hold-time-us` | `int` | ```text Power-off time in microseconds when changing from RX or TX to PG.  Default value is based on Table 6 of the nRF21540 Product Specification (v1.0), and can be overridden for tuned configurations. ```  Default value: `3` |
| `supply-voltage-mv` | `int` | ```text nRF21540 supply voltage in mV.  This is used if compensation for nRF21540 supply voltage is supported by software. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf21540-fem” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
