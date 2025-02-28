from datasets import load_dataset

data = load_dataset("MapEval/MapEval-Textual", split=[f"test[{k}%:{k+10}%]" for k in range(0, 100, 20)])

first_dataset = data[0]
for i in range(10):
    print(f"\n=== Sample {i+1} ===")
    print("----- ----- Context ----- -----")
    print(f"Context: {first_dataset[i]['context']}")
    print("----- ----- Question ----- -----")
    print(f"Question: {first_dataset[i]['question']}")