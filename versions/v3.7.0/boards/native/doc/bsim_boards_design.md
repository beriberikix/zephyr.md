---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/native/doc/bsim_boards_design.html
original_path: boards/native/doc/bsim_boards_design.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bsim boards

**Available bsim boards**

- [Simulated nRF52833 (nrf52\_bsim)](../nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim)
- [Simulated nRF5340 (nrf5340bsim)](../nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim)
- [Simulated nRF54L15 (nrf54l15bsim)](../nrf_bsim/doc/nrf54l15bsim.md#nrf54l15bsim)

This page covers the design, architecture and rationale, of the
nrf5x\_bsim boards and other similar bsim boards.
These boards are postfixed with \_bsim as they use [BabbleSim](https://BabbleSim.github.io)
(shortened bsim), to simulate the radio environment.
These boards use the [native simulator](https://github.com/BabbleSim/native_simulator/blob/main/docs/README.md) and the [POSIX architecture](arch_soc.md#posix-arch) to build
and execute the embedded code natively on Linux.

Particular details on the [nRF52](../nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim), [nRF5340](../nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim) and
[nRF54l15](../nrf_bsim/doc/nrf54l15bsim.md#nrf54l15bsim) simulation boards, including how to use them,
can be found in their respective documentation.

## [Overall objective](#id4)

The main purpose of these bsim boards is to be test-benches for
integration testing of embedded code on workstation/simulation.
Integration testing in the sense that the code under test will, at the very
least, run with the Zephyr RTOS just like for any other
[POSIX arch based board](arch_soc.md#posix-arch-rationale), but in addition these
will include some HW models which, to some degree, pretend to be the real
embedded HW.

These tests are run in workstation, that is, without using real embedded HW.
The intention being to be able to run tests much faster than real time,
without the need for real HW, and in a deterministic/reproducible fashion.

Unlike [native\_sim](../native_sim/doc/index.md#native-sim), bsim boards do not interact directly with any host
peripherals, and their execution is independent of the host load, or timing.

These boards are also designed to be used as prototyping and development environments,
which can help developing applications or communication stacks.

### [Different types of tests and how the bsim boards relate to them](#id5)

With the POSIX architecture we provided an overall
[comparison of what the POSIX arch provides vs other options](arch_soc.md#posix-arch-compare).
That comparison applies fully to these boards, but in this section we expand
further on the differences, benefits and drawbacks of different testing
methodologies normally employed by embedded SW developers and how they relate
to these boards.

- Unit tests:
  Typical unit tests frameworks provide unit testing
  support which covers a different need: testing a component in isolation.
  Zephyr provides a unit testing target (unit\_testing) which is not related to
  these bsim boards.
- Integration tests on real HW: Allows testing with the real SW
  components that may be too dependent on the exact HW particularities, and
  possibly without any changes compared to the final solution.
  As such can provide better integration coverage than simulation ins ome cases,
  but at the expense of slower execution, needing the real HW setups,
  test in general not being reproducible, and in many cases failures
  not being easy to debug.
  They otherwise serve a very similar purpose to simulation integration tests.
- Integration tests on workstation (what the POSIX arch and these boards enable)

  - Using bsim boards: Allow testing the embedded SW (or a subset), including
    the OS, models of peripherals etc. By testing them in conjunction,
    it is possible to test the components interactions and their integration.
  - Using bsim boards with the BabbleSim Physical layer simulation allows
    testing how several devices would interact with each other.
    For ex. how a left and a right earbud synchronize and exchange data and
    audio over their radio link, and how they interact with a mobile phone.
  - Using bsim boards, and the [EDTT](https://github.com/EDTTool/EDTT) framework: With the EDTT framework we can
    test the embedded code under test while controlling the test from external
    python test scripts. This is supported by compiling the embedded code with
    an special driver that handles the EDTT communication (its RPC transport)
    and an embedded application that handles the RPC calls themselves, while
    the python test scripts provide the test logic.
  - Using Zephyr’s [native\_sim](../native_sim/doc/index.md#native-sim) board: It also allows integration testing of
    the embedded code, but without any specific HW. In that way, many embedded
    components which are dependent on the HW would not be suited for testing in
    that platform. Just like the bsim boards, this Zephyr target board can
    be used with or without Zephyr’s ztest system and twister.
    The [native\_sim](../native_sim/doc/index.md#native-sim) board shares the [POSIX architecture](arch_soc.md#posix-arch),
    and native simulator runner with the bsim boards.
- Zephyr’s ztest infrastructure and Zephyr’s twister:
  Based on dedicated embedded test applications build with the code under test.
  The embedded test application is responsible for driving the tests and check
  the results on its own, and provide a test result to a PC which directs the
  test.
  Originally used as a framework for integration testing on target,
  with a very dedicated test application,
  these are fully supported with the bsim boards.

## [Design](#id6)

### [Layering: Zephyr’s arch, soc and board layers](#id7)

The basic architecture layering of these boards is as follows:

- The [native simulator](https://github.com/BabbleSim/native_simulator/blob/main/docs/README.md) runner is used to execute the code in your host.
- The architecture, SOC and board components of Zephyr are replaced with
  simulation specific ones.
- The architecture (arch) is the Zephyr [POSIX architecture](arch_soc.md#posix-arch)
  layer.
  The SOC layer is inf\_clock. And the board layer is dependent on
  the specific device we are simulating.
- The POSIX architecture provides an adaptation from the Zephyr arch API
  (which handles mostly the thread context switching) to the native simulator
  CPU thread emulation.
  See [POSIX arch architecture](arch_soc.md#posix-arch-architecture)
- The SOC inf\_clock layer provides an adaptation to the native simulator CPU “simulation”
  and the handling of control between the “CPU simulation” (Zephyr threads) and the
  HW models thread ( See [Threading](#threading) ).
- The board layer provides all SOC/ IC specific content, including
  selecting the HW models which are built in the native simulator runner context, IRQ handling,
  busy wait API (see [posix\_busy\_wait](arch_soc.md#posix-busy-wait)), and Zephyr’s printk backend.
  Note that in a normal Zephyr target interrupt handling and a custom busy wait
  would be provided by the SOC layer, but abusing Zephyr’s layering, and for the
  inf\_clock layer to be generic, these were delegated to the board.
  The board layer provides other test specific
  functionality like bs\_tests hooks, trace control, etc, and
  by means of the native simulator, provides the `main()` entry point for the Linux
  program, command line argument handling, and the overall time scheduling of
  the simulated device.
  Note that the POSIX arch and inf\_clock soc expect a set of APIs being provided by
  the board. This includes the busy wait API, a basic tracing API, the interrupt
  controller and interrupt handling APIs, `posix_exit()`,
  and `posix_get_hw_cycle()` (see `posix_board_if.h` and `posix_soc_if.h`).

![Zephyr layering in native & bsim builds](../../../_images/layering_natsim.svg)

Overall architecture in a Zephyr application in an embedded target vs a bsim
target

### [Important limitations and unsupported features](#id8)

All native and bsim boards share the same set of
[important limitations which](arch_soc.md#posix-arch-limitations)
are inherited from the POSIX arch and inf\_clock design.

Similarly, they inherit the POSIX architecture
[unsupported features set](arch_soc.md#posix-arch-unsupported).

### [Threading and overall scheduling of CPU and HW models](#id9)

The threading description, as well as the general SOC and board architecture
introduced in
[POSIX arch architecture](arch_soc.md#posix-arch-architecture) and on the
[native simulator design documentation](https://github.com/BabbleSim/native_simulator/blob/main/docs/Design.md) apply to the bsim boards.

Moreover in
[Architecture of HW models used for FW development and testing](https://babblesim.github.io/arch_hw_models.html)
a general introduction to the babblesim HW models and their scheduling are provided.

In case of the nRF bsim boards, more information can be found in the
[nRF HW models design documentation](https://github.com/BabbleSim/ext_nRF_hw_models/blob/main/docs/README_HW_models.md).

### [Time and the time\_machine](#id10)

Simulated time in bsim boards is in principle fully decoupled from
real wall-clock time. As described in
[POSIX arch architecture](arch_soc.md#posix-arch-architecture),
simulated time is advanced
as needed to the next scheduled HW event, and does not progress while
the simulated CPU is executing code.

In general simulation time will pass much faster than real time,
and the simulation results will not be affected in any way by the
load of the simulation host or by the process execution being “paused”
in a debugger or similar.

The native simulator HW scheduler provides the overall HW event time loop
required by the HW models, which consists of a very simple
“search for next event”, “advance time to next event and execute it” loop,
together with an API for components that use it to inform about their events
timers having been updated. Events are defined at design time,
they are not registered dynamically for simplicity and speed.

### [Use of babblesim components: tracing, random number generation, logging activity](#id11)

The same considerations as for the HW models apply to the bsim boards, see
[Architecture of HW models used for FW development and testing](https://babblesim.github.io/arch_hw_models.html).

The communication between a Zephyr device and other simulated devices is
handled over the bsim libPhyCom libraries. For the radio activity the figure
below represents this communication:

![Communication between a Zephyr device and other simulated devices](../../../_images/Zephyr_and_bsim.svg)

Communication between a Zephyr device and other simulated devices

Test code may also communicate with other devices’ test code using the bsim
backchannels. These provide a direct, reliable pipe between devices which test code
can use to exchange data.

### [About using Zephyr APIs](#id12)

Note that even though part of the bsim board code is linked with the Zephyr kernel,
one should in general not call Zephyr APIs from the board code itself.
In particular, one should not call Zephyr APIs from the original/HW models
thread as the Zephyr code would be called from the wrong context,
and will with all likelihood cause all kind of difficult to debug issues.

In general board code should be considered as lower level than the Zephyr OS,
and not dependent on it.
For example, board code should not use the printk API as that anyhow would
result in a call back into the board code (the bsim specific printk backend)
which relies on the bs\_trace API. Instead, for tracing the bs\_trace API
should be used directly.
The same applies to other Zephyr APIs, including the entropy API, etc.

### [posix\_print and nsi\_print backends](#id13)

The bsim board provides a backend for the `posix_print` API which is expected by the posix
ARCH and inf\_clock code, and for the `nsi_print` API expected by the native simulator.

These simply route this API calls into the `bs_trace` bsim API.
Any message printed to these APIs, and by extension by default to Zephyr’s `printk`,
will be printed to the console (stdout) together with all other device messages.

### [bs\_tests](#id14)

The bsim boards provide also the bs\_tests facility.

This allows tests to be defined (registered), and for each of these tests to
use a number of special test hooks which are present only in these simulated
targets.

These tests are built together with the embedded SW, and are present in the
binary but will not be executed by default.
From the command line the user can query what tests are present, and select
which test (if any) should be executed. When a test is selected its registered
callbacks are assigned to the respective hooks.

There is a set of one time hooks at different levels of initialization of the HW
and Zephyr OS, a hook to process possible command line arguments, and, a hook
that can be used to sniff or capture interrupts.
bs\_tests also provides a hook which will be called from the embedded application
`main()`, but this will only work if the main application supports it,
that is, if the main app is a version for simulation which calls
`bst_main()` when running in the bsim board.

Apart from these hooks, the bs\_tests system provides facilities to build a
dedicated test “task”. This will be executed in the HW models thread context,
but will have access to all SW variables. This task will be driven with a
special timer which can be configured to produce either periodic or one time
ticks. When these ticks occur a registered test tick function will be called.
This can be used to support the test logic, like run checks or perform actions
at specific points in time. This can be combined with Babblesim’s tb\_defs macros
to build quite complex test tasks which can wait for a given amount of time,
for conditions to be fulfilled, etc.

Note when writing the tests with bs\_tests one needs to be aware that other
bs tests will probably be built with the same application, and that therefore
the tests should not be registering initialization or callback functions using
NATIVE\_TASKS or Zephyr’s PRE/POST kernel driver initialization APIs as this
will execute even if the test is not selected.
Instead the equivalent bs\_tests provided hooks should be used.

Note also that, for AMP targets like the [nrf5340bsim](../nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim), each embedded MCU has
its own separate bs\_tests built with that MCU. You can select if and what test is used
for each MCU separatedly with the command line options.

### [Command line argument parsing](#id15)

bsim boards need to handle command line arguments. There are several sets of
arguments:

- Basic arguments: to enable selecting things like trace verbosity, random seed,
  simulation device number and simulation id (when connected to a phy), etc.
  This follow as much as possible the same convention as other bsim
  devices to ease use for developers.
- The HW models command line arguments: The HW models will expose which
  arguments they need to have processed, but the bsim board as actual
  integrating program ensures they are handled.
- Test (bs\_tests) control: To select a test for each embedded CPU,
  print which are available, and pass arguments to the tests themselves.

Command line argument parsing is handled by using the bs\_cmd\_line component
from Babblesim’s base/libUtilv1 library. And basic arguments definitions that
comply with the expected convention are provided in bs\_cmd\_line\_typical.h.

### [Other considerations](#id16)

- Endianness: Code will be built for the host target architecture, which is
  typically x86. x86 is little endian, which is typically also the case for the
  target architecture. If this is not the case, embedded code which works in one
  may not work in the other due to endianness bugs.
  Note that Zephyr code is be written to support both big and little endian.
- WordSize: The bsim targets, as well as normal embedded targets are 32 bit
  targets. In the case of the bsim targets this is done by explicitly targeting
  x86 (ILP32 ABI) instead of x86\_64. This is done purposefully to provide more
  accurate structures layout in memory and therefore better reproduce possible
  issues related to access to structures members or array overflows.
