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

## 2. Prime numbers

To create signatures we need hash functions (see next task). To create
hash functions, we need prime numbers.

### Task

Write a script that prints the list of `n` consecutive prime numbers
greater or equal to `c`. The script will print one number per line. A
simple way to test if an integer `x` is prime is to check that `x` is
not a multiple of any integer lower or equal than `sqrt(x)`. 

#### Required syntax

`primes.py <n> <c>`

### Test

`tests/test_primes.py`

## 3. Hash function generator

We will generate hash
functions of the form `h(x) = ax+b % p`, where a and b are random
numbers and p is a prime number.

### Task

Write a function that takes a pair of integers (`max`, `p`) and returns a hash
function `h(x)=(ax+b)%p` where `a` and `b` are random integers chosen
uniformly between 1 and `max`, using Python's `random.randint`. Write a
script that (1) initializes the random seed from `<seed>`, (2) generates a hash
function `h` from `<max>` and `<p>`, and (3) prints the value of `h(x)`.

#### Required syntax

`hash.py <seed> <max> <p> <x>`

### Test

`tests/test_hash.py`

## 4. Hash functions

We will generate "good" hash functions using the generator in 3 and
the prime numbers in 2.

### Task

Write a script that (1) creates a list of `<n>` hash functions where
the `ith` hash function is obtained using the generator in 3, defining
`<p>` as the `ith` prime number larger than `<max>` (`<p>` being
obtained as in 1), (2) prints the value of `h_i(x)`, where `h_i` is
the `ith` hash function in the list. The random seed must be initialized from `<seed>`.

#### Required syntax

`hash_list.py <seed> <max> <n> <i> <x>`

### Test

`tests/test_hash.py`



## 5. Min-hash signature matrix

We will now compute the min-hash signature matrix of the states. 

#### Task

Write a function that takes (1) a state dictionary as defined in 1
(yes, a *dictionary*, not an RDD, this function will be used later to
map an RDD), and (2) a list of `<n>` hash functions generated as in
the previous task. The function must return a state signature
dictionary containing a `name` key, storing the state name, and a set
of integer keys storing the min-hash signature values for the `<n>`
hash functions. For instance, `sig[i]` will contain the min-hash
signature value for the `ith` hash function. `sig[i]` must be computed
as the minimum of {`h_i(j)`, `state[j]=1`}, as in slide 28 of the
lecture on LSH, where `h_i` is the `ith` hash function in the list
generated in the previous task.

Apply this function to the RDD of dictionary states to
create a signature "matrix", in fact an RDD containing state
signatures represented as dictionaries. Write a script that collects
and prints the first `<n>` elements in this RDD.

#### Required syntax

`signatures.py <datafile> <seed> <n> <n>`

#### Test

`tests/test_signatures.py`

## 6. Hashing a band of a signature vector 

We will now hash the signature matrix in bands (I). 

#### Task

Write a script that, given a state signature dictionary (as defined in
the previous task), a band `<b>` and a number of rows `<r>`, (1)
constructs a signature string for band `<b>` as `str(sig_dict)`, where
`sig_dict` is a dictionary containing `<r>` keys defined as
`sig_dict[i]=sig_vect[i]` for i in [b*r, (b+1)*r[, (2) prints the hash
of `sig_dict` using Python's built-in `hash` function.

#### Required syntax

`hash_band.py <datafile> <seed> <state> <n>`

#### Test

`tests/test_hash_band.py`

## 7. Hashing all signature vectors 

We will now hash the signature matrix in bands (II). 

#### Task

Write a script that, given an RDD of state signature dictionary (as
defined previously), a number of bands `<b>` and a number of rows
`<r>`, (1) maps RDD elements to a list of `<b>` 'bucket dictionaries',
where the bucket dictionary of band `<i>` has a single key `sig_hash`
that equals the hash of the state signature dictionary for the `ith`
band (as defined in the previous task) and contains the abbreviation of the corresponding state (for instance `qc`), (2) collects and prints the first `<k>` elements in this RDD.

#### Required syntax

`hash_bands.py <datafile> <seed> <state> <n> <b> <r> <k>`

#### Test

`tests/test_hash_bands.py`

## 8. Merging hash buckets

We will now hash the signature matrix in bands (III). 

#### Task

Write a function `merge` that merges two hash buckets (as defined
previously) `x` and `y` in a hash bucket `z` such that `z[k]` is a
list containing all the elements in `x[k]` and all the elements in
`y[k]`, where `k` is a key of `x` or a key of `y`. Write a script that
takes the RDD produced in the previous task and (1) maps it, using the
`flatMap` transformation, to a set of (`b`, `buckets`) pairs, where
`b` is a band id and `buckets` are the buckets found in this band (as
defined previously), (2) reduces it by key (band id) and merges all
the buckets in a given band using function `merge`, (3) collects the first <k> elements and prints them.

#### Required syntax

`hash_bands_merge.py <datafile> <seed> <state> <n> <b> <r> <k>`

#### Test

`tests/test_hash_bands_merge.py`

## 9. Printing similar items

We will now hash the signature matrix in bands (IV).

#### Task

Write a script that prints the buckets that have more than 1 element,
for all bands. These are finally the similar items, and you got them
in O(n)!

#### Required syntax

`similar_items.py <datafile> <seed> <state> <n> <b> <r>`

#### Test

`tests/test_similar_items.py`

## 10. Bonus: similar items for a given similarity threshold

The script written for the previous task takes `<b>` and `<r>` as
parameters while a similarity threshold `<s>` would be more useful.

#### Task

Write a script that prints the similar items for a given similarity
threshold `<s>`.

Use the following relations:
* `r=n/b`, where `n` is the number of hash functions in the signature matrix and `b` is the number of bands.
* `s^n=(1/b)^(1/r)`

Hint: Johann Heinrich Lambert (1728-1777) was a Swiss mathematician.

#### Required syntax

`similar_items_s.py <datafile> <seed> <state> <n> <s>`

#### Test

`tests/test_similar_items_s.py`

