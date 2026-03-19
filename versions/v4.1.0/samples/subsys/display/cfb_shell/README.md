---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/display/cfb_shell/README.html
original_path: samples/subsys/display/cfb_shell/README.html
---

# Character Framebuffer shell module

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/display/cfb_shell/README.rst/..)

## Overview

This is a simple shell module that exercises displays using the Character
Framebuffer subsystem.

## Building and Running

Build the sample app by choosing the target board, for example:

```shell
# From the root of the zephyr repository
west build -b reel_board samples/subsys/display/cfb_shell
```

### Shell Module Command Help

```shell
cfb - Character Framebuffer shell commands
Options:
        -h, --help  :Show command help.
Subcommands:
        init        :[none]
        get_device  :[none]
        get_param   :<all, height, width, ppt, rows, cols>
        get_fonts   :[none]
        set_font    :<idx>
        invert      :[none]
        print       :<col: pos> <row: pos> <text>
        scroll      :<dir: (vertical|horizontal)> <col: pos> <row: pos>
                     <text>
        clear       :[none]
```

**init**: should be called first to initialize the display.

Command example (reel\_board):

```shell
uart:~$ cfb init
Framebuffer initialized: SSD16XX
Display Cleared
```

**get\_device**: prints the display device name.

Command example (reel\_board):

```shell
uart:~$ cfb get_device
Framebuffer Device: SSD16XX
```

**get\_param**: get the display parameters where height, width and ppt
(pixel per tile) are in pixels and the number of rows and columns. The row
position is incremented by a multiple of the ppt.

Command example (reel\_board):

```shell
uart:~$ cfb get_param all
param: height=120
param: width=250
param: ppt=8
param: rows=15
param: cols=250
```

**get\_fonts**: print the index, height and width in pixels of the static
defined fonts presented in the system.

Command example (reel\_board):

```shell
uart:~$ cfb get_fonts
idx=0 height=32 width=20
idx=1 height=24 width=15
idx=2 height=16 width=10
```

**set\_font**: choose the font to be used by passing the font index. Only one
font can be used at a time.

Command example (reel\_board):

```shell
uart:~$ cfb set_font 0
Font idx=0 height=32 width=20 set
```

**invert**: invert the pixel color of the display.

Command example (reel\_board):

```shell
uart:~$ cfb invert
Framebuffer Inverted
```

**print**: pass the initial column and row positions and the text in
double quotation marks when it contains spaces. If text hits the edge
of the display the remaining characters will be displayed on the next line. The
previous printed text will be overwritten.

Command example (reel\_board):

```shell
uart:~$ cfb print 60 5 ZEPHYR
```

**scroll**: pass the scroll direction, vertical or horizontal, the initial
column and row positions, and the text to be displayed in double quotation
marks when it contains spaces. If the text hits the edge of the display, the
remaining characters will be displayed in the next line. The text will scroll
until it hits the display boundary, last column for horizontal and last row
for vertical direction. The text passed with the scroll command will be moved
vertically or horizontally on the display.

Command example (reel\_board):

```shell
uart:~$ cfb scroll vertical 60 5 ZEPHYR
```

**clear**: clear the display screen.

Command example (reel\_board):

```shell
uart:~$ cfb clear
Display Cleared
```

## See also

[Monochrome Character Framebuffer](../../../../doxygen/html/group__monochrome__character__framebuffer.md)
