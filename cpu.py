import torch

def inquire_gpus():
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        print(f"Number of GPUs available: {num_gpus}\n")
        
        for i in range(num_gpus):
            gpu_name = torch.cuda.get_device_name(i)
            gpu_capability = torch.cuda.get_device_capability(i)
            gpu_memory = torch.cuda.get_device_properties(i).total_memory / (1024**3)
            
            print(f"GPU {i + 1}:")
            print(f"  Name: {gpu_name}")
            print(f"  Compute Capability: {gpu_capability}")
            print(f"  Total Memory: {gpu_memory:.2f} GB\n")
    else:
        print("No GPUs are available on this system.")

if __name__ == "__main__":
    inquire_gpus()
