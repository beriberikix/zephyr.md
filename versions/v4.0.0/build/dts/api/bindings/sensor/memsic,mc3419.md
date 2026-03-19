---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/memsic,mc3419.html
original_path: build/dts/api/bindings/sensor/memsic,mc3419.html
---

# memsic,mc3419 (on i2c bus)

Vendor: [MEMSIC Inc.](../../bindings.md#dt-vendor-memsic)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/memsic/mc3419/mc3419.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/memsic/mc3419/mc3419.c).

## Description

```text
MC3419 3-axis accel sensor

Example:
#include <zephyr/dt-bindings/sensor/mc3419.h>

mc3419: mc3419@0 {
  ...

  lpf-fc-sel = <MC3419_LPF_DISABLE>;
  decimation-rate = <MC3419_DECIMATE_IDR_BY_1>;
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `int-gpios` | `phandle-array` | ```text This property specifies the connection for INT, this pin defaults to active low when sample produce interrupt. ``` |
| `int-pin2` | `boolean` | ```text This property is used for interrupt routing.The sensor has two interrupt pins.By default the interrupt are routed to interrupt pin 1, by enabled this property interrupt are routed to interrupt pin 2. ``` |
| `lpf-fc-sel` | `int` | ```text Enable and select LPF cutoff frequency for a given IDR (Input Data Rate). Possible values are listed below. Either use Int value or Macro Name in node definition. +-----------+-------------------------------------+ | int value | Macro Name                          | +-----------+-------------------------------------+ | 0         | MC3419_LPF_DISABLE                  | | 9         | MC3419_LPF_EN_WITH_IDR_BY_4p255_FC  | | 10        | MC3419_LPF_EN_WITH_IDR_BY_6_FC      | | 11        | MC3419_LPF_EN_WITH_IDR_BY_12_FC     | | 13        | MC3419_LPF_EN_WITH_IDR_BY_16_FC     | +-----------+-------------------------------------+ Default is LPF disabled (reset value of the register). ```  Legal values: `0`, `9`, `10`, `11`, `13` |
| `decimation-rate` | `int` | ```text This helps in producing slower Output Data Rate (ODR) from given Input Data Rate (IDR). Possible values are listed below. Either use Int value or Macro Name in node definition. +-----------+-------------------------------+ | Int value | Macro Name                    | +-----------+-------------------------------+ | 0         | MC3419_DECIMATE_IDR_BY_1      | | 1         | MC3419_DECIMATE_IDR_BY_2      | | 2         | MC3419_DECIMATE_IDR_BY_4      | | 3         | MC3419_DECIMATE_IDR_BY_5      | | 4         | MC3419_DECIMATE_IDR_BY_8      | | 5         | MC3419_DECIMATE_IDR_BY_10     | | 6         | MC3419_DECIMATE_IDR_BY_16     | | 7         | MC3419_DECIMATE_IDR_BY_20     | | 8         | MC3419_DECIMATE_IDR_BY_40     | | 9         | MC3419_DECIMATE_IDR_BY_67     | | 10        | MC3419_DECIMATE_IDR_BY_80     | | 11        | MC3419_DECIMATE_IDR_BY_100    | | 12        | MC3419_DECIMATE_IDR_BY_200    | | 13        | MC3419_DECIMATE_IDR_BY_250    | | 14        | MC3419_DECIMATE_IDR_BY_500    | | 15        | MC3419_DECIMATE_IDR_BY_1000   | +-----------+-------------------------------+ Default is Decimation 0 (reset value of the register). ```  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “memsic,mc3419” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
