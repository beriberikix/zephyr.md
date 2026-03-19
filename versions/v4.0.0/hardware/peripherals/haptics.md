---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/haptics.html
original_path: hardware/peripherals/haptics.html
---

# Haptics

## Overview

The haptics API allows for the control of haptic driver devices for the
purposes of performing haptic feedback events.

During a haptic feedback event the haptic device drives a signal to an
actuator. The source of the haptic event signal varies depending on the
capabilities of the haptic device.

Some examples of haptic signal sources are analog signals, preprogrammed
(ROM) wavetables, synthesized (RAM) wavetables, and digital audio streams.

Additionally, haptic driver devices often offer controls for adjusting and
tuning the drive signal to meet the electrical requirements of their respective
actuators.

## API Reference

[Haptics Interface](../../doxygen/html/group__haptics__interface.md)

Related code samples

- [DRV2605 Haptic Driver](../../samples/drivers/haptics/drv2605/README.md#drv2605 "Drive an LRA using the DRV2605 haptic driver chip.")Drive an LRA using the DRV2605 haptic driver chip.
