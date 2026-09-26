import subprocess

pipelines = [
    "pipelines/raw_to_bronze.py",
    "pipelines/bronze_to_silver.py",
    "pipelines/silver_to_gold.py"
]

for pipeline in pipelines:
    print("\n" + "=" * 60)
    print(f"Running: {pipeline}")

    result = subprocess.run(["python" , pipeline])

    if result.returncode != 0:
        print(f"\n Pipeline Failed: {pipeline}")
        break

    print(f" Pipeline completed: {pipeline}")
else:
    print("\n" + "=" * 60)
    print(" All pipelines completed successfully!")
    print("=" * 60)