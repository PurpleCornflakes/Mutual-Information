# The calculation of Mutual Info

It's not a trivial thing.
[Binning matters.](http://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#sphx-glr-auto-examples-cluster-plot-adjusted-for-chance-measures-py)

### how to correctly modify calculation of entropy?
![](./LSTM.png)

### scikit-learn

scikit-learn has 3 methods to calculate mutual entropy.

1. Adjusted_MI
2. Normalized_MI: I(X;Y)/sqrt(H(X)H(Y)) (I wrote the same one by myself.)
3. MI
Below is a simple case for discrete integer data
![](./MI_sklearn.png)

### how to bin properly? k-mean clustering?

![](./latex-image-1.png)
