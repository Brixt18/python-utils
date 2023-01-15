# Library for text and datetime processing in Python, and other utils functions

This library contains a set of functions that perform different tasks related to text and datetime processing in Python. The functions are:

- `get_text_or_empty(text: str, strip: bool = False) -> str`: This function receives a text string and an optional flag strip that indicates whether whitespaces should be removed from the beginning and end of the string. If the string is empty or only contains whitespaces, the function returns an empty string. Otherwise, it returns the string with removed whitespaces if the strip flag is true, or the original string if it is false.

- `get_text_or_none(text: str, strip: bool = False) -> Union[str, None]`: This function receives a text string and an optional flag strip that indicates whether whitespaces should be removed from the beginning and end of the string. If the string is empty or only contains whitespaces, the function returns None. Otherwise, it returns the string with removed whitespaces if the strip flag is true, or the original string if it is false.

- `strip_dict_fields(data: dict) -> dict`: This function receives a dictionary and removes whitespaces from the beginning and end of all string values in the dictionary.

- `strip_list_fields(data: list) -> list`: This function receives a list and removes whitespaces from the beginning and end of all string values in the list.

- `delete_duplicate_from_list(data: list) -> list`: This function receives a list and removes duplicates from it.

- `parse_datetime_to_iso8601(data: datetime) -> str`: This function receives a datetime object and returns a string representation of the datetime object in the ISO 8601 format.

This library can be useful for cleaning and formatting text data, removing duplicates from lists, and converting datetime objects to a standardized format.
#
## How to install
Due to this is a "personal" library, it is not in [PyPI](https://pypi.org/). You will need to use this command in order to install this package:
```
$ pip install "git+https://github.com/Brixt18/python-utils"
```
#
Any contributions are welcome.
