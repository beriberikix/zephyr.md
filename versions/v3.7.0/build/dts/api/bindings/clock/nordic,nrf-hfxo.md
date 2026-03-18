---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/clock/nordic,nrf-hfxo.html
original_path: build/dts/api/bindings/clock/nordic,nrf-hfxo.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-hfxo

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic nRF high-frequency crystal oscillator
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**.  Constant value: `32000000` |
| `load-capacitors` | `string` | ```text Type of load capacitors connected to the crystal. If not specified, adjustments may still happen when the device trimming happens during system initialization. ```  Legal values: `'internal'`, `'external'` |
| `load-capacitance-femtofarad` | `int` | ```text Load capacitance in femtofarads. This property is only used when load-capacitors is set to "internal". ```  Legal values: `4000`, `4250`, `4500`, `4750`, `5000`, `5250`, `5500`, `5750`, `6000`, `6250`, `6500`, `6750`, `7000`, `7250`, `7500`, `7750`, `8000`, `8250`, `8500`, `8750`, `9000`, `9250`, `9500`, `9750`, `10000`, `10250`, `10500`, `10750`, `11000`, `11250`, `11500`, `11750`, `12000`, `12250`, `12500`, `12750`, `13000`, `13250`, `13500`, `13750`, `14000`, `14250`, `14500`, `14750`, `15000`, `15250`, `15500`, `15750`, `16000`, `16250`, `16500`, `16750`, `17000` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-hfxo” compatible.

(None)
