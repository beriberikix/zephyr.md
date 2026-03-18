---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/renesas,smartbond-lp-osc.html
original_path: build/dts/api/bindings/clock/renesas,smartbond-lp-osc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# renesas,smartbond-lp-osc

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

## Description

```text
Smartbond low power oscillator
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `calibration-interval` | `int` | ```text Time in seconds between calibration of low power clock RCX or RC32K. For XTAL32K this value is not used. If set to 0 calibration will not be performed. This can be applied when XTAL32K is enabled for low power clock and RCX or RC32K is used for watchdog and strict timing is not required. ```  Default value: `1` |
| `settle-time` | `int` | ```text This is only valid for XTAL32K. Time in ms needed to XTAL32K to settle. ```  Default value: `8000` |
| `clock-frequency` | `int` | ```text output clock frequency (Hz) ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “renesas,smartbond-lp-osc” compatible.

(None)
