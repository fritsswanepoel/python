# python
General python projects


##photo-to-sketch
A script to take an image and convert it into a pencil sketch using openCV

sample folder shows an example for a lighthouse - low res to load to repo

##text-graph-generator
Takes a .txt file as input and converts into a graph (with curved edges thanks to https://github.com/beyondbeneath/bezier-curved-edges-networkx). The idea it to take unique word pairs and use those to build up the edges from the first word to the last word you can reach from it in the text. Each word that follows the first word anywhere in the text will be the first set of nodes connected to and so on with no repeats.

So a story which is so-so and which has no story would become:

so  > a     > story > which X
                    > would > become    X
    > so    X
    > and   > which > is    > so
                    > has   > no        > story

There is both a full graph image and individual images produced. The individual images can then be animated to create quite beautiful sequences - I'd attempted to do the animation in Python but ultimately could not get that to work and used other tools to do that.
