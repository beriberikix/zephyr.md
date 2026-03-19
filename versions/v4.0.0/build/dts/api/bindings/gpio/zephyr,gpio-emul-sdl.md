---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/gpio/zephyr,gpio-emul-sdl.html
original_path: build/dts/api/bindings/gpio/zephyr,gpio-emul-sdl.html
---

# zephyr,gpio-emul-sdl

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/gpio/gpio\_emul\_sdl.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_emul_sdl.c).

## Description

```text
SDL keyboard GPIO input Emulator

Simulate GPIO state/interrupts using SDL keyboard events. This node has
to be a child of a `zephyr,gpio-emul` compatible.
Add a list of scancodes for the desired keys to be mapped.

This driver uses USB HID scancodes, they are different from linux key codes,
and thus do not match Zephyr code values as described in input-event-codes.h.
Refer to https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
section Keyboard/Keypad (p53) for a list of scancode values.

The following example maps the first 3 numeric keys to GPIO pins:
- Scancode 30: "Keyboard 1 and !", mapped to gpio0 0
- Scancode 31: "Keyboard 2 and @", mapped to gpio0 1
- Scancode 32: "Keyboard 3 and \#", mapped to gpio0 2

The "typical position" column from HID table suggests to match them
with standard keycode values 2, 3 and 4, corresponding to
INPUT_KEY_1, INPUT_KEY_2 and INPUT_KEY_3 in input-event-codes.h.

/* gpio0 has to be a zephyr,gpio-emul device */
&gpio0 {
  ngpios = <3>;

  sdl_gpio {
    compatible = "zephyr,gpio-emul-sdl";
    scancodes = <30 31 32>;
  };
};

keypad: keypad {
  compatible = "gpio-keys";
  key1: key1 {
    gpios = <&gpio0 0 GPIO_ACTIVE_HIGH>;
  };
  key2: key2 {
    gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>;
  };
  key3: key3 {
    gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
  };
};

The limitations of usage are:
- Only active high as we don't get events for keys that aren't pressed
- Pressing multiple keys is best effort, state will be kept but no events
  are generated once the last key is released
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `scancodes` | `array` | ```text An array of SDL scancodes mapped to its GPIO index ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,gpio-emul-sdl” compatible.

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
