---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/net/wireless/nordic,nrf-radio.html
original_path: build/dts/api/bindings/net/wireless/nordic,nrf-radio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-radio

Vendor: [Nordic Semiconductor](../../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic nRF family RADIO peripheral.

This controls the 2.4 GHz radio transceiver on nRF5x
SoCs, which is available for use with Bluetooth, 802.15.4,
and proprietary wireless protocols (not all of these
protocols are available on all SoCs; consult the product
specifications for details).

This binding is not relevant to the nRF91x baseband radio.

Front-End Module (FEM) support
------------------------------

External front-end modules are range extenders used for boosting
the link robustness and link budget of wireless SoCs. If your
system includes an external FEM, set it up in the devicetree using
this binding's 'fem' property, like this example:

  &radio {
          fem = <&nrf_radio_fem>;
  };

  nrf_radio_fem: my-fem {
          compatible = "...";
          ....
  };

Currently supported "compatible" properties for the FEM node are:

  - generic-fem-two-ctrl-pins
  - nordic,nrf21540-fem

Refer to the bindings for these compatibles for more information
about how to configure the FEM.

Direction Finding Extension
---------------------------

Some radios support the Bluetooth Direction Finding Extension (DFE).
The 'dfe-supported' property will be set when it is available.
In this case, the 'dfegpio[n]-gpios' properties configure GPIO pins
to use to drive antenna switching.

Each dfegpio[n]-gpios property which is set is used to initialize the
corresponding PSEL.DFEGPIO[n] register.

None of the dfegpio[n]-gpios properties are marked 'required',
since which PSEL.DFEGPIO[n] registers will be used to drive
antenna switches depends on the use case. Nevertheless, at least two
antennas must be available to use DFE.

That in turn means that at least one dfegpio[n]-gpios
property must be provided if DFE is used, to give the radio the
possibility to switch between two antennas. To use 12 antennas,
4 GPIOs must be provided (since 4 GPIO pins support switching up to
16 antennas).

GPIOs are used in order, following the indices of the dfegpio[n]-gpios
properties. The order is important because it affects the mapping of
antenna switch patterns to GPIOs.

Antenna switching patterns
--------------------------

An antenna switching pattern is a binary number where each bit is
applied to a particular antenna GPIO pin. For example, the pattern
0x3 means that antenna GPIOs at indexes 0 and 1 will be set, while
the following are left unset.

The number of GPIOs specified with dfegpio[n]-gpios properties
affects the allowed pattern values. For example, when using four
GPIOs, the pattern count cannot be greater than 16, and the
maximum allowed value is 15.

Antenna switch patterns are stored in DFE internal memory by
writes to the SWITCHPATTERN register. DFE handling code applies
antenna switch patterns during Constant Tone Extension (CTE)
receive (Angle of Arrival mode) or transmission (Angle of
Departure mode) procedure.

DFE States
----------

There are four states of DFE operation:

* Idle: in this state, PDU transmission happens.
  DFE uses SWITCHPATTERN[0] to select the antenna in this state.
  (The 'dfe-pdu-antenna' property value described below is stored
  in SWITCHPATTERN[0] by the radio controller code.)

* Guard: in this state, DFE prepares for reception or transmission
  of CTE. For this state, DFE selects the antenna by applying
  SWITCHPATTERN[1].

* Reference: in this state, DFE starts to receive or transmit CTE.
  In AoA mode, DFE collects reference IQ samples. The selected
  antenna is the same as in the guard state.

* Switch-sample: in this state, actual antenna switching happens.
  DFE selects antennas by applying SWITCHPATTERN[2..N]. If the
  number of switch-sample periods is greater than the number of
  stored switching patterns, DFE loops back to SWITCHPATTERN[2].
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `fem` | `phandle` | ```text Phandle linking the RADIO node to its external front-end module. ``` |
| `coex` | `phandle` | ```text Phandle linking the RADIO node to the external radio coexistence arbitrator. ``` |
| `dfe-supported` | `boolean` | ```text If set, the radio hardware supports the Direction Finding Extension. This property should be treated as read-only and should not be overridden; the correct value is provided for your target's SoC already. ``` |
| `dfe-antenna-num` | `int` | ```text Number of available antennas for the Direction Finding Extension.  This should only be set if dfe-supported is true. If you set this property, the value must be at least two. ``` |
| `dfe-pdu-antenna` | `int` | ```text Antenna switch pattern to be used for transmission of PDU before start of transmission of Constant Tone Extension.  This should only be set if dfe-supported is true.  This pattern is stored in SWITCHPATTERN[0] before actual antenna switching patterns. This pattern will also be used to drive GPIOs when the radio releases control of GPIOs used to switch antennas. ``` |
| `dfegpio0-gpios` | `phandle-array` | ```text Pin select for DFE pin 0. This should only be set if dfe-supported is true.  For example, to use P0.2 on an nRF5x SoC:    dfegpio1-gpios = <&gpio0 2 0>;  To use P1.4:    dfegpio1-gpios = <&gpio1 4 0>;  Note the last 'flags' cell in the property is not used, and should be set to 0 as shown. ``` |
| `dfegpio1-gpios` | `phandle-array` | ```text Pin select for DFE pin 1. See description for dfegpio0-gpios. ``` |
| `dfegpio2-gpios` | `phandle-array` | ```text Pin select for DFE pin 2. See description for dfegpio0-gpios. ``` |
| `dfegpio3-gpios` | `phandle-array` | ```text Pin select for DFE pin 3. See description for dfegpio0-gpios. ``` |
| `dfegpio4-gpios` | `phandle-array` | ```text Pin select for DFE pin 4. See description for dfegpio0-gpios. ``` |
| `dfegpio5-gpios` | `phandle-array` | ```text Pin select for DFE pin 5. See description for dfegpio0-gpios. ``` |
| `dfegpio6-gpios` | `phandle-array` | ```text Pin select for DFE pin 6. See description for dfegpio0-gpios. ``` |
| `dfegpio7-gpios` | `phandle-array` | ```text Pin select for DFE pin 7. See description for dfegpio0-gpios. ``` |
| `ieee802154-supported` | `boolean` | ```text If set, indicates that the radio hardware supports the IEEE 802.15.4 mode. ``` |
| `ble-2mbps-supported` | `boolean` | ```text If set, indicates that the radio hardware supports the 2 Mbps BLE mode. ``` |
| `ble-coded-phy-supported` | `boolean` | ```text If set, indicates that the radio hardware supports coded BLE PHY. ``` |
| `tx-high-power-supported` | `boolean` | ```text If set, indicates that the radio hardware supports high TX power settings. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-radio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
