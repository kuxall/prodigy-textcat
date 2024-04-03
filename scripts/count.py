import json

# Load the Prodigy dataset from file
with open("/home/kushal/Documents/textcat/datasets/categorization.jsonl", "r") as f:
    dataset = [json.loads(line) for line in f]

# Create a dictionary to store the answer counts
answer_counts = {"accept": 0, "ignore": 0, "reject": 0}

# Loop through each example in the dataset
for example in dataset:
    # Get the answer for the example
    answer = example["answer"]
    # Increment the count for the answer in the answer_counts dictionary
    answer_counts[answer] += 1

# Print the answer counts
for answer, count in answer_counts.items():
    print(f"{answer}: {count}")
