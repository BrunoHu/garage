# Garage
This is a garage to store my handwrite algorithms. Some are data analyzing and also some toy algorithm code. Following are done.

## K-means Algorithm

[中文详细版](http://migdal-bavel.in/2015/09/20/%E7%94%A8python%E5%AE%9E%E7%8E%B0kmeans%E7%AE%97%E6%B3%95/)
This algorithm is famous and easy.

`kmeans.py` is the code file which only have the kmeans function.
`test_kmeans.py` is a test file for upper file. You could get a visual glance for this algorithm.
`test_kmeans.png` is a example graph for a overview.

#### args
* dataset

> This is the dataset which you want to find kmeans subset. The form is list of tuple point like `[(1, 2),(5.5, 6.5),(4.8998, 0, 6.311)]`.

* k=2

> This arg means the number of kmeans subset you want to divide. The default value is 2.

* demension=2

> This arg means the demensions of data you want to process. For example, if you set the demension=2,the function will regard [(1, 2, 3, 4), (1.44, 99.2, 100)] as [(1, 2), (1.44, 99.2)] to process.
*warning:* The value could not bigger than any tuple point length. You could not set demension=5 in the front example.

#### return

This function return the k-means centers and divided subsets in a list like `[centers, subsets]`.
The subsets is a list of sets like `[subset1, subset2, ..., subsetn]` and subset is the same form like dataset in args. In other world, subsets is a list of dataset and length is k.

## lianliankan game solution algorithm

[中文详细版](http://migdal-bavel.in/2015/09/26/%E8%AE%A9%E6%88%91%E4%BB%AC%E6%9D%A5%E7%A0%94%E7%A9%B6%E4%B8%80%E4%B8%8B%E7%A5%9E%E5%A5%87%E7%9A%84%E8%BF%9E%E8%BF%9E%E7%9C%8B/)

A BFS solution　of lianliankan.

You could try it just clone it and `python simple_lianliankan.py`.

It has a very simple commandline interface and all number just appear twice. You could enter number which you want to vanish to play this game.


## soduku game solution algorithm

[中文详细版](http://migdal-bavel.in/2016/02/14/%E6%95%B0%E7%8B%AC%E7%9A%84%E9%AB%98%E6%95%88%E6%B7%B1%E5%BA%A6%E6%90%9C%E7%B4%A2%E8%A7%A3%E6%B3%95/)

A kind of pruning DFS algorithm to solve suduku.

If we regard every grid in soduku as a position has 9 possible choice, we could easily have a raw idea of data structure -- 9 degree tree. Obviously it could be solved by DFS, but the depth and time will be monster. So we need to have a strantegy to cut off bad bypass.

We use a very simple strategy base on the only rule to pruning. That is when a grid was commited, the grids in same colume, same row and same block could not be that one.

So, after each time we get a step futher, we could get a specific number in a grid and we could use this try step to cut off many possibilities. That means the algorithm could be very fast.

txt files are the sample soduku. You could write your soduku and repalce the path. Then after xiu~, answer appears~

