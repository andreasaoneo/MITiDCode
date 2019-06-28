import tensorflow as tf
tf.reset_default_graph()
from tensorflow.keras.datasets import mnist
import random
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)

color_channels = 1
image_height = 28
image_width = 28


class CNN:
    def __init__(self, image_height, image_width, channels, num_classes):
        self.input_layer = tf.placeholder(dtype=tf.float32, shape=[None, image_height, image_width, channels], name="inputs")
        conv_layer_1 = tf.layers.conv2d(self.input_layer, filters=32, kernel_size=[2, 2], padding="same", activation=tf.nn.relu)
        pooling_layer_1 = tf.layers.max_pooling2d(conv_layer_1, pool_size=[2, 2], strides=2)
        flattened_pooling = tf.layers.flatten(pooling_layer_1)
        dense_layer = tf.layers.dense(flattened_pooling, 1024, activation=tf.nn.relu)
        dropout = tf.layers.dropout(dense_layer, rate=0.4, training=True)
        outputs = tf.layers.dense(dropout, num_classes)

        self.choice = tf.argmax(outputs, axis=1)
        self.probability = tf.nn.softmax(outputs)
        self.labels = tf.placeholder(dtype=tf.float32, name="labels")
        self.accuracy, self.accuracy_op = tf.metrics.accuracy(self.labels, self.choice)
        one_hot_labels = tf.one_hot(indices=tf.cast(self.labels, dtype=tf.int32), depth=num_classes)
        self.loss = tf.losses.softmax_cross_entropy(onehot_labels=one_hot_labels, logits=outputs)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.066666)
        self.train_operation = optimizer.minimize(loss=self.loss, global_step=tf.train.get_global_step())

# RUNNING the CNN

steps = 10000
batch_size = 16
x_train = (x_train.reshape(-1, image_height, image_width, 1))/255
test_img = x_test[random.randint(0, 9)]
plt.imshow(test_img)
plt.show()
cnn = CNN(image_height, image_width, color_channels, 10)
test_img = (test_img.reshape(-1, 28, 28, 1))/255
with tf.Session() as sess:
    checkpoint = tf.train.get_checkpoint_state(path)
    saver.restore(sess, checkpoint.model_checkpoint_path)
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    # Create a saver.
    saver = tf.compat.v1.train.Saver()
    # Launch the graph and train, saving the model every 1,000 steps.
    sess = tf.compat.v1.Session()
    step = 0
    while step < steps:
        print(sess.run((cnn.train_operation, cnn.accuracy_op), feed_dict = {cnn.input_layer:x_train[step:step+batch_size], cnn.labels:y_train[step:step+batch_size]}))
        step += batch_size
    print(sess.run(cnn.choice, feed_dict = {cnn.input_layer:test_img}))

