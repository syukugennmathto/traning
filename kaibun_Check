from typing import Any, Iterable

def is_palindrome(obj: Any) -> bool:
    if isinstance(obj, int):
        obj = str(obj)
    elif not isinstance(obj, Iterable):
        raise TypeError("非イテラブル型は対応していません")

    obj_list = list(obj)
    return obj_list == obj_list[::-1]
