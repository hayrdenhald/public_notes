#!/usr/bin/env python
#
#
#
import sys
from typing import List, Tuple


def main():
    test_true = "Here comes inline code: `print('hello there')`, and this is where it ends `True != False`."
    test_false = "Here comes inline code: print('hello there'), and this is where it ends."
    print(convert_inline_code_to_html(test_true))
    print(convert_inline_code_to_html(test_false))


def encapsulate_text_in_code_tag(text: str) -> str:
    return f'<code="inline-code">{text}</code>'


def is_inline_code_symbol(char: str) -> bool:
    return char == '`'


def inline_code_indices(text: str) -> Tuple[bool, List[int]]:
    result = []
    gather = ()
    inside_code_block = False
    for idx, char in enumerate(text):
        if is_inline_code_symbol(char):
            if inside_code_block:
                inside_code_block = False
                gather = (gather[0], idx)
                result.append(gather)
                gather = ()
            else:
                gather = (idx, 0)
                inside_code_block = True
    return result


def convert_inline_code_to_html(text: str) -> str:
    indices = inline_code_indices(text)
    assert len(indices) % 2 == 0

    if indices:
        prev = 0
        result = []
        for (start, stop) in indices:
            result.append(text[prev:start])
            result.append(encapsulate_text_in_code_tag(
                text[start + 1:stop])
            )
            prev = stop + 1
        result.append(text[prev:])
        return ''.join(result)
    else:
        return text


if __name__ == "__main__":
    sys.exit(main())
