import numpy as np

# Constants used in the QLearning Agent
Q_ALGORITHM = 'Q'
Q_EPSILON = 0.4
Q_GAMMA = 0.9
Q_LEARNING_RATE = 0.1


class QLearningAgent:
    def __init__(self, action_size):
        self.action_size = action_size
        self.epsilon = Q_EPSILON
        self.gamma = Q_GAMMA
        self.learning_rate = Q_LEARNING_RATE
        self.q_table = {}

    def act(self, state):
        """
        Choose an action using the epsilon-greedy policy
        """
        chance = np.random.uniform(0, 1)
        if chance <= self.epsilon:
            return np.random.choice(self.action_size)

        else:
            if state not in self.q_table:
                self.q_table[state] = np.full(self.action_size, float('-inf'))
            return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        """
        Update the Q-value table based on the observed transition
        """
        if state not in self.q_table:
            self.q_table[state] = np.full(self.action_size, float('-inf'))
        if next_state not in self.q_table:
            self.q_table[next_state] = np.full(self.action_size, float('-inf'))

        old_q_value = self.q_table[state][action]
        if old_q_value == float('-inf'):
            new_q_value = reward
        else:
            max_q_next_state = np.max(self.q_table[next_state])
            if max_q_next_state == float('-inf'):
                max_q_next_state = 0
            new_q_value = old_q_value + self.learning_rate * (reward + self.gamma * max_q_next_state - old_q_value)
        self.q_table[state][action] = new_q_value
