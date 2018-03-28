import sys
import os

def pretty_print_bands(rdd):
    # rdd contains elements in the form ((band_id, bucket_id), [ state_names ])
    for x in sorted(rdd.collect()):
        if len(x[1]) < 2:
            continue # don't print buckets with a single element
        print("------------band {}, bucket {}-------------".format(x[0][0],x[0][1]))
        for y in sorted(x[1]):
            sys.stdout.write(y+" ")
        sys.stdout.write(os.linesep)
