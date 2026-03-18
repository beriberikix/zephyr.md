---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/tfm_integration/tfm_ipc/README.html
original_path: samples/tfm_integration/tfm_ipc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# TF-M IPC

## Overview

This is a simple TF-M integration example that can be used with an ARMv8-M
supported board.

It uses **IPC Mode** for communication, where TF-M API calls are made to the
secure image via an IPC mechanism, as opposed to **Library Mode**, where the
IPC mechanism is bypassed in favor of direct calls.

Zephyr uses Trusted Firmware (TF-M) Platform Security Architecture (PSA) APIs
to run this sample in a secure configuration, with Zephyr itself running in a
non-secure configuration.

The sample prints test info to the console either as a single-thread or
multi-thread application.

The sample reboots after 5 seconds to demonstrate rebooting with TF-M.
The sys\_reboot call is routed to TF-M, since the nonsecure app is not allowed
to perform the reboot directly.

## Building and Running

This project outputs test status and info to the console. It can be built and
executed on MPS2+ AN521 and ST Nucleo L552ZE Q.

### On MPS2+ AN521:

1. Build Zephyr with a non-secure configuration (`-DBOARD=mps2/an521/cpu0/ns`).

   ```shell
   cd $ZEPHYR_ROOT/samples/tfm_integration/tfm_ipc/
   mkdir build
   cd build
   cmake -DBOARD=mps2/an521/cpu0/ns ..
   make
   ```

You can also use west as follows:

> ```shell
> $ west build -p -b mps2/an521/cpu0/ns zephyr/samples/tfm_integration/tfm_ipc
> ```

1. Copy application binary files (mcuboot.bin and tfm\_sign.bin) to `<MPS2 device name>/SOFTWARE/`.
2. Open `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`. Edit the `AN521/images.txt` file as follows:

   ```shell
   TITLE: Versatile Express Images Configuration File

   [IMAGES]
   TOTALIMAGES: 2 ;Number of Images (Max: 32)

   IMAGE0ADDRESS: 0x10000000
   IMAGE0FILE: \SOFTWARE\mcuboot.bin  ; BL2 bootloader

   IMAGE1ADDRESS: 0x10080000
   IMAGE1FILE: \SOFTWARE\tfm_sign.bin ; TF-M with application binary blob
   ```
3. Reset MPS2+ board.

If you get the following error when running cmake:

> ```shell
> CMake Error at cmake/Common/FindGNUARM.cmake:121 (message):
> arm-none-eabi-gcc can not be found.  Either put arm-none-eabi-gcc on the
> PATH or set GNUARM_PATH properly.
> ```

You may need to edit the `CMakeLists.txt` file in the `tfm_ipc` project
folder to update the `-DGNUARM_PATH=/opt/toolchain/arm-none-eabi` path.

### On QEMU:

The MPS2+ AN521 target (`mps2/an521/cpu0/ns`), which is based on a
dual core ARM Cortex-M33 setup, also allows you to run TF-M tests using QEMU if
you don’t have access to a supported ARMv8-M development board.

As part of the normal build process above, a binary is also produced that can
be run via `qemu-system-arm`. The binary can be executed as follows:

> ```shell
> qemu-system-arm -M mps2-an521 -device loader,file=build/zephyr/tfm_merged.hex -serial stdio
> ```

You can also run the binary as part of the `west` build process by appending
the `-t run` flag to the end of your build command, or in the case of
ninja or make, adding the `run` commands:

> ```shell
> $ west build -b mps2/an521/cpu0/ns zephyr/samples/tfm_integration/tfm_ipc -t run
> ```

Or, post build:

> ```shell
> $ ninja run
> ```

### On ST Nucleo L552ZE Q or STM32L562E-DK Discovery:

This sample was tested on Ubuntu 18.04 with Zephyr SDK 0.11.3.

Build Zephyr with a non-secure configuration:

> Example, for building non-secure configuration for Nucleo L552ZE Q
>
> ```shell
> $ west build -b nucleo_l552ze_q/stm32l552xx/ns samples/tfm_integration/tfm_ipc/
> ```
>
> Example, for building non-secure configuration for STM32L562E-DK Discovery
>
> ```shell
> $ west build -b stm32l562e_dk/stm32l562xx/ns samples/tfm_integration/tfm_ipc/
> ```

The script to initialize the device is available in the `build/tfm` folder:

> - `regression.sh`: Sets platform option bytes config and erase platform.

Run them in the following order to flash the board:

> > ```shell
> > $ ./build/tfm/api_ns/regression.sh
> > $ west flash
> > ```
>
> Note
>
> Note that `arm-none-eabi-gcc` should be available in the PATH variable and that `STM32_Programmer_CLI` is required to run `regression.sh` (see [https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)). If you are still having trouble running these scripts, check the Programming and Debugging section of the [ST Nucleo L552ZE Q](../../../boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.md#nucleo-l552ze-q-board) or [ST STM32L562E-DK Discovery](../../../boards/st/stm32l562e_dk/doc/index.md#stm32l562e-dk-board) documentation.

### On LPCxpresso55S69:

Build Zephyr with a non-secure configuration:

> ```shell
> $ west build -p -b lpcxpresso55s69_ns samples/tfm_integration/tfm_ipc/ --
> ```

Make sure your board is set up with [LPC-Link2 J-Link Onboard Debug Probe](../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe),
since this isn’t the debug interface boards ship with from the factory;

Next we need to manually flash the resulting image (`tfm_merged.bin`) with a
J-Link as follows:

> ```shell
> JLinkExe -device lpc55s69 -if swd -speed 2000 -autoconnect 1
> J-Link>r
> J-Link>erase
> J-Link>loadfile build/zephyr/tfm_merged.bin
> ```

Resetting the board and erasing it will unlock the board, this is useful in case
it’s in an unknown state and can’t be flashed.

We need to reset the board manually after flashing the image to run this code.

### On nRF5340 and nRF9160:

Build Zephyr with a non-secure configuration
(`-DBOARD=nrf5340dk/nrf5340/cpuapp/ns` or `-DBOARD=nrf9160dk/nrf9160/ns`).

> Example, for nRF9160, using `cmake` and `ninja`
>
> ```shell
> cd <ZEPHYR_ROOT>/samples/tfm_integration/tfm_ipc/
> rm -rf build
> mkdir build && cd build
> cmake -GNinja -DBOARD=nrf9160dk/nrf9160/ns ..
> ```

If building with BL2 (MCUboot bootloader) enabled, manually flash
the MCUboot bootloader image binary (`bl2.hex`).

> Example, using `nrfjprog` on nRF9160:
>
> ```shell
> nrfjprog -f NRF91 --program tfm/bin/bl2.hex --sectorerase
> ```

Finally, flash the concatenated TF-M + Zephyr binary.

> Example, for nRF9160, using `cmake` and `ninja`
>
> ```shell
> ninja flash
> ```

### On BL5340:

Build Zephyr with a non-secure configuration
(`-DBOARD=bl5340_dvk/nrf5340/cpuapp/ns`).

> Example using `cmake` and `ninja`
>
> ```shell
> cd <ZEPHYR_ROOT>/samples/tfm_integration/tfm_ipc/
> rm -rf build
> mkdir build && cd build
> cmake -GNinja -DBOARD=bl5340_dvk/nrf5340/cpuapp/ns ..
> ```

Flash the concatenated TF-M + Zephyr binary.

> Example using `west`
>
> ```shell
> west flash --hex-file zephyr/tfm_merged.hex
> ```

### Sample Output

```shell
[INF] Starting bootloader
[INF] Swap type: none
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!
TFM level is: 1 [Sec Thread] Jumping to non-secure code...
**** Booting Zephyr OS build zephyr-v1.14.0-2904-g89616477b115 ****
The version of the PSA Framework API is 256.
The minor version is 1.
Connect success!
TFM service support minor version is 1.
psa_call is successful!
outvec1 is: It is just for IPC call test.
outvec2 is: It is just for IPC call test.
Connect success!
Call IPC_INIT_BASIC_TEST service Pass Connect success!
Call PSA RoT access APP RoT memory test service Pass
TF-M IPC on (.*)
```
