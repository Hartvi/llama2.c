import subprocess

# Base command with a placeholder for train_method
base_command = [
    "python", "train.py",
    "--out_dir=outmini",
    "--batch_size=128",
    "--max_seq_len=512",
    "--gradient_accumulation_steps=1",
    "--vocab_source=custom",
    "--vocab_size=512",
    "--dim=64",
    "--n_layers=5",
    "--n_heads=8",
    "--n_kv_heads=4",
    "--multiple_of=4",
    "--learning_rate=1e-3",
    "--dropout=0.05",
    "--weight_decay=0.01",
    "--max_iters=50",
    "--beta2=0.99",
    "--warmup_iters=3",
    "--eval_interval=3",
    "--eval_iters=10",
    "--n_outputs=3"
]

# Run the command with train_method values from 0 to 4
for i in range(0,5):
    command = base_command + [f"--train_method={i}"]
    print(f"Running command with train_method={i}...")
    subprocess.run(command)
