class CubeIterator:
    def __init__(self, max_cube_value):
        self.max_cube_value=max_cube_value
        self.current_root_value=0
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_root_value>=self.max_cube_value:
            raise StopIteration
        cube_value=self.current_root_value ** 3
        self.current_root_value=self.current_root_value+1
        return cube_value

for cube in CubeIterator(5):
    print(cube)