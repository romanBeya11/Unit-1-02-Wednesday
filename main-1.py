# Created by: Mr. Coxall
# Created on: Sep 2017
# Created for: ICS3U
# This program is the first file in a multi-scene game template
#    This template is meant to be used with the Xcode template,
#    to make apps for the App Store.
#
# Originally from: Ole Zorn, from the Xcode template
# for use with https://github.com/omz/PythonistaAppTemplate
# Also from the Pythonista community forum.
#
# This file creates the UIView that will be used by Xcode,
#  then creates the scene inside it. once everything is ready
#  to go, the scene transitions immediately to the first scene.
# It is assumed you bring along all your assets, 
#   and not use any of the mornal ones built into Pythonista.
#
# To exit the app in Pythonista, pull down with 2 fingers.

from scene import *
import ui

class FirstScene(Scene):
    def setup(self):
        # happens before the scene is shown
        self.background = SpriteNode(position = self.size / 2,
                                     color = (0.61, 0.78, 0.87),
                                     parent = self,
                                     size = self.size)
                                     
        self.school_crest = SpriteNode('./assests/sprites/school_crest.JPG', 
                                       parent = self,
                                       position = self.size / 2)                          
                                      
    def touch_moved(self, touch):
        # happens when your finger is moving around screen
        self.school_crest.position = touch.location

#  ..use when deploying app for Xcode and the App Store
main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = FirstScene()
main_view.present(hide_title_bar = True, animated = False)
