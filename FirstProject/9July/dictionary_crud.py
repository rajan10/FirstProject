import json

my_collection = {
    1: {"_id":1,"name":"John", "age":30},
    2: {"_id":2,"name":"Jani", "age":31},
    3: {"_id":3,"name":"Sita", "age":28}
}
class DictionaryAdd:
    def __init__(self, *data):
        self.my_dict = data
        self.new_key = self.max_key(my_collection)

    def max_key(self, my_collection):
        temp = 0
        for key in my_collection.keys():
            if key > temp:
                temp = key
        return temp
    def insert_many(self, my_collection):

        for item in self.my_dict:
            self.new_key += 1
            my_collection[self.new_key] = item
d1 = DictionaryAdd(
    {"_id":4,"name":"Samita", "age":27},
    {"_id":5,"name":"Julie", "age":20}
)
d1.insert_many(my_collection)
print(json.dumps(my_collection, indent=1))