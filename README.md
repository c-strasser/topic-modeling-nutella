# topic-modeling-nutella
This project deals with identifying frequent topics expressed by French-speaking consumers on social media in posts about the product 'Nutella'.

The problem of 'topic modeling' has beem tackle with the widely used LDA algorithm.

The LDA algorithm and the process of cleaning the social posts has been coded in [utils](./utils/). These functionalities have been [unit-tested](./unit_tests/).

The analysis and explanation of the project are to be found in a [notebook](./analysis.ipynb)


## Dependencies
- [gensim](https://radimrehurek.com/gensim/)
- [Tree Tagger software](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)
- [treetaggerwrapper package](http://treetaggerwrapper.readthedocs.io/en/latest/)


## How to get started
- After cloning the repo, create a folder 'tree_tagger' next to your copy of the repo
- Install the tree tagger software in this folder
- Install the other two dependencies	
