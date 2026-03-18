---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/mfd/nxp,sc18im704.html
original_path: build/dts/api/bindings/mfd/nxp,sc18im704.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,sc18im704 (on uart bus)

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

These nodes are “nxp,sc18im704” bus nodes.

```text
NXP SC18IM704 UART to I2C/GPIO bridge.

The SC18IM704 supports both an external I2C and GPIO controller. These
controllers have to be added to the Device Tree as children. While the
device itself has to be a child of a UART controller.

An example configuration:

&uart0 {
  status = "okay";
  pinctrl-0 = <&uart0_default>;
  pinctrl-names = "default";

  sc18im704: sc18im704 {
    compatible = "nxp,sc18im704";
    status = "okay";
    target-speed = <115200>;
    reset-gpios = <&gpio1 15 (GPIO_ACTIVE_LOW | GPIO_PULL_UP)>;

    i2c_ext: sc18im704_i2c {
      compatible = "nxp,sc18im704-i2c";
      status = "okay";
      #address-cells = <1>;
      #size-cells = <0>;
    };

    gpio_ext: sc18im704_gpio {
      compatible = "nxp,sc18im704-gpio";
      status = "okay";
      gpio-controller;
      #gpio-cells = <2>;
      ngpios = <8>;
    };
  };
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `reset-gpios` | `phandle-array` | ```text Driver reset pin of the bridge. If connected directly to the MCU, this pin should be configured as active low. ``` |
| `target-speed` | `int` | ```text UART baudrate which will be requested and to which UART interface will be reconfigured during initialization phase. ```  Legal values: `1200`, `2400`, `4800`, `9600`, `14400`, `19200`, `28800`, `38400`, `57600`, `76800`, `115200`, `230400`, `460800` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,sc18im704” compatible.

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
