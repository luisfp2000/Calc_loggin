import string
import numpy as np
from utilities.CustomLogging import CustomLogging


logger = CustomLogging(name="calculator", log_level="DEBUG", modulo =__name__)

class Calculator:
    def get_fractions(self, frac_str: (int or float or string)) -> (int or float):
        """Checks a number and returns to float type.

        Parameters
        ----------
        frac_str : int or float or string
            Number in int, float or string type.

        Returns
        -------
        float
            Fixed float type number.
        """

        if isinstance(frac_str, (int, float)):
            logger.info(f"fractions  is: {frac_str}")
            return frac_str

        if "/" not in frac_str:
            return float(frac_str)
        try:
            return float(frac_str)
        except ValueError as ex:
            logger.error(f"ValueError: {ex}")
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError as e:
                logger.error(f"ValueError: {e}")
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac


    def sum(self, a: any, b: any) -> (int or float):
        """Gets two numbers, adds them, and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the sum.
        """

        sum_a = self.get_fractions(a)
        sum_b = self.get_fractions(b)
        logger.info(f"The sum for {sum_a} add {sum_b} is: {np.sum([sum_a, sum_b])}")
        return np.sum([sum_a, sum_b])


    def subtract(self, a: any, b: any) -> (int or float):
        """Gets two numbers, subtracts the second from the first,
        and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the substraction.
        """

        minuend = self.get_fractions(a)
        subtrahend = self.get_fractions(b)
        logger.info(f"The subtract for {minuend} minus {subtrahend} is: {minuend - subtrahend}")
        return minuend - subtrahend


    def multiply(self, a: any, b: any) -> (int or float):
        """Gets two numbers, multiplies them, and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the multiplication.
        """

        multiplicand = self.get_fractions(a)
        multiplier = self.get_fractions(b)
        logger.info(f"The multiply for {multiplicand} and {multiplier} is: {multiplicand * multiplier}")
        return multiplicand * multiplier


    def divide(self, a: any, b: any) -> (int or float):
        """Gets two numbers, divide the first by the second,
        and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the division.
        """

        dividend = self.get_fractions(a)
        divider = self.get_fractions(b)
        
        try:
            return np.divide(dividend, divider)
        except ZeroDivisionError:
            logger.exception(f"Division by zero:")
            return "Division by zero is not allowed!"