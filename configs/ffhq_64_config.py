config = {}
config["batch_size"] = 64          # input batch size for training (default: 64)
config["epochs"] = 100             # number of epochs to train (default: 10)
config["no_cuda"] = False         # disables CUDA training
config["seed"] = 1265
config["image_size"] = 64
config["log_interval"] = 1     # how many batches to wait before logging training status
config["learning_rate"] = 1e-3
config["momentum"] = 0.1
config["gamma"] = 0.99
config["weight_decay"] = 0.0

config["num_hiddens"] = 128
config["num_residual_layers"] = 2
config["num_residual_hiddens"] = 32
config["num_filters"] = 64
config["embedding_dim"] = 64
config["num_embeddings"] = 512
config["num_channels"] = 3
config["data_set"] = "FFHQ"
config["representation_dim"] = 17
config["commitment_cost"] = 0.25
config["decay"] = 0.99

config["num_categories"] = config["num_embeddings"]
config["prior_start"] = 0