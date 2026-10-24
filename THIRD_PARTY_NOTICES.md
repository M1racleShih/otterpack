# Authors, sources and licenses

Otterpack is a curated collection. The root MIT license applies to new material for which the maintainer can grant that license. It does not replace any component license, create an upstream endorsement, or claim authorship of third-party projects.

| Material in this repository | Source / authors | License retained |
| --- | --- | --- |
| Pi Catppuccin theme files; the starting structure used for the parchment Pi theme | [M1racleShih/pi-catppuccin-theme](https://github.com/M1racleShih/pi-catppuccin-theme), Shq; [Catppuccin](https://github.com/catppuccin/catppuccin), Catppuccin contributors | [port MIT](licenses/pi-catppuccin-theme.txt) and [palette MIT](licenses/CATPPUCCIN.txt) |
| Herdr/Radar sidebar templates in `themes/parchment/herdr.toml` | [herdr-radar](https://github.com/M1racleShih/herdr-radar), copyright qintmb and herdr-kit contributors, with local palette changes | [MIT](licenses/herdr-radar.txt) |
| `patches/pi-hud/` | [pi-hud](https://github.com/M1racleShih/pi-hud), pi-hud contributors | [MIT](patches/pi-hud/LICENSE); original inspiration notices are kept beside the patch |
| `patches/conv-docs/` | [conv-docs](https://github.com/M1racleShih/conv-docs), conv-docs contributors | [MIT](patches/conv-docs/LICENSE); upstream third-party notices retained |
| `patches/herdr-remote-solution/` | [dcolinmorgan/herdr-remote](https://github.com/dcolinmorgan/herdr-remote) and contributors; M1racleShih's adaptation | **[AGPL-3.0-or-later](patches/herdr-remote-solution/LICENSE)** via the upstream open-source option |
| `extensions/pi/clear.ts`; Pi capture and offline fixture adaptations | [cooking-pi](https://github.com/M1racleShih/cooking-pi), M1racleShih | MIT, same copyright holder as this repository |
| New guides, helper scripts, integration fragments and mascot | M1racleShih / Otterpack; mascot created using an AI image tool | [MIT](LICENSE), to the extent applicable; [image provenance](docs/brand.md) |

## Herdr Remote boundary

The Herdr Remote patch is a modification of an AGPL component. The complete pinned baseline and patch are identified in [catalog.json](catalog.json); reconstruction produces the full source tree with its original license. Modifying, conveying or running that component as a network service can carry AGPL source-availability obligations. Follow its retained license, including the network-use terms, for your deployment. Mere inclusion here does not relicense the other independent components under AGPL.

The upstream also offers commercial terms; Otterpack relies on the open-source option and does not grant a commercial license. Screenshots of its interface are provided as part of this documented source-based demonstration under the component's applicable terms, not claimed as new MIT interface artwork.

## Referenced components

The remaining tools and npm packages are references, not vendored application source. `catalog.json` records exact commits or installed versions and package-declared licenses. Each installation brings the original project's license and dependency terms. Herdr and Pi are third-party hosts; no host binaries or fonts are bundled.

The reconstructed conv-docs source includes marked (MIT), DOMPurify (Apache-2.0) and highlight.js (BSD-3-Clause), with original license texts in its vendor directory. Keep those files with redistributed source or built assets. Its notice copy here is informational; vendor-license links point to the pinned upstream source.

Pi-HUD independently implements its behavior using Pi's public extension contract and credits Claude HUD for inspiration. Its retained notice links to the pinned upstream research record. Only link targets in the copied notices have been adjusted for this repository; attribution text is preserved.

## Images and fonts

Screenshots and terminal frames contain only synthetic demo content. The displayed UI belongs to the corresponding projects; provenance is recorded in [screenshots.md](docs/screenshots.md). Locally installed fonts are rendered into images but font files are not redistributed. The otter illustration is separately documented in [brand.md](docs/brand.md).
