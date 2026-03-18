---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/poweroff.html
original_path: services/poweroff.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Power off

*group* sys\_poweroff
:   Functions

    FUNC\_NORETURN void sys\_poweroff(void)
    :   Perform a system power off.

        This function will perform an immediate power off of the system. It is the responsability of the caller to ensure that the system is in a safe state to be powered off. Any required wake up sources must be enabled before calling this function.

        [`CONFIG_POWEROFF`](../kconfig.md#CONFIG_POWEROFF "CONFIG_POWEROFF") needs to be enabled to use this API.
