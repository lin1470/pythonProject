import tensorflow as tf
import pandas as pd
import numpy as np
# 读数据
data = pd.read_csv('wine.data',header=None)

# 分为train和target
target = data[0]
train = data.drop(0,axis=1)

# Z-score规范化feature,离散化分类
means = train.mean()
stds = train.std()
x = (train-means)/stds
y = pd.get_dummies(target)


# 打乱数据集,10个测试样例
mask = np.random.permutation(x.shape[0])
x_train = x.iloc[mask[10:]]
y_train = y.iloc[mask[10:]]
x_test = x.iloc[mask[:10]]
y_test  = y.iloc[mask[:10]]


X = tf.placeholder('float64',[None,x_train.shape[1]])
y_ = tf.placeholder('float64',[None,3])

# 第一层网络，有32个隐含层，sigmoid输出
W1 = np.random.normal(size=[x_train.shape[1],32])
b1 = np.random.normal(size=[1,32])
W1 = tf.Variable(W1)
b1 = tf.Variable(b1)
a1 = tf.matmul(X,W1) + b1
z1 = tf.sigmoid(a1)

# 第二层网络，有32个隐含层，sigmoid输出
W2 = np.random.normal(size=[32,32])
b2 = np.random.normal(size=[1,32])
W2 = tf.Variable(W2)
b2 = tf.Variable(b2)
a2 = tf.matmul(z1,W2) + b2
z2 = tf.sigmoid(a2)

# 有3个输出层，softmax输出
W3 = np.random.normal(size=[32,3])
b3 = np.random.normal(size=[1,3])
W3 = tf.Variable(W3)
b3 = tf.Variable(b3)
a3 = tf.matmul(z2,W3) + b3
z3 = tf.nn.softmax(a3)

# loss函数选用交叉熵
loss =tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=z3)
# 数据量不大，使用全局梯度下降优化
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

# 训练3万次
for i in range(30000):
    sess.run(optimizer,feed_dict={y_:y_train,X:x_train})

# 计算训练集上准确率
print(np.mean(np.argmax(sess.run(z3,feed_dict={X:x_train}),axis=1)+1 == target.iloc[mask[10:]]))
# 计算测试集上准确率
print(np.mean(np.argmax(sess.run(z3,feed_dict={X:x_test}),axis=1)+1 == target.iloc[mask[:10]]))
