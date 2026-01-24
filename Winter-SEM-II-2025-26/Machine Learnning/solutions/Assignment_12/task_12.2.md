# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 12 Task 2

Reinforcement learning is a type of learning where an agent performs actions and does not get any examples of the control behavior that it should realize. The agent can only learn based on performance feedback.

Reinforcement learning is an unsupervised learning algorithm that involves an agent observing an environment and in every time step the agent obtains a state. Where for this state the agent selects an action and finally in the next time step he gets a reward. This reward is also referred to as the reinforcement.

The learning task is to execute actions in environment, observe results and learn action policy that maximizes rewards from any starting state.

The goal of the learning process is to maximize one of the following target functions: Episodic processes or continuous processes.

Episodic processes:

$$R = \frac{1}{T}\sum_{t=1}^{T} r_t$$

Continuous processes:

$$R = r_1 + \gamma r_2 + \gamma^2 r_3 + ... = \sum_{t=1}^{\infty} \gamma^t r_t, 0\lt \gamma \le 1$$

Extending the learning algorithms table from [task 10.2](/Winter-SEM-II-2025-26/Machine%20Learnning/solutions/Assignment_10/task_10.2.md):

Task: learning the appropriate policy so that the agent can maximize its rewards.

Experience: performance feedback

Performance: reward functions: Episodic or continuous

Algorithm: Markov Decision processes

Practical example: fully automated self-driving for automobiles
