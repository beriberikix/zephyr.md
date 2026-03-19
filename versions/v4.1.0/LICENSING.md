---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/LICENSING.html
original_path: LICENSING.html
---

# Licensing of Zephyr Project components

The Zephyr kernel tree imports or reuses packages, scripts and other files that
are not covered by the [Apache 2.0 License](https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE). In some places
there is no LICENSE file or way to put a LICENSE file there, so we describe the
licensing in this document.

## Continuous Integration Scripts

- *Origin:* Linux Kernel
- *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING)
- *Impact:* These files are used in Continuous Integration (CI) and never linked into the firmware.
- *Files:*

  - [scripts/checkpatch.pl](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/checkpatch.pl)
  - [scripts/checkstack.pl](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/checkstack.pl)
  - [scripts/spelling.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/spelling.txt)

## Coccinelle Scripts

> - *Origin:* Coccinelle
> - *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING)
> - *Impact:* These files are used by [Coccinelle](https://coccinelle.gitlabpages.inria.fr/website/), a tool for transforming C-code, and never linked
>   into the firmware.
> - *Files:*
>
>   - [scripts/coccicheck](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccicheck)
>   - [scripts/coccinelle/array\_size.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/array_size.cocci)
>   - [scripts/coccinelle/deref\_null.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/deref_null.cocci)
>   - [scripts/coccinelle/deref\_null.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/deref_null.cocci)
>   - [scripts/coccinelle/deref\_null.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/deref_null.cocci)
>   - [scripts/coccinelle/mini\_lock.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/mini_lock.cocci)
>   - [scripts/coccinelle/mini\_lock.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/mini_lock.cocci)
>   - [scripts/coccinelle/mini\_lock.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/mini_lock.cocci)
>   - [scripts/coccinelle/noderef.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/noderef.cocci)
>   - [scripts/coccinelle/noderef.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/noderef.cocci)
>   - [scripts/coccinelle/returnvar.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/returnvar.cocci)
>   - [scripts/coccinelle/semicolon.cocci](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/coccinelle/semicolon.cocci)

## GCOV Coverage Header File

- *Origin:* GCC, the GNU Compiler Collection
- *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING) with Runtime Library Exception
- *Impact:* This file is only linked into the firmware if [`CONFIG_COVERAGE_GCOV`](kconfig.md#CONFIG_COVERAGE_GCOV "CONFIG_COVERAGE_GCOV") is
  enabled.
- *Files:*

  - [subsys/testsuite/coverage/coverage.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/coverage/coverage.h)

## ENE KB1200\_EVB Board OpenOCD Configuration

- *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING)
- *Impact:* This file is used by [OpenOCD](https://openocd.org) when programming and debugging the
  [ENE KB1200\_EVB](boards/ene/kb1200_evb/doc/index.md#kb1200_evb) board. It is never linked into the firmware.
- *Files:*

  - [boards/ene/kb1200\_evb/support/openocd.cfg](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1200_evb/support/openocd.cfg)

## Thread-Metric RTOS Test Suite Source Files

- *Origin:* ThreadX
- *Licensing:* [MIT License](https://opensource.org/licenses/MIT)
- *Impact:* These files are only linked into the Thread-Metric RTOS Test Suite test firmware.
- *Files:*

  - [tests/benchmarks/thread\_metric/thread\_metric\_readme.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/thread_metric_readme.txt)
  - [tests/benchmarks/thread\_metric/src/tm\_api.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_api.h)
  - [tests/benchmarks/thread\_metric/src/tm\_basic\_processing\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_basic_processing_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_cooperative\_scheduling\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_cooperative_scheduling_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_interrupt\_preemption\_processing\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_interrupt_preemption_processing_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_interrupt\_processing\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_interrupt_processing_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_memory\_allocation\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_memory_allocation_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_message\_processing\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_message_processing_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_porting\_layer.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_porting_layer.h)
  - [tests/benchmarks/thread\_metric/src/tm\_porting\_layer\_zephyr.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_porting_layer_zephyr.c)
  - [tests/benchmarks/thread\_metric/src/tm\_preemptive\_scheduling\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_preemptive_scheduling_test.c)
  - [tests/benchmarks/thread\_metric/src/tm\_synchronization\_processing\_test.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/benchmarks/thread_metric/src/tm_synchronization_processing_test.c)

## OpenThread Spinel HDLC RCP Host Interface Files

- *Origin:* OpenThread
- *Licensing:* [BSD-3-clause](https://opensource.org/license/bsd-3-clause)
- *Impact:* These files are only linked into the firmware if [`CONFIG_HDLC_RCP_IF`](kconfig.md#CONFIG_HDLC_RCP_IF "CONFIG_HDLC_RCP_IF") is
  enabled.
- *Files*:

  - [modules/openthread/platform/hdlc\_interface.hpp](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/hdlc_interface.hpp)
  - [modules/openthread/platform/radio\_spinel.cpp](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/radio_spinel.cpp)
  - [modules/openthread/platform/hdlc\_interface.cpp](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/hdlc_interface.cpp)

## Python Devicetree library test files

- *Licensing:* [BSD-3-clause](https://opensource.org/license/bsd-3-clause)
- *Impact:* These are only used for testing and never linked with the firmware.
- *Files*:

  - Various yaml files under `scripts/dts/python-devicetree/tests`
