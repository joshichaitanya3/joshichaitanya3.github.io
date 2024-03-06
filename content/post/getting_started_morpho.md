+++
title = "Getting started with Morpho development"
date = 2024-03-06
[taxonomies]
categories = ["code"]
tags = ["open-source"]
+++

_As a postdoctoral scholar, I started working on [Morpho](https://github.com/Morpho-lang/morpho) in August 2021. At the time, I had little experience in software development / engineering. I had written a lot of Python/C based scientific computing code, but it was mostly meant to just perform the simulations/analysis faithfully, with little thought towards the documentation, maintenance, best practices, etc. regarding the codebase. I **wanted** to contribute to Morpho, understand how it works, and in general improve it. Not having a background in software engineering, it took me a while to learn things on my own. The hope with this blog post is that if you find yourselves at a similar juncture, it should kickstart your exploration into Morpho much quicker._

## What is Morpho?

Morpho is a light-weight object-oriented programming enviromnemt for solving optimization problems in soft matter physics and beyond. You can think of it as a more modern [Surface Evolver](https://en.wikipedia.org/wiki/Surface_Evolver) --- we use simplicial meshes (and fields defined on them as well, unlike Surface Evolver) and perform direct optimization on the vertices, connectivities and field values. The scripting language can be used to write arbitrary prorams like in Python, but the main horse-power comes from data-structures implemented in C. Oh, yes, Morpho is written in C (we will get to this later).

## Where can I find documentation?

Morpho ships with an extensive User Manual, that is currently hosted on the main GitHub repository. I am [undertaking a project](https://github.com/joshichaitanya3/morpho-manual) to additionally provide it as a website for better accessibility. This would _also_ be a great avenue to contribute to Morpho!

In addition to the User Manual, which is meant for end-users, Morpho also provides a [developer's guide](https://github.com/Morpho-lang/morpho-devguide) which is a great (in progress) reference for Morpho internals. (See [below](#what-is-not-documented) for a collection of things that aren't documented well yet.)

## What is not documented?

Here are a bunch of things that I would love if we get documentation on. They are in no particular order, and might be of interest to physicists, mathematicians and/or experienced programmers.

- The central `Mesh` data-structure that representes the shapes we optimize is not well-documented. The code has some comments, but an explainer for how the data structure works hasn't been jotted down in ink yet.

- Similarly, the `Functional` objects like `Area`, `VolumeEnclosed`, `Nematic`, etc. need documentation on what disrete representations are used under the hood, etc.

- The `optimize` module uses various algorithms such as plain gradient descent (the `relax` method of the `Optimizer`), line searches (`linesearch`), the conjugate gradient algorithm (`conjugategradient`) are not documented. Some of the more [cutting edge optimization routines](https://github.com/Morpho-lang/morpho-optimize3) being developed in collaboration with Prof. James Adler's lab are documented in the form of [research papers](https://arxiv.org/abs/2310.04022v1), but a detailed account of the optimization module is not available.

- Morpho uses several integrators to carry out `AreaIntegral`s or `VolumeIntegrals`, etc. These are not documented.

- The Morpho language [grammar](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Grammars) is not written down, even in the devguide.
