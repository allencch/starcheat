# starcheat [![Build Status](https://travis-ci.org/wizzomafizzo/starcheat.png?branch=master)](https://travis-ci.org/wizzomafizzo/starcheat)

starcheat is a Starbound player save editor, you can get free pixels with this! (omg)

**Downloads for starcheat are [here](#downloads).**

![woohoo](https://raw.github.com/wizzomafizzo/starcheat/master/screen.png)

## Table of Contents

- [Downloads](#downloads)
	- [Windows](#windows)
	- [Mac](#mac)
- [Build Instructions](#build-instructions)
	- [Dependencies](#dependencies)
	- [Windows](#windows-1)
	- [Linux](#linux)
	- [Mac](#mac-1)
- [Troubleshooting](#troubleshooting)
	- [Reset all settings](#reset-all-settings)
	- [How to get logs](#how-to-get-logs)
	- [Unpacking Starbound assets](#unpacking-starbound-assets)

## Downloads
**Upgraded to Furious Koala? Don't forget to [clear your settings](#reset-all-settings) and [unpack your Starbound assets](#unpacking-starbound-assets) before trying to run starcheat.**

These are builds of the latest development version. They should work fine, but may be unstable. **Don't forget to back up your save files before using them.**

### Windows
[Download here](http://mcsi.mp/starcheat/) (get the newest file)

**NOTE:** If Windows complains about a system error (re: missing msvcr100.dll), you probably need to install the [Microsoft Visual C++ 2010 Redistributable Package](http://www.microsoft.com/en-au/download/details.aspx?id=5555).

#### How to run
* Download starcheat
* Extract all files somewhere
* Go into the ```dist/``` folder
* Run ```starcheat.exe```
* Follow the prompts to configure starcheat (only happens once)
* Open a player

### Mac
[Download here](https://github.com/wizzomafizzo/starcheat/releases) (get the newest release)

## Build Instructions
Here is how to build starcheat from source. Make sure everything in the dependencies section is installed before you do a build

### Dependencies
- [Python 3](http://www.python.org/getit/)
- [Qt 5](http://qt-project.org/downloads) (Windows users don't need this)
- [PyQt5](http://www.riverbankcomputing.com/software/pyqt/download5)

### Windows
Lines starting with ```PS>``` are to be run in PowerShell. Don't forget to [set your execution policy](http://technet.microsoft.com/en-us/library/ee176961.aspx) if it's the first time you're using PowerShell.

- ```PS> cd <starcheat top folder>```
- ```PS> ./build.ps1```
- Browse to newly created ```build/``` folder
- Double click ```starcheat.py```

#### Standalone Build
The standalone build makes an executable which includes all Python and Qt dependencies.

- Install [cx_freeze](http://cx-freeze.sourceforge.net/)
- ```PS> cd <starcheat top folder>```
- ```PS> ./build.ps1 -Standalone```
- Browse to newly created ```dist/``` folder
- Double click ```starcheat.exe```

### Linux
```
$ cd <starcheat top folder>
$ ./build.sh
$ ./build/starcheat.py
```

#### Arch Linux
Install [starcheat](https://aur.archlinux.org/packages/starcheat/) from AUR.

### Mac
- Install [homebrew](http://brew.sh/)
- ```$ brew install python3```
- ```$ brew install https://raw.github.com/wizzomafizzo/starcheat/master/mac/starcheat.rb``` (optionally pass ```--without-app``` (create no .app) or ```--without-binary``` (creates no binary linked into your prefix) )
- ```brew linkapps```(symlinks the .app into your Applications folder)

## Troubleshooting
Stuff you can do when starcheat stops working. Clearing local settings and checking you did the setup correctly is always a good first step.

### Reset all settings
This will remove all locally stored data for starcheat and force a new setup dialog next run.

#### Windows
- Press the Windows key and R (```Win+R```) to bring up the Run... dialog
- Type ```%APPDATA%\starcheat``` and press Enter
- Delete ```assets.db``` and ```starcheat.ini``` from the folder that pops up

#### Linux
In a terminal:
- ```$ rm ~/.starcheat/assets.db```
- ```$ rm ~/.starcheat/starcheat.ini```

#### Mac
In Finder:
- Open the ```Go``` menu and click ```Go to Folder``` (or press ```Cmd+Shift+G```)
- Type ```~/Library/Application Support/starcheat``` and press Enter
- Delete ```assets.db``` and ```starcheat.ini``` from the folder that pops up

### How to get logs
This will point you to where the starcheat logs are stored. If you're trying to report an error, you only need to upload the latest log file.

#### Windows
- Press the Windows key and R (```Win+R```) to bring up the Run... dialog
- Type ```%APPDATA%\starcheat\logs``` and press Enter

#### Linux
In a terminal:
- ```$ cd ~/.starcheat/logs```

#### Mac
In Finder:
- Open the ```Go``` menu and click ```Go to Folder``` (or press ```Cmd+Shift+G```)
- Type ```~/Library/Application Support/starcheat/logs``` and press Enter

### Unpacking Starbound assets
Furious Koala packs assets into a single file which we can't read yet. For now, you'll need to manually unpack the vanilla Starbound assets. You will have to do this for each mod you want starcheat to include as well.

If these instructions don't work for you, check out [this post](http://community.playstarbound.com/index.php?threads/how-to-successfully-pack-and-unpack-pak-files.66649/) on the forums for more options.

#### Windows
- Press the Windows key and R (```Win+R```) to bring up the Run... dialog
- Enter the following text into the prompt and press Enter:
  - "C:\Program Files (x86)\Steam\SteamApps\common\Starbound\win32\asset_unpacker.exe" "C:\Program Files (x86)\Steam\SteamApps\common\Starbound\assets\packed.pak" "C:\Program Files (x86)\Steam\SteamApps\common\Starbound\assets"

#### Linux
**NOTE: If you're on 32 bit, change the path to Starbound.**

In a terminal:
- $ "~/.steam/root/SteamApps/common/Starbound/linux64/asset_unpacker" "~/.steam/root/SteamApps/common/Starbound/assets/packed.pak" "~/.steam/root/SteamApps/common/Starbound/assets"

#### Mac
In a terminal:
- ```$ cd ~/Library/Application\ Support/Steam/SteamApps/common/Starbound; Starbound.app/Contents/MacOS/asset_unpacker assets/packed.pak assets```
