# Assignment instructions

## Preliminaries

With this assignment you will implement locality-sensitive hashing (LSH) in
Spark. Before starting, make sure that you understand the following concepts:
1. Hash functions,
2. Jaccard distance,
3. Signature matrix,
4. LSH (bands and rows).

Important preliminary notes:

* The requested tasks, described below, are all evaluated with a test
  run with [pytest](http://pytest.org). Your assignment will be graded
  directly from the result of those tests, see details
  [here](./README.md). You may want to get familiar with pytest before
  you start.
  
* The tests contain examples of expected outputs that you may want to
  check in case the instruction below are unclear. Every detail in
  your answer counts! In particular, you should pay attention to the
  exact syntax of the expected output: add quotes around your answer
  and the tests won't pass!

* Your answers to the tasks below *must* be located in directory `answers`. 

## Dataset

We will re-use the dataset used in LA3, available at
https://archive.ics.uci.edu/ml/datasets/Plants and extracted from the
[USDA plant dataset](https://plants.usda.gov/java). This dataset lists
the plants found in US and Canadian states.

The dataset is available in `data/plants.data`, in CSV format. Every
line in this file contains a tuple where the first element is the name
of a plant, and the remaining elements are the states in which the
plant is found. State abbreviations are in `data/stateabbr.txt` for
your information. 

## 1. Data preparation

Our implementation of LSH will be based on RDDs.  As in the clustering
part of LA3, we will represent each state in the dataset as a dictionary of boolean
values with an extra key to store the state name. We call this dictionary 'state dictionary'.

### Task (identical to LA3 -- clustering)

Write a script that:
1. Creates an RDD in which every element is a dictionary representing a state with the following keys and values:

| Key    | Value |
|--------|------|
| `name` | abbreviation of the state|
| `<plant>` | 1 if `<plant>` occurs in the state, 0 otherwise|

2. Prints to file `<output_file>` the value associated with key `<key>` in the dictionary
representing state `<state>`.

You are strongly encouraged to use the RDD created here in the remainder of the assignment. 

### Required syntax

`data_preparation.py <data_file> <key> <state> <output_file>`

### Test

`tests/test_data_preparation.py`

## Prime numbers

To create signatures we need hash functions (see next task). To create
hash functions, we need prime numbers.

### Task

Write a function that returns the list of *n* consecutive prime
numbers greater or equal to *c*. The function will, for every integer
*x* between *c* and *c+n*, add *x* to the current list if *x* is
prime. A simple way to test if an integer *x* is prime is to check
that *x* is not a multiple of any integer lower or equal than
\sqrt {x}, that is, that *x % y* is not 0 for every *y* in *[2,
\sqrt{x}]*.

### Test

## Hash functions

We will generate hash
functions of the form h(x) = ax+b % p, where a and b are random
numbers and p is a prime number.

### Task

Write a function that takes a pair (*max*, *p*) and returns a hash
function h(x)=(ax+b)%p where *a* and *b* are random integers chosen
uniformly between 1 and *max*, using Python's random.randint.

### Test

## Signature Matrix

Write a function that takes (1) a state dictionary, as previously
defined, and (2) a list of hash functions generated using the previous function. 

The columns of the signature matrix will be computed independently.
That is, every state dictionary in the RDD will be mapped to its
signature.

#### Task

Write a script that computes the squared Euclidean
distance between two states. 

#### Required syntax

`distance2.py <data_file> <state1> <state2>`

#### Test

`tests/test_distance.py`

### Initialization 

#### Task

Write a script that:
1. Randomly picks `<k>` states randomly from the
array in `answers/all_states.py` (you may import or copy this array to
your code) using the random seed passed as argument and Python's
`random.sample` function.
2. Prints each selected state abbreviation on a different line.

In the remainder, the centroids of the kmeans algorithm must be
initialized using the method implemented here, perhaps using a line
such as: `centroids = rdd.filter(lambda x: x['name'] in
init_states).collect()`, where `rdd` is the RDD created in the data
preparation task.

#### Required syntax

`init.py <k> <random_seed>`

#### Test

`tests/test_init.py`

### First iteration

#### Task

Write a script that:
1. Assigns each state that appears in `data/stateabbr.txt` to its 'closest' class where 'closest' means 'the class corresponding to the centroid closest to the state according to the distance defined in the distance function task'. Centroids must be initialized as
in the previous task. Note that some states in the data set are not in `data/stateabbr.txt`: you must ignore them.
2. Prints the classes in alphabetical order: 
states must be ordered alphabetically within classes, and classes
must be sorted according to the alphabetical order of their first
state. Check `tests/first_iteration.txt` for formatting requirements.

#### Required syntax

`first_iter.py <data_file> <k> <random_seed>`

#### Test

`tests/test_first_iter.py`

### Complete kmeans

#### Task

Write a script that:
1. Assigns states to classes as in the previous task.
2. Updates the centroids based on the assignments in 1.
3. Goes to step 1 if the assignments have not changed since the previous iteration.
4. Prints classes as in the previous task but in an output file.

#### Required syntax

`kmeans.py <data_file> <k> <random_seed> <output_file>`

#### Test

`tests/test_kmeans.py`

### Visualization

Here is a visualization of the clustering obtained in the previous
task, obtained with R's 'maps' package (Canadian provinces, Alaska and
Hawaii couldn't be represented and a different seed than used in the tests was used). The classes seem to make sense from a
geographical point of view!

![kmeans result](https://users.encs.concordia.ca/~tglatard/teaching/big-data/winter-2018/images/states.png)
