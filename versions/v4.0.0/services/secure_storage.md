---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/secure_storage.html
original_path: services/secure_storage.html
---

# Secure storage

The secure storage subsystem provides an implementation of the functions defined in the
[Platform Security Architecture (PSA) Secure Storage API](https://arm-software.github.io/psa-api/storage/).

It can be enabled on [board targets](../glossary.md#term-board-target)
that don’t already have an implementation of the API.

## Overview

The secure storage subsystem makes the PSA Secure Storage API available on all board targets with
non-volatile memory support.
As such, it provides an implementation of the API on those that don’t already have one, ensuring
functional support for the API.
Board targets with [Trusted Firmware-M (TF-M)](tfm/index.md#tfm) enabled (ending in `/ns`), for instance,
cannot enable the subsystem because TF-M already provides an implementation of the API.

In addition to providing functional support for the API, depending on
device-specific security features and the configuration, the subsystem
may secure the data stored via the PSA Secure Storage API at rest.

Keep in mind, however, that it’s preferable to use a secure processing environment like TF-M when
possible because it’s able to provide more security due to isolation guarantees.

## Limitations

The secure storage subsystem’s implementation of the PSA Secure Storage API:

- does not aim at full compliance with the specification.

  Its foremost goal is functional support for the API on all board targets.

  See below for important ways the implementation deviates from the specification.
- does not guarantee that the data it stores will be secure at rest in all cases.

  This depends on device-specific security features and the configuration.
- does not yet provide an implementation of the Protected Storage (PS) API as of this writing.

  Instead, the PS API directly calls into the Internal Trusted Storage (ITS) API
  (unless a [custom implementation](#whole-api) of the PS API is provided).

Below are some ways the implementation deviates from the specification
and an explanation why. This is not an exhaustive list.

- The data stored in the ITS is by default encrypted and authenticated (Against `1.` in
  [3.2. Internal Trusted Storage requirements](https://arm-software.github.io/psa-api/storage/1.0/overview/requirements.html#internal-trusted-storage-requirements).)

  The specification considers the storage underlying the ITS to be
  `implicitly confidential and protected from replay`
  ([2.4. The Internal Trusted Storage API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api))
  because `most embedded microprocessors (MCU) have on-chip flash storage that can be made
  inaccessible except to software running on the MCU`
  ([2.2. Technical Background](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#technical-background)).

  This is not the case on all MCUs. Thus, additional protection is provided to the stored data.

  However, this does not guarantee that the data stored will be secure at rest in all cases,
  because this depends on device-specific security features and the configuration.
  It requires a random entropy source and especially a secure encryption key provider
  ([`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER`](../kconfig.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER "CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER")).

  In addition, the data stored in the ITS is not protected against replay attacks,
  because this requires storage that is protected by hardware.
- The data stored via the PSA Secure Storage API is not protected from direct
  read/write by software or debugging. (Against `2.` and `10.` in
  [3.2. Internal Trusted Storage requirements](https://arm-software.github.io/psa-api/storage/1.0/overview/requirements.html#internal-trusted-storage-requirements).)

  It is only secured at rest. Protecting it at runtime as well
  requires specific hardware mechanisms to support this.

## Configuration

To configure the implementation of the PSA Secure Storage API provided by Zephyr, have a look at the
`CONFIG_SECURE_STORAGE_.*` Kconfig options. They are defined in the various Kconfig files found
under `subsys/secure_storage/`.

## Customization

Custom implementations can also replace those of Zephyr at different levels
if the functionality provided by the existing implementations isn’t enough.

### Whole API

If you already have an implementation of the whole ITS or PS API and want to make use of it, you
can do so by enabling the following Kconfig option and implementing the relevant functions:

- [`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM`](../kconfig.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM "CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM"), for the ITS API.
- [`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM`](../kconfig.md#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM "CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM"), for the PS API.

### ITS API

Zephyr’s implementation of the ITS API
([`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR`](../kconfig.md#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR "CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_ZEPHYR"))
makes use of the ITS transform and store modules, which can be configured and customized separately.
Have a look at the `CONFIG_SECURE_STORAGE_ITS_(STORE|TRANSFORM)_.*_CUSTOM`
Kconfig options to see the different customization possibilities.

It’s especially recommended to implement a custom encryption key provider
([`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM`](../kconfig.md#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM "CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_CUSTOM"))
that is more secure than the available options, if possible.

## Samples

- [PSA Crypto persistent key](../samples/psa/persistent_key/README.md#persistent_key "Manage and use persistent keys via the PSA Crypto API.")
- [PSA Internal Trusted Storage API](../samples/psa/its/README.md#psa_its "Use the PSA ITS API.")

## PSA Secure Storage API reference

[PSA Secure Storage API](../doxygen/html/group__psa__secure__storage.md)

Related code samples

- [PSA Internal Trusted Storage API](../samples/psa/its/README.md#psa_its "Use the PSA ITS API.")Use the PSA ITS API.
