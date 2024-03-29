#!python
from utils import time_it
from linkedlist import LinkedList

class HashTable(object):
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['\nBucket {!r}: {!r}'.format(i, bucket) for i, bucket in enumerate(self.buckets)]
        # items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '\n}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __iter__(self):
        for bucket in self.buckets:
            for item in bucket.items():
                yield item

    # @time_it
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    # @time_it
    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(bl) or O(n) loops through all buckets and all items in the buckets"""
        # Collect all keys in each bucket
        all_keys = []
        for items in self:
            all_keys.append(items[0])
        return all_keys

    # @time_it
    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(bl) or O(n) loops through all buckets and all items in the buckets"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for item in self:
            all_values.append(item[1])
        return all_values

    # @time_it
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(bl) or O(n) loops through all buckets and all items in the buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    # @time_it
    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(1) Only one return constant time"""
        return self.count

    # @time_it
    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(l) loops through average number of items in buckets linked list"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket._find(lambda item: item[0] == key)
        if item is not None:
            return True
        return False

    # @time_it
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(l) loops through average number of items in buckets linked list"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket._find(lambda item: item[0] == key)
        if item is not None and item.data[0] == key:
            return item.data[1]
        raise KeyError('Key not found: {}'.format(key))

    # @time_it
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(l) loops through average number of items in buckets linked list"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket_id = self._bucket_index(key)
        bucket = self.buckets[bucket_id]
        exists = self.contains(key)
        new_item = key, value
        # print("Exists:", exists)
        if not exists:
            # print("adding item: ", new_item)
            bucket.append(new_item)
            self.count += 1
        else:
            # print("\n\n----Changeing item----")
            old_item = bucket._find(lambda item: item[0] == key).data
            # print("old_item", old_item)
            # print("new_item", new_item)
            bucket.replace(old_item, new_item)
        # print("bucket", bucket_id, "has: ", bucket)

    # @time_it
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(l) loops through average number of items in buckets linked list"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_id = self._bucket_index(key)
        bucket = self.buckets[bucket_id]
        exists = self.contains(key)
        if exists:
            print("Count after Delete: ",self.count)
            self.count -= 1
            return bucket.delete(bucket._find(lambda item: item[0] == key).data)
        raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\n------Testing set:------')
    for key, value in [('I', 1), ('V', 5), ('X', 9), ('X', 10)]:
    # for key, value in [('X', 9), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    get_implemented = True
    if get_implemented:
        print('\n------Testing get:------')
        for key in ['I', 'V', 'X']:
            value = ht.get(key)
            print('get({!r}): {!r}'.format(key, value))

        print('contains({!r}): {}'.format('X', ht.contains('X')))
        print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\n------Testing delete:------')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
