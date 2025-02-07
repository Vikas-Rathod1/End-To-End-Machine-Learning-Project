import sys
from src import logger
import logging

def error_message_details(error, error_detail: sys):  # type: ignore
    """
    Generates a detailed error message including the filename, line number, and error description.

    Args:
        error (Exception): The exception instance.
        error_detail (sys): The system module used to extract error details.

    Returns:
        str: A formatted string containing the error details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    """
    Custom exception class that extends the built-in Exception class.

    This class captures and formats error messages with detailed information 
    about where the exception occurred.

    Args:
        error_message (str): The error message describing the exception.
        error_detail (sys): The system module used to extract error details.
    """

    def __init__(self, error_message, error_detail: sys):  # type: ignore
        """
        Initializes the CustomException instance with a detailed error message.

        Args:
            error_message (str): The error message describing the issue.
            error_detail (sys): The system module used to retrieve traceback details.
        """
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the formatted error message when the exception is printed.

        Returns:
            str: A detailed error message.
        """
        return self.error_message
    



