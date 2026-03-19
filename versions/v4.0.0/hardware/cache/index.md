---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/cache/index.html
original_path: hardware/cache/index.html
---

# Cache Interface

This is a high-level guide to cache interface and Kconfig options related to
cache controllers. See [Cache API](#cache-api) for API reference material.

Zephyr has different Kconfig options to control how the cache controller is
implemented and controlled.

- [`CONFIG_CPU_HAS_DCACHE`](../../kconfig.md#CONFIG_CPU_HAS_DCACHE "CONFIG_CPU_HAS_DCACHE") /
  [`CONFIG_CPU_HAS_ICACHE`](../../kconfig.md#CONFIG_CPU_HAS_ICACHE "CONFIG_CPU_HAS_ICACHE"): these hidden options should be
  selected at SoC / platform level when the CPU actually supports a data or
  instruction cache. The cache controller can be in the core or can be an
  external cache controller for which a driver is provided.

  These options have the goal to document an available feature and should be
  set whether we plan to support and use the caches in Zephyr or not.
- [`CONFIG_DCACHE`](../../kconfig.md#CONFIG_DCACHE "CONFIG_DCACHE") / [`CONFIG_ICACHE`](../../kconfig.md#CONFIG_ICACHE "CONFIG_ICACHE"): these
  options must be selected when support for data or instruction cache is
  present and working in zephyr.

  All the code paths related to cache control must be conditionally enabled
  depending on these symbols. When the symbol is set the cache is considered
  enabled and used.

  These symbols say nothing about the actual API interface exposed to the user.
  For example a platform using the data cache can enable the
  [`CONFIG_DCACHE`](../../kconfig.md#CONFIG_DCACHE "CONFIG_DCACHE") symbol and use some HAL exported function in
  some platform-specific code to enable and manage the d-cache.
- [`CONFIG_CACHE_MANAGEMENT`](../../kconfig.md#CONFIG_CACHE_MANAGEMENT "CONFIG_CACHE_MANAGEMENT"): this option must be selected when
  the cache operations are exposed to the user through a standard API (see
  [Cache API](#cache-api)).

  When this option is enabled we assume that all the cache functions are
  implemented in the architectural code or in an external cache controller
  driver.
- [`CONFIG_ARCH_CACHE`](../../kconfig.md#CONFIG_ARCH_CACHE "CONFIG_ARCH_CACHE")/[`CONFIG_EXTERNAL_CACHE`](../../kconfig.md#CONFIG_EXTERNAL_CACHE "CONFIG_EXTERNAL_CACHE"):
  mutually exclusive options for `CACHE_TYPE` used to define
  whether the cache operations are implemented at arch level or using an
  external cache controller with a provided driver.

  - [`CONFIG_ARCH_CACHE`](../../kconfig.md#CONFIG_ARCH_CACHE "CONFIG_ARCH_CACHE"): the cache API is implemented by the
    arch code
  - [`CONFIG_EXTERNAL_CACHE`](../../kconfig.md#CONFIG_EXTERNAL_CACHE "CONFIG_EXTERNAL_CACHE"): the cache API is implemented by a
    driver that supports the external cache controller. In this case the driver
    must be located as usual in the `drivers/cache/` directory

## Cache API

[Cache Interface](../../doxygen/html/group__cache__interface.md)
