#from typing import Optional

def process_items(items : list[str], item1 : tuple[int, str, bytes], item2: set[bytes], dic_item: dict[str, int]):
    for item in items:
        print(item.center, item1[0], item2.add(2))

    for key, value in dic_item:
        print(key)
        print(value)

def learning_types(item: int|str ):
    print(item)

def say_hi(name: str|None = None):
    if name is not None:
        print(f'Hello {name}')
    else:
        print('Hello Mehrnaz lovers XD')

say_hi()