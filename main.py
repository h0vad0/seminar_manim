from manim import *

class Sort(Scene):
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

    def construct(self):
        array = [5, 8, 3, 2, 9, 6, 4, 7]
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

        swaps = self.sort(array)

        for swap in swaps:
            self.play(Swap(group[swap[0]], group[swap[1]]))
            group.submobjects[swap[0]], group.submobjects[swap[1]] = group.submobjects[swap[1]], group.submobjects[swap[0]]
            self.wait(0.5)


class BinarySearch(Scene):
    def construct(self):
        arr = [2, 5, 8, 16, 23, 50, 71, 88, 99]
        target = 88
        group = Group()

        for index, item in enumerate(arr):
            square = Square(side_length=1.5)
            number = Text(text=str(item))

            square.add(number)
            if index != 0:
                square.next_to(group.submobjects[index-1], buff=0)

            group.add(square)
        group.center()

        target_text = Text(f"Target: {target}")
        target_text.to_edge(UP)

        self.add(group)
        self.wait()

        self.play(FadeIn(target_text))
        self.wait()

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            for index, item in enumerate(group.submobjects):
                if int(item.submobjects[0].text) == arr[mid]:
                    gr_mid = index
                    
            self.play(Circumscribe(group[gr_mid]))

            if arr[mid] == target:
                break

            elif arr[mid] < target:
                left = mid + 1
                comparison = Text(f"< {target}")
                slice = Group()
                for submobject in group[:gr_mid+1]:
                    slice.add(submobject)

            else:
                right = mid - 1
                comparison = Text(f"> {target}")
                slice = Group()
                for submobject in group[gr_mid:]:
                    slice.add(submobject)

            comparison.next_to(group[gr_mid], DOWN)
            self.play(FadeIn(comparison))
            self.wait()

            self.play(FadeOut(slice, comparison))
            for submobject in slice:
                group.remove(submobject)
            self.wait(0.5)

            self.play(group.animate.center())
            self.wait()

        comparison = Text(f"= {target}")
        comparison.next_to(group[gr_mid], DOWN)
        self.play(FadeIn(comparison))
        self.wait()

        slice = Group()
        for submobject in group:
            if int(submobject.submobjects[0].text) != target:
                slice.add(submobject)
            
        self.play(FadeOut(slice, comparison))
        for submobject in slice:
            group.remove(submobject)
        self.wait(0.5)

        self.play(group.animate.center())
        self.wait()

                
class MergeSort(Scene):
    def construct(self):
        arr = [5, 3, 8, 4, 2, 7, 1, 6]
        group = Group()

        for index, item in enumerate(arr):
            square = Square(side_length=1.5)
            number = Text(text=str(item))

            square.add(number)
            if index != 0:
                square.next_to(group.submobjects[index-1], buff=0)

            group.add(square)

        scene_width = 14 + 2/9
        spacing = 1

        group.scale_to_fit_width(scene_width*0.6)
        group.center()
        self.add(group)
        self.wait()

        subgroups = [group]
        while len(subgroups[-1]) != 1:
            halves = []

            for subgroup in subgroups:
                mid = len(subgroup) // 2
                half_l = subgroup[:mid]
                halves.append(half_l)
                half_r = subgroup[mid:]
                halves.append(half_r)
                self.play(half_l.animate.shift(LEFT*spacing), half_r.animate.shift(RIGHT*spacing))

            subgroups = halves

            spacing = spacing/2

        sorted_list = []
        i = j = 0

        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

