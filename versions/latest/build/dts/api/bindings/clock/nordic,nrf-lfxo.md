---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/nordic,nrf-lfxo.html
original_path: build/dts/api/bindings/clock/nordic,nrf-lfxo.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nordic,nrf-lfxo

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic nRF low-frequency crystal oscillator
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**.  Constant value: `32768` |
| `load-capacitors` | `string` | ```text Type of load capacitors connected to the crystal. If not specified, adjustments may still happen when the device trimming happens during system initialization. ```  Legal values: `'internal'`, `'external'` |
| `load-capacitance-femtofarad` | `int` | ```text Load capacitance in femtofarads. This property is only used when load-capacitors is set to "internal". ```  Legal values: `4000`, `4500`, `5000`, `5500`, `6000`, `6500`, `7000`, `7500`, `8000`, `8500`, `9000`, `9500`, `10000`, `10500`, `11000`, `11500`, `12000`, `12500`, `13000`, `13500`, `14000`, `14500`, `15000`, `15500`, `16000`, `16500`, `17000`, `17500`, `18000` |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-lfxo” compatible.

(None)
