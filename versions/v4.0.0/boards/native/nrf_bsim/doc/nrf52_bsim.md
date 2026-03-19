---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/native/nrf_bsim/doc/nrf52_bsim.html
original_path: boards/native/nrf_bsim/doc/nrf52_bsim.html
---

# NRF52 simulated board (BabbleSim)

## [Overview](#id1)

To allow simulating a nRF52833 SOC a Zephyr target boards is provided: the
nrf52\_bsim.

This uses [BabbleSim](https://BabbleSim.github.io) to simulate the radio activity, and the
[POSIX architecture](../../doc/arch_soc.md#posix-arch) and the [native simulator](https://github.com/BabbleSim/native_simulator/blob/main/docs/README.md) to
run applications natively on the development system. This has the benefit of
providing native code execution performance and easy debugging using
native tools, but inherits [its limitations](../../doc/arch_soc.md#posix-arch-limitations).

This board includes models of some of the nRF52 SOC peripherals:

- Radio
- Timers
- AAR (Accelerated Address Resolver)
- AES CCM & AES ECB encryption HW
- CLOCK (Clock control)
- EGU (Event Generator Unit)
- FICR (Factory Information Configuration Registers)
- GPIO & GPIOTE
- NVMC (Non-Volatile Memory Controller / Flash)
- PPI (Programmable Peripheral Interconnect)
- RNG (Random Number Generator)
- RTC (Real Time Counter)
- TEMP (Temperature sensor)
- UART & UARTE (UART with Easy DMA)
- UICR (User Information Configuration Registers)

and will use the same drivers as the nrf52 dk targets for these.
For more information on what is modelled to which level of detail,
check the [HW models implementation status](https://github.com/BabbleSim/ext_nRF_hw_models/blob/main/docs/README_impl_status.md).

Note that unlike a real nrf52 device, the nrf52\_bsim has unlimited RAM and flash for code.

## [Building and running](#id2)

This board requires the host 32 bit C library. See
[POSIX Arch dependencies](../../doc/arch_soc.md#posix-arch-deps).

To target this board you also need to have [BabbleSim](https://BabbleSim.github.io) compiled in your system.
If you do not have it yet, the easiest way to get it, is to enable the babblesim group
in your local west configuration, running west update, and building the simulator:

```shell
west config manifest.group-filter -- +babblesim
west update
cd ${ZEPHYR_BASE}/../tools/bsim
make everything -j 8
```

Note

If you need more BabbleSim components, or more up to date versions,
you can check the [BabbleSim web page](https://BabbleSim.github.io)
for instructions on how to
[fetch](https://babblesim.github.io/fetching.html) and
[build](https://babblesim.github.io/building.html) it.

You will now need to define two environment variables to point to your BabbleSim
installation, `BSIM_OUT_PATH` and `BSIM_COMPONENTS_PATH`.
If you followed the previous steps, you can just do:

```shell
export BSIM_OUT_PATH=${ZEPHYR_BASE}/../tools/bsim
export BSIM_COMPONENTS_PATH=${BSIM_OUT_PATH}/components/
```

Note

You can add these two lines to your `~/.zephyrrc` file, or to your shell
initialization script (`~/.bashrc`), so you won’t need to rerun them
manually for each new shell.

You’re now ready to build applications targeting this board, for example:

```shell
west build -b nrf52_bsim samples/hello_world
```

Then you can execute your application using:

```shell
$ ./build/zephyr/zephyr.exe -nosim
# Press Ctrl+C to exit
```

Note that the executable is a BabbleSim executable. The `-nosim` command line
option indicates you want to run it detached from a BabbleSim simulation. This
is possible only while there is no radio activity. But is perfectly fine for
most Zephyr samples and tests.

When you want to run a simulation with radio activity you need to run also the
BableSim 2G4 (2.4GHz) physical layer simulation (phy).

For example, if you would like to run a simple case with a BLE [Heart-rate Monitor (Central)](../../../../samples/bluetooth/central_hr/README.md#ble_central_hr "Connect to a Bluetooth LE heart-rate monitor and read heart-rate measurements.")
sample application connecting to a BLE [Heart-rate Monitor (Peripheral)](../../../../samples/bluetooth/peripheral_hr/README.md#ble_peripheral_hr "Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.") sample application:
Build the [Heart-rate Monitor (Central)](../../../../samples/bluetooth/central_hr/README.md#ble_central_hr "Connect to a Bluetooth LE heart-rate monitor and read heart-rate measurements.") application targeting this board and copy the
resulting executable to the simulator bin folder with a sensible name:

```shell
west build -b nrf52_bsim samples/bluetooth/central_hr
```

```shell
$ cp build/zephyr/zephyr.exe \
  ${BSIM_OUT_PATH}/bin/bs_nrf52_bsim_samples_bluetooth_central_hr
```

Do the same for the [Heart-rate Monitor (Peripheral)](../../../../samples/bluetooth/peripheral_hr/README.md#ble_peripheral_hr "Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.") sample app:

```shell
west build -b nrf52_bsim samples/bluetooth/peripheral_hr
```

```shell
$ cp build/zephyr/zephyr.exe \
  ${BSIM_OUT_PATH}/bin/bs_nrf52_bsim_samples_bluetooth_peripheral_hr
```

And then run them together with BabbleSim’s 2G4 physical layer simulation:

```shell
cd ${BSIM_OUT_PATH}/bin/
./bs_nrf52_bsim_samples_bluetooth_peripheral -s=trial_sim -d=0 &
./bs_nrf52_bsim_samples_bluetooth_central_hr -s=trial_sim -d=1 &
./bs_2G4_phy_v1 -s=trial_sim -D=2 -sim_length=10e6 &
```

Where the `-s` command line option provides a string which uniquely identifies
this simulation; the `-D` option tells the Phy how many devices will be run
in this simulation; the `-d` option tells each device which is its device
number in the simulation; and the `-sim_length` option specifies the length
of the simulation in microseconds.
BabbleSim devices and Phy support many command line switches.
Run them with `-help` for more information.

You can find more information about how to run BabbleSim simulations in
[this BabbleSim example](https://babblesim.github.io/example_2g4.html).

## [C library choice](#id3)

These nRF bsim boards use the [native simulator](https://github.com/BabbleSim/native_simulator/blob/main/docs/README.md) at their core, so you can chose with which
C library you want to build your embedded code.
Check the [native simulator C library choice section](../../native_sim/doc/index.md#native-sim-clib-choice) for more info.

## [Debugging, coverage and address sanitizer](#id4)

Just like with [native\_sim](../../native_sim/doc/index.md#native-sim-debug), the resulting
executables are Linux native applications.
Therefore they can be debugged or instrumented with the same tools as any other
native application, like for example `gdb` or `valgrind`.

The same
[code coverage analysis means from the POSIX arch](../../../../develop/test/coverage.md#coverage-posix)
are inherited in this board.
Similarly, the
[address and undefined behavior sanitizers can be used as in native\_sim](../../native_sim/doc/index.md#native-sim-asan).

Note that BabbleSim will run fine if one or several of its components are
being run in a debugger or instrumented. For example, pausing a device in a
breakpoint will pause the whole simulation.

BabbleSim is fully deterministic by design and the results are not affected by
the host computing speed. All randomness is controlled by random seeds which can
be provided as command line options.

## [About time in BabbleSim](#id5)

Note that time in BabbleSim is simulated and decoupled from real time. Normally
simulated time will pass several orders of magnitude faster than real time,
only limited by your workstation compute power.
If for some reason you want to limit the speed of the simulation to real
time or a ratio of it, you can do so by connecting the [handbrake device](https://github.com/BabbleSim/base/tree/master/device_handbrake)
to the BabbleSim Phy.
