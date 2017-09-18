# created by raymond octavious
# created on september 18, 2017
# created for class ics3u
# created for daily assignment


import ui

def answer_label_touch_up_inside(sender) : 
    #displays answer for area and perimeter
    view['area_answer_label'].text = 'Area = ' + str(5*3) + 'cm^2'
    view['perimeter_answer_label'].text = 'Perimeter = ' + str(2*5+2*3) + 'cm'
 
view = ui.load_view()
view.present('sheet')
