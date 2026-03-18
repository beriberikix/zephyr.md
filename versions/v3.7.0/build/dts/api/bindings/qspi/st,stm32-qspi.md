---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/qspi/st,stm32-qspi.html
original_path: build/dts/api/bindings/qspi/st,stm32-qspi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# st,stm32-qspi

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

These nodes are “qspi” bus nodes.

```text
STM32 QSPI device representation. A stm32 quadspi node would typically
looks to this:

    &quadspi {
        pinctrl-0 = <&quadspi_clk_pe10 &quadspi_ncs_pe11
                     &quadspi_bk1_io0_pe12 &quadspi_bk1_io1_pe13
                     &quadspi_bk1_io2_pe14 &quadspi_bk1_io3_pe15>;

        dmas = <&dma1 5 5 0x0000 0x03>;
        dma-names = "tx_rx";

        status = "okay";
    };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `dual-flash` | `boolean` | ```text configuration to enable the dual flash mode of the QSPI peripheral where two external quad SPI Flash memories (FLASH 1 and FLASH 2) are used in order to send/receive 8 bits (or 16 bits in DDR mode) every cycle, effectively doubling the throughput as well as the capacity. When true, the Flash ID number <flash-id> is useless. ``` |
| `flash-id` | `int` | ```text Flash ID number. This number, if defined, helps to select the right QSPI GPIO banks (defined as 'quadspi_bk[1/2]' in pinctrl property) to communicate with flash memory. Valid only if the <dual-flash> is not set.  For example    flash-id = <2>; ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-qspi” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text Optional DMA channel specifier. If DMA should be used, specifier should hold a phandle reference to the dma controller (not the DMAMUX even if present), the channel number, the slot number, channel configuration and finally features. (depending on the type of DMA: 'features' is optional)  When a DMAMUX is present and enabled, the channel is the dma one (not dmamux channel). The request is given by the DMAMUX (no 'features' required).  For example with DMA 2 for TX/RX on QSPI like stm32l496 (no 'features')    /* select DMA2 channel 7 request 3 for QUADSPI */    dmas = <&dma2 7 3 (STM32_DMA_PERIPH_TX | STM32_DMA_PRIORITY_HIGH)>; For example with a DMAMUX for TX/RX on QSPI like stm32wb55  (no 'features')    /* select DMA2 channel 0, request 20 for QUADSPI */    dmas = <&dma2 0 20 (STM32_DMA_PERIPH_TX | STM32_DMA_PRIORITY_HIGH)>; ``` |
| `dma-names` | `string-array` | ```text DMA channel name. If DMA should be used, expected value is "tx_rx".  For example    dma-names = "tx_rx"; ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
