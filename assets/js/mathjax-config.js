// MathJax Configuration
//
// v2 to v3 upgrade notes:
// - The CommonHTML.linebreaks option is not yet implemented (but may be in a future release)
// - The TeX.noUndefined.attributes option is not yet implemented (but may be in a future release)
let preamble = String.raw`\require{physics}`;

window.MathJax = {
  loader: {
    load: ["[tex]/noerrors"],
  },
  tex: {
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
    displayMath: [
      ["$$", "$$"],
      ["\\[", "\\]"],
    ],
    packages: {
      "[+]": ["noerrors"],
    },
  },
  startup: {
    pageReady: async () => {
      const fetcher = await fetch("/tex/TexPreambles/mathjax_preamble.sty", {
        method: "GET",
      });

      const preamble = await fetcher.text();

      await MathJax.tex2chtmlPromise(preamble);
      await MathJax.startup.defaultPageReady();
    },
  },
};
