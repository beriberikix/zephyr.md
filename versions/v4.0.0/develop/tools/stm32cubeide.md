---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/tools/stm32cubeide.html
original_path: develop/tools/stm32cubeide.html
---

# STM32CubeIDE

[STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html) is an Eclipse-based integrated development environment from STMicroelectronics designed for the STM32 series of MCUs and MPUs.

This guide describes the process of setting up, building, and debugging Zephyr
applications using the IDE.

A project must have already been created with Zephyr and west.

These directions have been validated to work with version 1.16.0 of the IDE
on Linux.

## Project Setup

1. Before you start, make sure you have a working Zephyr development environment, as per the
   instructions in the [Getting Started Guide](../getting_started/index.md#getting-started).
2. Run STM32CubeIDE from your Zephyr environment. Example:

   ```text
   $ /opt/st/stm32cubeide_1.16.0/stm32cubeide
   ```
3. Open your already existing project by going to
   File ‣ New ‣ STM32 CMake Project:

   ![Create new CMake project](../../_images/stm32cube_new_cmake.webp)
4. Select Project with existing CMake sources, then click Next.
5. Select Next and browse to the location of your sources. The
   folder that is opened should have the `CMakeLists.txt` and `prj.conf` files.
6. Select Next and select the appropriate MCU.
   Press Finish and your project should now be available.
   However, more actions must still be done in order to configure it properly.
7. Right-click on the newly created project in the workspace, and select
   Properties.
8. Go to the C/C++ Build page and set the Generator
   to `Ninja`. In Other Options, specify the target `BOARD` in
   CMake argument format. If an out-of-tree board is targeted, the `BOARD_ROOT`
   option must also be set. The resulting settings page should look similar to this:

   ![Properties dialog for project](../../_images/stm32cube_project_properties.webp)

   These options may or may not be needed depending on if you have an
   out-of-tree project or not.
9. Go to the C/C++ General ‣ Preprocessor Include page.
   Select the GNU C language, and click on the
   CDT User Settings Entries option.

   ![Properties dialog for preprocessor options](../../_images/stm32cube_preprocessor_include.webp)

   Click Add to add an Include File
   that points to Zephyr’s `autoconf.h`, which is located in
   `<build dir>/zephyr/include/generated/autoconf.h`. This will ensure
   that STM32CubeIDE picks up Zephyr configuration options.
   The following dialog will be shown. Fill it in as follows:

   ![Add include file dialog](../../_images/stm32cube_add_include.webp)

   Once the include file has been added, your properties page should look
   similar to the following:

   ![Properties page after adding autoconf.h file](../../_images/stm32cube_autoconf_h.webp)
10. Click Apply and Close
11. You may now build the project using the Build button on the toolbar.
    The project can be run using the Run button, as well as debugged
    using the Debug button.

## Troubleshooting

When configuring your project you see an error that looks similar to:

```text
Error message: Traceback (most recent call last):

  File "/path/to/zephyr/scripts/list_boards.py", line 11, in <module>
    import pykwalify.core

ModuleNotFoundError: No module named 'pykwalify'
```

This means that you did not start the IDE in a Zephyr environment. You must
delete the `config_default` build directory and start STM32CubeIDE again,
making sure that you can run `west` in the shell that you start STM32CubeIDE
from.
