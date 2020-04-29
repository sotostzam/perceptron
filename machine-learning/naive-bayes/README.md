# Naive Bayes

## Information

Naive Bayes classifiers are probabilistic classifiers using Bayes theorem to build a model on a given dataset. By using naive, we are refering to the strong independance among the features. This python implementation is showcasing a simple naive bayes model which can predict future data.

## Probabilistic model

![bayes](/images/bayes.png)

* P(Ck) is the prior probability of C occuring independantly.
* P(x) is the prior probability of x occuring independantly.
* P(Ck|x) is the posterior probability of Ck given x.
* P(x|Ck) is the likelihood that x occurs, given Ck.
