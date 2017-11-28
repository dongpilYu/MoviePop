import tensorflow as tf

tf.set_random_seed(486)

filename_queue = tf.train.string_input_producer(
    ['dataset.csv'], shuffle=False, name='filename_queue')
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)
record_defaults = [[0.], [0.], [0.], [0.], [0.]]
xy = tf.decode_csv(value, record_defaults=record_defaults)

train_x_batch, train_y_batch = tf.train.batch([xy[0:-1], xy[-1:]], batch_size=500)

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])
keep_prob = tf.placeholder(tf.float32)

W1 = tf.get_variable("W1", shape=[4, 128], initializer=tf.contrib.layers.xavier_initializer())
B1 = tf.Variable(tf.random_normal([128]), name="B1")
L1 = tf.nn.relu(tf.matmul(X, W1) + B1)
L1 = tf.nn.dropout(L1, keep_prob=keep_prob)

W2 = tf.get_variable("W2", shape=[128, 128], initializer=tf.contrib.layers.xavier_initializer())
B2 = tf.Variable(tf.random_normal([128]), name="B2")
L2 = tf.nn.relu(tf.matmul(L1, W2) + B2)
L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

W3 = tf.get_variable("W3", shape=[128, 128], initializer=tf.contrib.layers.xavier_initializer())
B3 = tf.Variable(tf.random_normal([128]), name="B3")
L3 = tf.nn.relu(tf.matmul(L2, W3) + B3)
L3 = tf.nn.dropout(L3, keep_prob=keep_prob)

W4 = tf.get_variable("W4", shape=[128, 128], initializer=tf.contrib.layers.xavier_initializer())
B4 = tf.Variable(tf.random_normal([128]), name="B4")
L4 = tf.nn.relu(tf.matmul(L3, W4) + B4)
L4 = tf.nn.dropout(L4, keep_prob=keep_prob)

W5 = tf.get_variable("W5", shape=[128, 1], initializer=tf.contrib.layers.xavier_initializer())
B5 = tf.Variable(tf.random_normal([1]), name="B5")
hypothesis = tf.matmul(L4, W5) + B5

cost = tf.reduce_mean(tf.square(hypothesis - Y))

learning_rate = 0.01
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for step in range(5001):
    x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_batch, Y: y_batch, keep_prob: 0.7})
    if step % 10 == 0:
        print(step, "Cost: ", cost_val)

coord.request_stop()
coord.join(threads)

saver = tf.train.Saver()
saver.save(sess, 'movie_model')
