---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/sip_svc/README.html
original_path: samples/subsys/sip_svc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SiP SVC sample

## Overview

This sample demonstrates the usage of SiP SVC subsystem.This sample
performs a voltage value query from Secure Device Manager in Intel Agilex
SoC FPGA.

## Caveats

- SiP SVC subsystem relies on the firmware running in EL3 layer to be in compatible
  with protocol defined inside the SiP SVC subsystem used by the project.
- The sample application relies on the Trusted Firmware ARM firmware in
  intel Agilex SoC FPGA query the voltage levels in Secure Device Manager.

## Building and Running

For building the application:

```shell
# From the root of the zephyr repository
west build -b intel_socfpga_agilex_socdk samples/subsys/sip_svc
```

For running the application the Zephyr image can be loaded in DDR memory
at address 0x00100000 and ATF BL31 at 0x00001000 from SD Card or QSPI Flash
in ATF BL2.

## Sample Output

```shell
*** Booting Zephyr OS build zephyr-v3.3.0-2963-gb5ba49ae300e ***
Got response of transaction id 0x00 and voltage is 0.846878v
Got response of transaction id 0x01 and voltage is 0.858170v
Got response of transaction id 0x02 and voltage is 0.860168v
Got response of transaction id 0x03 and voltage is 0.846832v
Got response of transaction id 0x04 and voltage is 0.858337v
Got response of transaction id 0x05 and voltage is 0.871704v
Got response of transaction id 0x06 and voltage is 0.859421v
Got response of transaction id 0x07 and voltage is 0.857254v
Got response of transaction id 0x08 and voltage is 0.858429v
Got response of transaction id 0x09 and voltage is 0.859879v
Got response of transaction id 0x0a and voltage is 0.845139v
Got response of transaction id 0x0b and voltage is 0.858459v
Got response of transaction id 0x0c and voltage is 0.859283v
Got response of transaction id 0x0d and voltage is 0.846207v
Got response of transaction id 0x0e and voltage is 0.855850v
Got response of transaction id 0x0f and voltage is 0.859283v
Got response of transaction id 0x00 and voltage is 0.846832v
Got response of transaction id 0x01 and voltage is 0.856049v
Got response of transaction id 0x02 and voltage is 0.859879v
```
