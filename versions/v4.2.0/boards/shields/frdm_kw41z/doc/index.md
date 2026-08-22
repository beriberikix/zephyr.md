---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/frdm_kw41z/doc/index.html
original_path: boards/shields/frdm_kw41z/doc/index.html
---

# NXP FRDM-KW41Z Shield

## Overview

The FRDM-KW41Z is a development kit enabled by the Kinetis® W series
KW41Z/31Z/21Z (KW41Z) family built on ARM® Cortex®-M0+ processor with
integrated 2.4 GHz transceiver supporting Bluetooth® Smart/Bluetooth® Low Energy
(BLE) v4.2, Generic FSK, IEEE® 802.15.4 and Thread.

The FRDM-KW41Z can be used as a standalone board or as an Arduino shield. This
document covers usage as a shield; see [FRDM-KW41Z](../../../nxp/frdm_kw41z/doc/index.md#frdm_kw41z) for usage as a
standalone board.

## Bluetooth Controller

To use the FRDM-KW41Z as a Bluetooth low energy controller shield with a serial
host controller interface (HCI):

1. Download the MCUXpresso SDK for FRDM-KW41Z from the [MCUXpresso SDK Builder
   Website](https://mcuxpresso.nxp.com) [[8]](#id15).
2. Open the MCUXpresso IDE or IAR project in
   `boards/frdmkw41z/wireless_examples/bluetooth/hci_black_box/bm`
3. Open `source/common/app_preinclude.h` and add the following line:

   ```shell
   #define gSerialMgrRxBufSize_c 64
   ```
4. Build the project to generate a binary `hci_black_box_frdmkw41z.bin`.
5. Connect the FRDM-KW41Z board to your computer with a USB cable. A USB mass
   storage device should enumerate.
6. Program the binary to flash by copying it to the USB mass storage device.
7. Remove the USB cable to power down the board.
8. Configure the jumpers J30 and J31 such that:

   - J30 pin 1 is attached to J31 pin 2
   - J30 pin 2 is attached to J31 pin 1

   The jumpers should be parallel to the Arduino headers. This configuration
   routes the UART RX and TX signals to the Arduino header, rather than to the
   OpenSDA circuit.
9. Attach the FRDM-KW41Z to the Arduino header on your selected main board,
   such as [MIMXRT1050-EVK](../../../nxp/mimxrt1050_evk/doc/index.md#mimxrt1050_evk) or [FRDM-K64F](../../../nxp/frdm_k64f/doc/index.md#frdm_k64f).
10. Set `--shield frdm_kw41z` when you invoke `west build` in
    your Zephyr bluetooth application. For example,

    ```shell
    # From the root of the zephyr repository
    west build -b frdm_k64f --shield frdm_kw41z samples/bluetooth/peripheral_hr
    ```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id1)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id3), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id5) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id7)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id9)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id11) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id13)

## References

[[1](#id2)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id4)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id6)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id8)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id10)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id12)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id14)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[[8](#id16)]

[https://mcuxpresso.nxp.com](https://mcuxpresso.nxp.com)
