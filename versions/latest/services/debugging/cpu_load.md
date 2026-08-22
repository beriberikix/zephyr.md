---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/services/debugging/cpu_load.html
original_path: services/debugging/cpu_load.html
---

# CPU load

Module can be used to track how much time is spent in idle. It is using tracing hooks
which are called before and after CPU goes to idle. Compared to [Thread analyzer](thread-analyzer.md#thread-analyzer)
it is more accurate since it takes into account time spent in the interrupt context as well.

Function [`cpu_load_get()`](../../doxygen/html/group__cpu__load.md#gaf44501a292aeef7749b68c706b34119f) is used to get the latest value. It is also used to reset
the measurement. By default, module is using [`k_cycle_get_32()`](../../doxygen/html/group__clock__apis.md#ga208687de625e0036558343b4e66143d3) but in cases when higher
precision is needed a [Counter](../../hardware/peripherals/counter.md#counter-api) device can be used.

Load can also be reported periodically using a logging message. Period is configured using [`CONFIG_CPU_LOAD_LOG_PERIODICALLY`](../../kconfig.md#CONFIG_CPU_LOAD_LOG_PERIODICALLY "CONFIG_CPU_LOAD_LOG_PERIODICALLY").

## Using counter device

In order to use [Counter](../../hardware/peripherals/counter.md#counter-api) device [`CONFIG_CPU_LOAD_USE_COUNTER`](../../kconfig.md#CONFIG_CPU_LOAD_USE_COUNTER "CONFIG_CPU_LOAD_USE_COUNTER") must be
enabled and chosen in devicetree must be set.

```devicetree
chosen {
  zephyr,cpu-load-counter = &counter_device;
};
```
