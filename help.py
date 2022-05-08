import matplotlib.pyplot as plt
import time

def step_gradient(X_train, Y_train, learning_rate, m,j):
    # Calculate new slope for jth feature
    m_j = 0
    n_data_pts = X_train.shape[0]
    N = len(m)
    for i in range(n_data_pts):
        # calculate the formula m1xi(1)+m2xi(2)+...
        x_i = X_train.iloc[i, :]
        y_i = Y_train.iloc[i]
        temp_sum = 0
        for k in range(N):
            temp_sum += m[k]*x_i[k]
        ### sub y_i from temp sum
        temp_sum = y_i - temp_sum
        ## complete formula
        m_j += (-2/n_data_pts) * (temp_sum) * x_i[j]
    # update m[j] and return
    m[j] = m[j] - (learning_rate*m_j)
    return m[j]

def gradient_descent(X_train, Y_train, learning_rate, num_iterations):
    # Start with random values for all m's
    m = [0]*(X_train.shape[1])
    m[-1] = 1 #c
    N = len(m)
    x_data = []
    y_data = []
    fig = plt.figure()
    for i in range(num_iterations):
        # For all iterations do the following
        for j in range(N):
            m[j] = step_gradient(X_train, Y_train, learning_rate, m,j)
        a = cost(X_train, Y_train, m)
        x_data.append(i)
        y_data.append(a)
        plt.plot(x_data,y_data,'*')
        print("Cost - : ", i, a)
        plt.draw()
        plt.pause(1e-17)
        time.sleep(0.1)
    return m

def cost(X_train, Y_train, m):
    # This will calculate mean square error
    cost = 0
    n_data_pts = len(X_train)
    N = len(m)
    for i in range(n_data_pts):
        x_i = X_train.iloc[i, :]
        y_i = Y_train.iloc[i]
        temp_sum = 0
        for k in range(N):
            temp_sum += m[k]*x_i[k]
        temp_sum = y_i - temp_sum
        cost += (1/n_data_pts) * ((temp_sum)**2)
    return cost

num_iterations = 10
learning_rate = 0.01
m = gradient_descent(x_train, y_train, learning_rate, num_iterations)
print(m)