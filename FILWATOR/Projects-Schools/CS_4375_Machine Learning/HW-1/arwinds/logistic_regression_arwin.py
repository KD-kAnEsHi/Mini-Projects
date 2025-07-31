# logistic_regression.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# personal and educational purposes provided that (1) you do not distribute
# or publish solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UT Dallas, including a link to http://cs.utdallas.edu.
#
# This file is part of Programming Assignment 1 for CS6375: Machine Learning.
# Nikhilesh Prabhakar (nikhilesh.prabhakar@utdallas.edu),
# Athresh Karanam (athresh.karanam@utdallas.edu),
# Sriraam Natarajan (sriraam.natarajan@utdallas.edu),
#
#
# INSTRUCTIONS:
# ------------
# 1. This file contains a skeleton for implementing a simple version of the 
# Logistic Regression algorithm. Insert your code into the various functions 
# that have the comment "INSERT YOUR CODE HERE".
#
# 2. Do NOT modify the classes or functions that have the comment "DO NOT
# MODIFY THIS FUNCTION".
#
# 3. Do not modify the function headers for ANY of the functions.
#
# 4. You may add any other helper functions you feel you may need to print,
# visualize, test, or save the data and results. 


## Karl Azangue (kka210001) and Aaron Fredericks (ajf220004)
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import pickle 


class SimpleLogisiticRegression():
    """
    A simple Logisitc Regression Model which uses a fixed learning rate
    and Gradient Ascent to update the model weights
    """
    def __init__(self):
        self.w = []
        pass

        
    def initialize_weights(self, num_features):
        #DO NOT MODIFY THIS FUNCTION
        w = np.zeros((num_features))
        return w

    def compute_loss(self,  X, y):
        """
        Compute binary cross-entropy loss for given model weights, features, and label.
        :param w: model weights
        :param X: features
        :param y: label
        :return: loss   
        """
        # INSERT YOUR CODE HERE
      
       # m = X.shape[0]  # Number of examples
        #y_pred = self.sigmoid(X @ self.w)  # Compute predictions
        #loss = -(1/m) * np.sum(y * np.log(y_pred + 1e-10) + (1 - y) * np.log(1 - y_pred + 1e-10))  # Avoid log(0) errors
        #return loss
        t,f = X.shape
        X = np.hstack((np.ones((t,1)),X))

        y_pred = self.sigmoid(X @ self.w)

        loss = -np.mean(y* np.log(y_pred + 1e-9) + (1-y) * np.log(1-y_pred + 1e-9))

        return loss
    
        #raise Exception('Function not yet implemented!')

    
    def sigmoid(self, val):

        """
        Implement sigmoid function
        :param val: Input value (float or np.array)
        :return: sigmoid(Input value)
        """
        return 1/ (1+ np.exp(-val))

        raise Exception('Function not yet implemented!')


    def gradient_ascent(self, w, X, y, lr):

        """
        Perform one step of gradient ascent to update current model weights. 
        :param w: model weights
        :param X: features
        :param y: label
        :param lr: learning rate
        Update the model weights
        """

        m = X.shape[0]
        y_pred = self.sigmoid(X @ w)
        gradient = (1/m) * (X.T @ (y-y_pred))
        w += lr *gradient
        return w
        # INSERT YOUR CODE HERE
   



    def fit(self,X, y, lr=0.1, iters=100, recompute=True):
        """
        Main training loop that takes initial model weights and updates them using gradient descent
        :param w: model weights
        :param X: features
        :param y: label
        :param lr: learning rate
        :param recompute: Used to reinitialize weights to 0s. If false, it uses the existing weights Default True

        NOTE: Since we are using a single weight vector for gradient ascent and not using 
        a bias term we would need to append a column of 1's to the train set (X)

        """
        # INSERT YOUR CODE HERE
        t,f = X.shape #of training examples(rows)  and features(columns)
        X = np.hstack((np.ones((t,1)),X)) #add bias


        if(recompute):
            self.w = self.initialize_weights(f + 1)  # Reinitialize the model weights
            pass

        losses = []

        for i in range(iters):
            self.w = self.gradient_ascent(self.w, X, y, lr)  #update weights
            pass

            if (i+1)%100 == 0:
                loss = self.compute_loss(X,y)
                losses.append(loss)
        return losses


    def predict_example(self, w, x):
        """
        Predicts the classification label for a single example x using the sigmoid function and model weights for a binary class example
        :param w: model weights
        :param x: example to predict
        :return: predicted label for x
        """
         # INSERT YOUR CODE HERE
        x = np.insert(x, 0, 1)  #  bias term
        
        return 1 if self.sigmoid(np.dot(w, x)) >= 0.5 else 0
    



    def compute_error(self, y_true, y_pred):
        """
        Computes the average error between the true labels (y_true) and the predicted labels (y_pred)
        :param y_true: true label
        :param y_pred: predicted label
        :return: error rate = (1/n) * sum(y_true!=y_pred)
        """
        # INSERT YOUR CODE HERE
        return np.mean(y_true != y_pred)




if __name__ == '__main__':

    # Load the training data
    M = np.genfromtxt('./data/monks-3.train', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    ytrn = M[:, 0]
    Xtrn = M[:, 1:]

    # Load the test data
    M = np.genfromtxt('./data/monks-3.test', missing_values=0, skip_header=0, delimiter=',', dtype=int)
    ytst = M[:, 0]
    Xtst = M[:, 1:]

    lr =  SimpleLogisiticRegression()
    
    #Part 1) Compute Train and Test Errors for different number of iterations and learning rates
    for iter in [10, 100,1000,10000]:
        for a in [0.01,0.1, 0.33]:
            print(f"Training with learn rate = {a} , itrations = {iter}")
            lr.fit(Xtrn, ytrn) #train the model

            ytrn_pred = np.array([lr.predict_example(lr.w, x) for x in Xtrn]) #predict on training data

            ytst_pred = np.array([lr.predict_example(lr.w, x) for x in Xtst]) 

            train_error = lr.compute_error(ytrn, ytrn_pred)
                
            test_error = lr.compute_error(ytst, ytst_pred)

            

            print(f"Train Error: {train_error:.4f}, Test Error: {test_error:.4f}\n")
            

    #Part 2) Retrain Logistic Regression on the best parameters and store the model as a pickle file
    #INSERT CODE HERE
    lr.fit(Xtrn, ytrn, lr=.33, iters=10000, recompute=True)

    # Code to store as pickle file
    netid = 'kka210001'
    file_pi = open('{}_model_1.obj'.format(netid), 'wb')  #Use your NETID
    pickle.dump(lr, file_pi)
    file_pi.close()



    #Part 3) Compare your model's performance to scikit-learn's LR model's default parameters 
    #INSERT CODE HERE
    sclr = LogisticRegression()
    sclr.fit(Xtrn, ytrn)
   
    ytrn_pred_sclr = sclr.predict(Xtrn)
    ytst_pred_sclr = sclr.predict(Xtst)

    #train_error_sclr = np.mean(ytrn != ytrn_pred_sclr)
    #test_error_sclr = np.mean(ytst != ytst_pred_sclr)

    train_error_sclr = lr.compute_error(ytrn, ytrn_pred_sclr)
    test_error_sclr = lr.compute_error(ytst, ytst_pred_sclr)

    # Although our model performance was somewhat close to that of sk-learn's model. sk-learn performed better as it had a less training 
    # (0.1639) and testing (0.1782) error. compared to our model whose training and testing error is (0.1803), and (0.1829) respectively.
    print(f"train skilearn model mean: {train_error_sclr:.4f}, test sklearn model mean: {test_error_sclr:.4f}")



    #Part 4) Plot curves on train and test loss for different learning rates. Using recompute=False might help
for a in [0.01, 0.1, 0.33]:

    lr.fit(Xtrn, ytrn)  # Initialize model

    train_losses = []
    test_losses = []

    iterations = list(range(100, 1100, 100))  # Every 100 iterations

    for i in range(10):  # Train in steps of 100 iterations
        losses = lr.fit(Xtrn, ytrn, lr=a, iters=1, recompute=True) 
        train_losses.extend(losses)

        # Compute test loss
        test_loss = lr.compute_loss(Xtst, ytst)
        test_losses.append(test_loss)

    # Plot curves
    plt.plot(iterations, train_losses, label="Train Loss")
    plt.plot(iterations, test_losses, label="Test Loss", linestyle="dashed")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title(f"Loss Curve for Learning Rate = {a}")
    plt.legend()
    plt.show()






# 1 - Where shoudl i write the results for part 1, should i print it or write a comment
# 2 - Check every part to make sure it is rigth
# 3 - Check the format of every part and make sure it is rigth