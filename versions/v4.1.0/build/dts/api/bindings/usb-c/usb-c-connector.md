---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/usb-c/usb-c-connector.html
original_path: build/dts/api/bindings/usb-c/usb-c-connector.html
---

# usb-c-connector

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

Note

An implementation of a driver matching this compatible is available in
[subsys/usb/usb\_c/usbc\_stack.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/usb/usb_c/usbc_stack.c).

## Description

```text
A USB Type-C connector node represents a physical USB Type-C connector.
It should be a child of a USB-C interface controller or a separate node
when it is attached to both MUX and USB-C interface controller.

This is based on Linux, documentation:
  https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings/connector/usb-connector.yaml?h=v5.19&id=3d7cb6b04c3f3115719235cc6866b10326de34cd

Example:

USB-C connector attached to a STM32 UCPD typec port controller, which has
power delivery support and enables SINK.

vbus1: vbus {
    compatible = "zephyr,usb-c-vbus-adc";
    io-channels = <&adc2 8>;
    output-ohms = <49900>;
    full-ohms = <(330000 + 49900)>;
};

ports {
    #address-cells = <1>;
    #size-cells = <0>;
    port1: usb-c-port@1 {
        compatible = "usb-c-connector";
        reg = <1>;
        tcpc = <&ucpd1>;
        vbus = <&vbus1>;
        power-role = "sink";
        sink-pdos = <PDO_FIXED(5000, 2000, PDO_FIXED_USB_COMM)
                     PDO_VAR(5000, 12000, 2000)>;
        op-sink-microwatt = <10000000>;
    };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `tcpc` | `phandle` | ```text Type-C Port Controller for this port. ```  This property is **required**. |
| `vbus` | `phandle` | ```text VBUS measurement and control for this port. ```  This property is **required**. |
| `ppc` | `phandle` | ```text Power path controller for this port ``` |
| `power-role` | `string` | ```text The Port power role. "dual" for Dual Role Port. ```  This property is **required**.  Legal values: `'sink'`, `'source'`, `'dual'` |
| `try-power-role` | `string` | ```text Preferred power role. ```  Legal values: `'sink'`, `'source'`, `'dual'` |
| `data-role` | `string` | ```text The Port data role.   * "host" for Downstream Facing Port (DFP)   * "device" for Upstream Facing Port (UFP)   * "dual" for Dual Role Data ```  Legal values: `'host'`, `'device'`, `'dual'` |
| `typec-power-opmode` | `string` | ```text Initial Type C advertised power, determined by the Rp when operating as a Source. * "default" corresponds to default USB voltage and current   defined by the  USB 2.0 and USB 3.2 specifications.     * 5V@500mA for USB 2.0     * 5V@900mA for USB 3.2 single-lane     * 5V@1500mA for USB 3.2 dual-lane * "1.5A" and "3.0A", 5V@1.5A and 5V@3.0A. ```  Legal values: `'default'`, `'1.5A'`, `'3.0A'` |
| `pd-disable` | `boolean` | ```text Disables power delivery when true ``` |
| `source-pdos` | `array` | ```text An array of source Power Data Objects (PDOs). Use the following macros to define the PDOs, defined in dt-bindings/usb-c/pd.h.   * PDO_FIXED   * PDO_BATT   * PDO_VAR   * PDO_PPS_APDO Valid range: 1 - 7 ``` |
| `sink-pdos` | `array` | ```text An array of sink Power Data Objects (PDOs). Use the following macros to define the PDOs, defined in dt-bindings/usb-c/pd.h.   * PDO_FIXED   * PDO_BATT   * PDO_VAR   * PDO_PPS_APDO Valid range: 1 - 7 ``` |
| `sink-vdos` | `array` | ```text An array of sink Vendor Defined Objects (VDOs). Use the following macros to define the VDOs, defined in dt-bindings/usb-c/pd.h.   * VDO_IDH   * VDO_CERT   * VDO_PRODUCT   * VDO_UFP   * VDO_DFP   * VDO_PCABLE   * VDO_ACABLE   * VDO_VPD Valid range: 3 - 6 ``` |
| `sink-vdos-v1` | `array` | ```text An array of sink Vendor Defined Objects (VDOs). Use the following macros to define the VDOs, defined in dt-bindings/usb-c/pd.h.   * VDO_IDH   * VDO_CERT   * VDO_PRODUCT   * VDO_CABLE   * VDO_AMA Valid range: 3 - 6 ``` |
| `op-sink-microwatt` | `int` | ```text Minimum power, in microwatts, needed by the sink. A Capability Mismatch is sent to the Source if the power can't be met. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “usb-c-connector” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
