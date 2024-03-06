+++
title = "Morpho manual on the web"
date = 2024-03-06
[taxonomies]
categories = ["code"]
tags = ["#open-source", "#documentation"]
+++

I am working on converting the [Morpho](https://github.com/Morpho-lang/morpho) manual, currently in [PDF format hosted on GitHub and written in LyX](https://github.com/Morpho-lang/morpho/tree/main/manual/), into an accessible [mdbook](https://github.com/rust-lang/mdBook) format.

You can find the resulting website [here](https://joshichaitanya3.github.io/morpho-manual/) and the code on GitHub [here](https://github.com/joshichaitanya3/morpho-manual).

I am still deciding on the design principle for the mdBook manual, whether to have it always auto-converted from LyX when the manual is updated, or to have the bulk of it auto-converted and the new edits manually. In the first case, the authoring ease need not be emphasized, but would get trickier with the auto-conversion (think formatting equations correctly, handling footnotes, etc.) In the latter case, the authoring needs to be easy while still maintaining quality and accessibility (think inserting a figure with the proper Figure environment, captions and alt-texts.) I would love to hear your thoughts! Reach out on the GitHub, contributions of all kinds are very welcome!
