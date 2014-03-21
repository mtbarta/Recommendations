#Recommendation Engine
###A WIP repo for a complete, incremental SVD algorithm in Python.

This is an implementation of an SVD algorithm with user/item regularization.
This implementation uses a MySQL database to hold the data.

##Usage

```Python
#train_data: (user, item, rating) tuple
algo = SVD_gradients(train, 943, 1682, rank = 10)
algo.train()
print algo.validate(test)
```

##References
http://www.csie.ntu.edu.tw/~r95007/thesis/svdnetflix/report/report.pdf

http://arek-paterek.com/ap_kdd_poster.pdf
