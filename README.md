# PeaZip Right-Click 🗜️

**PeaZip Right-Click** is a full context-menu integration for PeaZip on Linux, generated with [ClickMesh](https://github.com/ahmed-x86/click_mesh). It brings the classic WinRAR-style right-click experience to Linux — Add to archive, Extract here, Extract to folder, and more — for **6 file managers at once**.

✨ Features

- **One JSON, Every File Manager:** Built with ClickMesh from a single `peazip.json`
- **WinRAR-like Experience:** Add to ZIP/7Z, Extract Here, Extract to folder, Open with PeaZip
- **6 File Managers Supported:** Nautilus, Nemo, Caja, Thunar, Dolphin, PCManFM
- **Smart Groups:** 5 groups for Dolphin/PCManFM to avoid menu clutter
- **No Wine Needed:** Native `peazip` binary integration

🛠️ Dependencies

- `peazip` ( `sudo pacman -S peazip` )
- File manager python bindings if you use Nautilus/Nemo/Caja/Thunar:
  `python-nautilus`, `python-nemo`, `python-caja`, `thunarx-python`

🚀 Install

Quick install with ClickMesh (Recommended)

```bash
git clone https://github.com/ahmed-x86/click_mesh.git
cd click_mesh
python clickmesh.py --from-json ../peazip_rightclick/peazip.json -install make ../peazip_rightclick/output
```
Or manually:

1. Nautilus (GNOME)
```bash
mkdir -p ~/.local/share/nautilus-python/extensions/
cp output/nautilus/PeaZipMenu.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```
2. Nemo (Cinnamon)
```bash
mkdir -p ~/.local/share/nemo-python/extensions/
cp output/nemo/PeaZipMenu.py ~/.local/share/nemo-python/extensions/
nemo -q
```
3. Caja (MATE)
```bash
mkdir -p ~/.local/share/caja-python/extensions/
cp output/caja/PeaZipMenu.py ~/.local/share/caja-python/extensions/
caja -q
```
4. Thunar (XFCE)
```bash
mkdir -p ~/.local/share/thunarx-python/extensions/
cp output/thunar/PeaZipMenu.py ~/.local/share/thunarx-python/extensions/
thunar -q
```
5. Dolphin (KDE Plasma 5 & 6)
```bash
mkdir -p ~/.local/share/kio/servicemenus/
cp output/dolphin/*.desktop ~/.local/share/kio/servicemenus/
For Plasma 5 compat
mkdir -p ~/.local/share/kservices5/ServiceMenus/
cp output/dolphin/*.desktop ~/.local/share/kservices5/ServiceMenus/
```
6. PCManFM (LXDE / LXQt)
```bash
mkdir -p ~/.local/share/file-manager/actions/
cp output/pcmanfm/*.desktop ~/.local/share/file-manager/actions/
```
🧩 How it was built

This whole repo was generated from one file:

`peazip.json` -> ClickMesh -> 14 extensions
python clickmesh.py --from-json peazip.json make ./output
Check the main project: *https://github.com/ahmed-x86/click_mesh*

## 📄 License

GPL-3.0-or-later - See
[LICENSE](./LICENSE)