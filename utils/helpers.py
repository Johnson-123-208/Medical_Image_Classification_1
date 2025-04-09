# import os
# from kaggle.api.kaggle_api_extended import KaggleApi

# def download_kaggle_dataset(dataset: str, path: str = "data"):
#     kaggle_json_path = os.path.expanduser("~/.kaggle/kaggle.json")
    
#     if not os.path.exists(kaggle_json_path):
#         raise FileNotFoundError(
#             "❌ Kaggle API key not found. Please place kaggle.json in ~/.kaggle/"
#         )
    
#     print("📦 Authenticating Kaggle API...")
#     api = KaggleApi()
#     api.authenticate()
    
#     print(f"⬇️ Downloading '{dataset}' to '{path}' ...")
#     api.dataset_download_files(dataset, path=path, unzip=True)
#     print("✅ Download complete.")
