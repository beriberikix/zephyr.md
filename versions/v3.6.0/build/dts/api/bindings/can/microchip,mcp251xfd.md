---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/can/microchip,mcp251xfd.html
original_path: build/dts/api/bindings/can/microchip,mcp251xfd.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# microchip,mcp251xfd (on spi bus)

Vendor: [Microchip Technology Inc.](../../bindings.md#dt-vendor-microchip)

## Description

```text
Microchip MCP251XFD SPI CAN FD controller

The MCP251XFD node is defined on an SPI bus. An example
configuration is:

&mikrobus_spi {
    cs-gpios = <&mikrobus_header 2 GPIO_ACTIVE_LOW>;

    mcp2518fd_mikroe_mcp2518fd_click: mcp2518fd@0 {
        compatible = "microchip,mcp251xfd";
        status = "okay";

        spi-max-frequency = <18000000>;
        int-gpios = <&mikrobus_header 7 GPIO_ACTIVE_LOW>;
        reg = <0x0>;
        osc-freq = <40000000>;

        bus-speed = <125000>;
        sample-point = <875>;
        bus-speed-data = <1000000>;
        sample-point-data = <875>;
    };
};
```

## Properties

### Top level properties

These property descriptions apply to “microchip,mcp251xfd”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `osc-freq` | `int` | ```text Frequency of the external oscillator in Hz. ```  This property is **required**. |
| `int-gpios` | `phandle-array` | ```text The interrupt signal from the controller is active low in push-pull mode. The property value should ensure the flags properly describe the signal that is presented to the driver. ```  This property is **required**. |
| `pll-enable` | `boolean` | ```text Enables controller PLL, which multiplies input clock frequency by 10. This parameter also implicitly sets whether the clock is from the PLL output or directly from the oscillator. If this option is enabled the clock source is the PLL, otherwise its the oscillator. ``` |
| `timestamp-prescaler` | `int` | ```text Prescaler value for computing the timestamps of received messages. The timestamp counter is derived from the internal clock divided by this value. Valid range is [1, 1024]. ```  Default value: `1` |
| `sof-on-clko` | `boolean` | ```text Output start-of-frame (SOF) signal on the CLKO pin every time a Start bit of a CAN message is transmitted or received. If this option is not set, then an internal clock (typically 40MHz or 20MHz) will be output on CLKO pin instead. ``` |
| `clko-div` | `int` | ```text The factor to divide the system clock for CLKO pin. ```  Default value: `10`  Legal values: `1`, `2`, `4`, `10` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `bus-speed-data` | `int` | ```text Initial data phase bitrate in bit/s. ```  This property is **required**. |
| `sample-point-data` | `int` | ```text Initial data phase sample point in per mille (e.g. 875 equals 87.5%).  This property is required unless the timing is specified using time quanta based properties (`sjw-data`, `prop-seg-data`, `phase-seg1-data`, and `phase-seg2-data`).  If this property is present, the time quanta based timing properties are ignored. ``` |
| `tx-delay-comp-offset` | `int` |  |
| `bus-speed` | `int` | ```text Initial bitrate in bit/s. ```  This property is **required**. |
| `sample-point` | `int` | ```text Initial sample point in per mille (e.g. 875 equals 87.5%).  This property is required unless the timing is specified using time quanta based properties (`sjw`, `prop-seg`, `phase-seg1`, and `phase-seg2`).  If this property is present, the time quanta based timing properties are ignored. ``` |
| `phys` | `phandle` | ```text Actively controlled CAN transceiver.  Example:   transceiver0: can-phy0 {     compatible = "nxp,tja1040", "can-transceiver-gpio";     standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;     max-bitrate = <1000000>;     #phy-cells = <0>;   };    &can0 {     status = "okay";      phys = <&transceiver0>;   }; ``` |

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
may apply to the “microchip,mcp251xfd” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `max-bitrate` | `int` | ```text The maximum bitrate supported by the CAN transceiver in bits/s. ```  This property is **required**. |
