import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
    print("I will use GPU: ", torch.cuda.get_device_name(0))
#Just testing with .py script if my CUDA instalation was successfull:)
