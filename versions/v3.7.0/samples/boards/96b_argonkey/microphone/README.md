---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/96b_argonkey/microphone/README.html
original_path: samples/boards/96b_argonkey/microphone/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ArgonKey Board Microphone

## Overview

This sample provides an example of how to acquire audio through
the on-board MP34DT05 microphone. The microphone generates a PDM
stream which is acquired through I2S. The PDM stream is then
converted to PCM using the OpenPDMFilter library, which is available
in source code in this sample.

## Requirements

This sample requires the ArgonKey board plus a USB to TTL 1V8 serial
cable to get the output audio stream. The board can be powered
in either one of the following two ways:

- mezzanine mode, plugging the ArgonKey to HiKey board through its 96Board
  low-speed connector
- standalone mode, supplying 5V directly on P1 connector

## References

- [96Boards Argonkey](../../../../boards/96boards/argonkey/doc/index.md#b-argonkey)

## Building and Running

```shell
west build -b 96b_argonkey samples/boards/96b_argonkey/microphone
west build -t run
```

### Sample Output

The example acquires 5s of audio and prints out the PCM stream on COM port.
A USB to TTL 1V8 serial cable may be attached to the low speed connector on
the back of the board on P3.5 (TX) and P3.7 (RX).

As soon as the acquisition starts the green LED glows. At the end of the
acquisition both the green and red LEDs go on and the PCM stream is sent
on COM port. When the output is completed the green LED goes off and the red
LED stays on. The process can be reiterated by pressing the RST button.

- audio acquisition starts: GRN on - RED off
- audio acquisition ends: GRN on - RED on
- audio output ends: GRN off - RED on

The characteristics of the PCM audio are hardcoded in the example:

- 16KHz sample rate
- 16 bits per sample
- 1 channel (mono), as only 1 microphone is available

Five seconds of acquisition at a 16KHz sampling rate yields 80,000 16-bit samples.
The microphone PDM requested clock should lead the MP34DT05 driver to select an
oversampling/decimation factor equal to 128, resulting in a 2.048MHz bit clock.

See pcm and pdm configuration in file [samples/boards/96b\_argonkey/microphone/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/96b_argonkey/microphone/src/main.c).

Note

It is possible to change the AUDIO\_FREQ to 32000 acquiring only 2500 ms. In this
case the oversampling/decimation factor will be 64.

At the end of the acquisition the PCM data will be printed on the terminal
emulator in either binary or ASCII format. The output is controlled by
following macro, off by default, in [samples/boards/96b\_argonkey/microphone/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/96b_argonkey/microphone/src/main.c):

- `PCM_OUTPUT_IN_ASCII`

#### Binary PCM Output

The ttyUSB0 port must be configured in raw mode to avoid having
characters ‘cooked’ out.

```shell
stty -F /dev/ttyUSB0 115200 raw
cat /dev/ttyUSB0 > /tmp/sound.raw
```

Note

The “cat /dev/ttyUSB0 > /tmp/sound.raw” command should be launched after the audio
acquisition starts (after green led glows) to avoid initial boot messages to enter in the file,
and before audio acquisition ends (before red led glows).

Note

In case the character 0x0a is interpreted as NL and an 0x0d (CR) is added,
you may need to remove it:

```text
dos2unix -f /tmp/sound.raw
```

#### ASCII PCM Output

It is also possible to recompile and to have PCM output in ASCII, which needs
to be converted to binary later on. The output format is the following:

```shell
ArgonKey test!!
-- start
0xfbe0,
0xfbf0,
0xfc0c,
0xfc24,
0xfc3c,
0xfc4c,
0xfc68,
0xfc48,

[...]

0xfb98,
0xfb98,
0xfbb8,
0xfbac,
0xfbc4,
0xfbe8,
0xfbf4,
-- end
```

#### Play PCM Audio

Now that we have a binary PCM file (say sound.raw), you can use,
for example, the audacity open source editor/player to load and play it.
Use the ‘Import->Raw Data’ menu to load the sound.raw file as
signed 16 bit PCM, Little Endian, mono format @16KHz.
