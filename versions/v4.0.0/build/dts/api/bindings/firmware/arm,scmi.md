---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/firmware/arm,scmi.html
original_path: build/dts/api/bindings/firmware/arm,scmi.html
---

# arm,scmi

Vendor: [ARM Ltd.](../../bindings.md#dt-vendor-arm)

Note

An implementation of a driver matching this compatible is available in
[drivers/firmware/scmi](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/firmware/scmi).

## Description

```text
System Control and Management Interface (SCMI) with doorbell
and shared memory (SHMEM) transport.

Devicetree example:
    #include <mem.h>

    scmi_res0: memory@44611000 {
        compatible = "arm,scmi-shmem";
        reg = <0x44611000 0x80>;
    };

    mu5: mailbox@44610000 {
        compatible = "nxp,mbox-imx-mu";
        reg = <0x44610000 DT_SIZE_K(4)>;
        interrupts = <205 0>;
        #mbox-cells = <1>;
    };

    scmi {
        compatible = "arm,scmi";
        shmem = <&scmi_res0>;
        mboxes = <&mu5 0>;
        mbox-names = "tx";

        protocol@14 {
            compatible = "arm,scmi-clock";
            reg = <0x14>;
            #clock-cells = <1>;
        };

        protocol@19 {
            compatible = "arm,scmi-pinctrl";
            reg = <0x19>;

            pinctrl {
                compatible = "nxp,imx95-pinctrl", "nxp,imx93-pinctrl";
            };
        };
    };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `shmem` | `phandle` | ```text Phandle to node describing TX channel shared memory area. This translates to a **single** SCMI transmit channel. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “arm,scmi” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `mboxes` | `phandle-array` | ```text List of mailbox channel specifiers. It should contain one or two specifiers:   1) tx - 1 mbox / 1 shmem (platform and agent use the same   mailbox channel for signaling)   2) tx_reply - 2 mbox / 1 shmem (platform and agent use different   mailbox channels for signaling) ```  This property is **required**. |
| `mbox-names` | `string-array` | ```text mailbox channel specifier names ```  This property is **required**. |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
