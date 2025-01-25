```python
import json

class JsonManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_json_file()

    def read_json_file(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def write_json_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def find_by_id(self, id):
        for item in self.data:
            if item['id'] == id:
                return item
        return None

    def add_item(self, item):
        self.data.append(item)
        self.write_json_file()

    def update_item(self, id, new_item):
        for i, item in enumerate(self.data):
            if item['id'] == id:
                self.data[i] = new_item
                self.write_json_file()
                break
        else:
            print(f"No item found with id {id}")

    def remove_item(self, id):
        self.data = [item for item in self.data if item['id'] != id]
        self.write_json_file()

# Example usage
filename = "example.json"
manager = JsonManager(filename)

# Add items
items = [
    {"id": 1, "valor1": 1, "valor2": 2},
    {"id": 2, "valor1": 3, "valor2": 4},
    {"id": 3, "valor1": 5, "valor2": 6}
]

for item in items:
    manager.add_item(item)

# Search for an item by ID
id_to_search = 2
found_item = manager.find_by_id(id_to_search)

if found_item:
    print(f"Found item with id {id_to_search}:")
    print(json.dumps(found_item, indent=4))
else:
    print(f"No item found with id {id_to_search}")

# Update an item
updated_item = {"id": 2, "valor1": 100, "valor2": 200}
manager.update_item(2, updated_item)

# Remove an item
manager.remove_item(3)

# Print the final list of items
print("\nFinal list of items:")
print(json.dumps(manager.data, indent=4))
```
