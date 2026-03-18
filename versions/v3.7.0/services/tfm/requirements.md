---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/tfm/requirements.html
original_path: services/tfm/requirements.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# TF-M Requirements

The following are some of the boards that can be used with TF-M:

| Board | NSPE board name |
| --- | --- |
| [ARM MPS2+ AN521](../../boards/arm/mps2/doc/mps2_an521.md#mps2-an521-board) | `mps2_an521_ns` (qemu supported) |
| [ARM MPS3 AN547](../../boards/arm/mps3/doc/index.md#mps3-an547-board) | `mps3_an547_ns` (qemu supported) |
| [Ezurio BL5340 DVK](../../boards/ezurio/bl5340_dvk/doc/index.md#bl5340-dvk) | `bl5340_dvk/nrf5340/cpuapp/ns` |
| [NXP LPCXPRESSO55S69](../../boards/nxp/lpcxpresso55s69/doc/index.md#lpcxpresso55s69) | `lpcxpresso55s69_ns` |
| [nRF9160 DK](../../boards/nordic/nrf9160dk/doc/index.md#nrf9160dk-nrf9160) | `nrf9160dk/nrf9160/ns` |
| [nRF5340 DK](../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340) | `nrf5340dk/nrf5340/cpuapp/ns` |
| [ST B\_U585I\_IOT02A Discovery kit](../../boards/st/b_u585i_iot02a/doc/index.md#b-u585i-iot02a-board) | `b_u585i_iot02a/stm32u585xx/ns` |
| [ST Nucleo L552ZE Q](../../boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.md#nucleo-l552ze-q-board) | `nucleo_l552ze_q/stm32l552xx/ns` |
| [ST STM32L562E-DK Discovery](../../boards/st/stm32l562e_dk/doc/index.md#stm32l562e-dk-board) | `stm32l562e_dk/stm32l562xx/ns` |
| [ARM V2M Musca B1](../../boards/arm/v2m_musca_b1/doc/index.md#v2m-musca-b1-board) | `v2m_musca_b1_ns` |
| [ARM V2M Musca-S1](../../boards/arm/v2m_musca_s1/doc/index.md#v2m-musca-s1-board) | `v2m_musca_s1_ns` |

You can run `west boards -n _ns$` to search for non-secure variants
of different board targets. To make sure TF-M is supported for a board
in its output, check that [`CONFIG_TRUSTED_EXECUTION_NONSECURE`](../../kconfig.md#CONFIG_TRUSTED_EXECUTION_NONSECURE "CONFIG_TRUSTED_EXECUTION_NONSECURE")
is set to `y` in that board’s default configuration.

## Software Requirements

The following Python modules are required when building TF-M binaries:

- cryptography
- pyasn1
- pyyaml
- cbor>=1.0.0
- imgtool>=1.9.0
- jinja2
- click

You can install them via:

> ```shell
> $ pip3 install --user cryptography pyasn1 pyyaml cbor>=1.0.0 imgtool>=1.9.0 jinja2 click
> ```

They are used by TF-M’s signing utility to prepare firmware images for
validation by the bootloader.

Part of the process of generating binaries for QEMU and merging signed
secure and non-secure binaries on certain platforms also requires the use of
the `srec_cat` utility.

This can be installed on Linux via:

> ```shell
> $ sudo apt-get install srecord
> ```

And on OS X via:

> ```shell
> $ brew install srecord
> ```

For Windows-based systems, please make sure you have a copy of the utility
available on your system path. See, for example:
[SRecord for Windows](https://sourceforge.net/projects/srecord/files/srecord-win32)
