# Getting started

Install Anaconda w/ Brew

```
brew cask install anaconda
```

Anaconda acts like virtualenv, and with the advent of Py3... there is technically
'no more' virtualenv as it is baked into the language.

```
# create an environment with conda
conda create -n env python=3.6

# Install scikit
conda install -n env scikit-learn

# Install deps for visual graph
conda install -n env -c conda-forge pydotplus
brew install graphviz
```

# Using the env

In order to use the conda environment you just created w/ conda install...

```
source activate env
```
