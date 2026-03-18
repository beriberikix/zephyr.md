---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/can/ti,tcan4x5x.html
original_path: build/dts/api/bindings/can/ti,tcan4x5x.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ti,tcan4x5x (on spi bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

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
      sample-point = <875>;
      sample-point-data = <875>;
      bus-speed = <125000>;
      bus-speed-data = <1000000>;
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
| `bus-speed-data` | `int` | ```text Initial data phase bitrate in bit/s. ```  This property is **required**. |
| `sample-point-data` | `int` | ```text Initial data phase sample point in per mille (e.g. 875 equals 87.5%).  This property is required unless the timing is specified using time quanta based properties (`sjw-data`, `prop-seg-data`, `phase-seg1-data`, and `phase-seg2-data`).  If this property is present, the time quanta based timing properties are ignored. ``` |
| `tx-delay-comp-offset` | `int` |  |
| `bus-speed` | `int` | ```text Initial bitrate in bit/s. ```  This property is **required**. |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  This property is required unless the timing is specified using time quanta based properties (`sjw`, `prop-seg`, `phase-seg1`, and `phase-seg2`).  If this property is present, the time quanta based timing properties are ignored. ``` |
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
| `sjw-data` | `int` | ```text Initial time quanta of resynchronization jump width for the data phase (ISO11898-1:2015).  Deprecated in favor of automatic calculation of a suitable default SJW based on existing timing parameters. Default of 1 matches the default value previously used for all in-tree CAN controller devicetree instances.  Applications can still manually set the SJW using the CAN timing APIs. ```  Default value: `1` |
| `prop-seg-data` | `int` | ```text Initial time quanta of propagation segment for the data phase (ISO11898-1:2015). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg1-data` | `int` | ```text Initial time quanta of phase buffer 1 segment for the data phase (ISO11898-1:2015). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg2-data` | `int` | ```text Initial time quanta of phase buffer 2 segment for the data phase (ISO11898-1:2015). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `sjw` | `int` | ```text Initial time quanta of resynchronization jump width (ISO 11898-1).  Deprecated in favor of automatic calculation of a suitable default SJW based on existing timing parameters. Default of 1 matches the default value previously used for all in-tree CAN controller devicetree instances.  Applications can still manually set the SJW using the CAN timing APIs. ```  Default value: `1` |
| `prop-seg` | `int` | ```text Initial time quanta of propagation segment (ISO 11898-1). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg1` | `int` | ```text Initial time quanta of phase buffer 1 segment (ISO 11898-1). Deprecated in favor of setting advanced timing parameters from the application. ``` |
| `phase-seg2` | `int` | ```text Initial time quanta of phase buffer 2 segment (ISO 11898-1). Deprecated in favor of setting advanced timing parameters from the application. ``` |

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `max-bitrate` | `int` | ```text The maximum bitrate supported by the CAN transceiver in bits/s. ```  This property is **required**. |
