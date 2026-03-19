---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/fuel_gauge.html
original_path: hardware/peripherals/fuel_gauge.html
---

# Fuel Gauge

The fuel gauge subsystem exposes an API to uniformly access battery fuel gauge devices. Currently,
only reading data is supported.

Note: This API is currently experimental and this doc will be significantly changed as new features
are added to the API.

## Basic Operation

### Properties

Fundamentally, a property is a quantity that a fuel gauge device can measure.

Fuel gauges typically support multiple properties, such as temperature readings of the battery-pack
or present-time current/voltage.

Properties are fetched by the client one at a time using [`fuel_gauge_get_prop()`](../../doxygen/html/group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1), or fetched
in a batch using [`fuel_gauge_get_props()`](../../doxygen/html/group__fuel__gauge__interface.md#gac721c19bc2c9714c11ede5e6d86fd0b0).

Properties are set by the client one at a time using [`fuel_gauge_set_prop()`](../../doxygen/html/group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d), or set in a
batch using [`fuel_gauge_set_props()`](../../doxygen/html/group__fuel__gauge__interface.md#ga55bb2be9c9eae7c3a8d01df051178d01).

### Battery Cutoff

Many fuel gauges embedded within battery packs expose a register address that when written to with a
specific payload will do a battery cutoff. This battery cutoff is often referred to as ship, shelf,
or sleep mode due to its utility in reducing battery drain while devices are stored or shipped.

The fuel gauge API exposes battery cutoff with the [`fuel_gauge_battery_cutoff()`](../../doxygen/html/group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc) function.

### Caching

The Fuel Gauge API explicitly provides no caching for its clients.

## API Reference

[Fuel Gauge Interface](../../doxygen/html/group__fuel__gauge__interface.md)

[Fuel gauge backend emulator APIs](../../doxygen/html/group__fuel__gauge__emulator__backend.md)
