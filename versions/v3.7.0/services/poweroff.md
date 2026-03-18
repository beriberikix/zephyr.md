---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/poweroff.html
original_path: services/poweroff.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Power off

*group* System power off
:   Functions

    FUNC\_NORETURN void sys\_poweroff(void)
    :   Perform a system power off.

        This function will perform an immediate power off of the system. It is the responsibility of the caller to ensure that the system is in a safe state to be powered off. Any required wake up sources must be enabled before calling this function.

        [`CONFIG_POWEROFF`](../kconfig.md#CONFIG_POWEROFF "CONFIG_POWEROFF") needs to be enabled to use this API.
