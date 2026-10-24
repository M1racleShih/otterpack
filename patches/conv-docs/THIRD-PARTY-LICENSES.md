# Third-Party Licenses

conv-docs itself is released under the MIT License ([LICENSE](LICENSE)). That license covers **conv-docs' own code and artwork only**. The distribution bundles third-party components that remain under **their own original licenses**; nothing here relicenses them.

## Bundled in the distribution

These files ship inside `src/conv_docs/web/vendor/` and run on the phone's browser:

| Component | Version | License (SPDX) | Files | Original text |
|-----------|---------|----------------|-------|---------------|
| [marked](https://github.com/markedjs/marked) | 18.0.14 | `MIT` | `marked.umd.js` | [LICENSE.marked.txt](https://github.com/M1racleShih/conv-docs/blob/3224a59fffe77f5f1776bae911eeef7ca7347448/src/conv_docs/web/vendor/LICENSE.marked.txt) |
| [DOMPurify](https://github.com/cure53/DOMPurify) | 3.4.16 | `Apache-2.0` (dual `Apache-2.0 OR MPL-2.0`, distributed here under Apache-2.0) | `purify.min.js` | [LICENSE.dompurify.txt](https://github.com/M1racleShih/conv-docs/blob/3224a59fffe77f5f1776bae911eeef7ca7347448/src/conv_docs/web/vendor/LICENSE.dompurify.txt) |
| [highlight.js](https://github.com/highlightjs/highlight.js) | 11.12.0 | `BSD-3-Clause` | `highlight.min.js`, `github.min.css` | [LICENSE.highlightjs.txt](https://github.com/M1racleShih/conv-docs/blob/3224a59fffe77f5f1776bae911eeef7ca7347448/src/conv_docs/web/vendor/LICENSE.highlightjs.txt) |

All three are permissive licenses. Redistributing them inside an MIT-licensed project is standard and compliant, provided that:

1. **Each component keeps its own license and copyright notices** — preserved above and in `vendor/LICENSE.*`, and the minified sources carry their embedded license headers;
2. **No warranty is implied** — the MIT disclaimer in [LICENSE](LICENSE) applies to our code; each component also carries its own disclaimer;
3. **Apache-2.0 obligations are met** — the Apache license text is retained (done), modifications (none made to the library sources; only vendored as-is) would need to be stated, and the patent grant in Apache-2.0 benefits downstream users. Apache-2.0 is not "less safe" than MIT for redistribution — it adds a patent clause that MIT lacks;
4. **Trademarks are not implied** — names and logos are used only to identify the components.

## Development-only dependencies (not distributed)

`pytest`, `typescript` and their transitive dependencies are installed locally via uv/npm for testing and building. They are not part of the distributed product, so their licenses (MIT for pytest, Apache-2.0 for the TypeScript compiler) do not affect the distribution.

## Practical takeaway

A downstream user may take conv-docs under MIT **except** for the three bundled libraries, which they receive under MIT / Apache-2.0 / BSD-3-Clause respectively. This "aggregate work with per-component licensing" arrangement is exactly what the permissive licenses intend. If you ever need a fully MIT-only distribution, replace the vendored libraries with MIT-licensed alternatives or load them at runtime from the user's own environment — but for public release the current arrangement is legal and conventional.
