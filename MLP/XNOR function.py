import numpy as np

W1 = np.random.rand(3 , 2)
W2 = np.random.rand(2 , 2)
W3 = np.random.rand(2 , 1)

print('w1 befor traning :', W1)
print('w2 befor traning :', W2)
print('w3 befor traning :', W3)

x = np.array([[0 , 0 , 1] , [1 , 0 , 1] , [0 , 1 ,1] , [1 , 1 , 1]])
y = np.array([1 , 0 , 0 , 1])
learningrate = 0.05

def relu(input):
    return np.where(input >0  , input , 0)

def drelu(input):
    return np.where(input>0 , 1 , 0)

for i in range(10000):
    for input in range(len(x)) : 
        firstlayer = relu(x[input].dot(W1))
        secondlayer = relu(firstlayer.dot(W2))
        yhat = secondlayer.dot(W3)
        error = y[input] - yhat
        delta3 = error
        delta2 = drelu(relu(x[input].dot(W1)).dot(W2)) * (delta3 * W3.T)
        delta1 = drelu(x[input].dot(W1)) * (delta2.dot(W2.T))
        W3 = W3 + learningrate * (delta3 *relu(relu(x[input].dot(W1)).dot(W2)))[: , np.newaxis]
        W2 = W2 + learningrate * ((x[input].dot(W1))[: , np.newaxis].dot(delta2))
        W1 = W1 + learningrate * (x[input][: , np.newaxis].dot(delta1))


print('w1 after traning :', W1)
print('w2 after traning :', W2)
print('w3 after traning :', W3)

for input in range(len(x)) : 
    print(relu(relu(x[input].dot(W1)).dot(W2)).dot(W3))



