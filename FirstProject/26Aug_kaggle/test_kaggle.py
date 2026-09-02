import kagglehub

print("Kaggle authentication:")
print(kagglehub.whoami())

print("\nTesting public dataset download...")

path = kagglehub.dataset_download("yashdogra/cats-and-dogs")

print("\nSUCCESS!")
print("Dataset downloaded to:")
print(path)