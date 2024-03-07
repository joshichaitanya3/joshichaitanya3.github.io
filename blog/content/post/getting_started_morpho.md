+++
title = "Getting started with Morpho development"
date = 2024-03-06
[taxonomies]
categories = ["code"]
tags = ["open-source"]
[extra]
math = true
+++

_As a postdoctoral scholar, I started working on [Morpho](https://github.com/Morpho-lang/morpho) in August 2021. At the time, I had little experience in software development. I **wanted** to contribute to Morpho, understand how it works, and in general improve it. Not having a background in software engineering, it took me a while to learn things on my own. The hope with this blog post is that if you find yourselves at a similar juncture, it should kickstart your exploration into Morpho much quicker._

## What is Morpho?

Morpho is an open-source, light-weight object-oriented programming environment {{ fn(num=1) }} for solving optimization problems in soft matter physics and beyond. You can think of it as a more modern [Surface Evolver](https://en.wikipedia.org/wiki/Surface_Evolver) --- we use simplicial meshes (and fields defined on them as well, unlike Surface Evolver) and perform direct optimization on the vertices, connectivities and field values. The scripting language can be used to write arbitrary programs like in Python, but the main horse-power comes from data-structures implemented in C. Oh, yes, Morpho itself is written in C.

## What can I find the source code?

The source code is hosted on GitHub at [Morpho-lang/morpho](https://github.com/Morpho-lang/morpho). The code is fully open-source and is licensed under the MIT License. This means that it is free to use and modify. If you are not familiar with GitHub, it is a platform for hosting and maintaining code collaboratively. It is a great place to learn about version control, code review, and other best practices in software development. The [CONTRIBUTING.md](https://github.com/Morpho-lang/morpho/blob/main/CONTRIBUTING.md) file in the repository documents guidelines and avenues for contributing to Morpho. With this series of blog posts, I hope to provide additional pointers and details that were not obvious to me when I started.

## Where can I find documentation?

Morpho ships with an extensive User Manual, that is currently hosted on the main GitHub repository. I am [converting it to a website](../morpho-manual-mdbook/) to provide additional accessibility. This would _also_ be a great avenue to contribute to Morpho!

In addition to the User Manual, which is meant for end-users, Morpho also provides a [developer's guide](https://github.com/Morpho-lang/morpho-devguide) which is a great (in progress) reference for Morpho internals. (See [below](#future-posts) for a collection of things I hope to write about that is not covered in the developer's guide.)

## Are there any language tools available?

Since the language is in its early stage, there are no language servers or linters available. However, there is a [syntax highlighting extension for Morpho](https://marketplace.visualstudio.com/items?itemName=mattsep.morpho) for the Visual Studio Code editor {{ fn(num=2) }}. This turns a code like this

![Sample Morpho code without syntax highlighting](/images/no-highlight.png)

to like this:

![Sample Morpho code with syntax highlighting](/images/highlight.png)

This is a great tool to have if you are writing Morpho code, and as such, I would recommend using Visual Studio Code for writing Morpho code for the time-being.

## How is a language like Morpho invented?

A great reference is the book Crafting Interpreters by Robert Nystrom, which is cited in the [preprint paper describing Morpho](https://doi.org/10.48550/arXiv.2208.07859). The best thing? You can [read the book online](http://craftinginterpreters.com/) on his website, for free! 

The book walks the reader through the process of writing an interpreter for a language called Lox. It showcases two implementations of the interpreter, one in Java (easier to write, focusing on concepts) and the other in C (faster, focusing on performance). Morpho is similar to the C implementation of Lox, but with a lot of additional features and certain implementation differences (these also would be great to document!). 

## Future posts

Here are a bunch of things that I would love if we get documentation on. They are in no particular order, and might be of interest to physicists, mathematicians and / or experienced programmers. I am hoping to write some of these on my own.

- The central `Mesh` data-structure that representes the shapes we optimize.

- Similarly, the `Functional` objects like `Area`, `VolumeEnclosed`, `Nematic`, etc. and their disrete representations used under the hood.

- The various optimization algorithms used by the `optimize` module (such as plain gradient descent, line searches and the conjugate gradient algorithm). 

- The integrators used to carry out `AreaIntegral`s or `VolumeIntegrals`, etc. 

- The `graphics` module that is used to visualize the shapes and fields.

- The Morpho language [grammar](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Grammars).

If any of these topics interest you, or you want to write about them, please reach out to me on the GitHub repository!

1. {{ fnt(num=1,
          footnote="It can be thought of as a domain-specific language.") 
    }}

2. {{ fnt(num=2,
          footnote="This is developed by my friend Matthew Peterson, who is an alumni of Tufts and a super-early user of Morpho.") }}
