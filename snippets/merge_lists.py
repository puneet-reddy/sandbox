#!/usr/bin/env python

def merge_lists(data):
    '''
    Trying to achievel O(n*log(n)) time complexity.
    I believe this should be possible but have no clue how exactly (-_-)
    '''
    bins = list(range(len(data)))
    nums = dict()

    data = [set(datum) for datum in data]
    for r, row in enumerate(data):
        for num in row:
            if num not in nums:
                nums[num] = r
                continue
            else:
                dest = locatebin(bins, nums[num])
                if dest == r:
                    continue
                elif dest > r:
                    dest, r= r, dest
                data[dest].update(data[r])
                data[r] = None
                bins[r] = dest
                r = dest

    have = [m for m in data if m]
    print(len(have))
    return have

def locatebin(bins, n):
    while bins[n] != n:
        n = bins[n]
    return n