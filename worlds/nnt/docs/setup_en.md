# Oddworld: New 'n' Tasty Archipelago Setup Guide

## Required Software

- Oddworld: New 'n' Tasty from either [Steam](https://store.steampowered.com/app/314660/Oddworld_New_n_Tasty/) or [GOG](https://www.gog.com/en/game/oddworld_new_n_tasty).
- BepInEx 5 from [GitHub](https://github.com/bepinex/bepinex/releases) (Requires the x86 version rather than the x64 version).
- New 'n' Tasty Archipelago Mod from [GitHub](https://github.com/Knuxfan24/New-n-Tasty-Archipelago/releases). Be sure to download the correct version for your copy of the game!

## Installation Procedures

### BepInEx and Mod Setup

1. Install the game and then extract the contents of the BepInEx ZIP archive to the game's root (likely to be `C:\Program Files (x86)\Steam\steamapps\common\Oddworld New n Tasty`).

2. Run the game once (which will end with the game crashing) to generate BepInEx's configuration files.

3. Open the BepInEx configuration file (likely to be at `C:\Program Files (x86)\Steam\steamapps\common\Oddworld New n Tasty\BepInEx\config\BepInEx.cfg`) and change the `Type = Application` line under `[Preloader.Entrypoint]` to `Type = MonoBehaviour`. It is also recommended to turn the `Enabled` option under `[Logging.Console]` to `true` and set the `LogLevels` option to `All`.

4. Extract the contents of the Archipelago 7-Zip archive to the game's root (likely to be `C:\Program Files (x86)\Steam\steamapps\common\Oddworld New n Tasty`) and choose to merge it with the existing BepInEx folder.

5. Run the game once to generate the mod's configuration file.

## Joining a MultiWorld Game

Open the mod's configuration file (likely to be at `C:\Program Files (x86)\Steam\steamapps\common\Oddworld New n Tasty\BepInEx\config\K24_NNT_Archipelago.cfg`) and fill in the information for your server's address, slot and (if applicable) password. Then launch the game; upon reaching the save selection screen the game will attempt to connect using the specified configuration options.