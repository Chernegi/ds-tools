# data science tools

<details>
<summary>tSNE and PCA algorythms</summary>
<!--All you need is a blank line-->

    +
        + t-SNE algorythm (t-distributed Stochastic Neighbor Embedding)
        + PCA - Principal Component analysis
        + https://www.datacamp.com/community/tutorials/introduction-t-sne
        + https://habr.com/ru/company/ods/blog/325654/
        + is a non-linear technique for dimensionality reduction that is particularly well suited for the visualization of high-dimensional datasets. It is extensively applied in image processing, NLP, genomic data and speech processing. To keep things simple, here’s a brief overview of working of t-SNE:
    + The algorithms starts by calculating the probability of similarity of points in high-dimensional space and calculating the probability of similarity of points in the corresponding low-dimensional space. The similarity of points is calculated as the conditional probability that a point A would choose point B as its neighbor if neighbors were picked in proportion to their probability density under a Gaussian (normal distribution) centered at A. It then tries to minimize the difference between these conditional probabilities (or similarities) in higher-dimensional and lower-dimensional space for a perfect representation of data points in lower-dimensional space. To measure the minimization of the sum of difference of conditional probability t-SNE minimizes the sum of Kullback-Leibler divergence of overall data points using a gradient descent method.
</details>

<details>
<summary>data visualisation tools</summary>
<!--All you need is a blank line-->

    + markdown list 1
        + nested list 1
        + nested list 2
    + markdown list 2
</details>


