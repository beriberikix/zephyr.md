---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/can/ti,tcan4x5x.html
original_path: build/dts/api/bindings/can/ti,tcan4x5x.html
---

# ti,tcan4x5x (on spi bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/can/can\_tcan4x5x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/can_tcan4x5x.c).

## Description

```text
Texas Instruments TCAN4x5x SPI CAN FD controller.

Example:
  &spi0 {
    tcan4x5x: can@0 {
      compatible = ti,tcan4x5x";
      reg = <0>;
      spi-max-frequency = <18000000>;
      clock-frequency = <40000000>;
      device-state-gpios = <&gpio0 0 GPIO_ACTIVE_LOW>;
      device-wake-gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>;
      reset-gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
      int-gpios = <&gpio0 3 GPIO_ACTIVE_LOW>;
      bosch,mram-cfg = <0x0 15 15 5 5 0 10 10>;
      status = "okay";

      can-transceiver {
        max-bitrate = <8000000>;
      };
    };
  };
```

## Properties

### Top level properties

These property descriptions apply to “ti,tcan4x5x”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text TCAN4x5x oscillator clock frequency in Hz (20MHz or 40MHz). ```  This property is **required**.  Legal values: `20000000`, `40000000` |
| `device-state-gpios` | `phandle-array` | ```text GPIO connected to the TCAN4x5x nWKRQ output. This signal is active low. ``` |
| `device-wake-gpios` | `phandle-array` | ```text GPIO connected to the TCAN4x5x WAKE input. This signal is high-voltage, active high. ``` |
| `reset-gpios` | `phandle-array` | ```text GPIO connected to the TCAN4x5x RST input. This signal is active high. ``` |
| `int-gpios` | `phandle-array` | ```text GPIO connected to the TCAN4x5x nINT interrupt output. This signal is open-drain, active low. ```  This property is **required**. |
| `bosch,mram-cfg` | `array` | ```text Bosch M_CAN message RAM configuration. The cells in the array have the following format:  <offset std-filter-elements ext-filter-elements rx-fifo0-elements rx-fifo1-elements rx-buffer-elements tx-event-fifo-elements tx-buffer-elements>  The 'offset' is an address offset of the message RAM where the following elements start from. This is normally set to 0x0 when using a non-shared message RAM. The remaining cells specify how many elements are allocated for each filter type/FIFO/buffer.  The Bosch M_CAN IP supports the following elements: 11-bit Filter    0-128 elements / 0-128 words 29-bit Filter     0-64 elements / 0-128 words Rx FIFO 0                   0-64 elements / 0-1152 words Rx FIFO 1                   0-64 elements / 0-1152 words Rx Buffers          0-64 elements / 0-1152 words Tx Event FIFO     0-32 elements / 0-64 words Tx Buffers          0-32 elements / 0-576 words ```  This property is **required**. |
| `bitrate-data` | `int` | ```text Initial data phase bitrate in bit/s.  If this is unset, the initial data phase bitrate is set to CONFIG_CAN_DEFAULT_BITRATE_DATA. ``` |
| `sample-point-data` | `int` | ```text Initial data phase sample point in per mille (e.g. 875 equals 87.5%).  If this is unset (or if it is set to 0), the initial sample point will default to 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. ``` |
| `bitrate` | `int` | ```text Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  If this is unset (or if it is set to 0), the initial sample point will default to 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. ``` |
| `phys` | `phandle` | ```text Actively controlled CAN transceiver.  Example:   transceiver0: can-phy0 {     compatible = "nxp,tja1040", "can-transceiver-gpio";     standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;     max-bitrate = <1000000>;     #phy-cells = <0>;   };    &can0 {     status = "okay";      phys = <&transceiver0>;   }; ``` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bus-speed-data` | `int` | ```text Deprecated. This property has been renamed to bitrate-data.  Initial data phase bitrate in bit/s.  If this is unset, the initial data phase bitrate is set to CONFIG_CAN_DEFAULT_BITRATE_DATA. ``` |
| `bus-speed` | `int` | ```text Deprecated. This property has been renamed to bitrate.  Initial bitrate in bit/s. If this is unset, the initial bitrate is set to CONFIG_CAN_DEFAULT_BITRATE. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,tcan4x5x” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `min-bitrate` | `int` | ```text The minimum bitrate supported by the CAN transceiver in bits/s. ``` |
| `max-bitrate` | `int` | ```text The maximum bitrate supported by the CAN transceiver in bits/s. ```  This property is **required**. |
