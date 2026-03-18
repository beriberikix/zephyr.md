---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/cache/index.html
original_path: hardware/cache/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

*group* Cache Interface
:   Functions

    ALWAYS\_INLINE static void sys\_cache\_data\_enable(void)
    :   Enable the d-cache.

        Enable the data cache

    ALWAYS\_INLINE static void sys\_cache\_data\_disable(void)
    :   Disable the d-cache.

        Disable the data cache

    ALWAYS\_INLINE static void sys\_cache\_instr\_enable(void)
    :   Enable the i-cache.

        Enable the instruction cache

    ALWAYS\_INLINE static void sys\_cache\_instr\_disable(void)
    :   Disable the i-cache.

        Disable the instruction cache

    ALWAYS\_INLINE static int sys\_cache\_data\_flush\_all(void)
    :   Flush the d-cache.

        Flush the whole data cache.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_instr\_flush\_all(void)
    :   Flush the i-cache.

        Flush the whole instruction cache.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_data\_invd\_all(void)
    :   Invalidate the d-cache.

        Invalidate the whole data cache.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_instr\_invd\_all(void)
    :   Invalidate the i-cache.

        Invalidate the whole instruction cache.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_data\_flush\_and\_invd\_all(void)
    :   Flush and Invalidate the d-cache.

        Flush and Invalidate the whole data cache.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_instr\_flush\_and\_invd\_all(void)
    :   Flush and Invalidate the i-cache.

        Flush and Invalidate the whole instruction cache.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    int sys\_cache\_data\_flush\_range(void \*addr, size\_t size)
    :   Flush an address range in the d-cache.

        Flush the specified address range of the data cache.

        Note

        the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

        Parameters:
        :   - **addr** – Starting address to flush.
            - **size** – Range size.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_instr\_flush\_range(void \*addr, size\_t size)
    :   Flush an address range in the i-cache.

        Flush the specified address range of the instruction cache.

        Note

        the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

        Parameters:
        :   - **addr** – Starting address to flush.
            - **size** – Range size.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    int sys\_cache\_data\_invd\_range(void \*addr, size\_t size)
    :   Invalidate an address range in the d-cache.

        Invalidate the specified address range of the data cache.

        Note

        the cache operations act on cache line. When multiple data structures share the same cache line being invalidated, all the portions of the non-read-only data structures sharing the same line will be invalidated as well. This is a destructive process that could lead to data loss and/or corruption. When `addr` is not aligned to the cache line and/or `size` is not a multiple of the cache line size the behaviour is undefined.

        Parameters:
        :   - **addr** – Starting address to invalidate.
            - **size** – Range size.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_instr\_invd\_range(void \*addr, size\_t size)
    :   Invalidate an address range in the i-cache.

        Invalidate the specified address range of the instruction cache.

        Note

        the cache operations act on cache line. When multiple data structures share the same cache line being invalidated, all the portions of the non-read-only data structures sharing the same line will be invalidated as well. This is a destructive process that could lead to data loss and/or corruption. When `addr` is not aligned to the cache line and/or `size` is not a multiple of the cache line size the behaviour is undefined.

        Parameters:
        :   - **addr** – Starting address to invalidate.
            - **size** – Range size.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    int sys\_cache\_data\_flush\_and\_invd\_range(void \*addr, size\_t size)
    :   Flush and Invalidate an address range in the d-cache.

        Flush and Invalidate the specified address range of the data cache.

        Note

        the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed before being invalidated. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

        Parameters:
        :   - **addr** – Starting address to flush and invalidate.
            - **size** – Range size.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static int sys\_cache\_instr\_flush\_and\_invd\_range(void \*addr, size\_t size)
    :   Flush and Invalidate an address range in the i-cache.

        Flush and Invalidate the specified address range of the instruction cache.

        Note

        the cache operations act on cache line. When multiple data structures share the same cache line being flushed, all the portions of the data structures sharing the same line will be flushed before being invalidated. This is usually not a problem because writing back is a non-destructive process that could be triggered by hardware at any time, so having an aligned `addr` or a padded `size` is not strictly necessary.

        Parameters:
        :   - **addr** – Starting address to flush and invalidate.
            - **size** – Range size.

        Return values:
        :   - **0** – If succeeded.
            - **-ENOTSUP** – If not supported.
            - **-errno** – Negative errno for other failures.

    ALWAYS\_INLINE static size\_t sys\_cache\_data\_line\_size\_get(void)
    :   Get the d-cache line size.

        The API is provided to get the data cache line.

        The cache line size is calculated (in order of priority):

        - At run-time when  [`CONFIG_DCACHE_LINE_SIZE_DETECT`](../../kconfig.md#CONFIG_DCACHE_LINE_SIZE_DETECT "CONFIG_DCACHE_LINE_SIZE_DETECT") is set.
        - At compile time using the value set in  [`CONFIG_DCACHE_LINE_SIZE`](../../kconfig.md#CONFIG_DCACHE_LINE_SIZE "CONFIG_DCACHE_LINE_SIZE") .
        - At compile time using the `d-cache-line-size` CPU0 property of the DT.
        - 0 otherwise

        Return values:
        :   - **size** – Size of the d-cache line.
            - **0** – If the d-cache is not enabled.

    ALWAYS\_INLINE static size\_t sys\_cache\_instr\_line\_size\_get(void)
    :   Get the i-cache line size.

        The API is provided to get the instruction cache line.

        The cache line size is calculated (in order of priority):

        - At run-time when  [`CONFIG_ICACHE_LINE_SIZE_DETECT`](../../kconfig.md#CONFIG_ICACHE_LINE_SIZE_DETECT "CONFIG_ICACHE_LINE_SIZE_DETECT") is set.
        - At compile time using the value set in  [`CONFIG_ICACHE_LINE_SIZE`](../../kconfig.md#CONFIG_ICACHE_LINE_SIZE "CONFIG_ICACHE_LINE_SIZE") .
        - At compile time using the `i-cache-line-size` CPU0 property of the DT.
        - 0 otherwise

        Return values:
        :   - **size** – Size of the d-cache line.
            - **0** – If the d-cache is not enabled.

    ALWAYS\_INLINE static bool sys\_cache\_is\_ptr\_cached(void \*ptr)
    :   Test if a pointer is in cached region.

        Some hardware may map the same physical memory twice so that it can be seen in both (incoherent) cached mappings and a coherent “shared” area. This tests if a particular pointer is within the cached, coherent area.

        Parameters:
        :   - **ptr** – Pointer

        Return values:
        :   - **True** – if pointer is in cached region.
            - **False** – if pointer is not in cached region.

    ALWAYS\_INLINE static bool sys\_cache\_is\_ptr\_uncached(void \*ptr)
    :   Test if a pointer is in un-cached region.

        Some hardware may map the same physical memory twice so that it can be seen in both (incoherent) cached mappings and a coherent “shared” area. This tests if a particular pointer is within the un-cached, incoherent area.

        Parameters:
        :   - **ptr** – Pointer

        Return values:
        :   - **True** – if pointer is not in cached region.
            - **False** – if pointer is in cached region.

    ALWAYS\_INLINE static void \*sys\_cache\_cached\_ptr\_get(void \*ptr)
    :   Return cached pointer to a RAM address.

        This function takes a pointer to any addressable object (either in cacheable memory or not) and returns a pointer that can be used to refer to the same memory through the L1 data cache. Data read through the resulting pointer will reflect locally cached values on the current CPU if they exist, and writes will go first into the cache and be written back later.

        See also

        arch\_uncached\_ptr()

        Note

        This API returns the same pointer if CONFIG\_CACHE\_DOUBLEMAP is not enabled.

        Parameters:
        :   - **ptr** – A pointer to a valid C object

        Returns:
        :   A pointer to the same object via the L1 dcache

    ALWAYS\_INLINE static void \*sys\_cache\_uncached\_ptr\_get(void \*ptr)
    :   Return uncached pointer to a RAM address.

        This function takes a pointer to any addressable object (either in cacheable memory or not) and returns a pointer that can be used to refer to the same memory while bypassing the L1 data cache. Data in the L1 cache will not be inspected nor modified by the access.

        See also

        arch\_cached\_ptr()

        Note

        This API returns the same pointer if CONFIG\_CACHE\_DOUBLEMAP is not enabled.

        Parameters:
        :   - **ptr** – A pointer to a valid C object

        Returns:
        :   A pointer to the same object bypassing the L1 dcache
