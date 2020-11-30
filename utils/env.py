import gym
import gym_minigrid
import sys
sys.path.append("../gym-minigrid/")

def make_env(env_key, seed=None):
    print("env key is" , env_key)
    env = gym.make(env_key)
    env.seed(seed)
    return env
