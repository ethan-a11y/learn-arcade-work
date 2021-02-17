import arcade

arcade.open_window(600, 600, "RoAd")

# BACKGROUND
arcade.set_background_color(arcade.csscolor.GREEN)

arcade.start_render()

# ROAD
arcade.draw_lrtb_rectangle_filled(0, 800, 210, 20, arcade.color.BLACK)

# CAR? - SOME VEHICLE
arcade.draw_lrtb_rectangle_filled(30, 300, 100, 170, arcade.color.GRAY_BLUE)

def draw_tree_circle(x):
    arcade.draw_rectangle_filled(x, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x, 350, 30, arcade.csscolor.DARK_GREEN)

def draw_tree_ellipsed(x):
    arcade.draw_rectangle_filled(x, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(x, 370, 60, 80, arcade.csscolor.DARK_GREEN)

draw_tree_circle(100)
draw_tree_ellipsed(200)
draw_tree_circle(300)
draw_tree_ellipsed(400)
draw_tree_circle(500)

arcade.finish_render()
arcade.run()



# TREE 1
#arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
#arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
# TREE 2
#arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
#arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
# TREE 3
#arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
#arcade.draw_circle_filled(300, 350, 30, arcade.csscolor.DARK_GREEN)
# TREE 4
#arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
#arcade.draw_ellipse_filled(400, 370, 60, 80, arcade.csscolor.DARK_GREEN)
# TREE 5
#arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
#arcade.draw_circle_filled(500, 350, 30, arcade.csscolor.DARK_GREEN)
