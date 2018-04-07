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
functions of the form `h(x) = (ax+b) % p`, where a and b are random
numbers and p is a prime number.

### Task

Write a function that takes a pair of integers (`max`, `p`) and returns a hash
function `h(x)=(ax+b)%p` where `a` and `b` are random integers chosen
uniformly between 1 and `max`, using Python's `random.randint`. Write a
script that:
1. initializes the random seed from `<seed>`,
2. generates a hash
function `h` from `<max>` and `<p>`,
3. prints the value of `h(x)`.

#### Required syntax

`hash.py <seed> <max> <p> <x>`

### Test

`tests/test_hash.py`

## 4. Hash functions

We will generate "good" hash functions using the generator in 3 and
the prime numbers in 2.

### Task

Write a script that:
1. creates a list of `<n>` hash functions where
the `ith` hash function is obtained using the generator in 3, defining
`<p>` as the `ith` prime number larger than `<max>` (`<p>` being
obtained as in 1),
2. prints the value of `h_i(x)`, where `h_i` is
the `ith` hash function in the list. The random seed must be initialized from `<seed>`.

#### Required syntax

`hash_list.py <seed> <max> <n> <i> <x>`

### Test

`tests/test_hash.py`



## 5. Min-hash signature matrix

We will now compute the min-hash signature matrix of the states. 

#### Task

Write a function that takes:
1. a state dictionary as defined in 1
(yes, a *dictionary*, not an RDD, this function will be used later to
map an RDD), and
2. a list of `<n>` hash functions generated as in
the previous task, setting `<max>` to the number of lines in
`<datafile>`.

The function must return a state signature dictionary
containing a `name` key, storing the state name, and a set of integer
keys storing the min-hash signature values for the `<n>` hash
functions. For instance, `sig[i]` will contain the min-hash signature
value for the `ith` hash function. `sig[i]` must be computed as the
minimum of {`h_i(j)`, `state[k]=1`, `k` is the `jth` key in `state`
(in alphabetical order)}, as in slide 28 of the lecture on LSH, where
`h_i` is the `ith` hash function in the list generated in the previous
task.

Apply this function to the RDD of dictionary states to create a
signature "matrix", in fact an RDD containing state signatures
represented as dictionaries. Write a script that prints
the element of this RDD corresponding to state '<state>' using function `pretty_print_dict` (provided in `answers`).

The random seed used to generate
the hash function must be initialized from `<seed>`, as previously.

#### Required syntax

`signatures.py <datafile> <seed> <n> <state>`

#### Test

`tests/test_signatures.py`

## 6. Hashing a band of a signature vector 

We will now hash the signature matrix in bands. All signature vectors,
that is, state signatures contained in the RDD computed in the
previous question, can be hashed independently. Here we compute the
hash of a band of a signature vector.  

#### Task

Write a script that, given the signature dictionary of state `<state>` computed from
`<n>` hash functions (as defined in the previous task), a particular
band `<b>` and a number of rows `<n_r>`:
1. constructs a signature
string for band `<b>` as the string representation (obtained with
`str`) of a dictionary `sig_dict` containing `<r>` keys defined as
`sig_dict[i]=sig_vect[i]` for i in `[b.n_r, (b+1).n_r[`,
2. prints the hash
of `sig_dict` using Python's built-in `hash` function.

The random seed must be initialized from `<seed>`, as previously.

#### Required syntax

`hash_band.py <datafile> <seed> <state> <n> <b> <n_r>`

#### Test

`tests/test_hash_band.py`

## 7. Hashing all the signature vectors 

We will now hash the complete signature matrix in bands. 

#### Task

Write a script that, given an RDD of state signature dictionaries
constructed from `n=<n_b>*<n_r>` hash functions (as in 5), a number of bands
`<n_b>` and a number of rows `<n_r>`:
1. maps each RDD element (using
`flatMap`) to a list of `((b, hash), state_name)` tuples where `hash`
is the hash of the signature vector of state `state_name` in band `b` as defined in 6. Note: it is not a triple, it is a pair.
2. groups the resulting RDD by key: states that hash to the same bucket for band `b` will appear together.
3. prints the buckets with more than 2 elements using the function in `pretty_print_bands.py`.

That's it, you have printed the similar items, in O(n)!


#### Required syntax

`hash_bands.py <datafile> <seed> <n_b> <n_r>`

#### Test

`tests/test_hash_bands.py`

## 8. Bonus: similar items for a given similarity threshold

The script written for the previous task takes `<n_b>` and `<n_r>` as
parameters while a similarity threshold `<s>` would be more useful.

#### Task

Write a script that prints the number of bands `<b>` and rows `<r>` to
be used with a number `<n>` of hash functions to find the similar
items for a given similarity threshold `<s>`. Your script should also
print `<n_actual>` and `<s_actual>`, the actual values of `<n>` and
`<b>` that will be used, which may differ from `<n>` and `<s>` due to
rounding issues. Printing format is found in `tests/test-get-b-and-r.txt`. 

Use the following relations:
* `r=n/b`
* `s^n=(1/b)^(1/r)`

Hint: Johann Heinrich Lambert (1728-1777) was a Swiss mathematician.

#### Required syntax

`get_b_and_r.py <n> <s>`

#### Test

`tests/test_b_and_r.py`

