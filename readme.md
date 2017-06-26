in order to use virtualenv in python 3.6.... and since you have conda... us this command for environment

Training data is what we'll use to train our algo
Testing data is what we will use to verify that it is correct? Or testing data is data we need to use on the algorithm?

```
// Instead of virtualenv for py, python3 has its
// own version built in.... but since we are using anaconda....
// we can instead create an environment with conda
conda create -n env python=3.6

// Install scikit
conda install -n env scikit-learn

// Install deps for visual graph
conda install -n env -c conda-forge pydotplus
brew install graphviz
```

# Using the env

In order to use the conda environment you just created w/ conda install...

```
source activate env
```
