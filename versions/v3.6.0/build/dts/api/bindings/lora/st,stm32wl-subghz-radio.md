---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/lora/st,stm32wl-subghz-radio.html
original_path: build/dts/api/bindings/lora/st,stm32wl-subghz-radio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,stm32wl-subghz-radio (on spi bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32WL SUBGHZ Radio
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `power-amplifier-output` | `string` | ```text Selects between the low- and high-power power amplifier output pin. ```  This property is **required**.  Legal values: `'rfo-lp'`, `'rfo-hp'` |
| `rfo-lp-max-power` | `int` | ```text Maximum design power for the board's RFO_LP output matching network.  The default setting of +14 dBm is a prevalent board configuration; however, for optimal performance, it is advisable to align the value with the board's RF design.  See ST application note AN5457, chapter 5.1.2 for more information. ```  Default value: `14`  Legal values: `10`, `14`, `15` |
| `rfo-hp-max-power` | `int` | ```text Maximum design power for the board's RFO_HP output matching network.  The default setting of +22 dBm is a prevalent board configuration; however, for optimal performance, it is advisable to align the value with the board's RF design.  See ST application note AN5457, chapter 5.1.2 for more information. ```  Default value: `22`  Legal values: `14`, `17`, `20`, `22` |
| `reset-gpios` | `phandle-array` | ```text GPIO connected to the modem's NRESET signal.  This signal is open-drain, active-low as interpreted by the modem. ``` |
| `busy-gpios` | `phandle-array` | ```text GPIO connected to the modem's BUSY signal. ``` |
| `antenna-enable-gpios` | `phandle-array` | ```text Antenna power enable pin. ``` |
| `tx-enable-gpios` | `phandle-array` | ```text Antenna switch TX enable GPIO. If set, the driver tracks the state of the radio and controls the RF switch. ``` |
| `rx-enable-gpios` | `phandle-array` | ```text Antenna switch RX enable GPIO. If set, the driver tracks the state of the radio and controls the RF switch. ``` |
| `dio1-gpios` | `phandle-array` | ```text GPIO connected to DIO1. This GPIO will be used as a generic IRQ line from the chip. ``` |
| `dio2-tx-enable` | `boolean` | ```text Use DIO2 to drive an RF switch selecting between the TX and RX paths. When enabled, DIO2 goes high when the chip is transmitting. ``` |
| `dio3-tcxo-voltage` | `int` | ```text TCXO supply voltage controlled by DIO3 if present.  See constants in dt-bindings/lora/sx126x.h. ``` |
| `tcxo-power-startup-delay-ms` | `int` | ```text Startup delay to let the TCXO stabilize after TCXO power on. ``` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32wl-subghz-radio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `interrupts` | `array` | ```text Position of the "Radio IRQ, Busy" interrupt line. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
