from tqdm import tqdm
from tqdm import trange


class Models_Params:
     def __init__(self, args, version, policy_loss, value_loss, optim, lr, game_params, mean_score=0):
        self.params = args
        self.version = version
        self.policy_loss = policy_loss
        self.value_loss = value_loss
        self.optim = optim
        self.lr = lr
        self.mean_score = mean_score
        self.game_params = game_params

    
