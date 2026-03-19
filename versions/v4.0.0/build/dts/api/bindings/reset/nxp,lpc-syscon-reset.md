---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/reset/nxp,lpc-syscon-reset.html
original_path: build/dts/api/bindings/reset/nxp,lpc-syscon-reset.html
---

# nxp,lpc-syscon-reset

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/reset/reset\_lpc\_syscon.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/reset/reset_lpc_syscon.c).

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
