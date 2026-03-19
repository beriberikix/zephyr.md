---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/qspi/nxp,s32-qspi-sfp-mdad.html
original_path: build/dts/api/bindings/qspi/nxp,s32-qspi-sfp-mdad.html
---

# nxp,s32-qspi-sfp-mdad

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP MDAD.
The SFP MDAD performs first-level checks on input transactions, based on the secure attribute and MGID associated with each transaction.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `secure-attribute` | `int` | ```text Selects the secure attribute, defined in dt-bindings/qspi/nxp-s32-qspi.h: - NXP_S32_QSPI_NON_SECURE: Allow the bus attribute for this master to non-secure - NXP_S32_QSPI_SECURE: Allow the bus attribute for this master to secure Allowed combinations: - NXP_S32_QSPI_NON_SECURE - NXP_S32_QSPI_SECURE - NXP_S32_QSPI_NON_SECURE | NXP_S32_QSPI_SECURE ```  This property is **required**. |
| `mask-type` | `string` | ```text Selects the mask type: - AND: AND-ed mask - OR: OR-ed mask The default corresponds to the reset value of the register field. ```  Default value: `AND`  Legal values: `'AND'`, `'OR'` |
| `mask` | `int` | ```text Defines the mask value for the ID-Match comparison. Valid range: 0 - 63. The default corresponds to the reset value of the register field. ``` |
| `domain-id` | `int` | ```text Domain ID Reference value of the Domain-ID (MID) for MID-comparison. Valid range: 0 - 63. ```  This property is **required**. |
