---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/net/wireless/nordic,nrf-radio.html
original_path: build/dts/api/bindings/net/wireless/nordic,nrf-radio.html
---

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
| `cs-supported` | `boolean` | ```text If set, the radio hardware supports the BLE Channel Sounding feature. This property should be treated as read-only and should not be overridden; the correct value is provided for your target's SoC already. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-radio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
