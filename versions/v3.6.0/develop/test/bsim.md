---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/test/bsim.html
original_path: develop/test/bsim.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# BabbleSim

## BabbleSim and Zephyr

In the Zephyr project we use the [Babblesim](https://BabbleSim.github.io) simulator to test some of the Zephyr radio protocols,
including the BLE stack, 802.15.4, and some of the networking stack.

[BabbleSim](https://BabbleSim.github.io) is a physical layer simulator, which in combination with the Zephyr
[bsim boards](../../boards/posix/doc/bsim_boards_design.md#bsim-boards)
can be used to simulate a network of BLE and 15.4 devices.
When we build Zephyr targeting a [bsim board](../../boards/posix/doc/bsim_boards_design.md#bsim-boards) we produce a Linux
executable, which includes the application, Zephyr OS, and models of the HW.

When there is radio activity, this Linux executable will connect to the BabbleSim Phy simulation
to simulate the radio channel.

In the BabbleSim documentation you can find more information on how to
[get](https://babblesim.github.io/fetching.html) and
[build](https://babblesim.github.io/building.html) the simulator.
In the [nrf52\_bsim](../../boards/posix/nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim) and [nrf5340bsim](../../boards/posix/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim) boards documentation
you can find more information about how to build Zephyr targeting these particular boards,
and a few examples.

## Types of tests

### Tests without radio activity: bsim tests with twister

The [bsim boards](../../boards/posix/doc/bsim_boards_design.md#bsim-boards) can be used without radio activity, and in that case, it is not
necessary to connect them to a physical layer simulation. Thanks to this, these target boards can
be used just like [native\_sim](../../boards/posix/native_sim/doc/index.md#native-sim) with [twister](twister.md#twister-script),
to run all standard Zephyr twister tests, but with models of a real SOC HW, and their drivers.

### Tests with radio activity

When there is radio activity, BabbleSim tests require at the very least a physical layer simulation
running, and most, more than 1 simulated device. Due to this, these tests are not build and run
with twister, but with a dedicated set of tests scripts.

These tests are kept in the `tests/bsim/` folder. There you can find a README with more
information about how to build and run them, as well as the convention they follow.

There are two main sets of tests of these type:

- Self checking embedded application/tests: In which some of the simulated devices applications are
  built with some checks which decide if the test is passing or failing. These embedded
  applications tests use the [bs\_tests](../../boards/posix/doc/bsim_boards_design.md#bsim-boards-bs-tests) system to report the pass or
  failure, and in many cases to build several tests into the same binary.
- Test using the [EDTT](https://github.com/EDTTool/EDTT) tool, in which a EDTT (python) test controls the embedded applications over
  an RPC mechanism, and decides if the test passes or not.
  Today these tests include a very significant subset of the BT qualification test suite.

More information about how different tests types relate to BabbleSim and the bsim boards can be
found in the [bsim boards tests section](../../boards/posix/doc/bsim_boards_design.md#bsim-boards-tests).

## Test coverage and BabbleSim

As the [nrf52\_bsim](../../boards/posix/nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim) and [nrf5340bsim](../../boards/posix/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim) boards are based on the
POSIX architecture, you can easily collect test coverage information.

You can use the script [tests/bsim/generate\_coverage\_report.sh](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bsim/generate_coverage_report.sh) to generate an html
coverage report from tests.

Check [the page on coverage generation](coverage.md#coverage-posix) for more info.
