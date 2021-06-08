import pytest

#1
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)


# 3
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count


# 4
import time
def check_time_to_now_even(seconds):
    """
    Checks whether time difference between now and given time in seconds is even
    """
    if seconds < 0:
        raise ValueError('received negative input')
   
    now=time.time()
    return (seconds-now)%2 == 0


# 5
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1




def test_check_time(monkeypatch):
  def mocktime():
    return 2
  monkeypatch.setattr(time,"time",mocktime)
  assert check_time_to_now_even(0) == 1
  assert check_time_to_now_even(1) == 0