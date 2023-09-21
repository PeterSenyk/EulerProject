rec_l = float((input("Enter the rectangles length: ")))
rec_w = float(input("Enter the rectangles width: "))


def surface_area(rec_l, rec_w):
    area = rec_l * rec_w
    return area

def perimiter(rec_l, rec_w):
    perm = (rec_l * 2) + (rec_w * 2)
    return perm

area = surface_area(rec_l, rec_w)
print("the surface area is: ", area)
perm = perimiter(rec_l, rec_w)
print("the perimiter is: ", perm)