---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/tools/vscode.html
original_path: develop/tools/vscode.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) (VS Code for short) is a popular cross-platform IDE that supports C projects
and has a rich set of extensions.

This guide describes the process of setting up VS Code for Zephyr’s
[Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample in VS Code.

The instructions have been tested on Linux, but the steps should be the same for macOS and
Windows, just make sure to adjust the paths if needed.

## Get VS Code

[Download VS Code](https://code.visualstudio.com/Download) and install it.

Install the required extensions through the Extensions marketplace in the left panel.
Search for the [C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack) and install it.

## Initialize a new workspace

This guide gives details on how to configure the [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
sample application, but the instructions would be similar for any Zephyr project and [workspace
layout](../west/workspaces.md#west-workspaces).

Before you start, make sure you have a working Zephyr development environment, as per the
instructions in the [Getting Started Guide](../getting_started/index.md#getting-started).

## Open the project in VS Code

1. In VS Code, select File ‣ Open Folder from the main menu.
2. Navigate to your Zephyr workspace and select it (i.e. the `zephyrproject` folder in your
   HOME directory if you have followed the Getting Started instructions).
3. If prompted, enable workspace trust.

## Generate compile commands

In order to support code navigation and linting capabilities, you must compile your project once to
generate the `compile_commands.json` file that will provide the C/C++ extension with the
required information (ex. include paths):

> ```shell
> west build -b native_sim/native/64 samples/basic/blinky
> ```

## Configure the C/C++ extension

You’ll now need to point to the generated `compile_commands.json` file to enable linting and
code navigation in VS Code.

1. Go to the File ‣ Preferences ‣ Settings in the VS Code top menu.
2. Search for the parameter C\_Cpp > Default: Compile Commands and set its value to:
   `zephyr/build/compile_commands.json`.

   Linting errors in the code should now be resolved, and you should be able to navigate through the
   code.

## Additional resources

There are many other extensions that can be useful when working with Zephyr and VS Code. While this
guide does not cover them yet, you may refer to their documentation to set them up:

### Contribution tooling

- [Checkpatch Extension](https://marketplace.visualstudio.com/items?itemName=idanp.checkpatch)
- [EditorConfig Extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

### Documentation languages extensions

- [reStructuredText Extension Pack](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext-pack)

### IDE extensions

- [CMake Extension documentation](https://code.visualstudio.com/docs/cpp/cmake-linux)
- [nRF Kconfig Extension](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-kconfig)
- [nRF DeviceTree Extension](https://marketplace.visualstudio.com/items?itemName=nordic-semiconductor.nrf-devicetree)
- [GNU Linker Map files Extension](https://marketplace.visualstudio.com/items?itemName=trond-snekvik.gnu-mapfiles)

### Additional guides

- [How to Develop Zephyr Apps with a Modern, Visual IDE](https://github.com/beriberikix/zephyr-vscode-example)

Note

Please be aware that these extensions might not all have the same level of quality and maintenance.
