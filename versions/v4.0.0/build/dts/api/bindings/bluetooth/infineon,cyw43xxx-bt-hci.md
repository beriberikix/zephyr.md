---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/bluetooth/infineon,cyw43xxx-bt-hci.html
original_path: build/dts/api/bindings/bluetooth/infineon,cyw43xxx-bt-hci.html
---

# infineon,cyw43xxx-bt-hci

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/bluetooth/hci/h4\_ifx\_cyw43xxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/h4_ifx_cyw43xxx.c).

## Description

```text
CYW43xxx Connectivity that uses Zephyr's Bluetooth Host Controller Interface UART
driver.

Example of enabling CYW43xxx device:

  &uart2 {
    status = "okay";
    current-speed = <115200>;

    /* HCI-UART pins*/
    pinctrl-0 = <&p3_1_scb2_uart_tx &p3_0_scb2_uart_rx
                 &p3_2_scb2_uart_rts &p3_3_scb2_uart_cts>;
    pinctrl-names = "default";

    /* HW Flow control must be enabled for HCI H4 */
    hw-flow-control;

    bt-hci {
      status = "okay";
      compatible = "infineon,cyw43xxx-bt-hci";
      bt-reg-on-gpios = <&gpio_prt3 4 (GPIO_ACTIVE_HIGH)>;

      fw-download-speed = <3000000>;
    };
  };

NOTE1: The UART bus speed (current_speed) for zephyr_bt_uart should be the same
       as the default baudrate defined in CYW43xx firmware (default 115200).

NOTE2: Use fw-download-speed and hci-operation-speed properties to configure UART
       speeds for firmware download (fw-download-speed) and HCI operation
       (hci-operation-speed).
       If hci-operation-speed or fw-download-speed are not defined in bt-hci node,
       cyw43xx driver will use bus/current-speed as default speed.

NOTE3: CYW43xxx requires fetch binary files of BT controller. To fetch binary blobs:
       west blobs fetch hal_infineon
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `bt-reg-on-gpios` | `phandle-array` | ```text Power-up/down gpio to control the internal regulators used by the Bluetooth section of CYW43xx device. ``` |
| `bt-dev-wake-gpios` | `phandle-array` | ```text Bluetooth device wake-up gpio. Signal from the host to the CYW43xx indicating that the host requires attention. ``` |
| `bt-host-wake-gpios` | `phandle-array` | ```text Host wake-up gpio. Signal from the CYW43xx to the host indicating that the CYW43xx requires attention. ``` |
| `hci-operation-speed` | `int` | ```text HCI UART boudrate for feature operation. If not defined bus/current-speed will be used as default. ``` |
| `fw-download-speed` | `int` | ```text HCI UART boudrate for FW download operation. If not defined bus/current-speed will be used as default. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,cyw43xxx-bt-hci” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
