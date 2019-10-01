import tensorflow as tf

print(tf.__version__)

loaded = tf.saved_model.load("D:\\Machine Learning\\distributed-traffic-analysis\\models\\")
print(list(loaded.signatures.keys()))  # ["serving_default"]