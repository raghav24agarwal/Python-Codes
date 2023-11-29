from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        # Implementation of QuickSort algorithm


class MergeSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using MergeSort")
        # Implementation of MergeSort algorithm


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Sorting using BubbleSort")
        # Implementation of BubbleSort algorithm


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        self.strategy.sort(data)


# Usage
data = [5, 2, 7, 1, 3]

sorter = Sorter(QuickSortStrategy())
sorter.sort_data(data)  # Output: Sorting using QuickSort

sorter.set_strategy(MergeSortStrategy())
sorter.sort_data(data)  # Output: Sorting using MergeSort

sorter.set_strategy(BubbleSortStrategy())
sorter.sort_data(data)  # Output: Sorting using BubbleSort
