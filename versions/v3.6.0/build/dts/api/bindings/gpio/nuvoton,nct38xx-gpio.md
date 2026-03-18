---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/gpio/nuvoton,nct38xx-gpio.html
original_path: build/dts/api/bindings/gpio/nuvoton,nct38xx-gpio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nuvoton,nct38xx-gpio

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
Nuvoton NCT38XX series I2C-based GPIO expander

This must be a child of the NCT38xx multi-function device.

Example:
  &i2c0_0 {
    nct3807@70 {
      compatible = "nuvoton,nct38xx";
      reg = <0x70>;

      nct3807-gpio {
        #address-cells = <1>;
        #size-cells = <0>;
        compatible = "nuvoton,nct38xx-gpio";

        gpio@0 {
          compatible = "nuvoton,nct38xx-gpio-port";
          reg = <0x0>;
          gpio-controller;
          #gpio-cells = <2>;
          ngpios = <8>;
          pin_mask = <0xff>;
          pinmux_mask = <0xf7>;
        };

        gpio@1 {
          compatible = "nuvoton,nct38xx-gpio-port";
          reg = <0x1>;
          gpio-controller;
          #gpio-cells = <2>;
          ngpios = <8>;
          pin_mask = <0xff>;
        };
      };
    };

    nct3808_0_P1@71 {
      compatible = "nuvoton,nct38xx";
      reg = <0x71>;

      nct3808-0-p1-gpio {
        #address-cells = <1>;
        #size-cells = <0>;
        compatible = "nuvoton,nct38xx-gpio";

        gpio@0 {
          compatible = "nuvoton,nct38xx-gpio-port";
          reg = <0x0>;
          gpio-controller;
          #gpio-cells = <2>;
          ngpios = <8>;
          pin_mask = <0xdc>;
          pinmux_mask = <0xff>;
        };
      };
    };

    nct3808_0_P2@75 {
      compatible = "nuvoton,nct38xx";
      reg = <0x75>;

      nct3808-0-P2-gpio {
        #address-cells = <1>;
        #size-cells = <0>;
        compatible = "nuvoton,nct38xx-gpio";

        gpio@0 {
          compatible = "nuvoton,nct38xx-gpio-port";
          reg = <0x0>;
          gpio-controller;
          #gpio-cells = <2>;
          ngpios = <8>;
          pin_mask = <0xdc>;
          pinmux_mask = <0xff>;
        };
      };
    };
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,nct38xx-gpio” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
