from manim import *

array = [5, 8, 3, 2, 9, 6, 4, 7]

def sort(array):

    swaps = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            max = array[i]
            max_index = i

            for j in range(i+1, len(array)):
                if array[j] % 2 == 1: 
                    continue

                if array[j] > max:
                    max = array[j]
                    max_index = j

            if array[i] != array[max_index]:
                array[i], array[max_index] = array[max_index], array[i]
                swaps.append([i, max_index])

        if array[i] % 2 == 1:
            min = array[i]
            min_index = i

            for j in range(i+1, len(array)):
                if array[j] % 2 == 0: 
                    continue

                if array[j] < min:
                    min = array[j]
                    min_index = j

            if array[i] != array[min_index]:
                array[i], array[min_index] = array[min_index], array[i]
                swaps.append([i, min_index])

    return swaps

class Sort(Scene):
    def construct(self):

        group = Group()

        for index, item in enumerate(array):
            square = Square(side_length=1.5)
            number = Text(text=str(item))

            square.add(number)
            if index != 0:
                square.next_to(group.submobjects[index-1], buff=0)

            group.add(square)

        group.center()

        self.add(group)
        self.wait(1)

        swaps = sort(array)

        for swap in swaps:
            self.play(Swap(group[swap[0]], group[swap[1]]))
            group.submobjects[swap[0]], group.submobjects[swap[1]] = group.submobjects[swap[1]], group.submobjects[swap[0]]
            self.wait(0.5)




