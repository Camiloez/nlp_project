params = {
    'epochs': 50, # Épocas
    'emb_sz' :300, #tamaño embedding
    'k' : 4, #ancho kernel para CNN
    'nh' : 600, #Neuronas ocultas
    'nl' : 4, # Número de capas
    'downbot' : 20, # in the bottleneck layers, how much to decrease channel depth
    'batch_size': 20, #Tamaño del batch para DataLoader (está restringido por el tamaño de la GPU)
    'lr' : 1, #learning rate
    'mom': 0.95, #momentum
    'wd': 5e-5, #weight-decay. Solo sirve si opttype==sgd
    'nesterov': True, #Nesterov momentum. Solo sirve si if opttype==sgd
    'grad_clip': 0.07, #gradient clipping value. Set to 0 for no effect. See nn.utils.clip_grad_value_
    'opttype': 'sgd', #adam, sgd
    'use_gpu': True, #Si se usa o no GPU
}
