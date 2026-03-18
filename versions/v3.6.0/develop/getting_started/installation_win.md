---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/getting_started/installation_win.html
original_path: develop/getting_started/installation_win.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Windows alternative setup instructions

## Windows 10 WSL (Windows Subsystem for Linux)

If you are running a recent version of Windows 10 you can make use of the
built-in functionality to natively run Ubuntu binaries directly on a standard
command-prompt. This allows you to use software such as the [Zephyr SDK](../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk) without setting up a virtual machine.

Warning

Windows 10 version 1803 has an issue that will cause CMake to not work
properly and is fixed in version 1809 (and later).
More information can be found in [Zephyr Issue 10420](https://github.com/zephyrproject-rtos/zephyr/issues/10420).

1. [Install the Windows Subsystem for Linux (WSL)](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide).

   Note

   For the Zephyr SDK to function properly you will need Windows 10
   build 15002 or greater. You can check which Windows 10 build you are
   running in the “About your PC” section of the System Settings.
   If you are running an older Windows 10 build you might need to install
   the Creator’s Update.
2. Follow the Ubuntu instructions in the [Install Linux Host Dependencies](installation_linux.md#installation-linux) document.
