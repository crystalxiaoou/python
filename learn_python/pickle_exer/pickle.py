try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name = 'Bob', age = 20, score = 88)

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
    f.close()

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    f.close()

print d