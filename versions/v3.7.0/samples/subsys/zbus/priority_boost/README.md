---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/zbus/priority_boost/README.html
original_path: samples/subsys/zbus/priority_boost/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# zbus Priority Boost

## Overview

This sample implements a simple application that illustrates the priority boost feature. The
application implements the below figure scenario. When the priority boost feature is disabled, the
execution sequence presents a priority inversion problem, which may not affect much of the
developer’s application. Those who want to avoid priority inversions between message subscribers and
plain subscribers should use the priority boost strategy.

```c
ZBUS_CHAN_DEFINE(chan_a,
                 int,
                 NULL,
                 NULL,
                 ZBUS_OBSERVERS(l1, ms1, ms2, s1, l2),
                 0
);
```

[![ZBus priority boost scenario example.](../../../../_images/zbus_publishing_process_example_scenario.svg)](../../../../_images/zbus_publishing_process_example_scenario.svg)

Note

The developer must use the [`zbus_obs_attach_to_thread()`](../../../../services/zbus/index.md#c.zbus_obs_attach_to_thread "zbus_obs_attach_to_thread") function to ensure a proper
priority boost execution.

## Building and Running

The figure below illustrates the execution of the cited scenario but with the priority boost
disabled.

[![ZBus example scenario for priority boost disabled.](../../../../_images/without_hlp_priority_boost_feature.svg)](../../../../_images/without_hlp_priority_boost_feature.svg)

It can be built and executed on QEMU as follows:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/subsys/zbus/priority_boost -- -DCONFIG_ZBUS_PRIORITY_BOOST=n
west build -t run
```

### Sample Output

```shell
I: --------------
I: 0 -> T1: prio before 5
I: 0 ---> L1: T1 prio 5
I: 0 -> MS1:  T1 prio 5
I: 0 -> MS2:  T1 prio 5
I: 0 ---> L2: T1 prio 5
I: 0 -> T1: prio after 5
I: N -> S1:  T1 prio 5
I: 0 -> S1:  T1 prio 5
I: --------------
I: 1 -> T1: prio before 5
I: 1 ---> L1: T1 prio 5
I: 1 -> MS1:  T1 prio 5
I: 1 -> MS2:  T1 prio 5
I: 1 ---> L2: T1 prio 5
I: 1 -> T1: prio after 5
I: N -> S1:  T1 prio 5
I: 1 -> S1:  T1 prio 5
I: --------------
I: 2 -> T1: prio before 5
I: 2 ---> L1: T1 prio 5
I: 2 -> MS1:  T1 prio 5
I: 2 ---> L2: T1 prio 5
I: 2 -> T1: prio after 5
I: 2 -> MS2:  T1 prio 5
I: --------------
I: 3 -> T1: prio before 5
I: 3 ---> L1: T1 prio 5
I: 3 -> MS1:  T1 prio 5
I: 3 ---> L2: T1 prio 5
I: 3 -> T1: prio after 5
I: 3 -> MS2:  T1 prio 5
I: --------------
I: 4 -> T1: prio before 5
I: 4 ---> L1: T1 prio 5
I: 4 ---> L2: T1 prio 5
I: 4 -> T1: prio after 5
I: 4 -> MS2:  T1 prio 5
I: --------------
I: 5 -> T1: prio before 5
I: 5 ---> L1: T1 prio 5
I: 5 ---> L2: T1 prio 5
I: 5 -> T1: prio after 5
I: 5 -> MS2:  T1 prio 5
I: --------------
I: 6 -> T1: prio before 5
I: 6 ---> L1: T1 prio 5
I: 6 -> MS1:  T1 prio 5
I: 6 -> MS2:  T1 prio 5
I: 6 ---> L2: T1 prio 5
I: 6 -> T1: prio after 5
I: N -> S1:  T1 prio 5
I: 6 -> S1:  T1 prio 5
I: --------------
<continues>
```

Exit QEMU by pressing `CTRL+A` `x`.

The figure below illustrates the execution of the same scenario but with the priority boost enabled.
The developer must enable the priority boost and properly attach all the observers to their threads.

[![ZBus example scenario for priority boost enabled.](../../../../_images/with_hlp_priority_boost_feature.svg)](../../../../_images/with_hlp_priority_boost_feature.svg)

To execute the sample with priority boost feature enabled, run the following command:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/subsys/zbus/priority_boost -- -DCONFIG_ZBUS_PRIORITY_BOOST=y
west build -t run
```

### Sample Output

```shell
I: --------------
I: 0 -> T1: prio before 5
I: 0 ---> L1: T1 prio 1
I: 0 ---> L2: T1 prio 1
I: N -> S1:  T1 prio 5
I: 0 -> S1:  T1 prio 5
I: 0 -> MS1:  T1 prio 5
I: 0 -> MS2:  T1 prio 5
I: 0 -> T1: prio after 5
I: --------------
I: 1 -> T1: prio before 5
I: 1 ---> L1: T1 prio 1
I: 1 ---> L2: T1 prio 1
I: N -> S1:  T1 prio 5
I: 1 -> S1:  T1 prio 5
I: 1 -> MS1:  T1 prio 5
I: 1 -> MS2:  T1 prio 5
I: 1 -> T1: prio after 5
I: --------------
I: 2 -> T1: prio before 5
I: 2 ---> L1: T1 prio 2
I: 2 ---> L2: T1 prio 2
I: 2 -> MS1:  T1 prio 5
I: 2 -> MS2:  T1 prio 5
I: 2 -> T1: prio after 5
I: --------------
I: 3 -> T1: prio before 5
I: 3 ---> L1: T1 prio 2
I: 3 ---> L2: T1 prio 2
I: 3 -> MS1:  T1 prio 5
I: 3 -> MS2:  T1 prio 5
I: 3 -> T1: prio after 5
I: --------------
I: 4 -> T1: prio before 5
I: 4 ---> L1: T1 prio 3
I: 4 ---> L2: T1 prio 3
I: 4 -> MS2:  T1 prio 5
I: 4 -> T1: prio after 5
I: --------------
I: 5 -> T1: prio before 5
I: 5 ---> L1: T1 prio 3
I: 5 ---> L2: T1 prio 3
I: 5 -> MS2:  T1 prio 5
I: 5 -> T1: prio after 5
I: --------------
I: 6 -> T1: prio before 5
I: 6 ---> L1: T1 prio 1
I: 6 ---> L2: T1 prio 1
I: N -> S1:  T1 prio 5
I: 6 -> S1:  T1 prio 5
I: 6 -> MS1:  T1 prio 5
I: 6 -> MS2:  T1 prio 5
I: 6 -> T1: prio after 5
I: --------------
<continues>
```

Exit QEMU by pressing `CTRL+A` `x`.
