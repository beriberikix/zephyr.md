---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/qspi/nxp,s32-qspi-sfp-frad.html
original_path: build/dts/api/bindings/qspi/nxp,s32-qspi-sfp-frad.html
---

# nxp,s32-qspi-sfp-frad

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP FRAD.
The SFP FRAD performs second-level checks on input flash write and erase transactions, based on the address range of each transaction.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `master-domain-acp-policy` | `int` | ```text Selects the master domain access control policy, defined in dt-bindings/qspi/nxp-s32-qspi.h: - NXP_S32_QSPI_NON_SECURE: Selects the non-secure access control policy. - NXP_S32_QSPI_SECURE: Selects the secure access control policy. - NXP_S32_QSPI_PRIVILEGE: Selects the privilege access control policy. Allowed combinations: - NXP_S32_QSPI_SECURE - NXP_S32_QSPI_SECURE | NXP_S32_QSPI_PRIVILEGE - NXP_S32_QSPI_NON_SECURE | NXP_S32_QSPI_PRIVILEGE - NXP_S32_QSPI_NON_SECURE | NXP_S32_QSPI_SECURE | NXP_S32_QSPI_PRIVILEGE ```  This property is **required**. |
| `exclusive-access-lock` | `string` | ```text Selects the exclusive access lock: - DISABLED: The exclusive access lock disabled, granting write permissions for all masters - ENABLED: The exclusive access lock enabled, granting write permissions only to the   exclusive access owner master and disabling write permissions for other masters. - NONE: This configuration should not be used The default corresponds to the reset value of the register field. ```  Default value: `DISABLED`  Legal values: `'DISABLED'`, `'OWNER'`, `'NONE'` |
| `exclusive-access-owner` | `int` | ```text The domain master ID that owns the exclusive access lock. Valid range: 0 - 63. The default corresponds to the reset value of the register field. ``` |
