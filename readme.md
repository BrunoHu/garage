#Garage
This is a garage to store my handwrite algorithms, especiall for data analysis. Following are done.

## K-means Algorithm

This algorithm is famous and easy.
`kmeans.py` is the code file which only have the kmeans function.
`test_kmeans.py` is a test file for upper file. You could get a visual glance for this algorithm.

*args*
> dataset

This is the dataset which you want to find kmeans subset. The form is list of tuple point like `[(1, 2),(5.5, 6.5),(4.8998, 0, 6.311)]`.

> k=2

This arg means the number of kmeans subset you want to divide. The default value is 2.

> demension=2

This arg means the demensions of data you want to process. For example, if you set the demension=2,the function will regard [(1, 2, 3, 4), (1.44, 99.2, 100)] as [(1, 2), (1.44, 99.2)] to process.
*warning:* The value could not bigger than any tuple point length. You could not set demension=5 in the front example.

*return*
This function return the k-means centers and divided subsets in a list like `[centers, subsets]`.
The subsets is a list of sets like `[subset1, subset2, ..., subsetn]` and subset is the same form like dataset in args. In other world, subsets is a list of dataset and length is k.
