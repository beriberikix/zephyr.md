---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/index.html
original_path: boards/index.html
---

# Supported Boards and Shields

If you are looking to add Zephyr support for a new board, please start with the
[Board Porting Guide](../hardware/porting/board_porting.md#board-porting-guide).

When adding support documentation for a board, remember to use the template
available under [doc/templates/board.tmpl](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/templates/board.tmpl).

Shields are hardware add-ons that can be stacked on top of a board to add extra
functionality. They are listed separately from boards, towards [the end of
this page](#boards-shields).

Search Tips

- Use the form below to filter the list of supported boards. If a field is left empty, it will
  not be used in the filtering process.
- A board must meet **all** criteria selected across different fields. For example, if you select
  both a vendor and an architecture, only boards that match both will be displayed. Within a
  single field, selecting multiple options (such as two architectures) will show boards matching
  **either** option.
- The list of supported hardware features for each board is automatically generated using
  information from the Devicetree. It may not be reflecting the full list of supported features
  since some of them may not be enabled by default.
- Can’t find your exact board? Don’t worry! If a similar board with the same or a closely related
  MCU exists, you can use it as a [starting point](../hardware/porting/board_porting.md#create-your-board-directory) for adding
  support for your own board.

Name

Architecture

Select an architecture
Altera Nios II
ARM
ARM 64
MIPS
POSIX
RISC-V
SPARC
Synopsys DesignWare ARC
x86
Xtensa

Vendor

Select a vendor
Diglent, Inc.
Telink Semiconductor
QEMU, a generic and open source machine emulator and virtualizer
STMicroelectronics
Croxel, Inc.
MikroElektronika d.o.o.
Blue Clover Devices
Blues Wireless
Gaisler
WEMOS Electronics
Realtek Semiconductor Corp.
WinChipHead
NXP Semiconductors
TDK Corporation.
Silicon Laboratories
Franzininho
Enclustra
Efinix Inc
FANKE Technology Co., Ltd.
Andes Technology Corporation
innblue UG
UP Bridge the Gap
Pine64
Nordic Semiconductor
Shenzhen Fuyuansheng Electronic Technology Co., Ltd.
Ambiq Micro, Inc.
Alientek
Raspberry Pi Foundation
LuatOS Team
01Space
Contextual Electronics
ASPEED Technology Inc.
Hardkernel Co., Ltd
Infineon Technologies
PHYTEC
BBC
Waveshare Electronics
Shenzhen Sipeed Technology Co., Ltd.
96Boards
Dragino Technology Co., Limited
u-blox
PJRC
Würth Elektronik GmbH.
Google, Inc.
Analog Devices, Inc.
SEGGER Microcontroller GmbH
WeAct Studio
Ezurio
Electronut Labs
lowRISC Community Interest Company
Ruuvi Innovations Ltd (Oy)
Ronoth
KinCony Electronics Co., Ltd.
Seagate Technology PLC
SiFive, Inc.
ITE Tech. Inc.
Antmicro
ENE Technology, Inc.
Panasonic Corporation
SparkFun Electronics
Raytac Corporation
QuickLogic Corp.
Adafruit Industries, LLC
Chengdu Ebyte Electronic Technology
Project ACRN
Norik Systems
Texas Instruments
aconno GmbH
RAKwireless Technology Limited
Renesas Electronics Corporation
Altera Corp.
OLIMEX Ltd.
Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd
Antmicro's open source simulation and virtual development framework
Other/Unknown
VNGIoTLab
Synopsys, Inc.
Element14 (A Premier Farnell Company)
Shenzhen FeiKaiTe Technology Co., Ltd.
SECO S.p.A.
Circuit Dojo
Qorvo, Inc.
open-isa.org
Atmark Techno, Inc.
Shanghai MXCHIP Information Technology Co., Ltd.
Khadas
TechNexion
BeagleBoard.org Foundation
Shenzhen Zaowubang Technology Co., Ltd.
Nuvoton Technology Corporation
Cadence Design Systems Inc.
M5Stack
Actinius B.V.
Particle.io
VCC-GND Studio
Chengdu Heltec Automation Technology Co., Ltd.
Peregrine Consultoria e Servicos
Shenzhen Holyiot Technology Co., Ltd.
Broadcom Corporation
CTHINGS.CO
Firefly
Toradex AG
ARM Ltd.
WIZnet Co., Ltd.
Seeed Technology Co., Ltd
StarFive Technology Co. Ltd.
Space Cubics, LLC
Arduino
Xen Hypervisor
Witte Technology
bytesatwork AG
EnjoyDigital
Atmel Corporation
Advanced Micro Devices (AMD), Inc.
Intel Corporation
sensry.io
GigaDevice Semiconductor
Udoo
DPTechnics
MediaTek Inc.
Makerbase Co., Ltd.
Microchip Technology Inc.
Cypress Semiconductor Corporation
Espressif Systems
GARDENA GmbH

Family

Series

SoC

Supported Hardware Capabilities

Reset Filters

Switch to Compact View

[

aconno GmbH

acn52832

arm

](../boards/aconno/acn52832/doc/index.md)
[

Advanced Micro Devices (AMD), Inc.

ACP 6.0 Xtensa Audio DSP

](../boards/amd/acp_6_0_adsp/doc/index.md)
[

Project ACRN

![A picture of the ACRN hypervisor board](../_images/ACRN-Hybrid.jpg)

ACRN hypervisor

x86

](../boards/acrn/acrn/doc/index.md)
[

Project ACRN

![A picture of the ACRN on EHL hypervisor board](../_images/ACRN-Hybrid.jpg)

ACRN on EHL hypervisor

x86

](../boards/acrn/acrn/doc/index.md)
[

Analog Devices, Inc.

![A picture of the AD-APARD32690-SL board](../_images/apard32690_img.webp)

AD-APARD32690-SL

arm

](../boards/adi/apard32690/doc/index.md)
[

Analog Devices, Inc.

![A picture of the AD-SWIOT1L-SL board](../_images/ad_swiot1l_sl.webp)

AD-SWIOT1L-SL

arm

](../boards/adi/ad_swiot1l_sl/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Adafruit MacroPad RP2040 board](../_images/adafruit_macropad_rp2040.webp)

Adafruit MacroPad RP2040

arm

](../boards/adafruit/macropad_rp2040/doc/index.md)
[

Andes Technology Corporation

![A picture of the ADP-XC7K AE350 board](../_images/adp_xc7k410.jpg)

ADP-XC7K AE350

riscv

](../boards/andestech/adp_xc7k_ae350/doc/index.md)
[

Contextual Electronics

![A picture of the Advanced BLE Cell board](../_images/contextualelectronics_abc.jpg)

Advanced BLE Cell

arm

](../boards/contextualelectronics/abc/doc/index.md)
[

96Boards

![A picture of the Aerocore2 board](../_images/96b_aerocore2.jpg)

Aerocore2

arm

](../boards/96boards/aerocore2/doc/index.md)
[

Intel Corporation

Agilex SoC Development Kit

arm64

](../boards/intel/socfpga/agilex_socdk/doc/index.md)
[

Intel Corporation

Agilex™ 5 SoC FPGA Development Kit

arm64

](../boards/intel/socfpga/agilex5_socdk/doc/index.md)
[

Intel Corporation

Alder Lake CRB

x86

](../boards/intel/adl/doc/index.md)
[

Intel Corporation

Alder Lake RVP

x86

](../boards/intel/adl/doc/index.md)
[

Ambiq Micro, Inc.

![A picture of the Apollo3 Blue EVB board](../_images/apollo3-blue-soc-eval-board.jpg)

Apollo3 Blue EVB

arm

](../boards/ambiq/apollo3_evb/doc/index.md)
[

Ambiq Micro, Inc.

![A picture of the Apollo3 Blue Plus EVB board](../_images/apollo3-blue-plus-soc-eval-board.jpg)

Apollo3 Blue Plus EVB

arm

](../boards/ambiq/apollo3p_evb/doc/index.md)
[

Ambiq Micro, Inc.

![A picture of the Apollo4 Blue Plus KXR EVB board](../_images/apollo4-blue-plus-kxr-soc-eval-board.jpg)

Apollo4 Blue Plus KXR EVB

arm

](../boards/ambiq/apollo4p_blue_kxr_evb/doc/index.md)
[

Ambiq Micro, Inc.

![A picture of the Apollo4P EVB board](../_images/apollo4-plus-soc-eval-board.jpg)

Apollo4P EVB

arm

](../boards/ambiq/apollo4p_evb/doc/index.md)
[

Synopsys, Inc.

![A picture of the ARC EM Software Development Platform board](../_images/emsdp.jpg)

ARC EM Software Development Platform

arc

](../boards/snps/emsdp/doc/index.md)
[

Synopsys, Inc.

![A picture of the ARC EM Starter Kit board](../_images/em_starterkit.jpg)

ARC EM Starter Kit

arc

](../boards/snps/em_starterkit/doc/index.md)
[

Synopsys, Inc.

![A picture of the ARC HS Development Kit board](../_images/hsdk.jpg)

ARC HS Development Kit

arc

](../boards/snps/hsdk/doc/index.md)
[

Synopsys, Inc.

![A picture of the ARC HS4x/HS4xD Development Kit board](../_images/hsdk4xd.jpg)

ARC HS4x/HS4xD Development Kit

arc

](../boards/snps/hsdk4xd/doc/index.md)
[

Synopsys, Inc.

![A picture of the ARC IoT Development Kit board](../_images/iotdk.jpg)

ARC IoT Development Kit

arc

](../boards/snps/iotdk/doc/index.md)
[

Synopsys, Inc.

ARC nSIM and HAPS FPGA boards

arc

](../boards/snps/nsim/arc_classic/doc/index.md)
[

Arduino

![A picture of the Arduino Due board](../_images/arduino_due.jpg)

Arduino Due

arm

](../boards/arduino/due/doc/index.md)
[

Arduino

![A picture of the Arduino GIGA R1 WiFi board](../_images/arduino_giga_r1.jpg)

Arduino GIGA R1 WiFi

arm

](../boards/arduino/giga_r1/doc/index.md)
[

Arduino

![A picture of the Arduino MKR Zero board](../_images/arduino_mkrzero.jpg)

Arduino MKR Zero

arm

](../boards/arduino/mkrzero/doc/index.md)
[

Arduino

![A picture of the Arduino Nano 33 BLE (Sense) board](../_images/arduino_nano_33_ble_sense.jpg)

Arduino Nano 33 BLE (Sense)

arm

](../boards/arduino/nano_33_ble/doc/index.md)
[

Arduino

![A picture of the Arduino Nano 33 IOT board](../_images/nano_33_iot.jpg)

Arduino Nano 33 IOT

arm

](../boards/arduino/nano_33_iot/doc/index.md)
[

Arduino

![A picture of the Arduino Nicla Sense ME board](../_images/arduino_nicla_sense_me.jpg)

Arduino Nicla Sense ME

arm

](../boards/arduino/nicla_sense_me/doc/index.md)
[

Arduino

![A picture of the Arduino Nicla Vision board](../_images/arduino_nicla_vision.webp)

Arduino Nicla Vision

arm

](../boards/arduino/nicla_vision/doc/index.md)
[

Arduino

![A picture of the Arduino OPTA board](../_images/arduino_opta.jpeg)

Arduino OPTA

arm

](../boards/arduino/opta/doc/index.md)
[

Arduino

![A picture of the Arduino Portenta H7 board](../_images/arduino_portenta_h7.jpeg)

Arduino Portenta H7

arm

](../boards/arduino/portenta_h7/doc/index.md)
[

Arduino

Arduino UNO R4 Minima

arm

](../boards/arduino/uno_r4/doc/index.md)
[

Arduino

Arduino UNO R4 WiFi

arm

](../boards/arduino/uno_r4/doc/index.md)
[

Arduino

![A picture of the Arduino/Genuino Zero board](../_images/arduino_zero.jpg)

Arduino/Genuino Zero

arm

](../boards/arduino/zero/doc/index.md)
[

Particle.io

![A picture of the Argon board](../_images/particle_argon.jpg)

Argon

arm

](../boards/particle/argon/doc/index.md)
[

96Boards

![A picture of the Argonkey board](../_images/96b_argonkey.jpg)

Argonkey

arm

](../boards/96boards/argonkey/doc/index.md)
[

Xen Hypervisor

ARMv8 Xen Virtual Machine Example

arm64

](../boards/xen/xenvm/doc/index.md)
[

Other/Unknown

![A picture of the Arturo182 Serpente board](../_images/serpente.jpg)

Arturo182 Serpente

arm

](../boards/others/serpente/doc/index.md)
[

Diglent, Inc.

![A picture of the Arty board](../_images/arty_a7-35.jpg)

Arty

arm

](../boards/digilent/arty_a7/doc/index.md)
[

ASPEED Technology Inc.

![A picture of the AST1030_EVB board](../_images/ast1030_evb.jpg)

AST1030\_EVB

arm

](../boards/aspeed/ast1030_evb/doc/index.md)
[

M5Stack

![A picture of the ATOM Lite board](../_images/m5stack_atom_lite.webp)

ATOM Lite

xtensa

](../boards/m5stack/m5stack_atom_lite/doc/index.md)
[

M5Stack

![A picture of the AtomS3 board](../_images/m5stack_atoms3.webp)

AtomS3

xtensa

](../boards/m5stack/m5stack_atoms3/doc/index.md)
[

M5Stack

![A picture of the AtomS3 Lite board](../_images/m5stack_atoms3_lite.webp)

AtomS3 Lite

xtensa

](../boards/m5stack/m5stack_atoms3_lite/doc/index.md)
[

96Boards

![A picture of the Avenger96 board](../_images/96b_avenger96.jpg)

Avenger96

arm

](../boards/96boards/avenger96/doc/index.md)
[

Shanghai MXCHIP Information Technology Co., Ltd.

![A picture of the AZ3166 MXChip IoT DevKit board](../_images/az3166-iotdevkit.webp)

AZ3166 MXChip IoT DevKit

arm

](../boards/mxchip/az3166_iotdevkit/doc/index.md)
[

STMicroelectronics

![A picture of the B-G474E-DPOW1 Discovery board](../_images/b_g474e_dpow1.jpg)

B-G474E-DPOW1 Discovery

arm

](../boards/st/b_g474e_dpow1/doc/index.md)
[

STMicroelectronics

![A picture of the B-L072Z-LRWAN1 Discovery kit board](../_images/b_l072z_lrwan1.jpg)

B-L072Z-LRWAN1 Discovery kit

arm

](../boards/st/b_l072z_lrwan1/doc/index.md)
[

STMicroelectronics

![A picture of the B-L4S5I-IOT01A Discovery kit board](../_images/b-l4s5i_iot01a.jpg)

B-L4S5I-IOT01A Discovery kit

arm

](../boards/st/b_l4s5i_iot01a/doc/index.md)
[

STMicroelectronics

![A picture of the B-U585I-IOT02A Discovery kit board](../_images/b-u585i-iot02a.jpg)

B-U585I-IOT02A Discovery kit

arm

](../boards/st/b_u585i_iot02a/doc/index.md)
[

ARM Ltd.

BASE RevC AEMv8A Fixed Virtual Platforms

arm64

](../boards/arm/fvp_base_revc_2xaemv8a/doc/index.md)
[

Broadcom Corporation

BCM958401M2

arm

](../boards/brcm/bcm958401m2/doc/index.md)
[

Broadcom Corporation

BCM958402M2 (Cortex-M7)

arm64, arm

](../boards/brcm/bcm958402m2/doc/a72.md)
[

BeagleBoard.org Foundation

![A picture of the BeagleBone AI-64 board](../_images/beaglebone_ai_64.webp)

BeagleBone AI-64

arm

](../boards/beagle/beaglebone_ai64/doc/index.md)
[

BeagleBoard.org Foundation

![A picture of the BeagleConnect Freedom board](../_images/beagleconnect_freedom.webp)

BeagleConnect Freedom

arm

](../boards/beagle/beagleconnect_freedom/doc/index.md)
[

BeagleBoard.org Foundation

![A picture of the BeaglePlay (CC1352) board](../_images/beagle_play.webp)

BeaglePlay (CC1352)

arm

](../boards/beagle/beagleplay/doc/beagleplay_cc1352p7.md)
[

BeagleBoard.org Foundation

![A picture of the BeagleV®-Fire board](../_images/BeagleV-Fire-Front-Annotated-768x432.webp)

BeagleV®-Fire

riscv

](../boards/beagle/beaglev_fire/doc/index.md)
[

BeagleBoard.org Foundation

![A picture of the BeagleY-AI board](../_images/beagley_ai.webp)

BeagleY-AI

arm

](../boards/beagle/beagley_ai/doc/index.md)
[

Ezurio

![A picture of the BL5340 DVK board](../_images/bl5340_dvk_top.jpg)

BL5340 DVK

arm

](../boards/ezurio/bl5340_dvk/doc/index.md)
[

Ezurio

![A picture of the BL652 DVK board](../_images/bl652_dvk.jpg)

BL652 DVK

arm

](../boards/ezurio/bl652_dvk/doc/bl652_dvk.md)
[

Ezurio

![A picture of the BL653 DVK board](../_images/bl653_dvk.jpg)

BL653 DVK

arm

](../boards/ezurio/bl653_dvk/doc/bl653_dvk.md)
[

Ezurio

![A picture of the BL654 DVK board](../_images/bl654_dvk.jpg)

BL654 DVK

arm

](../boards/ezurio/bl654_dvk/doc/bl654_dvk.md)
[

Ezurio

![A picture of the BL654 Sensor Board board](../_images/bl654_sensor_board.jpg)

BL654 Sensor Board

arm

](../boards/ezurio/bl654_sensor_board/doc/bl654_sensor_board.md)
[

Ezurio

![A picture of the BL654 USB (451-00004) board](../_images/bl654_usb.jpg)

BL654 USB (451-00004)

arm

](../boards/ezurio/bl654_usb/doc/bl654_usb.md)
[

WeAct Studio

![A picture of the Black Pill V1.2 board](../_images/blackpill-v3.jpg)

Black Pill V1.2

arm

](../boards/weact/blackpill_f401cc/doc/index.md)
[

WeAct Studio

![A picture of the Black Pill V2.0 board](../_images/blackpill-v2.jpg)

Black Pill V2.0

arm

](../boards/weact/blackpill_f411ce/doc/index.md)
[

WeAct Studio

![A picture of the Black Pill V3.0 board](../_images/blackpill-v3.jpg)

Black Pill V3.0

arm

](../boards/weact/blackpill_f401ce/doc/index.md)
[

Other/Unknown

![A picture of the Black STM32 F407VE Development Board board](../_images/black_f407ve.jpg)

Black STM32 F407VE Development Board

arm

](../boards/others/black_f407ve/doc/index.md)
[

Other/Unknown

![A picture of the Black STM32 F407ZG Pro Development Board board](../_images/black_f407zg_pro.jpg)

Black STM32 F407ZG Pro Development Board

arm

](../boards/others/black_f407zg_pro/doc/index.md)
[

Waveshare Electronics

![A picture of the BLE400 board](../_images/nrf51_ble400.jpg)

BLE400

arm

](../boards/waveshare/nrf51_ble400/doc/index.md)
[

Blue Clover Devices

![A picture of the Blue Clover PLT Demo V2 nRF52832 board](../_images/blueclover_plt_demo_v2.jpg)

Blue Clover PLT Demo V2 nRF52832

arm

](../boards/bcdevices/plt_demo_v2/doc/index.md)
[

Particle.io

![A picture of the Boron board](../_images/particle_boron.jpg)

Boron

arm

](../boards/particle/boron/doc/index.md)
[

bytesatwork AG

![A picture of the byteSENSI-L board](../_images/byteSENSI-L.jpg)

byteSENSI-L

arm

](../boards/bytesatwork/bytesensi_l/doc/index.md)
[

Other/Unknown

![A picture of the CANbardo board](../_images/canbardo.webp)

CANbardo

arm

](../boards/others/canbardo/doc/index.md)
[

Other/Unknown

![A picture of the candleLight board](../_images/candlelight.webp)

candleLight

arm

](../boards/others/candlelight/doc/index.md)
[

Other/Unknown

![A picture of the candleLightFD board](../_images/candlelightfd.webp)

candleLightFD

arm

](../boards/others/candlelightfd/doc/index.md)
[

96Boards

![A picture of the Carbon board](../_images/96b_carbon.jpg)

Carbon

arm

](../boards/96boards/carbon/doc/stm32f401xe.md)
[

Texas Instruments

![A picture of the CC1352P1 LaunchXL board](../_images/cc1352p1_launchxl.jpg)

CC1352P1 LaunchXL

arm

](../boards/ti/cc1352p1_launchxl/doc/index.md)
[

Texas Instruments

![A picture of the CC1352P7 LaunchPad board](../_images/lp-cc1352p7-top.jpg)

CC1352P7 LaunchPad

arm

](../boards/ti/cc1352p7_launchpad/doc/index.md)
[

Texas Instruments

![A picture of the CC1352R SensorTag board](../_images/cc1352r_sensortag.jpg)

CC1352R SensorTag

arm

](../boards/ti/cc1352r_sensortag/doc/index.md)
[

Texas Instruments

![A picture of the CC1352R1 LaunchXL board](../_images/cc1352r1_launchxl.jpg)

CC1352R1 LaunchXL

arm

](../boards/ti/cc1352r1_launchxl/doc/index.md)
[

Texas Instruments

![A picture of the CC2340R5 LaunchPad board](../_images/lp_em_cc2340r5.webp)

CC2340R5 LaunchPad

arm

](../boards/ti/lp_em_cc2340r5/doc/index.md)
[

Texas Instruments

![A picture of the CC26x2R1 LaunchXL board](../_images/cc26x2r1_launchxl.jpg)

CC26x2R1 LaunchXL

arm

](../boards/ti/cc26x2r1_launchxl/doc/index.md)
[

Texas Instruments

CC3220SF LaunchXL

arm

](../boards/ti/cc3220sf_launchxl/doc/index.md)
[

Texas Instruments

CC3235SF LaunchXL

arm

](../boards/ti/cc3235sf_launchxl/doc/index.md)
[

MikroElektronika d.o.o.

![A picture of the Clicker 2 for STM32 board](../_images/clicker-2-stm32f4-thickbox_default-2.jpg)

Clicker 2 for STM32

arm

](../boards/mikroe/clicker_2/doc/mikroe_clicker_2.md)
[

MikroElektronika d.o.o.

![A picture of the Clicker RA4M1 board](../_images/mikroe_clicker_ra4m1.jpg)

Clicker RA4M1

arm

](../boards/mikroe/clicker_ra4m1/doc/index.md)
[

M5Stack

![A picture of the Core2 board](../_images/m5stack_core2.webp)

Core2

xtensa

](../boards/m5stack/m5stack_core2/doc/index.md)
[

M5Stack

![A picture of the CoreS3 board](../_images/m5stack_cores3.webp)

CoreS3

xtensa

](../boards/m5stack/m5stack_cores3/doc/index.md)
[

SEGGER Microcontroller GmbH

![A picture of the Cortex-M Trace Reference Board V1.2 board](../_images/segger_trb_stm32f407.jpg)

Cortex-M Trace Reference Board V1.2

arm

](../boards/segger/trb_stm32f407/doc/index.md)
[

Antmicro's open source simulation and virtual development framework

Cortex-R8 Virtual

arm

](../boards/renode/cortex_r8_virtual/doc/index.md)
[

CTHINGS.CO

![A picture of the CTHINGS.CO Connectivity Card board](../_images/ctcc_nrf52840_m2.webp)

CTHINGS.CO Connectivity Card

arm

](../boards/ct/ctcc/doc/index.md)
[

Croxel, Inc.

![A picture of the CX1825 nRF52840 board](../_images/cx1825_nrf52840.jpg)

CX1825 nRF52840

arm

](../boards/croxel/croxel_cx1825/doc/index.md)
[

Infineon Technologies

![A picture of the CY8CPROTO-062-4343W board](../_images/board.jpg)

CY8CPROTO-062-4343W

arm

](../boards/infineon/cy8cproto_062_4343w/doc/index.md)
[

Infineon Technologies

![A picture of the CY8CPROTO-063-BLE board](../_images/cy8cproto-063-ble.jpg)

CY8CPROTO-063-BLE

arm

](../boards/infineon/cy8cproto_063_ble/doc/index.md)
[

Intel Corporation

![A picture of the Cyclone® V SoC Development Kit board](../_images/cyclonev_socdk.jpg)

Cyclone® V SoC Development Kit

arm

](../boards/intel/socfpga_std/cyclonev_socdk/doc/index.md)
[

Infineon Technologies

![A picture of the CYW920829M2EVK-02 board](../_images/cyw920829m2evk_02.webp)

CYW920829M2EVK-02

arm

](../boards/infineon/cyw920829m2evk_02/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the DA14695 Development Kit USB board](../_images/da14695-00hqdevkt-u-usb-board.jpg)

DA14695 Development Kit USB

arm

](../boards/renesas/da14695_dk_usb/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the DA1469x Development Kit Pro board](../_images/da14695-00hqdevkt-board.jpg)

DA1469x Development Kit Pro

arm

](../boards/renesas/da1469x_dk_pro/doc/index.md)
[

ARM Ltd.

![A picture of the Debug with Arm DS board](../_images/create-new-model-configuration.jpg)

Debug with Arm DS

arm, arm64

](../boards/arm/fvp_baser_aemv8r/doc/debug-with-arm-ds.md)
[

Qorvo, Inc.

Decawave DWM1001

arm

](../boards/qorvo/decawave_dwm1001_dev/doc/index.md)
[

Qorvo, Inc.

Decawave DWM3001CDK

arm

](../boards/qorvo/decawave_dwm3001cdk/doc/index.md)
[

Atmark Techno, Inc.

![A picture of the Degu Evaluation Kit board](../_images/degu_evk.jpg)

Degu Evaluation Kit

arm

](../boards/atmarktechno/degu_evk/doc/index.md)
[

STMicroelectronics

![A picture of the Disco L475 IOT01 (B-L475E-IOT01A) board](../_images/disco_l475_iot1.jpg)

Disco L475 IOT01 (B-L475E-IOT01A)

arm

](../boards/st/disco_l475_iot1/doc/index.md)
[

Google, Inc.

Dragonclaw Development Board

arm

](../boards/google/dragonclaw/doc/index.md)
[

Chengdu Ebyte Electronic Technology

![A picture of the E73-TBB board](../_images/ebyte_e73_tbb_nrf52832.jpg)

E73-TBB

arm

](../boards/ebyte/e73_tbb/doc/index.md)
[

Khadas

Edge-V

arm64

](../boards/khadas/edgev/doc/index.md)
[

Khadas

![A picture of the Edge2 board](../_images/khadas_edge2.jpg)

Edge2

arm64

](../boards/khadas/edge2/doc/index.md)
[

Silicon Laboratories

![A picture of the EFM32 Giant Gecko 11 (SLSTK3701A) board](../_images/slstk3701a.jpg)

EFM32 Giant Gecko 11 (SLSTK3701A)

arm

](../boards/silabs/starter_kits/slstk3701a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFM32 Happy Gecko (SLSTK3400A) board](../_images/slstk3400a.jpg)

EFM32 Happy Gecko (SLSTK3400A)

arm

](../boards/silabs/starter_kits/slstk3400a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFM32 Pearl Gecko (SLSTK3401A) board](../_images/slstk3401a.jpg)

EFM32 Pearl Gecko (SLSTK3401A)

arm

](../boards/silabs/starter_kits/slstk3401a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFM32 Pearl Gecko 12 (SLSTK3402A) board](../_images/slstk3402a.jpg)

EFM32 Pearl Gecko 12 (SLSTK3402A)

arm

](../boards/silabs/starter_kits/slstk3402a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFM32 Wonder Gecko (EFM32WG-STK3800) board](../_images/efm32wg_stk3800.jpg)

EFM32 Wonder Gecko (EFM32WG-STK3800)

arm

](../boards/silabs/starter_kits/efm32wg_stk3800/doc/index.md)
[

Silicon Laboratories

![A picture of the EFM32GG12 Thunderboard (SLTB009A) board](../_images/sltb009a.jpg)

EFM32GG12 Thunderboard (SLTB009A)

arm

](../boards/silabs/dev_kits/sltb009a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32BG13 2.4 GHz 10 dBm (SLWRB4104A) board](../_images/efr32bg13-slwrb4104a.jpg)

EFR32BG13 2.4 GHz 10 dBm (SLWRB4104A)

arm

](../boards/silabs/radio_boards/slwrb4104a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32BG22 Thunderboard (SLTB010A) board](../_images/sltb010a.jpg)

EFR32BG22 Thunderboard (SLTB010A)

arm

](../boards/silabs/dev_kits/sltb010a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32FG1 2400/868 MHz 13 dBm Dual Band (SLWRB4250B) board](../_images/efr32fg1-slwrb4250b.jpg)

EFR32FG1 2400/868 MHz 13 dBm Dual Band (SLWRB4250B)

arm

](../boards/silabs/radio_boards/slwrb4250b/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32FG13 2400/915 MHz 19 dBm Dual Band (SLWRB4255A) board](../_images/efr32fg13-slwrb4255a.jpg)

EFR32FG13 2400/915 MHz 19 dBm Dual Band (SLWRB4255A)

arm

](../boards/silabs/radio_boards/slwrb4255a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32MG12 2.4 GHz 19 dBm (SLWRB4161A) board](../_images/efr32mg12-slwrb4161a.jpeg)

EFR32MG12 2.4 GHz 19 dBm (SLWRB4161A)

arm

](../boards/silabs/radio_boards/slwrb4161a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32MG12 2400/868-915 MHz 19 dBm Dual Band (SLWRB4170A) board](../_images/efr32mg12-slwrb4170a.jpg)

EFR32MG12 2400/868-915 MHz 19 dBm Dual Band (SLWRB4170A)

arm

](../boards/silabs/radio_boards/slwrb4170a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32MG12 Thunderboard (SLTB004A) board](../_images/sltb004a.jpg)

EFR32MG12 Thunderboard (SLTB004A)

arm

](../boards/silabs/dev_kits/sltb004a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32xG21 2.4 GHz 20 dBm (SLWRB4180A) board](../_images/efr32mg21-slwrb4180a.jpg)

EFR32xG21 2.4 GHz 20 dBm (SLWRB4180A)

arm

](../boards/silabs/radio_boards/slwrb4180a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A) board](../_images/efr32zg23-xg23-rb4210a.jpg)

EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A)

arm

](../boards/silabs/radio_boards/xg23_rb4210a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C) board](../_images/efr32mg24-xg24-rb4187c.jpg)

EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)

arm

](../boards/silabs/radio_boards/xg24_rb4187c/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32xG24 Dev Kit (xG24-DK2601B) board](../_images/xg24_dk2601b.jpg)

EFR32xG24 Dev Kit (xG24-DK2601B)

arm

](../boards/silabs/dev_kits/xg24_dk2601b/doc/index.md)
[

Silicon Laboratories

EFR32xG24 Explorer Kit (xG24-EK2703A)

arm

](../boards/silabs/dev_kits/xg24_ek2703a/doc/index.md)
[

Silicon Laboratories

![A picture of the EFR32xG27 Dev Kit (xG27-DK2602A) board](../_images/xg27_dk2602a.png)

EFR32xG27 Dev Kit (xG27-DK2602A)

arm

](../boards/silabs/dev_kits/xg27_dk2602a/doc/index.md)
[

Silicon Laboratories

EFR32xG29 2.4 GHz 8 dBm Buck (xG29-RB4412A)

arm

](../boards/silabs/radio_boards/xg29_rb4412a/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the ek_ra2l1 board](../_images/ek_ra2l1.webp)

ek\_ra2l1

arm

](../boards/renesas/ek_ra2l1/doc/index.md)
[

Intel Corporation

Elkhart Lake CRB

x86

](../boards/intel/ehl/doc/index.md)
[

ENE Technology, Inc.

ENE KB1200\_EVB

arm

](../boards/ene/kb1200_evb/doc/index.md)
[

Espressif Systems

![A picture of the ESP-WROVER-KIT board](../_images/esp_wrover_kit.jpg)

ESP-WROVER-KIT

xtensa

](../boards/espressif/esp_wrover_kit/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-C3-DevKit-RUST board](../_images/esp32c3_rust.webp)

ESP32-C3-DevKit-RUST

riscv

](../boards/espressif/esp32c3_rust/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-C3-DevKitC board](../_images/esp32c3_devkitc.webp)

ESP32-C3-DevKitC

riscv

](../boards/espressif/esp32c3_devkitc/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-C3-DevKitM board](../_images/esp32c3_devkitm.webp)

ESP32-C3-DevKitM

riscv

](../boards/espressif/esp32c3_devkitm/doc/index.md)
[

Other/Unknown

![A picture of the ESP32-C3-SUPERMINI board](../_images/esp32c3_supermini.webp)

ESP32-C3-SUPERMINI

riscv

](../boards/others/esp32c3_supermini/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-C6-DevKitC board](../_images/esp32c6_devkitc.webp)

ESP32-C6-DevKitC

riscv

](../boards/espressif/esp32c6_devkitc/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-DevKitC-WROOM board](../_images/esp32_devkitc_wroom.jpg)

ESP32-DevKitC-WROOM

xtensa

](../boards/espressif/esp32_devkitc_wroom/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-DevKitC-WROVER board](../_images/esp32_devkitc_wrover.jpg)

ESP32-DevKitC-WROVER

xtensa

](../boards/espressif/esp32_devkitc_wrover/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-Ethernet-Kit board](../_images/esp32_ethernet_kit.jpg)

ESP32-Ethernet-Kit

xtensa

](../boards/espressif/esp32_ethernet_kit/doc/index.md)
[

OLIMEX Ltd.

![A picture of the ESP32-EVB board](../_images/ESP32-EVB.jpg)

ESP32-EVB

xtensa

](../boards/olimex/olimex_esp32_evb/doc/index.md)
[

Franzininho

![A picture of the ESP32-S2 Franzininho board](../_images/esp32_s2_franzininho.jpg)

ESP32-S2 Franzininho

xtensa

](../boards/franzininho/esp32s2_franzininho/doc/index.md)
[

WEMOS Electronics

![A picture of the ESP32-S2 Lolin Mini board](../_images/esp32_s2_lolin_mini.jpg)

ESP32-S2 Lolin Mini

xtensa

](../boards/wemos/esp32s2_lolin_mini/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-S2-DevKitC board](../_images/esp32s2_devkitc.webp)

ESP32-S2-DevKitC

xtensa

](../boards/espressif/esp32s2_devkitc/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-S2-Saola board](../_images/esp32s2_saola.webp)

ESP32-S2-Saola

xtensa

](../boards/espressif/esp32s2_saola/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-S3-DevKitC board](../_images/esp32s3_devkitc.webp)

ESP32-S3-DevKitC

xtensa

](../boards/espressif/esp32s3_devkitc/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-S3-DevKitM board](../_images/esp32s3_devkitm.webp)

ESP32-S3-DevKitM

xtensa

](../boards/espressif/esp32s3_devkitm/doc/index.md)
[

Espressif Systems

![A picture of the ESP32-S3-EYE board](../_images/esp32s3_eye.webp)

ESP32-S3-EYE

xtensa

](../boards/espressif/esp32s3_eye/doc/index.md)
[

Waveshare Electronics

![A picture of the ESP32-S3-Touch-LCD-1.28 board](../_images/esp32s3_touch_lcd_1_28.webp)

ESP32-S3-Touch-LCD-1.28

xtensa

](../boards/waveshare/esp32s3_touch_lcd_1_28/doc/index.md)
[

01Space

![A picture of the ESP32C3 0.42 OLED board](../_images/esp32c3_042_oled.webp)

ESP32C3 0.42 OLED

riscv

](../boards/01space/esp32c3_042_oled/doc/index.md)
[

LuatOS Team

![A picture of the ESP32C3_LUATOS_CORE board](../_images/esp32c3_luatos_core.jpg)

ESP32C3\_LUATOS\_CORE

riscv

](../boards/luatos/esp32c3_luatos_core/doc/index.md)
[

LuatOS Team

![A picture of the ESP32S3-Luatos-Core board](../_images/esp32s3_luatos_core.jpg)

ESP32S3-Luatos-Core

xtensa

](../boards/luatos/esp32s3_luatos_core/doc/index.md)
[

Espressif Systems

![A picture of the ESP8684-DevKitM board](../_images/esp8684_devkitm.webp)

ESP8684-DevKitM

riscv

](../boards/espressif/esp8684_devkitm/doc/index.md)
[

Analog Devices, Inc.

![A picture of the EVAL-ADIN1110EVB Evaluation board board](../_images/adi_eval_adin1110ebz.webp)

EVAL-ADIN1110EVB Evaluation board

arm

](../boards/adi/eval_adin1110ebz/doc/index.md)
[

Analog Devices, Inc.

![A picture of the EVAL-ADIN2111EVB Evaluation board board](../_images/adi_eval_adin2111ebz.webp)

EVAL-ADIN2111EVB Evaluation board

arm

](../boards/adi/eval_adin2111ebz/doc/index.md)
[

u-blox

![A picture of the EVK NINA-B11x board](../_images/EVK-NINA-B1.jpg)

EVK NINA-B11x

arm

](../boards/u-blox/ubx_evkninab1/doc/index.md)
[

u-blox

![A picture of the EVK NINA-B40x board](../_images/EVK-NINA-B406_Top_web.jpg)

EVK NINA-B40x

arm

](../boards/u-blox/ubx_evkninab4/doc/index.md)
[

u-blox

![A picture of the EVK-ANNA-B11x board](../_images/EVK-ANNA-B112.jpg)

EVK-ANNA-B11x

arm

](../boards/u-blox/ubx_evkannab1/doc/index.md)
[

u-blox

![A picture of the EVK-BMD-30/35: BMD-300-EVAL, BMD-301-EVAL, and BMD-350-EVAL board](../_images/bmd-300-eval_pin_out.jpg)

EVK-BMD-30/35: BMD-300-EVAL, BMD-301-EVAL, and BMD-350-EVAL

arm

](../boards/u-blox/ubx_bmd300eval/doc/index.md)
[

u-blox

![A picture of the EVK-BMD-330: BMD-330-EVAL board](../_images/bmd-300-eval_pin_out.jpg)

EVK-BMD-330: BMD-330-EVAL

arm

](../boards/u-blox/ubx_bmd330eval/doc/index.md)
[

u-blox

![A picture of the EVK-BMD-34/38: BMD-340-EVAL and BMD-341-EVAL board](../_images/bmd-340-eval_pin_out.jpg)

EVK-BMD-34/38: BMD-340-EVAL and BMD-341-EVAL

arm

](../boards/u-blox/ubx_bmd340eval/doc/index.md)
[

u-blox

![A picture of the EVK-BMD-34/38: BMD-345-EVAL board](../_images/bmd-345-eval_features.jpg)

EVK-BMD-34/38: BMD-345-EVAL

arm

](../boards/u-blox/ubx_bmd345eval/doc/index.md)
[

u-blox

![A picture of the EVK-BMD-34/48: BMD-380-EVAL board](../_images/bmd-340-eval_pin_out.jpg)

EVK-BMD-34/48: BMD-380-EVAL

arm

](../boards/u-blox/ubx_bmd380eval/doc/index.md)
[

u-blox

![A picture of the EVK-BMD-360: BMD-360-EVAL board](../_images/bmd-300-eval_pin_out.jpg)

EVK-BMD-360: BMD-360-EVAL

arm

](../boards/u-blox/ubx_bmd360eval/doc/index.md)
[

u-blox

![A picture of the EVK-NINA-B3 board](../_images/EVK-NINA-B3.jpg)

EVK-NINA-B3

arm

](../boards/u-blox/ubx_evkninab3/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Feather M0 Basic Proto board](../_images/adafruit_feather_m0_basic_proto.jpg)

Feather M0 Basic Proto

arm

](../boards/adafruit/feather_m0_basic_proto/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Feather M0 LoRa board](../_images/adafruit_feather_m0_lora.jpg)

Feather M0 LoRa

arm

](../boards/adafruit/feather_m0_lora/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Feather M4 Express board](../_images/adafruit_feather_m4_express.webp)

Feather M4 Express

arm

](../boards/adafruit/feather_m4_express/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Feather nRF52840 (Express, Sense) board](../_images/adafruit_feather_nrf52840_sense.jpg)

Feather nRF52840 (Express, Sense)

arm

](../boards/adafruit/feather_nrf52840/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Feather STM32F405 Express board](../_images/adafruit_feather_stm32f405.jpg)

Feather STM32F405 Express

arm

](../boards/adafruit/feather_stm32f405/doc/index.md)
[

Seagate Technology PLC

![A picture of the FireCuda Gaming SSD (FaZe) board board](../_images/firecuda-gaming-ssd.jpg)

FireCuda Gaming SSD (FaZe) board

arm

](../boards/seagate/faze/doc/index.md)
[

FANKE Technology Co., Ltd.

![A picture of the FK750M1-VBT6 board](../_images/fk750m1_vbt6.webp)

FK750M1-VBT6

arm

](../boards/fanke/fk750m1_vbt6/doc/index.md)
[

FANKE Technology Co., Ltd.

![A picture of the FK7B0M1-VBT6 board](../_images/fk7b0m1_vbt6.webp)

FK7B0M1-VBT6

arm

](../boards/fanke/fk7b0m1_vbt6/doc/index.md)
[

NXP Semiconductors

![A picture of the FMURT6 board](../_images/mimxrt1062_fmurt6.webp)

FMURT6

arm

](../boards/nxp/mimxrt1062_fmurt6/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-K22F board](../_images/frdm_k22f.jpg)

FRDM-K22F

arm

](../boards/nxp/frdm_k22f/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-K64F board](../_images/frdm_k64f.jpg)

FRDM-K64F

arm

](../boards/nxp/frdm_k64f/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-K82F board](../_images/frdm_k82f.jpg)

FRDM-K82F

arm

](../boards/nxp/frdm_k82f/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-KE15Z board](../_images/frdm_ke15z.webp)

FRDM-KE15Z

arm

](../boards/nxp/frdm_ke15z/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-KE17Z board](../_images/frdmke17z.webp)

FRDM-KE17Z

arm

](../boards/nxp/frdm_ke17z/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-KE17Z512 board](../_images/frdm_ke17z512.webp)

FRDM-KE17Z512

arm

](../boards/nxp/frdm_ke17z512/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-KL25Z board](../_images/frdm_kl25z.jpg)

FRDM-KL25Z

arm

](../boards/nxp/frdm_kl25z/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-KW41Z board](../_images/frdm_kw41z.jpg)

FRDM-KW41Z

arm

](../boards/nxp/frdm_kw41z/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXA156 board](../_images/frdm_mcxa156.webp)

FRDM-MCXA156

arm

](../boards/nxp/frdm_mcxa156/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXC242 board](../_images/frdm_mcxc242.webp)

FRDM-MCXC242

arm

](../boards/nxp/frdm_mcxc242/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXC444 board](../_images/frdm_mcxc444.webp)

FRDM-MCXC444

arm

](../boards/nxp/frdm_mcxc444/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXN236 board](../_images/frdm_mcxn236.webp)

FRDM-MCXN236

arm

](../boards/nxp/frdm_mcxn236/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXN947 board](../_images/frdm_mcxn947.webp)

FRDM-MCXN947

arm

](../boards/nxp/frdm_mcxn947/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXW71 board](../_images/frdm_mcxw71.webp)

FRDM-MCXW71

arm

](../boards/nxp/frdm_mcxw71/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM-MCXW72 board](../_images/frdm_mcxw72.webp)

FRDM-MCXW72

arm

](../boards/nxp/frdm_mcxw72/doc/index.md)
[

NXP Semiconductors

![A picture of the FRDM_RW612 board](../_images/frdm_rw612.webp)

FRDM\_RW612

arm

](../boards/nxp/frdm_rw612/doc/index.md)
[

sensry.io

![A picture of the Ganymed Break-Out-Board (BOB) board](../_images/ganymed_bob_sy120_gen1.webp)

Ganymed Break-Out-Board (BOB)

riscv

](../boards/sensry/ganymed_bob/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32A503V-EVAL board](../_images/gd32a503v_eval.jpg)

GD32A503V-EVAL

arm

](../boards/gd/gd32a503v_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32E103V-EVAL board](../_images/gd32e103v_eval.jpg)

GD32E103V-EVAL

arm

](../boards/gd/gd32e103v_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32E507V-START board](../_images/gd32e507v_start.jpg)

GD32E507V-START

arm

](../boards/gd/gd32e507v_start/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32E507Z-EVAL board](../_images/gd32e507z_eval.webp)

GD32E507Z-EVAL

arm

](../boards/gd/gd32e507z_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F350R-EVAL board](../_images/gd32f350r_eval.webp)

GD32F350R-EVAL

arm

](../boards/gd/gd32f350r_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F403Z-EVAL board](../_images/gd32f403z_eval.jpg)

GD32F403Z-EVAL

arm

](../boards/gd/gd32f403z_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F407V-START board](../_images/gd32f407v_start.webp)

GD32F407V-START

arm

](../boards/gd/gd32f407v_start/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F450I-EVAL board](../_images/gd32f450i_eval.webp)

GD32F450I-EVAL

arm

](../boards/gd/gd32f450i_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F450V-START board](../_images/gd32f450v_start.webp)

GD32F450V-START

arm

](../boards/gd/gd32f450v_start/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F450Z-EVAL board](../_images/gd32f450z_eval.webp)

GD32F450Z-EVAL

arm

](../boards/gd/gd32f450z_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32F470I-EVAL board](../_images/gd32f470i_eval.jpg)

GD32F470I-EVAL

arm

](../boards/gd/gd32f470i_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32L233R-EVA board](../_images/gd32l233r_eval.jpg)

GD32L233R-EVA

arm

](../boards/gd/gd32l233r_eval/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32VF103C-STARTER board](../_images/gd32vf103c_starter.jpg)

GD32VF103C-STARTER

riscv

](../boards/gd/gd32vf103c_starter/doc/index.md)
[

GigaDevice Semiconductor

![A picture of the GD32VF103V-EVAL board](../_images/gd32vf103v_eval.jpg)

GD32VF103V-EVAL

riscv

](../boards/gd/gd32vf103v_eval/doc/index.md)
[

Gaisler

Generic LEON3

sparc

](../boards/gaisler/generic_leon3/doc/index.md)
[

Gaisler

![A picture of the GR716-MINI Development Board board](../_images/gr716a_mini.jpg)

GR716-MINI Development Board

sparc

](../boards/gaisler/gr716a_mini/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Grand Central M4 Express board](../_images/adafruit_grand_central_m4_express.webp)

Grand Central M4 Express

arm

](../boards/adafruit/grand_central_m4_express/doc/index.md)
[

NXP Semiconductors

![A picture of the Hexiwear board](../_images/hexiwear_k64.jpg)

Hexiwear

arm

](../boards/nxp/hexiwear/doc/index.md)
[

SiFive, Inc.

![A picture of the HiFive Unleashed board](../_images/hifive_unleashed.jpg)

HiFive Unleashed

riscv

](../boards/sifive/hifive_unleashed/doc/index.md)
[

SiFive, Inc.

![A picture of the HiFive Unmatched board](../_images/hifive_unmatched.jpg)

HiFive Unmatched

riscv

](../boards/sifive/hifive_unmatched/doc/index.md)
[

SiFive, Inc.

![A picture of the HiFive1 board](../_images/hifive1.jpg)

HiFive1

riscv

](../boards/sifive/hifive1/doc/index.md)
[

Toradex AG

![A picture of the i.MX 7 Computer on Module - Colibri iMX7 board](../_images/colibri_imx7d.jpg)

i.MX 7 Computer on Module - Colibri iMX7

arm

](../boards/toradex/colibri_imx7d/doc/index.md)
[

NXP Semiconductors

i.MX 8QuadMax Multisensory Enablement Kit (MEK)

xtensa

](#)
[

NXP Semiconductors

i.MX 8QuadXPlus Multisensory Enablement Kit (MEK)

xtensa

](#)
[

NXP Semiconductors

i.MX 8ULP Evaluation Kit

xtensa

](#)
[

NXP Semiconductors

i.MX8MM EVK

arm64, arm

](../boards/nxp/imx8mm_evk/doc/index.md)
[

NXP Semiconductors

i.MX8MN EVK (Cortex-A53)

arm64

](../boards/nxp/imx8mn_evk/doc/index.md)
[

NXP Semiconductors

i.MX8MP EVK

xtensa, arm64, arm

](../boards/nxp/imx8mp_evk/doc/index.md)
[

NXP Semiconductors

i.MX91 EVK

arm64

](../boards/nxp/imx91_evk/doc/index.md)
[

NXP Semiconductors

i.MX93 EVK

arm64, arm

](../boards/nxp/imx93_evk/doc/index.md)
[

NXP Semiconductors

i.MX95 EVK

arm64, arm

](../boards/nxp/imx95_evk/doc/index.md)
[

Actinius B.V.

![A picture of the Icarus board](../_images/Icarus_front.jpg)

Icarus

arm

](../boards/actinius/icarus/doc/index.md)
[

Actinius B.V.

![A picture of the Icarus Bee board](../_images/icarus-bee-external-pins.jpg)

Icarus Bee

arm

](../boards/actinius/icarus_bee/doc/index.md)
[

Actinius B.V.

![A picture of the Icarus SoM board](../_images/icarus-som.jpg)

Icarus SoM

arm

](../boards/actinius/icarus_som/doc/index.md)
[

Actinius B.V.

![A picture of the Icarus SoM DK board](../_images/icarus_som_dk_block_diagram.jpg)

Icarus SoM DK

arm

](../boards/actinius/icarus_som_dk/doc/index.md)
[

Other/Unknown

![A picture of the ICE-V Wireless board](../_images/icev_wireless.jpg)

ICE-V Wireless

riscv

](../boards/others/icev_wireless/doc/index.md)
[

Google, Inc.

Icetower Development Board

arm

](../boards/google/icetower/doc/index.md)
[

Intel Corporation

Integrated Sensor Hub (ISH) 5.4.1

x86

](../boards/intel/ish/doc/index.md)
[

Intel Corporation

Integrated Sensor Hub (ISH) 5.6.0

x86

](../boards/intel/ish/doc/index.md)
[

Intel Corporation

Integrated Sensor Hub (ISH) 5.8.0

x86

](../boards/intel/ish/doc/index.md)
[

Intel Corporation

Intel ADSP

](../boards/intel/adsp/doc/index.md)
[

Intel Corporation

INTEL FPGA niosv\_g

riscv

](../boards/intel/niosv_g/doc/index.md)
[

Intel Corporation

INTEL FPGA niosv\_m

riscv

](../boards/intel/niosv_m/doc/index.md)
[

SEGGER Microcontroller GmbH

![A picture of the IP Switch Board board](../_images/ip_k66f.jpg)

IP Switch Board

arm

](../boards/segger/ip_k66f/doc/index.md)
[

ITE Tech. Inc.

![A picture of the IT82XX2 series board](../_images/it82xx2_evb_wiring.jpg)

IT82XX2 series

riscv

](../boards/ite/it82xx2_evb/doc/index.md)
[

ITE Tech. Inc.

![A picture of the IT8XXX2 series board](../_images/it8xxx2_evb_and_debug_card.jpg)

IT8XXX2 series

riscv

](../boards/ite/it8xxx2_evb/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the ItsyBitsy M4 Express board](../_images/adafruit_itsybitsy_m4_express.jpg)

ItsyBitsy M4 Express

arm

](../boards/adafruit/itsybitsy_m4_express/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the ItsyBitsy nRF52840 board](../_images/adafruit_itsybitsy_nrf52840.jpeg)

ItsyBitsy nRF52840

arm

](../boards/adafruit/itsybitsy/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the KB2040 board](../_images/kb2040.jpg)

KB2040

arm

](../boards/adafruit/kb2040/doc/index.md)
[

KinCony Electronics Co., Ltd.

![A picture of the KC868-A32 board](../_images/kincony_kc868_a32.jpg)

KC868-A32

xtensa

](../boards/kincony/kincony_kc868_a32/doc/index.md)
[

Advanced Micro Devices (AMD), Inc.

![A picture of the KV260 Development Board RPU Cortex-R5 board](../_images/kv260-starter-kit.jpg)

KV260 Development Board RPU Cortex-R5

arm

](../boards/amd/kv260_r5/doc/index.md)
[

Electronut Labs

![A picture of the Labs Blip board](../_images/nrf52840_blip.jpg)

Labs Blip

arm

](../boards/electronut/nrf52840_blip/doc/index.md)
[

Electronut Labs

![A picture of the Labs Papyr board](../_images/nrf52840_papyr.jpg)

Labs Papyr

arm

](../boards/electronut/nrf52840_papyr/doc/nrf52840_papyr.md)
[

Seagate Technology PLC

![A picture of the Legend board](../_images/firecuda_gaming_hard_drive.jpg)

Legend

arm

](../boards/seagate/legend/doc/index.md)
[

Witte Technology

![A picture of the Linum Board board](../_images/linum-stm32h753bi-top.jpg)

Linum Board

arm

](../boards/witte/linum/doc/index.md)
[

EnjoyDigital

![A picture of the LiteX VexRiscv board](../_images/litex_vexriscv.jpg)

LiteX VexRiscv

riscv

](../boards/enjoydigital/litex_vexriscv/doc/index.md)
[

Ronoth

![A picture of the LoDev board](../_images/ronoth_lodev.jpg)

LoDev

arm

](../boards/ronoth/lodev/doc/index.md)
[

Shenzhen Sipeed Technology Co., Ltd.

![A picture of the Longan Nano board](../_images/longan_nano.jpg)

Longan Nano

riscv

](../boards/sipeed/longan_nano/doc/index.md)
[

OLIMEX Ltd.

![A picture of the LoRa STM32WL DevKit board](../_images/olimex-stm32wl-devkit.jpg)

LoRa STM32WL DevKit

arm

](../boards/olimex/lora_stm32wl_devkit/doc/olimex_lora_stm32wl_devkit.md)
[

Seeed Technology Co., Ltd

![A picture of the LoRa-E5 Dev Board board](../_images/lora_e5_dev_board.jpg)

LoRa-E5 Dev Board

arm

](../boards/seeed/lora_e5_dev_board/doc/lora_e5_dev_board.md)
[

Seeed Technology Co., Ltd

![A picture of the LoRa-E5 mini board](../_images/lora_e5_mini.jpg)

LoRa-E5 mini

arm

](../boards/seeed/lora_e5_mini/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXpresso11U68 board](../_images/lpcxpresso11u68.jpg)

LPCXpresso11U68

arm

](../boards/nxp/lpcxpresso11u68/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXPRESSO51U68 board](../_images/lpcxpresso51u68.jpg)

LPCXPRESSO51U68

arm

](../boards/nxp/lpcxpresso51u68/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXPRESSO54114 board](../_images/lpcxpresso54114_m4.jpg)

LPCXPRESSO54114

arm

](../boards/nxp/lpcxpresso54114/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXpresso55S06 board](../_images/lpcxpress55s06.jpg)

LPCXpresso55S06

arm

](../boards/nxp/lpcxpresso55s06/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXpresso55S16 board](../_images/lpcxpresso55S16.jpg)

LPCXpresso55S16

arm

](../boards/nxp/lpcxpresso55s16/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXpresso55S28 board](../_images/LPC55S28-EVK.jpg)

LPCXpresso55S28

arm

](../boards/nxp/lpcxpresso55s28/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXpresso55S36 board](../_images/lpcxpresso55S36.jpg)

LPCXpresso55S36

arm

](../boards/nxp/lpcxpresso55s36/doc/index.md)
[

NXP Semiconductors

![A picture of the LPCXPRESSO55S69 board](../_images/lpcxpresso55s69.jpg)

LPCXPRESSO55S69

arm

](../boards/nxp/lpcxpresso55s69/doc/index.md)
[

NXP Semiconductors

LS1046A RDB

arm64

](../boards/nxp/ls1046ardb/doc/index.md)
[

Dragino Technology Co., Limited

![A picture of the LSN50 LoRA Sensor Node board](../_images/dragino_lsn50.jpg)

LSN50 LoRA Sensor Node

arm

](../boards/dragino/lsn50/doc/index.md)
[

Microchip Technology Inc.

M2GL025 Mi-V

riscv

](../boards/microchip/m2gl025_miv/doc/index.md)
[

M5Stack

M5StickC PLUS

xtensa

](../boards/m5stack/m5stickc_plus/doc/index.md)
[

Altera Corp.

![A picture of the MAX10 board](../_images/altera_max10.jpg)

MAX10

nios2

](../boards/altr/max10/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32650EVKIT board](../_images/max32650evkit.webp)

MAX32650EVKIT

arm

](../boards/adi/max32650evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32650FTHR board](../_images/max32650fthr.webp)

MAX32650FTHR

arm

](../boards/adi/max32650fthr/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32655EVKIT board](../_images/max32655evkit_img2.jpg)

MAX32655EVKIT

arm

](../boards/adi/max32655evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32655FTHR board](../_images/max32655fthr_img2.jpg)

MAX32655FTHR

arm

](../boards/adi/max32655fthr/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32660EVSYS board](../_images/max32660evsys.webp)

MAX32660EVSYS

arm

](../boards/adi/max32660evsys/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32662EVKIT board](../_images/max32662evkit.webp)

MAX32662EVKIT

arm

](../boards/adi/max32662evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32666EVKIT board](../_images/max32666evkit.webp)

MAX32666EVKIT

arm

](../boards/adi/max32666evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32666FTHR board](../_images/max32666fthr_img2.jpg)

MAX32666FTHR

arm

](../boards/adi/max32666fthr/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32670EVKIT board](../_images/max32670evkit.webp)

MAX32670EVKIT

arm

](../boards/adi/max32670evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32672EVKIT board](../_images/max32672evkit.webp)

MAX32672EVKIT

arm

](../boards/adi/max32672evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32672FTHR board](../_images/max32672fthr_img2.webp)

MAX32672FTHR

arm

](../boards/adi/max32672fthr/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32675EVKIT board](../_images/max32675evkit.webp)

MAX32675EVKIT

arm

](../boards/adi/max32675evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32680EVKIT board](../_images/max32680evkit_img1.jpg)

MAX32680EVKIT

arm

](../boards/adi/max32680evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX32690EVKIT board](../_images/max32690evkit.jpg)

MAX32690EVKIT

arm

](../boards/adi/max32690evkit/doc/index.md)
[

Analog Devices, Inc.

MAX32690FTHR

arm

](../boards/adi/max32690fthr/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX78000EVKIT board](../_images/max78000evkit_img1.webp)

MAX78000EVKIT

arm

](../boards/adi/max78000evkit/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX78000FTHR board](../_images/max78000fthr_img1.webp)

MAX78000FTHR

arm

](../boards/adi/max78000fthr/doc/index.md)
[

Analog Devices, Inc.

![A picture of the MAX78002EVKIT board](../_images/max78002evkit.webp)

MAX78002EVKIT

arm

](../boards/adi/max78002evkit/doc/index.md)
[

NXP Semiconductors

![A picture of the MCXW72-EVK board](../_images/mcxw72_evk.webp)

MCXW72-EVK

arm

](../boards/nxp/mcxw72_evk/doc/index.md)
[

Raytac Corporation

![A picture of the MDBT50Q-DB-33 board](../_images/mdbt50q_db_33.jpg)

MDBT50Q-DB-33

arm

](../boards/raytac/mdbt50q_db_33/doc/index.md)
[

Raytac Corporation

![A picture of the MDBT50Q-DB-40 board](../_images/mdbt50q_db_40.jpg)

MDBT50Q-DB-40

arm

](../boards/raytac/mdbt50q_db_40/doc/index.md)
[

Raytac Corporation

![A picture of the MDBT53-DB-40 board](../_images/MDBT53-DB-40.jpg)

MDBT53-DB-40

arm

](../boards/raytac/mdbt53_db_40/doc/index.md)
[

Raytac Corporation

![A picture of the MDBT53V-DB-40 board](../_images/MDBT53V-DB-40.jpg)

MDBT53V-DB-40

arm

](../boards/raytac/mdbt53v_db_40/doc/index.md)
[

Microchip Technology Inc.

![A picture of the MEC1501 Modular card ASSY6885 board](../_images/mec1501modular_assy6885.jpg)

MEC1501 Modular card ASSY6885

arm

](../boards/microchip/mec1501modular_assy6885/doc/index.md)
[

Microchip Technology Inc.

![A picture of the MEC15xxEVB ASSY6853 board](../_images/mec15xxevb_assy6853.jpg)

MEC15xxEVB ASSY6853

arm

](../boards/microchip/mec15xxevb_assy6853/doc/index.md)
[

Microchip Technology Inc.

![A picture of the MEC172x Modular Card ASSY6930 (Rev. B) board](../_images/mec172xmodular_assy6930.jpg)

MEC172x Modular Card ASSY6930 (Rev. B)

arm

](../boards/microchip/mec172xmodular_assy6930/doc/mec172xmodular_assy6930.md)
[

Microchip Technology Inc.

![A picture of the MEC172xEVB ASSY6906 board](../_images/mec172xevb_assy6906.jpg)

MEC172xEVB ASSY6906

arm

](../boards/microchip/mec172xevb_assy6906/doc/index.md)
[

96Boards

![A picture of the Meerkat96 board](../_images/96b_meerkat96.jpg)

Meerkat96

arm

](../boards/96boards/meerkat96/doc/index.md)
[

Enclustra

MERCURY-XU

arm

](#)
[

BBC

![A picture of the micro:bit board](../_images/bbc_microbit.jpg)

micro:bit

arm

](../boards/bbc/microbit/doc/index.md)
[

BBC

![A picture of the micro:bit V2 board](../_images/bbc_microbit2.jpg)

micro:bit V2

arm

](../boards/bbc/microbit_v2/doc/index.md)
[

SparkFun Electronics

![A picture of the MicroMod board Processor board](../_images/sparkfun_micromod.webp)

MicroMod board Processor

arm

](../boards/sparkfun/micromod/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMX8MQ EVK board](../_images/mimx8mq_evk.jpg)

MIMX8MQ EVK

arm

](../boards/nxp/imx8mq_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1010-EVK board](../_images/mimxrt1010_evk.jpg)

MIMXRT1010-EVK

arm

](../boards/nxp/mimxrt1010_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1015-EVK board](../_images/mimxrt1015_evk.jpg)

MIMXRT1015-EVK

arm

](../boards/nxp/mimxrt1015_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1020-EVK board](../_images/mimxrt1020_evk.jpg)

MIMXRT1020-EVK

arm

](../boards/nxp/mimxrt1020_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1024-EVK board](../_images/mimxrt1024_evk.jpg)

MIMXRT1024-EVK

arm

](../boards/nxp/mimxrt1024_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1040-EVK board](../_images/mimxrt1040_evk.jpg)

MIMXRT1040-EVK

arm

](../boards/nxp/mimxrt1040_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1050-EVK board](../_images/mimxrt1050_evk.jpg)

MIMXRT1050-EVK

arm

](../boards/nxp/mimxrt1050_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1060-EVK board](../_images/mimxrt1060_evk.jpg)

MIMXRT1060-EVK

arm

](../boards/nxp/mimxrt1060_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1064-EVK board](../_images/mimxrt1064_evk.jpg)

MIMXRT1064-EVK

arm

](../boards/nxp/mimxrt1064_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1160-EVK board](../_images/mimxrt1160_evk.jpg)

MIMXRT1160-EVK

arm

](../boards/nxp/mimxrt1160_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1170-EVK/EVKB board](../_images/mimxrt1170_evk.jpg)

MIMXRT1170-EVK/EVKB

arm

](../boards/nxp/mimxrt1170_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT1180-EVK board](../_images/mimxrt1180_evk.webp)

MIMXRT1180-EVK

arm

](../boards/nxp/mimxrt1180_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT595-EVK board](../_images/mimxrt595_evk.jpg)

MIMXRT595-EVK

xtensa, arm

](../boards/nxp/mimxrt595_evk/doc/index.md)
[

NXP Semiconductors

![A picture of the MIMXRT685-EVK board](../_images/mimxrt685_evk.jpg)

MIMXRT685-EVK

arm

](../boards/nxp/mimxrt685_evk/doc/index.md)
[

NXP Semiconductors

MIMXRT700-EVK

arm

](../boards/nxp/mimxrt700_evk/doc/index.md)
[

MikroElektronika d.o.o.

![A picture of the MINI-M4 for STM32 board](../_images/mikroe_mini_m4_for_stm32.jpg)

MINI-M4 for STM32

arm

](../boards/mikroe/mini_m4_for_stm32/doc/mikroe_mini_m4_for_stm32.md)
[

WeAct Studio

![A picture of the MiniSTM32H743 Core Board board](../_images/mini_stm32h743.webp)

MiniSTM32H743 Core Board

arm

](../boards/weact/mini_stm32h743/doc/index.md)
[

WeAct Studio

![A picture of the MiniSTM32H7B0 Core Board board](../_images/mini_stm32h7b0.webp)

MiniSTM32H7B0 Core Board

arm

](../boards/weact/mini_stm32h7b0/doc/index.md)
[

Makerbase Co., Ltd.

![A picture of the MKS CANable V2.0 board](../_images/mks_canable_v20.webp)

MKS CANable V2.0

arm

](../boards/makerbase/mks_canable_v20/doc/index.md)
[

Microchip Technology Inc.

mpfs\_icicle

riscv

](../boards/microchip/mpfs_icicle/doc/index.md)
[

ARM Ltd.

![A picture of the MPS3 AN547 board](../_images/mps3.jpg)

MPS3 AN547

arm

](../boards/arm/mps3/doc/index.md)
[

NXP Semiconductors

![A picture of the MR-CANHUBK3 board](../_images/mr_canhubk3_top.jpg)

MR-CANHUBK3

arm

](../boards/nxp/mr_canhubk3/doc/index.md)
[

Texas Instruments

![A picture of the MSP-EXP432P401R LaunchXL board](../_images/msp_exp432p401r_launchxl.jpg)

MSP-EXP432P401R LaunchXL

arm

](../boards/ti/msp_exp432p401r_launchxl/doc/index.md)
[

MediaTek Inc.

mt8186

](#)
[

MediaTek Inc.

mt8188

](#)
[

MediaTek Inc.

MT8195 ADSP

](#)
[

MediaTek Inc.

mt8196

](#)
[

Antmicro

![A picture of the Myra SiP Baseboard board](../_images/myra_sip_baseboard.webp)

Myra SiP Baseboard

arm

](../boards/antmicro/myra_sip_baseboard/doc/index.md)
[

Other/Unknown

Native POSIX execution (native\_posix)

posix

](../boards/native/native_posix/doc/index.md)
[

Other/Unknown

Native simulator - native\_sim

posix

](../boards/native/native_sim/doc/index.md)
[

Dragino Technology Co., Limited

![A picture of the NBSN95 NB-IoT Sensor Node board](../_images/dragino_nbsn95.jpg)

NBSN95 NB-IoT Sensor Node

arm

](../boards/dragino/nbsn95/doc/index.md)
[

Udoo

![A picture of the Neo Full board](../_images/udoo_neo_full_mcimx6x_m4.jpg)

Neo Full

arm

](../boards/udoo/udoo_neo_full/doc/index.md)
[

96Boards

![A picture of the Neonkey board](../_images/96b_neonkey.jpg)

Neonkey

arm

](../boards/96boards/neonkey/doc/index.md)
[

Other/Unknown

NEORV32

riscv

](../boards/others/neorv32/doc/index.md)
[

96Boards

![A picture of the Nitrogen board](../_images/96b_nitrogen.jpg)

Nitrogen

arm

](../boards/96boards/nitrogen/doc/index.md)
[

Nuvoton Technology Corporation

![A picture of the NPCM400_EVB board](../_images/npcm400_evb.webp)

NPCM400\_EVB

arm

](../boards/nuvoton/npcm400_evb/doc/index.md)
[

Nuvoton Technology Corporation

![A picture of the NPCX4M8F_EVB board](../_images/npcx4m8f_evb.jpg)

NPCX4M8F\_EVB

arm

](../boards/nuvoton/npcx4m8f_evb/doc/index.md)
[

Nuvoton Technology Corporation

![A picture of the NPCX7M6FB_EVB board](../_images/npcx7m6fb_evb.jpg)

NPCX7M6FB\_EVB

arm

](../boards/nuvoton/npcx7m6fb_evb/doc/index.md)
[

Nuvoton Technology Corporation

![A picture of the NPCX9M6F_EVB board](../_images/npcx9m6f_evb.jpg)

NPCX9M6F\_EVB

arm

](../boards/nuvoton/npcx9m6f_evb/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF21540 DK board](../_images/nrf21540dk_nrf52840.jpg)

nRF21540 DK

arm

](../boards/nordic/nrf21540dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF51 DK board](../_images/nrf51dk_nrf51822.jpg)

nRF51 DK

arm

](../boards/nordic/nrf51dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF51 Dongle board](../_images/nrf51dongle_nrf51822.jpg)

nRF51 Dongle

arm

](../boards/nordic/nrf51dongle/doc/index.md)
[

VNGIoTLab

![A picture of the nRF51-VBLUno51 board](../_images/nrf51_vbluno51.jpg)

nRF51-VBLUno51

arm

](../boards/vngiotlab/nrf51_vbluno51/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the nRF52 Adafruit Feather board](../_images/nrf52_adafruit_feather.jpg)

nRF52 Adafruit Feather

arm

](../boards/adafruit/nrf52_adafruit_feather/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF52 DK board](../_images/nrf52dk_nrf52832.jpg)

nRF52 DK

arm

](../boards/nordic/nrf52dk/doc/index.md)
[

Other/Unknown

nRF52 simulated board (BabbleSim)

posix

](../boards/native/nrf_bsim/doc/nrf52_bsim.md)
[

VNGIoTLab

![A picture of the nRF52-VBLUno52 board](../_images/nrf52_vbluno52.jpg)

nRF52-VBLUno52

arm

](../boards/vngiotlab/nrf52_vbluno52/doc/index.md)
[

SparkFun Electronics

nRF52832 breakout

arm

](#)
[

Shenzhen Zaowubang Technology Co., Ltd.

nRF52832-mdk

arm

](../boards/makerdiary/nrf52832_mdk/doc/index.md)
[

Nordic Semiconductor

nRF52833 DK

arm

](../boards/nordic/nrf52833dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF52840 DK board](../_images/nrf52840dk_nrf52840.jpg)

nRF52840 DK

arm

](../boards/nordic/nrf52840dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF52840 Dongle board](../_images/nrf52840dongle_nrf52840.jpg)

nRF52840 Dongle

arm

](../boards/nordic/nrf52840dongle/doc/index.md)
[

Shenzhen Zaowubang Technology Co., Ltd.

![A picture of the nRF52840 MDK USB Dongle board](../_images/nrf52840-mdk-usb-dongle-pinout.jpg)

nRF52840 MDK USB Dongle

arm

](../boards/makerdiary/nrf52840_mdk_usb_dongle/doc/index.md)
[

Shenzhen Zaowubang Technology Co., Ltd.

nRF52840-mdk

arm

](../boards/makerdiary/nrf52840_mdk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF5340 Audio DK board](../_images/nrf5340_audio_dk.jpg)

nRF5340 Audio DK

arm

](../boards/nordic/nrf5340_audio_dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF5340 DK board](../_images/nrf5340dk.jpg)

nRF5340 DK

arm

](../boards/nordic/nrf5340dk/doc/index.md)
[

Other/Unknown

nRF5340 simulated boards (BabbleSim)

posix

](../boards/native/nrf_bsim/doc/nrf5340bsim.md)
[

Nordic Semiconductor

nRF54H20 DK

riscv, arm

](../boards/nordic/nrf54h20dk/doc/index.md)
[

Nordic Semiconductor

nRF54L09 PDK

arm

](../boards/nordic/nrf54l09pdk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF54L15 DK board](../_images/nrf54l15dk_nrf54l15.webp)

nRF54L15 DK

riscv, arm

](../boards/nordic/nrf54l15dk/doc/index.md)
[

Other/Unknown

nRF54L15 simulated boards (BabbleSim)

posix

](../boards/native/nrf_bsim/doc/nrf54l15bsim.md)
[

Nordic Semiconductor

nRF54L20 PDK

arm

](../boards/nordic/nrf54l20pdk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF7002 DK board](../_images/nrf7002dk.jpg)

nRF7002 DK

arm

](../boards/nordic/nrf7002dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF9131 EK board](../_images/nrf9131ek_nrf9131.webp)

nRF9131 EK

arm

](../boards/nordic/nrf9131ek/doc/index.md)
[

Nordic Semiconductor

nRF9151 DK

arm

](../boards/nordic/nrf9151dk/doc/index.md)
[

Nordic Semiconductor

![A picture of the nRF9160 DK board](../_images/nrf9160dk_nrf9160.jpg)

nRF9160 DK

arm

](../boards/nordic/nrf9160dk/doc/index.md)
[

Circuit Dojo

![A picture of the nRF9160 Feather board](../_images/circuitdojo_feather_nrf9160.jpg)

nRF9160 Feather

arm

](../boards/circuitdojo/feather/doc/index.md)
[

innblue UG

![A picture of the nRF9160 INNBLUE21 board](../_images/nrf9160_innblue21.jpg)

nRF9160 INNBLUE21

arm

](../boards/innblue/innblue21/doc/index.md)
[

innblue UG

![A picture of the nRF9160 INNBLUE22 board](../_images/nrf9160_innblue22.jpg)

nRF9160 INNBLUE22

arm

](../boards/innblue/innblue22/doc/index.md)
[

SparkFun Electronics

![A picture of the nRF9160 Thing Plus board](../_images/sparkfun_thing_plus_nrf9160.jpg)

nRF9160 Thing Plus

arm

](../boards/sparkfun/thing_plus/doc/index.md)
[

Nordic Semiconductor

nRF9161 DK

arm

](../boards/nordic/nrf9161dk/doc/index.md)
[

Nordic Semiconductor

nRF9280 PDK

riscv, arm

](#)
[

STMicroelectronics

![A picture of the Nucleo C031C6 board](../_images/nucleo_c031c6.jpg)

Nucleo C031C6

arm

](../boards/st/nucleo_c031c6/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo C071RB board](../_images/nucleo_c071rb.webp)

Nucleo C071RB

arm

](../boards/st/nucleo_c071rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F030R8 board](../_images/nucleo_f030r8.jpg)

Nucleo F030R8

arm

](../boards/st/nucleo_f030r8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F031K6 board](../_images/nucleo_f031k6.jpg)

Nucleo F031K6

arm

](../boards/st/nucleo_f031k6/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F042K6 board](../_images/nucleo_f042k6.jpg)

Nucleo F042K6

arm

](../boards/st/nucleo_f042k6/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F070RB board](../_images/nucleo_f070rb.jpg)

Nucleo F070RB

arm

](../boards/st/nucleo_f070rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F072RB board](../_images/nucleo_f072rb.webp)

Nucleo F072RB

arm

](../boards/st/nucleo_f072rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F091RC board](../_images/nucleo_f091rc.jpg)

Nucleo F091RC

arm

](../boards/st/nucleo_f091rc/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F103RB board](../_images/nucleo_f103rb.jpg)

Nucleo F103RB

arm

](../boards/st/nucleo_f103rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F207ZG board](../_images/nucleo_f207zg.jpg)

Nucleo F207ZG

arm

](../boards/st/nucleo_f207zg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F302R8 board](../_images/nucleo_f302r8.jpg)

Nucleo F302R8

arm

](../boards/st/nucleo_f302r8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F303K8 board](../_images/nucleo_f303k8.jpg)

Nucleo F303K8

arm

](../boards/st/nucleo_f303k8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F303RE board](../_images/nucleo_f303re.jpg)

Nucleo F303RE

arm

](../boards/st/nucleo_f303re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F334R8 board](../_images/nucleo_f334r8.jpg)

Nucleo F334R8

arm

](../boards/st/nucleo_f334r8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F401RE board](../_images/nucleo_f401re.jpg)

Nucleo F401RE

arm

](../boards/st/nucleo_f401re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F410RB board](../_images/nucleo_f410rb.jpg)

Nucleo F410RB

arm

](../boards/st/nucleo_f410rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F411RE board](../_images/nucleo_f411re.jpg)

Nucleo F411RE

arm

](../boards/st/nucleo_f411re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F412ZG board](../_images/nucleo_f412zg.jpg)

Nucleo F412ZG

arm

](../boards/st/nucleo_f412zg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F413ZH board](../_images/nucleo_f413zh.jpg)

Nucleo F413ZH

arm

](../boards/st/nucleo_f413zh/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F429ZI board](../_images/nucleo_f429zi.jpg)

Nucleo F429ZI

arm

](../boards/st/nucleo_f429zi/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F446RE board](../_images/nucleo_f446re.jpg)

Nucleo F446RE

arm

](../boards/st/nucleo_f446re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F446ZE board](../_images/nucleo_f446ze.jpg)

Nucleo F446ZE

arm

](../boards/st/nucleo_f446ze/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F722ZE board](../_images/nucleo_f722ze.jpg)

Nucleo F722ZE

arm

](../boards/st/nucleo_f722ze/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F746ZG board](../_images/nucleo_f746zg.jpg)

Nucleo F746ZG

arm

](../boards/st/nucleo_f746zg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F756ZG board](../_images/nucleo_f756zg.jpg)

Nucleo F756ZG

arm

](../boards/st/nucleo_f756zg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo F767ZI board](../_images/nucleo_f767zi.jpg)

Nucleo F767ZI

arm

](../boards/st/nucleo_f767zi/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G031K8 board](../_images/nucleo_g031k8.jpg)

Nucleo G031K8

arm

](../boards/st/nucleo_g031k8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G070RB board](../_images/nucleo_g070rb.jpg)

Nucleo G070RB

arm

](../boards/st/nucleo_g070rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G071RB board](../_images/nucleo_g071rb.jpg)

Nucleo G071RB

arm

](../boards/st/nucleo_g071rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G0B1RE board](../_images/nucleo_g0b1re.jpg)

Nucleo G0B1RE

arm

](../boards/st/nucleo_g0b1re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G431KB board](../_images/nucleo_g431kb.webp)

Nucleo G431KB

arm

](../boards/st/nucleo_g431kb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G431RB board](../_images/nucleo_g431rb.jpg)

Nucleo G431RB

arm

](../boards/st/nucleo_g431rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo G474RE board](../_images/nucleo_g474re.jpg)

Nucleo G474RE

arm

](../boards/st/nucleo_g474re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H503RB board](../_images/nucleo_h503rb.png)

Nucleo H503RB

arm

](../boards/st/nucleo_h503rb/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H533RE board](../_images/nucleo_h533re.jpg)

Nucleo H533RE

arm

](../boards/st/nucleo_h533re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H563ZI board](../_images/nucleo_h563zi.jpg)

Nucleo H563ZI

arm

](../boards/st/nucleo_h563zi/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H723ZG board](../_images/nucleo_h723zg.jpg)

Nucleo H723ZG

arm

](../boards/st/nucleo_h723zg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H743ZI board](../_images/nucleo_h743zi.jpg)

Nucleo H743ZI

arm

](../boards/st/nucleo_h743zi/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H745ZI-Q board](../_images/nucleo_h745zi_q.jpg)

Nucleo H745ZI-Q

arm

](../boards/st/nucleo_h745zi_q/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H753ZI board](../_images/nucleo_h753zi.jpg)

Nucleo H753ZI

arm

](../boards/st/nucleo_h753zi/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H755ZI-Q board](../_images/nucleo_h755zi_q.webp)

Nucleo H755ZI-Q

arm

](../boards/st/nucleo_h755zi_q/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H7A3ZI-Q board](../_images/nucleo_h7a3zi_q.jpg)

Nucleo H7A3ZI-Q

arm

](../boards/st/nucleo_h7a3zi_q/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo H7S3L8 board](../_images/nucleo_h7s3l8.webp)

Nucleo H7S3L8

arm

](../boards/st/nucleo_h7s3l8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L011K4 board](../_images/nucleo_l011k4.jpg)

Nucleo L011K4

arm

](../boards/st/nucleo_l011k4/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L031K6 board](../_images/nucleo_l031k6.jpg)

Nucleo L031K6

arm

](../boards/st/nucleo_l031k6/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L053R8 board](../_images/nucleo_l053r8.jpg)

Nucleo L053R8

arm

](../boards/st/nucleo_l053r8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L073RZ board](../_images/nucleo_l073rz.jpg)

Nucleo L073RZ

arm

](../boards/st/nucleo_l073rz/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L152RE board](../_images/nucleo_l152re.jpg)

Nucleo L152RE

arm

](../boards/st/nucleo_l152re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L412RB-P board](../_images/nucleo_l412rb_p.jpg)

Nucleo L412RB-P

arm

](../boards/st/nucleo_l412rb_p/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L432KC board](../_images/nucleo_l432kc.jpg)

Nucleo L432KC

arm

](../boards/st/nucleo_l432kc/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L433RC board](../_images/nucleo_l433rc_p.jpg)

Nucleo L433RC

arm

](../boards/st/nucleo_l433rc_p/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L452RE board](../_images/nucleo_l452re_p_pinout.jpg)

Nucleo L452RE

arm

](../boards/st/nucleo_l452re/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L476RG board](../_images/nucleo_l476rg.jpg)

Nucleo L476RG

arm

](../boards/st/nucleo_l476rg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L496ZG board](../_images/nucleo_l496zg.jpg)

Nucleo L496ZG

arm

](../boards/st/nucleo_l496zg/doc/index.md)
[

STMicroelectronics

Nucleo L4A6ZG

arm

](../boards/st/nucleo_l4a6zg/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L4R5ZI board](../_images/nucleo_l4r5zi.jpg)

Nucleo L4R5ZI

arm

](../boards/st/nucleo_l4r5zi/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo L552ZE Q board](../_images/nucleo_l552ze_q.jpg)

Nucleo L552ZE Q

arm

](../boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.md)
[

STMicroelectronics

![A picture of the Nucleo N657X0-Q board](../_images/nucleo_n657x0_q.webp)

Nucleo N657X0-Q

](../boards/st/nucleo_n657x0_q/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo U031R8 board](../_images/nucleo_u031r8.jpg)

Nucleo U031R8

arm

](../boards/st/nucleo_u031r8/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo U083RC board](../_images/nucleo_u083rc.jpg)

Nucleo U083RC

arm

](../boards/st/nucleo_u083rc/doc/index.md)
[

STMicroelectronics

Nucleo U575ZI Q

arm

](../boards/st/nucleo_u575zi_q/doc/index.md)
[

STMicroelectronics

Nucleo U5A5ZJ Q

arm

](../boards/st/nucleo_u5a5zj_q/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo WB05KZ board](../_images/nucleo_wb05kz.webp)

Nucleo WB05KZ

arm

](../boards/st/nucleo_wb05kz/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo WB07CC board](../_images/nucleo_wb07cc.webp)

Nucleo WB07CC

arm

](../boards/st/nucleo_wb07cc/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo WB09KE board](../_images/nucleo_wb09ke.webp)

Nucleo WB09KE

arm

](../boards/st/nucleo_wb09ke/doc/index.md)
[

STMicroelectronics

![A picture of the Nucleo WB55RG board](../_images/nucleowb55rg.jpg)

Nucleo WB55RG

arm

](../boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.md)
[

STMicroelectronics

![A picture of the Nucleo WBA52CG board](../_images/nucleowba52cg.jpg)

Nucleo WBA52CG

arm

](../boards/st/nucleo_wba52cg/doc/nucleo_wba52cg.md)
[

STMicroelectronics

![A picture of the Nucleo WBA55CG board](../_images/nucleowba55cg.jpg)

Nucleo WBA55CG

arm

](../boards/st/nucleo_wba55cg/doc/nucleo_wba55cg.md)
[

STMicroelectronics

![A picture of the Nucleo WL55JC board](../_images/nucleo_wl55jc.jpg)

Nucleo WL55JC

arm

](../boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.md)
[

Nuvoton Technology Corporation

![A picture of the NUMAKER M2L31KI board](../_images/m2l31ki.webp)

NUMAKER M2L31KI

arm

](../boards/nuvoton/numaker_m2l31ki/doc/index.md)
[

Nuvoton Technology Corporation

![A picture of the NUMAKER PFM M467 board](../_images/pfm_m467.jpeg)

NUMAKER PFM M467

arm

](../boards/nuvoton/numaker_pfm_m467/doc/index.md)
[

Nuvoton Technology Corporation

![A picture of the NUMAKER PFM M487 board](../_images/pfm_m487.jpg)

NUMAKER PFM M487

arm

](../boards/nuvoton/numaker_pfm_m487/doc/index.md)
[

Space Cubics, LLC

![A picture of the OBC module 1 board](../_images/scobc.jpg)

OBC module 1

arm

](../boards/sc/scobc_module1/doc/index.md)
[

Würth Elektronik GmbH.

![A picture of the Oceanus-I EV board](../_images/we_oceanus1ev.webp)

Oceanus-I EV

arm

](../boards/we/oceanus1ev/doc/index.md)
[

Norik Systems

![A picture of the Octopus IO-Board board](../_images/octopus_io_board.webp)

Octopus IO-Board

arm

](../boards/norik/octopus_io_board/doc/index.md)
[

Norik Systems

![A picture of the Octopus SoM board](../_images/octopus_som.webp)

Octopus SoM

arm

](../boards/norik/octopus_som/doc/index.md)
[

Hardkernel Co., Ltd

![A picture of the ODROID-GO board](../_images/odroid_go.jpg)

ODROID-GO

xtensa

](../boards/hardkernel/odroid_go/doc/index.md)
[

OLIMEX Ltd.

![A picture of the OLIMEX-STM32-E407 board](../_images/olimex_stm32_e407.jpg)

OLIMEX-STM32-E407

arm

](../boards/olimex/stm32_e407/doc/index.md)
[

OLIMEX Ltd.

![A picture of the OLIMEX-STM32-H103 board](../_images/olimex_stm32_h103_top.jpg)

OLIMEX-STM32-H103

arm

](../boards/olimex/stm32_h103/doc/index.md)
[

OLIMEX Ltd.

![A picture of the OLIMEX-STM32-H405 board](../_images/olimex_stm32_h405_top.jpg)

OLIMEX-STM32-H405

arm

](../boards/olimex/stm32_h405/doc/index.md)
[

OLIMEX Ltd.

![A picture of the OLIMEX-STM32-H407 board](../_images/olimex_stm32_h407.jpg)

OLIMEX-STM32-H407

arm

](../boards/olimex/stm32_h407/doc/index.md)
[

OLIMEX Ltd.

![A picture of the OLIMEX-STM32-P405 board](../_images/olimex_stm32_p405.jpg)

OLIMEX-STM32-P405

arm

](../boards/olimex/stm32_p405/doc/index.md)
[

OLIMEX Ltd.

![A picture of the OLIMEXINO-STM32 board](../_images/olimexino_stm32.jpg)

OLIMEXINO-STM32

arm

](../boards/olimex/olimexino_stm32/doc/index.md)
[

Waveshare Electronics

![A picture of the Open103Z board](../_images/waveshare_open103z.jpg)

Open103Z

arm

](../boards/waveshare/open103z/doc/index.md)
[

open-isa.org

![A picture of the OpenISA VEGAboard board](../_images/rv32m1_vega.jpg)

OpenISA VEGAboard

riscv

](../boards/openisa/rv32m1_vega/doc/index.md)
[

lowRISC Community Interest Company

OpenTitan Earl Grey

riscv

](../boards/lowrisc/opentitan_earlgrey/doc/index.md)
[

Würth Elektronik GmbH.

![A picture of the Ophelia-I EV NRF52805 board](../_images/we_ophelia1ev_nrf52805.jpg)

Ophelia-I EV NRF52805

arm

](../boards/we/ophelia1ev/doc/index.md)
[

Würth Elektronik GmbH.

![A picture of the Orthosie-I-EV board](../_images/we_orthosie1ev.webp)

Orthosie-I-EV

riscv

](../boards/we/orthosie1ev/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN B511 Evaluation Board board](../_images/panb511evb.webp)

PAN B511 Evaluation Board

riscv, arm

](../boards/panasonic/panb511evb/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1770 Evaluation Board board](../_images/pan1770_evaluation_board.jpg)

PAN1770 Evaluation Board

arm

](../boards/panasonic/pan1770_evb/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1780 Evaluation Board board](../_images/pan1780_evaluation_board.jpg)

PAN1780 Evaluation Board

arm

](../boards/panasonic/pan1780_evb/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1781 Evaluation Board board](../_images/pan1781_evaluation_board.jpg)

PAN1781 Evaluation Board

arm

](../boards/panasonic/pan1781_evb/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1782 Evaluation Board board](../_images/pan1782_evaluation_board.jpg)

PAN1782 Evaluation Board

arm

](../boards/panasonic/pan1782_evb/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1783 Evaluation Board board](../_images/pan1783_evb.webp)

PAN1783 Evaluation Board

arm

](../boards/panasonic/pan1783/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1783A Evaluation Board board](../_images/pan1783_evb.webp)

PAN1783A Evaluation Board

arm

](../boards/panasonic/pan1783/doc/index.md)
[

Panasonic Corporation

![A picture of the PAN1783A-PA Evaluation Board board](../_images/pan1783_evb.webp)

PAN1783A-PA Evaluation Board

arm

](../boards/panasonic/pan1783/doc/index.md)
[

PHYTEC

![A picture of the phyBOARD-Electra AM64x M4F Core board](../_images/phyCORE-AM64x_Electra_frontside.webp)

phyBOARD-Electra AM64x M4F Core

arm

](../boards/phytec/phyboard_electra/doc/index.md)
[

PHYTEC

![A picture of the phyBOARD-Lyra AM62x A53 Core board](../_images/phyCORE-AM62x_Lyra_frontside.webp)

phyBOARD-Lyra AM62x A53 Core

arm64, arm

](../boards/phytec/phyboard_lyra/doc/phyboard_lyra_am62xx_m4.md)
[

PHYTEC

![A picture of the phyBOARD-Nash i.MX93 board](../_images/phyboard_nash.webp)

phyBOARD-Nash i.MX93

arm64, arm

](../boards/phytec/phyboard_nash/doc/index.md)
[

PHYTEC

![A picture of the phyBOARD-Polis i.MX8M Mini board](../_images/phyBOARD-Polis.jpg)

phyBOARD-Polis i.MX8M Mini

arm

](../boards/phytec/phyboard_polis/doc/index.md)
[

PHYTEC

![A picture of the phyBOARD-Pollux i.MX8M Plus board](../_images/Phyboard_Pollux.jpg)

phyBOARD-Pollux i.MX8M Plus

arm

](../boards/phytec/phyboard_pollux/doc/index.md)
[

TechNexion

![A picture of the Pico-Pi i.MX7D - Android Things IoT Development Platform board](../_images/pico_pi.jpg)

Pico-Pi i.MX7D - Android Things IoT Development Platform

arm

](../boards/technexion/pico_pi/doc/index.md)
[

Pine64

![A picture of the PineTime DevKit0 board](../_images/pinetime_devkit0.jpg)

PineTime DevKit0

arm

](../boards/pine64/pinetime_devkit0/doc/index.md)
[

Ezurio

![A picture of the Pinnacle 100 DVK board](../_images/pinnacle_100_dvk.jpg)

Pinnacle 100 DVK

arm

](../boards/ezurio/pinnacle_100_dvk/doc/index.md)
[

Other/Unknown

![A picture of the Pro Micro nRF52840 board](../_images/others_promicro_nrf52840.webp)

Pro Micro nRF52840

arm

](../boards/others/promicro_nrf52840/doc/index.md)
[

SparkFun Electronics

![A picture of the Pro Micro RP2040 board](../_images/sparkfun_pro_micro_rp2040.jpg)

Pro Micro RP2040

arm

](../boards/sparkfun/pro_micro_rp2040/doc/index.md)
[

Würth Elektronik GmbH.

![A picture of the Proteus-II-EV board](../_images/we_proteus2ev_nrf52832.jpg)

Proteus-II-EV

arm

](../boards/we/proteus2ev/doc/index.md)
[

Würth Elektronik GmbH.

![A picture of the Proteus-III-EV board](../_images/we_proteus3ev_nrf52840.jpg)

Proteus-III-EV

arm

](../boards/we/proteus3ev/doc/index.md)
[

Infineon Technologies

![A picture of the PSOC 6 AI Evaluation Kit board](../_images/cy8ckit_062s2_ai.webp)

PSOC 6 AI Evaluation Kit

arm

](../boards/infineon/cy8ckit_062s2_ai/doc/index.md)
[

Cypress Semiconductor Corporation

![A picture of the PSOC 6 WiFi-BT Pioneer Kit board](../_images/cy8ckit_062_wifi_bt_m0.jpg)

PSOC 6 WiFi-BT Pioneer Kit

arm

](../boards/cypress/cy8ckit_062_wifi_bt/doc/index.md)
[

Infineon Technologies

![A picture of the PSOC 62S4 Pioneer Kit board](../_images/cy8ckit_062s4.png)

PSOC 62S4 Pioneer Kit

arm

](../boards/infineon/cy8ckit_062s4/doc/index.md)
[

Cypress Semiconductor Corporation

![A picture of the PSOC 63 BLE Pioneer Kit board](../_images/cy8ckit-062-ble.jpg)

PSOC 63 BLE Pioneer Kit

arm

](../boards/cypress/cy8ckit_062_ble/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for Altera Nios-II

nios2

](../boards/qemu/nios2/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for ARCv2 & ARCv3

arc

](../boards/qemu/arc/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for ARM AArch64 Virt KVM

arm64

](../boards/qemu/kvm_arm64/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for ARM Cortex-A53

arm64

](../boards/qemu/cortex_a53/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for ARM Cortex-M0

arm

](../boards/qemu/cortex_m0/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for ARM Cortex-M3

arm

](../boards/qemu/cortex_m3/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for ARM Cortex-R5

arm

](../boards/qemu/cortex_r5/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for Cortex-A9

arm

](#)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for LEON3

sparc

](../boards/qemu/leon3/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for MIPS Malta

mips

](../boards/qemu/malta/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for RISCV32

riscv

](../boards/qemu/riscv32/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for RISCV32 XIP

riscv

](../boards/qemu/riscv32_xip/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for RISCV32E

riscv

](../boards/qemu/riscv32e/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for RISCV64

riscv

](../boards/qemu/riscv64/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for X86

x86

](../boards/qemu/x86/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for X86 / Lakemont CPU

x86

](../boards/qemu/x86/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for X86 64bit

x86

](../boards/qemu/x86/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for X86 Minimal Configuration

x86

](../boards/qemu/x86/doc/index.md)
[

QEMU, a generic and open source machine emulator and virtualizer

QEMU Emulation for Xtensa

xtensa

](../boards/qemu/xtensa/doc/index.md)
[

QuickLogic Corp.

![A picture of the Qomu board](../_images/qomu-board.png)

Qomu

arm

](../boards/quicklogic/qomu/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the QT Py ESP32-S3 board](../_images/adafruit_qt_py_esp32s3.webp)

QT Py ESP32-S3

xtensa

](../boards/adafruit/qt_py_esp32s3/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the QT Py RP2040 board](../_images/qtpy_rp2040.jpg)

QT Py RP2040

arm

](../boards/adafruit/qt_py_rp2040/doc/index.md)
[

QuickLogic Corp.

![A picture of the QuickFeather board](../_images/feather-board.jpg)

QuickFeather

arm

](../boards/quicklogic/quick_feather/doc/index.md)
[

Google, Inc.

Quincy

arm

](../boards/google/quincy/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the R-CAR H3 ARM CA57 (ARMv8) board](../_images/rcar_h3ulcb_bottom.jpg)

R-CAR H3 ARM CA57 (ARMv8)

arm64, arm

](../boards/renesas/rcar_h3ulcb/doc/rcar_h3ulcb_r7.md)
[

Renesas Electronics Corporation

![A picture of the R-Car H3 Salvator-X board](../_images/r-car-h3-salvator-x-connections.jpg)

R-Car H3 Salvator-X

arm

](../boards/renesas/rcar_salvator_x/doc/rcar_salvator_x.md)
[

Renesas Electronics Corporation

R-CAR Salvator XS M3 ARM CA57 (ARMv8)

arm64

](../boards/renesas/rcar_salvator_xs/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the R-CAR Spider S4 (ARM64) board](../_images/rcar_s4_spider_full.jpg)

R-CAR Spider S4 (ARM64)

arm64, arm

](../boards/renesas/rcar_spider_s4/doc/rcar_spider_r52.md)
[

Renesas Electronics Corporation

![A picture of the RA2A1 Evaluation Kit board](../_images/ek_ra2a1.webp)

RA2A1 Evaluation Kit

arm

](../boards/renesas/ek_ra2a1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4E1 Fast Prototyping Board board](../_images/fpb_ra4e1.webp)

RA4E1 Fast Prototyping Board

arm

](../boards/renesas/fpb_ra4e1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4E1 Voice User Reference Kit board](../_images/voice_ra4e1.webp)

RA4E1 Voice User Reference Kit

arm

](../boards/renesas/voice_ra4e1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4E2 Evaluation Kit board](../_images/ek_ra4e2.webp)

RA4E2 Evaluation Kit

arm

](../boards/renesas/ek_ra4e2/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4L1 Evaluation Kit board](../_images/ek_ra4l1.webp)

RA4L1 Evaluation Kit

arm

](../boards/renesas/ek_ra4l1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4M1 Evaluation Kit board](../_images/ek_ra4m1.webp)

RA4M1 Evaluation Kit

arm

](../boards/renesas/ek_ra4m1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4M2 Evaluation Kit board](../_images/ek_ra4m2.webp)

RA4M2 Evaluation Kit

arm

](../boards/renesas/ek_ra4m2/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4M3 Evaluation Kit board](../_images/ek_ra4m3.webp)

RA4M3 Evaluation Kit

arm

](../boards/renesas/ek_ra4m3/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA4W1 Evaluation Kit board](../_images/ek_ra4w1.webp)

RA4W1 Evaluation Kit

arm

](../boards/renesas/ek_ra4w1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6E1 Fast Prototyping Board board](../_images/fpb_ra6e1.webp)

RA6E1 Fast Prototyping Board

arm

](../boards/renesas/fpb_ra6e1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6E2 Evaluation Kit board](../_images/ek_ra6e2.webp)

RA6E2 Evaluation Kit

arm

](../boards/renesas/ek_ra6e2/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6E2 Fast Prototyping Board board](../_images/fpb_ra6e2.webp)

RA6E2 Fast Prototyping Board

arm

](../boards/renesas/fpb_ra6e2/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6M1 Evaluation Kit board](../_images/ek_ra6m1.webp)

RA6M1 Evaluation Kit

arm

](../boards/renesas/ek_ra6m1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6M2 Evaluation Kit board](../_images/ek_ra6m2.webp)

RA6M2 Evaluation Kit

arm

](../boards/renesas/ek_ra6m2/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6M3 Evaluation Kit board](../_images/ek_ra6m3.webp)

RA6M3 Evaluation Kit

arm

](../boards/renesas/ek_ra6m3/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6M4 Evaluation Kit board](../_images/ek_ra6m4.webp)

RA6M4 Evaluation Kit

arm

](../boards/renesas/ek_ra6m4/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA6M5 Evaluation Kit board](../_images/ek_ra6m5.webp)

RA6M5 Evaluation Kit

arm

](../boards/renesas/ek_ra6m5/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA8D1 Evaluation Kit board](../_images/ek_ra8d1.jpg)

RA8D1 Evaluation Kit

arm

](../boards/renesas/ek_ra8d1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA8M1 Evaluation Kit board](../_images/ek_ra8m1.jpg)

RA8M1 Evaluation Kit

arm

](../boards/renesas/ek_ra8m1/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RA8T1 Motor Control Kit board](../_images/mck_ra8t1.jpg)

RA8T1 Motor Control Kit

arm

](../boards/renesas/mck_ra8t1/doc/index.md)
[

RAKwireless Technology Limited

![A picture of the RAK11720 board](../_images/rak11720.webp)

RAK11720

arm

](../boards/rakwireless/rak11720/doc/index.md)
[

RAKwireless Technology Limited

![A picture of the RAK3172 board](../_images/rak3172.webp)

RAK3172

arm

](../boards/rakwireless/rak3172/doc/index.md)
[

RAKwireless Technology Limited

![A picture of the RAK4631 board](../_images/rak4631-front-parts.jpg)

RAK4631

arm

](../boards/rakwireless/rak4631/doc/index.md)
[

RAKwireless Technology Limited

![A picture of the RAK5010 board](../_images/rak5010-front-parts.jpg)

RAK5010

arm

](../boards/rakwireless/rak5010/doc/index.md)
[

Intel Corporation

Raptor Lake P CRB

x86

](../boards/intel/rpl/doc/index.md)
[

Intel Corporation

Raptor Lake S CRB

x86

](../boards/intel/rpl/doc/index.md)
[

Raspberry Pi Foundation

Raspberry Pi 4 Model B (Cortex-A72)

arm64

](../boards/raspberrypi/rpi_4b/doc/index.md)
[

Raspberry Pi Foundation

Raspberry Pi 5 (Cortex-A76)

arm64

](../boards/raspberrypi/rpi_5/doc/index.md)
[

Raspberry Pi Foundation

![A picture of the Raspberry Pi Pico board](../_images/rpi_pico.jpg)

Raspberry Pi Pico

arm

](../boards/raspberrypi/rpi_pico/doc/index.md)
[

Raspberry Pi Foundation

![A picture of the Raspberry Pi Pico 2 board](../_images/rpi_pico2.webp)

Raspberry Pi Pico 2

arm

](../boards/raspberrypi/rpi_pico2/doc/index.md)
[

NXP Semiconductors

RD-RW612-BGA

arm

](../boards/nxp/rd_rw612_bga/doc/index.md)
[

NXP Semiconductors

![A picture of the RDDRONE-FMUK66 board](../_images/rddrone_fmuk66.jpg)

RDDRONE-FMUK66

arm

](../boards/nxp/rddrone_fmuk66/doc/index.md)
[

SparkFun Electronics

![A picture of the RED-V Things Plus board](../_images/sparkfun_red_v_things_plus.jpg)

RED-V Things Plus

riscv

](../boards/sparkfun/red_v_things_plus/doc/index.md)
[

Particle.io

![A picture of the Redbear Labs Nano board](../_images/nrf51_blenano.jpg)

Redbear Labs Nano

arm

](../boards/particle/nrf51_blenano/doc/index.md)
[

Particle.io

![A picture of the Redbear Labs Nano v2 board](../_images/nrf52_blenano2.jpg)

Redbear Labs Nano v2

arm

](../boards/particle/nrf52_blenano2/doc/index.md)
[

PHYTEC

![A picture of the reel board board](../_images/reel_board.jpg)

reel board

arm

](../boards/phytec/reel_board/doc/index.md)
[

Synopsys, Inc.

RISC-V nSIM and HAPS FPGA boards

riscv

](../boards/snps/nsim/arc_v/doc/index.md)
[

Antmicro's open source simulation and virtual development framework

RISCV32 Virtual

riscv

](../boards/renode/riscv32_virtual/doc/index.md)
[

Ezurio

![A picture of the RM1xx DVK board](../_images/rm1xx_dvk.jpg)

RM1xx DVK

arm

](../boards/ezurio/rm1xx_dvk/doc/index.md)
[

TDK Corporation.

![A picture of the RoboKit 1 board](../_images/tdk_robokit1.jpg)

RoboKit 1

arm

](../boards/tdk/robokit1/doc/index.md)
[

Firefly

ROC-RK3568-PC (Quad-core Cortex-A55)

arm64

](../boards/firefly/roc_rk3568_pc/doc/index.md)
[

Waveshare Electronics

![A picture of the RP2040-Zero board](../_images/rp2040_zero.png)

RP2040-Zero

arm

](../boards/waveshare/rp2040_zero/doc/index.md)
[

Realtek Semiconductor Corp.

![A picture of the RTS5912 Evaluation Board board](../_images/rts5912evb.webp)

RTS5912 Evaluation Board

arm

](../boards/realtek/rts5912_evb/doc/index.md)
[

Ruuvi Innovations Ltd (Oy)

![A picture of the RuuviTag board](../_images/ruuvitag.jpg)

RuuviTag

arm

](../boards/ruuvi/ruuvitag/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the RZ/G3S SMARC Evaluation Board Kit board](../_images/rzg3s_smarc.webp)

RZ/G3S SMARC Evaluation Board Kit

arm

](../boards/renesas/rzg3s_smarc/doc/index.md)
[

Atmel Corporation

![A picture of the SAM C21N Xplained Pro Evaluation Kit board](../_images/atsamc21n_xpro.jpg)

SAM C21N Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/samc21n_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM D20 Xplained Pro Evaluation Kit board](../_images/atsamd20_xpro.jpg)

SAM D20 Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/samd20_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM D21 Xplained Pro Evaluation Kit board](../_images/atsamd21_xpro.jpg)

SAM D21 Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/samd21_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM E54 Xplained Pro Evaluation Kit board](../_images/atsame54_xpro.jpg)

SAM E54 Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/same54_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM E70(B) Xplained board](../_images/sam_e70_xplained.jpg)

SAM E70(B) Xplained

arm

](../boards/atmel/sam/sam_e70_xplained/doc/index.md)
[

Atmel Corporation

![A picture of the SAM L21 Xplained Pro Evaluation Kit board](../_images/atsaml21-xpro-pinout.jpg)

SAM L21 Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/saml21_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM R21 Xplained Pro Evaluation Kit board](../_images/atsamr21_xpro.jpg)

SAM R21 Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/samr21_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM R34 Xplained Pro Evaluation Kit board](../_images/atsamr34-xpro-pinout.jpg)

SAM R34 Xplained Pro Evaluation Kit

arm

](../boards/atmel/sam0/samr34_xpro/doc/index.md)
[

Atmel Corporation

![A picture of the SAM V71(B) Xplained Ultra board](../_images/sam_v71_xult.jpg)

SAM V71(B) Xplained Ultra

arm

](../boards/atmel/sam/sam_v71_xult/doc/index.md)
[

Atmel Corporation

![A picture of the SAM4E Xplained Pro board](../_images/sam4e_xpro.jpg)

SAM4E Xplained Pro

arm

](../boards/atmel/sam/sam4e_xpro/doc/index.md)
[

Peregrine Consultoria e Servicos

![A picture of the SAM4L WM-400 Cape Board board](../_images/wm-400-pin-out.webp)

SAM4L WM-400 Cape Board

arm

](../boards/peregrine/sam4l_wm400_cape/doc/index.md)
[

Atmel Corporation

![A picture of the SAM4L-EK board](../_images/atmel-sam4l-ek-callouts.jpg)

SAM4L-EK

arm

](../boards/atmel/sam/sam4l_ek/doc/index.md)
[

Atmel Corporation

![A picture of the SAM4S Xplained board](../_images/sam4s_xplained.jpg)

SAM4S Xplained

arm

](../boards/atmel/sam/sam4s_xplained/doc/index.md)
[

Analog Devices, Inc.

![A picture of the SDP-K1 board](../_images/adi_sdp_k1.webp)

SDP-K1

arm

](../boards/adi/sdp_k1/doc/index.md)
[

SECO S.p.A.

![A picture of the SECO SBC-3.5-PX30 (JUNO - D23) (STM32F302) board](../_images/stm32f3_seco_d23.jpg)

SECO SBC-3.5-PX30 (JUNO - D23) (STM32F302)

arm

](../boards/seco/stm32f3_seco_d23/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the Seeeduino XIAO board](../_images/seeeduino_xiao.jpg)

Seeeduino XIAO

arm

](../boards/seeed/seeeduino_xiao/doc/index.md)
[

STMicroelectronics

![A picture of the SensorTile.box board](../_images/sensortile_box.jpg)

SensorTile.box

arm

](../boards/st/sensortile_box/doc/index.md)
[

STMicroelectronics

![A picture of the SensorTile.box PRO board](../_images/sensortile_box_pro.jpg)

SensorTile.box PRO

arm

](../boards/st/sensortile_box_pro/doc/index.md)
[

Ezurio

![A picture of the Sentrius BT510 Sensor board](../_images/bt510.jpg)

Sentrius BT510 Sensor

arm

](../boards/ezurio/bt510/doc/bt510.md)
[

Ezurio

![A picture of the Sentrius BT610 Sensor board](../_images/bt610.jpg)

Sentrius BT610 Sensor

arm

](../boards/ezurio/bt610/doc/bt610.md)
[

Ezurio

![A picture of the Sentrius™ MG100 Gateway board](../_images/mg100.jpg)

Sentrius™ MG100 Gateway

arm

](../boards/ezurio/mg100/doc/index.md)
[

Silicon Laboratories

![A picture of the SiM3U1xx 32-bit MCU USB Development Kit board](../_images/sim3u1xx_dk.webp)

SiM3U1xx 32-bit MCU USB Development Kit

arm

](../boards/silabs/dev_kits/sim3u1xx_dk/doc/index.md)
[

Silicon Laboratories

![A picture of the SiWx917 Wi-Fi 6 and Bluetooth LE SoC 8 MB Flash Radio Board (SLWRB4338A) board](../_images/siwx917_rb4338a.webp)

SiWx917 Wi-Fi 6 and Bluetooth LE SoC 8 MB Flash Radio Board (SLWRB4338A)

arm

](../boards/silabs/radio_boards/siwx917_rb4338a/doc/index.md)
[

Texas Instruments

![A picture of the SK-AM62 M4F Core board](../_images/sk_am62_angled.webp)

SK-AM62 M4F Core

arm

](../boards/ti/sk_am62/doc/index.md)
[

GARDENA GmbH

![A picture of the Smart Garden Radio Module board](../_images/sgrm.webp)

Smart Garden Radio Module

arm

](../boards/gardena/sgrm/doc/index.md)
[

STMicroelectronics

![A picture of the ST25DV Discovery, MB1283 version board](../_images/st25dv_mb1283_disco.jpg)

ST25DV Discovery, MB1283 version

arm

](../boards/st/st25dv_mb1283_disco/doc/index.md)
[

M5Stack

STAMP-C3

riscv

](../boards/m5stack/stamp_c3/doc/index.md)
[

M5Stack

![A picture of the StampS3 board](../_images/m5stack_stamps3.webp)

StampS3

xtensa

](../boards/m5stack/m5stack_stamps3/doc/index.md)
[

Renesas Electronics Corporation

![A picture of the Starter Kit+ for RZ/T2M board](../_images/rzt2m_starterkit.png)

Starter Kit+ for RZ/T2M

arm

](../boards/renesas/rzt2m_starterkit/doc/index.md)
[

STMicroelectronics

![A picture of the STEVAL STWINBX1 Development kit board](../_images/steval_stwinbx1.jpg)

STEVAL STWINBX1 Development kit

arm

](../boards/st/steval_stwinbx1/doc/index.md)
[

STMicroelectronics

![A picture of the STM32 Flight Controller Unit board](../_images/steval_fcu001v1.jpg)

STM32 Flight Controller Unit

arm

](../boards/st/steval_fcu001v1/doc/index.md)
[

MikroElektronika d.o.o.

![A picture of the STM32 M4 Clicker board](../_images/stm32_m4_clicker.webp)

STM32 M4 Clicker

arm

](../boards/mikroe/stm32_m4_clicker/doc/index.md)
[

Other/Unknown

![A picture of the STM32 Mini F401 board](../_images/STM32_Mini_F401-1.jpg)

STM32 Mini F401

arm

](../boards/others/stm32f401_mini/doc/index.md)
[

Other/Unknown

![A picture of the STM32 Minimum Development Board board](../_images/stm32_min_dev.jpg)

STM32 Minimum Development Board

](../boards/others/stm32_min_dev/doc/index.md)
[

96Boards

![A picture of the STM32 Sensor Mezzanine board](../_images/96b_stm32_sensor_mez.jpg)

STM32 Sensor Mezzanine

arm

](../boards/96boards/stm32_sensor_mez/doc/index.md)
[

STMicroelectronics

![A picture of the STM3210C Evaluation board](../_images/stm3210c_eval.jpg)

STM3210C Evaluation

arm

](../boards/st/stm3210c_eval/doc/index.md)
[

STMicroelectronics

![A picture of the STM32373C Evaluation board](../_images/stm32373c_eval.jpg)

STM32373C Evaluation

arm

](../boards/st/stm32373c_eval/doc/index.md)
[

STMicroelectronics

![A picture of the STM32C0116-DK Discovery Kit board](../_images/stm32c0116_dk.jpg)

STM32C0116-DK Discovery Kit

arm

](../boards/st/stm32c0116_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F0 Discovery board](../_images/stm32f0_disco.jpg)

STM32F0 Discovery

arm

](../boards/st/stm32f0_disco/doc/index.md)
[

Other/Unknown

![A picture of the STM32F030 DEMO BOARD board](../_images/stm32f030_demo.jpg)

STM32F030 DEMO BOARD

arm

](../boards/others/stm32f030_demo/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F072 Evaluation board](../_images/stm32f072_eval.jpg)

STM32F072 Evaluation

arm

](../boards/st/stm32f072_eval/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F072B Discovery board](../_images/stm32f072b_disco.jpg)

STM32F072B Discovery

arm

](../boards/st/stm32f072b_disco/doc/index.md)
[

Other/Unknown

![A picture of the STM32F103 Mini board](../_images/stm32f103_mini_pin.jpg)

STM32F103 Mini

arm

](../boards/others/stm32f103_mini/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F3 Discovery board](../_images/stm32f3_disco.jpg)

STM32F3 Discovery

arm

](../boards/st/stm32f3_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F4 Discovery board](../_images/stm32f4_disco.jpg)

STM32F4 Discovery

arm

](../boards/st/stm32f4_disco/doc/index.md)
[

WeAct Studio

![A picture of the STM32F405 Core Board V1.0 board](../_images/stm32f405_core.jpg)

STM32F405 Core Board V1.0

arm

](../boards/weact/stm32f405_core/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F411E Discovery board](../_images/stm32f411e_disco.jpg)

STM32F411E Discovery

arm

](../boards/st/stm32f411e_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F412G Discovery board](../_images/stm32f412g_disco.jpg)

STM32F412G Discovery

arm

](../boards/st/stm32f412g_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F413H Discovery board](../_images/stm32F413H_DiscoveryKit.webp)

STM32F413H Discovery

arm

](../boards/st/stm32f413h_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F429I Discovery board](../_images/stm32f429i_disc1.jpg)

STM32F429I Discovery

arm

](../boards/st/stm32f429i_disc1/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F469I Discovery board](../_images/stm32f469i_disco.jpg)

STM32F469I Discovery

arm

](../boards/st/stm32f469i_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F723E Discovery board](../_images/stm32f723e_disco.jpg)

STM32F723E Discovery

arm

](../boards/st/stm32f723e_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F746G Discovery board](../_images/stm32f746g_disco.jpg)

STM32F746G Discovery

arm

](../boards/st/stm32f746g_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F7508-DK Discovery Kit board](../_images/stm32f7508_dk.jpg)

STM32F7508-DK Discovery Kit

arm

](../boards/st/stm32f7508_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32F769I Discovery board](../_images/stm32f769i_disco.jpg)

STM32F769I Discovery

arm

](../boards/st/stm32f769i_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32G0316 Discovery board](../_images/stm32g0316_disco.jpg)

STM32G0316 Discovery

arm

](../boards/st/stm32g0316_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32G071B Discovery board](../_images/stm32g071b_disco.jpg)

STM32G071B Discovery

arm

](../boards/st/stm32g071b_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32G081B Evaluation board](../_images/stm32g081b_eval.jpg)

STM32G081B Evaluation

arm

](../boards/st/stm32g081b_eval/doc/index.md)
[

WeAct Studio

STM32G431 Core Board

arm

](../boards/weact/stm32g431_core/doc/index.md)
[

WeAct Studio

STM32H5 Core Board

arm

](../boards/weact/stm32h5_core/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H573I-DK Discovery board](../_images/stm32h573i_dk.jpg)

STM32H573I-DK Discovery

arm

](../boards/st/stm32h573i_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H735G Discovery board](../_images/stm32h735g_disco.jpg)

STM32H735G Discovery

arm

](../boards/st/stm32h735g_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H745I Discovery board](../_images/stm32h745i-disco.jpg)

STM32H745I Discovery

arm

](../boards/st/stm32h745i_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H747I Discovery board](../_images/stm32h747i_disco.jpg)

STM32H747I Discovery

arm

](../boards/st/stm32h747i_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H750B Discovery Kit board](../_images/stm32h750b_dk.png)

STM32H750B Discovery Kit

arm

](../boards/st/stm32h750b_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H7B3I Discovery kit board](../_images/stm32h7b3i_dk.jpg)

STM32H7B3I Discovery kit

arm

](../boards/st/stm32h7b3i_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32H7S78-DK Discovery board](../_images/stm32h7s78_dk.jpg)

STM32H7S78-DK Discovery

arm

](../boards/st/stm32h7s78_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32L1 Discovery board](../_images/stm32l1_disco.jpg)

STM32L1 Discovery

arm

](../boards/st/stm32l1_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32L152C Discovery board](../_images/stm32l1_disco.jpg)

STM32L152C Discovery

arm

](../boards/st/stm32l1_disco/doc/index.md)
[

Alientek

![A picture of the STM32L475 Pandora board](../_images/pandora_stm32l475.jpg)

STM32L475 Pandora

arm

](../boards/alientek/pandora_stm32l475/doc/index.md)
[

STMicroelectronics

![A picture of the STM32L476G Discovery board](../_images/stm32l476g_disco.jpg)

STM32L476G Discovery

arm

](../boards/st/stm32l476g_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32L496G Discovery board](../_images/stm32l496g_disco.jpg)

STM32L496G Discovery

arm

](../boards/st/stm32l496g_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32L4R9I Discovery board](../_images/stm32l4r9i_disco.jpg)

STM32L4R9I Discovery

arm

](../boards/st/stm32l4r9i_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32L562E-DK Discovery board](../_images/stm32l562e_dk.jpg)

STM32L562E-DK Discovery

arm

](../boards/st/stm32l562e_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32MP157C-DK2 Discovery board](../_images/en.stm32mp157c-dk2.jpg)

STM32MP157C-DK2 Discovery

arm

](../boards/st/stm32mp157c_dk2/doc/stm32mp157_dk2.md)
[

STMicroelectronics

![A picture of the STM32N6570-DK board](../_images/stm32n6570_dk.webp)

STM32N6570-DK

](../boards/st/stm32n6570_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32U083C-DK board](../_images/stm32u083c_dk.jpg)

STM32U083C-DK

arm

](../boards/st/stm32u083c_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32U5A9J Discovery Kit board](../_images/bottom_view.jpg)

STM32U5A9J Discovery Kit

arm

](../boards/st/stm32u5a9j_dk/doc/index.md)
[

STMicroelectronics

![A picture of the STM32VL Discovery board](../_images/stm32vl_disco.jpg)

STM32VL Discovery

arm

](../boards/st/stm32vl_disco/doc/index.md)
[

STMicroelectronics

![A picture of the STM32WB5MM-DK board](../_images/STM32WB5MM_DK.jpg)

STM32WB5MM-DK

arm

](../boards/st/stm32wb5mm_dk/doc/stm32wb5mm_dk.md)
[

STMicroelectronics

![A picture of the STM32WB5MMG board](../_images/STM32WB5MMG.jpg)

STM32WB5MMG

arm

](../boards/st/stm32wb5mmg/doc/stm32wb5mmg.md)
[

Blues Wireless

![A picture of the Swan board](../_images/swan.jpg)

Swan

arm

](../boards/blues/swan_r5/doc/index.md)
[

Shenzhen FeiKaiTe Technology Co., Ltd.

![A picture of the SwiftIO board](../_images/mm_swiftio.jpg)

SwiftIO

arm

](../boards/madmachine/mm_swiftio/doc/index.md)
[

Shenzhen FeiKaiTe Technology Co., Ltd.

![A picture of the SwiftIO Feather board](../_images/mm_feather.jpg)

SwiftIO Feather

arm

](../boards/madmachine/mm_feather/doc/index.md)
[

PJRC

![A picture of the Teensy 4.0 board](../_images/teensy40.jpg)

Teensy 4.0

arm

](../boards/pjrc/teensy4/doc/index.md)
[

PJRC

![A picture of the Teensy 4.1 board](../_images/teensy41.jpg)

Teensy 4.1

arm

](../boards/pjrc/teensy4/doc/index.md)
[

SparkFun Electronics

![A picture of the THING PLUS MATTER board](../_images/MGM240P_Thing_Plus.jpg)

THING PLUS MATTER

arm

](../boards/sparkfun/thing_plus_matter_mgm240p/doc/index.md)
[

Nordic Semiconductor

![A picture of the Thingy:52 board](../_images/thingy52_nrf52832.jpg)

Thingy:52

arm

](../boards/nordic/thingy52/doc/index.md)
[

Nordic Semiconductor

Thingy:53

arm

](../boards/nordic/thingy53/doc/index.md)
[

Efinix Inc

![A picture of the Titanium Ti60 F225 board](../_images/titanium_ti60_f225.jpg)

Titanium Ti60 F225

riscv

](../boards/efinix/titanium_ti60_f225/doc/index.md)
[

Telink Semiconductor

![A picture of the TLSR9518ADK80D board](../_images/tlsr9518adk80d.jpg)

TLSR9518ADK80D

riscv

](../boards/telink/tlsr9518adk80d/doc/index.md)
[

Adafruit Industries, LLC

![A picture of the Trinket M0 board](../_images/adafruit_trinket_m0.jpg)

Trinket M0

arm

](../boards/adafruit/trinket_m0/doc/index.md)
[

Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

![A picture of the TTGO LoRa32 board](../_images/ttgo_lora32.webp)

TTGO LoRa32

xtensa

](../boards/lilygo/ttgo_lora32/doc/index.md)
[

Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

![A picture of the TTGO T7 Mini32 V1.5 board](../_images/ttgo_t7v1_5.webp)

TTGO T7 Mini32 V1.5

xtensa

](../boards/lilygo/ttgo_t7v1_5/doc/index.md)
[

Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

![A picture of the TTGO T8-C3 board](../_images/ttgo_t8c3.webp)

TTGO T8-C3

riscv

](../boards/lilygo/ttgo_t8c3/doc/index.md)
[

Lilygo Shenzhen Xinyuan Electronic Technology Co., Ltd

![A picture of the TTGO T8-S3 board](../_images/ttgo_t8s3.webp)

TTGO T8-S3

xtensa

](../boards/lilygo/ttgo_t8s3/doc/index.md)
[

Google, Inc.

Twinkie V2

arm

](../boards/google/twinkie_v2/doc/index.md)
[

NXP Semiconductors

![A picture of the TWR-KE18F board](../_images/TWR-KE18F-DEVICE.jpg)

TWR-KE18F

arm

](../boards/nxp/twr_ke18f/doc/index.md)
[

NXP Semiconductors

![A picture of the TWR-KV58F220M board](../_images/twr_kv58f220m.jpg)

TWR-KV58F220M

arm

](../boards/nxp/twr_kv58f220m/doc/index.md)
[

Shenzhen Fuyuansheng Electronic Technology Co., Ltd.

![A picture of the UCAN board](../_images/ucan.webp)

UCAN

arm

](../boards/fysetc/ucan/doc/index.md)
[

NXP Semiconductors

![A picture of the UCANS32K1SIC board](../_images/ucans32k1sic_top.webp)

UCANS32K1SIC

arm

](../boards/nxp/ucans32k1sic/doc/index.md)
[

UP Bridge the Gap

![A picture of the UP Squared board](../_images/up_squared.jpg)

UP Squared

x86

](../boards/up-bridge-the-gap/up_squared/doc/index.md)
[

UP Bridge the Gap

UP Squared Pro 7000

x86

](../boards/up-bridge-the-gap/up_squared_pro_7000/doc/up_squared_pro_7000.md)
[

Microchip Technology Inc.

![A picture of the UPD301C Basic Sink Application Example board](../_images/ev11l78a.jpg)

UPD301C Basic Sink Application Example

arm

](../boards/microchip/ev11l78a/doc/index.md)
[

NXP Semiconductors

USB-KW24D512

arm

](../boards/nxp/usb_kw24d512/doc/index.md)
[

WeAct Studio

![A picture of the USB2CANFDV1 board](../_images/usb2canfdv1.webp)

USB2CANFDV1

arm

](../boards/weact/usb2canfdv1/doc/index.md)
[

ARM Ltd.

![A picture of the V2M Beetle board](../_images/v2m_beetle.jpg)

V2M Beetle

arm

](../boards/arm/v2m_beetle/doc/index.md)
[

ARM Ltd.

![A picture of the V2M MPS2 board](../_images/mps2.jpg)

V2M MPS2

arm

](../boards/arm/mps2/doc/index.md)
[

ARM Ltd.

![A picture of the V2M Musca B1 board](../_images/v2m_musca_b1.jpg)

V2M Musca B1

arm

](../boards/arm/v2m_musca_b1/doc/index.md)
[

ARM Ltd.

![A picture of the V2M Musca-S1 board](../_images/v2m_musca_s1.jpg)

V2M Musca-S1

arm

](../boards/arm/v2m_musca_s1/doc/index.md)
[

Toradex AG

![A picture of the Verdin iMX8M Mini board](../_images/verdin_imx8mm_m4.webp)

Verdin iMX8M Mini

arm

](../boards/toradex/verdin_imx8mm/doc/index.md)
[

Toradex AG

![A picture of the Verdin iMX8M Plus SoM board](../_images/verdin_imx8mp_front.jpg)

Verdin iMX8M Plus SoM

arm

](../boards/toradex/verdin_imx8mp/doc/index.md)
[

StarFive Technology Co. Ltd.

![A picture of the VisionFive 2 JH7110 board](../_images/visionfive2.webp)

VisionFive 2 JH7110

riscv

](../boards/starfive/visionfive2/doc/index.md)
[

NXP Semiconductors

![A picture of the VMU RT1170 board](../_images/vmu_rt1170.jpg)

VMU RT1170

arm

](../boards/nxp/vmu_rt1170/doc/index.md)
[

WIZnet Co., Ltd.

![A picture of the W5500 Evaluation Pico board](../_images/w5500_evb_pico_side.png)

W5500 Evaluation Pico

arm

](../boards/wiznet/w5500_evb_pico/doc/index.md)
[

DPTechnics

![A picture of the Walter board](../_images/walter.webp)

Walter

xtensa

](../boards/dptechnics/walter/doc/index.md)
[

Element14 (A Premier Farnell Company)

![A picture of the WaRP7 - Next Generation IoT and Wearable Development Platform board](../_images/warp7.jpg)

WaRP7 - Next Generation IoT and Wearable Development Platform

arm

](../boards/element14/warp7/doc/index.md)
[

WinChipHead

![A picture of the WCH CH32V003EVT board](../_images/ch32v003evt.webp)

WCH CH32V003EVT

riscv

](../boards/wch/ch32v003evt/doc/index.md)
[

Silicon Laboratories

![A picture of the WGM160P Wi-Fi Module (SLWRB4321A) board](../_images/wgm160p-starter-kit.jpg)

WGM160P Wi-Fi Module (SLWRB4321A)

arm

](../boards/silabs/radio_boards/slwrb4321a/doc/index.md)
[

Chengdu Heltec Automation Technology Co., Ltd.

WiFi LoRa 32 (V2)

xtensa

](../boards/heltec/heltec_wifi_lora32_v2/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the Wio Terminal board](../_images/wio_terminal.png)

Wio Terminal

arm

](../boards/seeed/wio_terminal/doc/index.md)
[

Chengdu Heltec Automation Technology Co., Ltd.

![A picture of the Wireless Stick Lite (V3) board](../_images/heltec_wireless_stick_lite_v3.webp)

Wireless Stick Lite (V3)

xtensa

](../boards/heltec/heltec_wireless_stick_lite_v3/doc/index.md)
[

96Boards

![A picture of the WisTrio board](../_images/96b-wistrio.jpg)

WisTrio

arm

](../boards/96boards/wistrio/doc/96b_wistrio.md)
[

NXP Semiconductors

X-S32Z27X-DC (DC2)

arm

](../boards/nxp/s32z2xxdc2/doc/index.md)
[

Particle.io

![A picture of the Xenon board](../_images/particle_xenon.jpg)

Xenon

arm

](../boards/particle/xenon/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the XIAO BLE (Sense) board](../_images/xiao_ble.jpg)

XIAO BLE (Sense)

arm

](../boards/seeed/xiao_ble/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the XIAO ESP32C3 board](../_images/xiao_esp32c3_pinout.jpg)

XIAO ESP32C3

riscv

](../boards/seeed/xiao_esp32c3/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the XIAO ESP32C6 board](../_images/xiao_esp32c6.webp)

XIAO ESP32C6

riscv

](../boards/seeed/xiao_esp32c6/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the XIAO ESP32S3 board](../_images/xiao_esp32s3.jpg)

XIAO ESP32S3

xtensa

](../boards/seeed/xiao_esp32s3/doc/index.md)
[

Seeed Technology Co., Ltd

![A picture of the XIAO RP2040 board](../_images/xiao_rp2040.webp)

XIAO RP2040

arm

](../boards/seeed/xiao_rp2040/doc/index.md)
[

Infineon Technologies

![A picture of the XMC45-RELAX-KIT board](../_images/xmc45_relax_kit.jpg)

XMC45-RELAX-KIT

arm

](../boards/infineon/xmc45_relax_kit/doc/index.md)
[

Infineon Technologies

![A picture of the XMC47-RELAX-KIT board](../_images/xmc47_relax_kit.jpg)

XMC47-RELAX-KIT

arm

](../boards/infineon/xmc47_relax_kit/doc/index.md)
[

Cadence Design Systems Inc.

![A picture of the Xtensa simulator board](../_images/xt-sim.jpg)

Xtensa simulator

xtensa

](../boards/cdns/xt-sim/doc/index.md)
[

VCC-GND Studio

![A picture of the YD-ESP32 board](../_images/yd_esp32.png)

YD-ESP32

xtensa

](../boards/vcc-gnd/yd_esp32/doc/index.md)
[

VCC-GND Studio

![A picture of the YD-STM32H750VB board](../_images/yd_stm32h750vb.png)

YD-STM32H750VB

arm

](../boards/vcc-gnd/yd_stm32h750vb/doc/index.md)
[

Shenzhen Holyiot Technology Co., Ltd.

![A picture of the YJ-16019 board](../_images/holyiot_yj16019_front.jpg)

YJ-16019

arm

](../boards/holyiot/yj16019/doc/index.md)
[

Diglent, Inc.

![A picture of the Zybo board](../_images/zybo-0.jpg)

Zybo

arm

](../boards/digilent/zybo/doc/index.md)

# Shields
