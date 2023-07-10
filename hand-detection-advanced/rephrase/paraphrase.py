from parrot import Parrot
import torch
import warnings

warnings.filterwarnings("ignore")

# def random_state(seed):
#   torch.manual_seed(seed)
#   if torch.cuda.is_available():
#     torch.cuda.manual_seed_all(seed)

# random_state(1234)

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

def Paraphrase(input_phrase):
    phrases = parrot.augment(input_phrase=input_phrase)
    ret = []
    for p in phrases:
        ret.append(p[0])
    return phrases