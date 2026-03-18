---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/usb-c/usb-c-connector.html
original_path: build/dts/api/bindings/usb-c/usb-c-connector.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# usb-c-connector

Vendor: [Generic or vendor-independent](../../bindings.md#dt-no-vendor)

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
