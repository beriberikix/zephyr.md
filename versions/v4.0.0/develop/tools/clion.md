---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/tools/clion.html
original_path: develop/tools/clion.html
---

# CLion

[CLion](https://www.jetbrains.com/clion/) is a cross-platform C/C++ IDE that supports multi-threaded RTOS debugging.

This guide describes the process of setting up, building, and debugging Zephyr’s
[Basic thread manipulation](../../samples/basic/threads/README.md#multi-thread-blinky "Spawn multiple threads that blink LEDs and print information to the console.") sample in CLion.

The instructions have been tested on Windows. In terms of the CLion workflow, the steps would be the
same for macOS and Linux, but make sure to select the correct environment file and to adjust the
paths.

## Get CLion

[Download CLion](https://www.jetbrains.com/clion/download) and install it.

## Initialize a new workspace

This guide gives details on how to build and debug the [Basic thread manipulation](../../samples/basic/threads/README.md#multi-thread-blinky "Spawn multiple threads that blink LEDs and print information to the console.")
sample application, but the instructions would be similar for any Zephyr project and [workspace
layout](../west/workspaces.md#west-workspaces).

Before you start, make sure you have a working Zephyr development environment, as per the
instructions in the [Getting Started Guide](../getting_started/index.md#getting-started).

## Open the project in CLion

1. In CLion, click Open on the Welcome screen or select File ‣ Open
   from the main menu.
2. Navigate to your Zephyr workspace (i.e.the `zephyrproject` folder in your HOME directory if
   you have followed the Getting Started instructions), then select
   `zephyr/samples/basic/threads` or another sample project folder.

   Click OK.
3. If prompted, click Trust Project.

   See the [Project security](https://www.jetbrains.com/help/clion/project-security.html#projects_security) section in CLion web help for more information on project security.

## Configure the toolchain and CMake profile

CLion will open the Open Project Wizard with the CMake profile settings. If that does
not happen, go to Settings ‣ Build, Execution, Deployment ‣ CMake.

1. Click Manage Toolchains next to the Toolchain field. This will open the
   Toolchain settings dialog.
2. We recommend that you use the Bundled MinGW toolchain with default settings on
   Windows, or the System (default) toolchain on Unix machines.
3. Click Add environment ‣ From file and select
   `..\.venv\Scripts\activate.bat`.

   [![MinGW toolchain with environment script](../../_images/clion_toolchain_mingw.webp)
   ](../../_images/clion_toolchain_mingw.webp)

   Click Apply to save the changes.
4. Back in the CMake profile settings dialog, specify your board in the CMake options
   field. For example:

   ```text
   -DBOARD=nrf52840dk/nrf52840
   ```

   [![CMake profile](../../_images/clion_cmakeprofile.webp)
   ](../../_images/clion_cmakeprofile.webp)
5. Click Apply to save the changes.

   CMake load should finish successfully.

## Configure Zephyr parameters for debug

1. In the configuration switcher on the top right, select guiconfig and click the hammer
   icon.
2. Use the GUI application to set the following flags:

   ```text
   DEBUG_THREAD_INFO
   THREAD_RUNTIME_STATS
   DEBUG_OPTIMIZATIONS
   ```

## Build the project

In the configuration switcher, select **zephyr\_final** and click the hammer icon.

Note that other CMake targets like `puncover` or `hardenconfig` can also be called at this
point.

## Enable RTOS integration

1. Go to Settings ‣ Build, Execution, Deployment ‣ Embedded Development ‣ RTOS
   Integration.
2. Set the Enable RTOS Integration checkbox.

   This option enables Zephyr tasks view during debugging. See [Multi-threaded RTOS debug](https://www.jetbrains.com/help/clion/rtos-debug.html) in CLion
   web help for more information.

   You can leave the option set to Auto. CLion will detect Zephyr automatically.

## Create an Embedded GDB Server configuration

In order to debug a Zephyr application in CLion, you need to create a run/debug configuration out of
the Embedded GDB Server template.

Instructions below show the case of a Nordic Semiconductor board and a Segger J-Link debug probe. If
your setup is different, make sure to adjust the configuration settings accordingly.

1. Select Run ‣ New Embedded Configuration from the main menu.
2. Configure the settings:

   > | Option | Value |
   > | --- | --- |
   > | Name (optional) | Zephyr-threads |
   > | GDB Server Type | Segger JLink |
   > | Location | The path to `JLinkGDBServerCL.exe` on Windows or the `JLinkGDBServer` binary on macOS/Linux. |
   > | Debugger | Bundled GDB  Note  For non-ARM and non-x86 architectures, use a GDB executable from Zephyr SDK. Make sure to pick a version with Python support (for example, **riscv64-zephyr-elf-gdb-py**) and check that Python is present in the system `PATH`. |
   > | Target | zephyr-final |
   > | Executable binary | zephyr-final |
   > | Download binary | Always |
   > | TCP/IP port | Auto |
   >
   > [![Embedded GDB server configuration](../../_images/clion_gdbserverconfig.webp)
   > ](../../_images/clion_gdbserverconfig.webp)
3. Click Next to set the Segger J-Link parameters.

   > [![Segger J-Link parameters](../../_images/clion_segger_settings.webp)
   > ](../../_images/clion_segger_settings.webp)
4. Click Create when ready.

## Start debugging

1. Place breakpoints by clicking in the left gutter next to the code lines.
2. Make sure that **Zephyr-threads** is selected in the configuration switcher and click the bug
   icon or press `Ctrl`+`D`.
3. When a breakpoint is hit, CLion opens the Debug tool window.

   Zephyr tasks are listed in the Threads & Variables pane. You can switch between them
   and inspect the variables for each task.

   > [![Viewing Zephyr tasks during a debug session](../../_images/clion_debug_threads.webp)
   > ](../../_images/clion_debug_threads.webp)

   Refer to [CLion web help](https://www.jetbrains.com/help/clion/debugging-code.html) for detailed description of the IDE debug capabilities.
