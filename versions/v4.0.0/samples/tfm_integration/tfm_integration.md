---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/tfm_integration/tfm_integration.html
original_path: samples/tfm_integration/tfm_integration.html
---

# TF-M Integration

These TF-M integration examples can be used with a supported Armv8-M board, and demonstrate how
the TF-M APIs can be used with Zephyr.

- [TF-M IPC](tfm_ipc/README.md#tfm_ipc "Implement communication between the secure and non-secure images using IPC.")Implement communication between the secure and non-secure images using IPC.
- [TF-M PSA crypto](psa_crypto/README.md#tfm_psa_crypto "Use the PSA Crypto API for cryptography and device certificate signing requests.")Use the PSA Crypto API for cryptography and device certificate signing requests.
- [TF-M PSA Protected Storage](psa_protected_storage/README.md#psa_protected_storage "Use the Protected Storage (PS) API to store encrypted data.")Use the Protected Storage (PS) API to store encrypted data.
- [TF-M Secure Partition](tfm_secure_partition/README.md#tfm_secure_partition "Create a secure partition that exposes secure services.")Create a secure partition that exposes secure services.

## Overview

Trusted Firmware Platform Security Architecture (PSA) APIs are used for the
secure processing environment (S), with Zephyr running in the non-secure
processing environment (NS).

As part of the standard build process, the secure bootloader (BL2) is normally
built, in addition to the TF-M S and Zephyr NS binary images. The S and NS
images are then merged and signed using the private signing keys, whose public
key values are stored in the secure bootloader. This allows the application
images to be verified and either accepted or rejected during the image
verification process at startup, based on a pair of private keys that you
control.

## What is Trusted Firmware-M (TF-M)?

Trusted Firmware-M (TF-M) is the reference implementation of [Platform Security
Architecture (PSA)](https://pages.arm.com/psa-resources.html).

TF-M provides a highly configurable set of software components to create a
Trusted Execution Environment. This is achieved by a set of secure run time
services such as Secure Storage, Cryptography, Audit Logs and Attestation.
Additionally, secure boot in TF-M ensures integrity of run time software and
supports firmware upgrade.

The current TF-M implementation specifically targets TrustZone for ARMv8-M.

Trusted Firmware-M source code is available at
[git.trustedfirmware.org](https://git.trustedfirmware.org), although a fork
of this source code is maintained by the Zephyr Project as a module for
convenience sake at
[https://github.com/zephyrproject-rtos/trusted-firmware-m](https://github.com/zephyrproject-rtos/trusted-firmware-m).

For further information consult the official [TF-M documentation](https://tf-m-user-guide.trustedfirmware.org/)
