---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/reset/nxp,lpc-syscon-reset.html
original_path: build/dts/api/bindings/reset/nxp,lpc-syscon-reset.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,lpc-syscon-reset

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
LPC SYSCON Peripheral reset controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#reset-cells` | `int` | ```text Number of cells in reset property. There must be a cell named "id" to use the reset_dt_spec macros. ```  This property is **required**.  Constant value: `1` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,lpc-syscon-reset” compatible.

(None)

## Specifier cell names

- reset cells: id
