import datetime


def get_text_or_empty(text: str, strip: bool = False) -> str:
    """
    This function receives a text string and an optional flag 'strip' that indicates whether whitespaces should be removed from the beginning and end of the string. 
    If the string is empty or only contains whitespaces, the function returns an empty string.
    Otherwise, it returns the string with removed whitespaces if the 'strip' flag is true, or the original string if it is false.
    
    PARAMS
    ----------
    text: str
        The input text string
    strip: bool (default=False)
        Flag indicating whether to remove whitespaces from the input text
    
    RETURNS
    -------
    str
        The processed text string
    """
    if (not text) or (not text.strip()):
        return ""

    return text.strip() if strip else text


def get_text_or_none(text: str, strip: bool = False) -> "str" | "None":
    """
    This function receives a text string and an optional flag 'strip' that indicates whether whitespaces should be removed from the beginning and end of the string. 
    If the string is empty or only contains whitespaces, the function returns None.
    Otherwise, it returns the string with removed whitespaces if the 'strip' flag is true, or the original string if it is false.
    
    PARAMS
    ----------
    text: str
        The input text string
    strip: bool (default=False)
        Flag indicating whether to remove whitespaces from the input text
    
    RETURNS
    -------
    Union[str, None]
        The processed text string or None
    """
    if (not text) or (not text.strip()):
        return None

    return text.strip() if strip else text


def strip_dict_fields(data: dict) -> dict:
    """
    This function receives a dictionary and removes whitespaces from the beginning and end of all string values in the dictionary.
    
    PARAMS
    ----------
    data: dict
        The input dictionary
    
    RETURNS
    -------
    dict
        The processed dictionary with whitespaces removed from string values
    """
    return {k: v.strip() if isinstance(v, str) else v for k, v in data.items()}


def strip_list_fields(data: list) -> list:
    """
    This function receives a list and removes whitespaces from the beginning and end of all string values in the list.
    
    PARAMS
    ----------
    data: list
        The input list
    
    RETURNS
    -------
    list
        The processed list with whitespaces removed from string values
    """
    return [i.strip() if isinstance(i, str) else i for i in data]


def delete_duplicate_from_list(data: list) -> list:
    """
    This function receives a list and removes duplicates from it.
    
    PARAMS
    ----------
    data: list
        The input list
    
    RETURNS
    -------
    list
        The processed list with duplicates removed
    """
    return list(set(data))


def parse_datetime_to_iso8601(data: datetime) -> str:
    """
    This function receives a datetime object and returns a string representation of the datetime object in the ISO 8601 format.
    
    PARAMS
    ----------
    data: datetime
        The input datetime object
    
    RETURNS
    -------
    str
        The string representation of the input datetime object in ISO 8601 format
    """
    return data.isoformat()
