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
        x_spacing = 1
        y_spacing = 1.5

        group.scale_to_fit_width(scene_width*0.6)
        square_width = group[0].width
        group.center()
        self.add(group)
        self.wait()

        up_groups = [group]
        down_groups = []
        while len(up_groups[-1]) != 1:

            for up_group in up_groups:
                mid = len(up_group) // 2

                if mid != 0: #lichypocet prvku
                    down_l = up_group[:mid]
                    down_groups.append(down_l)
                down_r = up_group[mid:]
                down_groups.append(down_r)

                self.play(down_l.animate.shift(LEFT*x_spacing), down_r.animate.shift(RIGHT*x_spacing))

            up_groups = down_groups
            down_groups = []
            x_spacing = x_spacing/2

        self.wait()
        self.play(Group(*self.mobjects).animate.shift(UP*y_spacing))

        while len(up_groups) != 1:
            x_spacing = x_spacing*2
            for i in range(0, len(up_groups), 2):
                j, k = 0, 0
                down_group = Group()

                if i != len(up_groups)-1:
                    up_l = up_groups[i]
                    up_r = up_groups[i+1]
                else:
                    down = up_groups[i].copy()
                    self.play(down.animate.shift(DOWN*y_spacing))
                    down_groups.append(down)
                    break

                highlight_l = Square(color=BLUE).surround(up_l[j], buff=SMALL_BUFF)
                highlight_r = Square(color=YELLOW).surround(up_r[k], buff=SMALL_BUFF)
                self.play(Create(highlight_l), Create(highlight_r))

                while j < len(up_l) and k < len(up_r):
                    down_l = up_l[j].copy()
                    down_r = up_r[k].copy()

                    val_l = int(down_l.submobjects[0].text)
                    val_r = int(down_r.submobjects[0].text)

                    if j==k==0:
                        pos = up_l[j].get_center() + DOWN*y_spacing*square_width + RIGHT*x_spacing
                    else:
                        pos = down_group[-1].get_center() + RIGHT*square_width

                    if  val_l <= val_r:
                        self.play(down_l.animate.move_to(pos))
                        down_group.add(down_l)
                        j+=1
                        if j < len(up_l): 
                            self.play(highlight_l.animate.move_to(up_l[j])) 

                    else:
                        self.play(down_r.animate.move_to(pos))
                        down_group.add(down_r)
                        k+=1
                        if k < len(up_r): 
                            self.play(highlight_r.animate.move_to(up_r[k]))

                for up in up_l.submobjects[j:]:     #zlepsit dodani zbytku
                    down = up.copy()
                    self.play(down.animate.next_to(down_group[-1], buff=0))
                    down_group.add(down)
                    j+=1
                    if j < len(up_l): 
                        self.play(highlight_l.animate.move_to(up_l[j]))

                for up in up_r.submobjects[k:]:
                    down = up.copy()
                    self.play(down.animate.next_to(down_group[-1], buff=0))
                    down_group.add(down)
                    k+=1
                    if k < len(up_r): 
                        self.play(highlight_l.animate.move_to(up_r[k]))
                
                down_groups.append(down_group)
                self.play(Uncreate(highlight_l), Uncreate(highlight_r))

            self.play(FadeOut(*up_groups, shift=UP*y_spacing), Group(*down_groups).animate.shift(UP*y_spacing))
            up_groups = down_groups 
            down_groups = []