---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/charger.html
original_path: hardware/peripherals/charger.html
---

# Chargers

The charger subsystem exposes an API to uniformly access battery charger devices.

A charger device, or charger peripheral, is a device used to take external power provided to the
system as an input and provide power as an output downstream to the battery pack(s) and system.
The charger device can exist as a module, an integrated circuit, or as a functional block in a power
management integrated circuit (PMIC).

The action of charging a battery pack is referred to as a charge cycle. When the charge cycle is
executed the battery pack is charged according to the charge profile configured on the charger
device. The charge profile is defined in the battery pack’s specification that is provided by the
manufacturer. On charger devices with a control port, the charge profile can be configured by the
host controller by setting the relevant properties, and can be adjusted at runtime to respond to
environmental changes.

## Basic Operation

### Initiating a Charge Cycle

A charge cycle is initiated or terminated using [`charger_charge_enable()`](../../doxygen/html/group__charger__interface.md#gace1ea9841574d75d314db078df5a0b3a).

### Properties

Fundamentally, a property is a configurable setting, state, or quantity that a charger device can
measure.

Chargers typically support multiple properties, such as temperature readings of the battery-pack
or present-time current/voltage.

Properties are fetched by the client one at a time using [`charger_get_prop()`](../../doxygen/html/group__charger__interface.md#ga00e5b61d517c93d7d3c863b14b07b738).
Properties are set by the client one at a time using [`charger_set_prop()`](../../doxygen/html/group__charger__interface.md#ga0036e3f5924585457a99a2e444ef5aab).

## API Reference

[Charger Interface](../../doxygen/html/group__charger__interface.md)

Related code samples

- [Charger](../../samples/drivers/charger/README.md#charger "Charge a battery using the charger driver API.")Charge a battery using the charger driver API.
