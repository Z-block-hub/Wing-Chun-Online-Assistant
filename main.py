import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
import time, sys, random
from threading import Thread
from kivy.app import runTouchApp


#################################### Variables and Containers ####################


# minimum cooldown between redirections
cooldown = 2

global session_time
session_time = 0

# change of guard redirections
cog_redirections = {"1": "Tan_sau", "2": "Bong_sau", "3": "Kau_sau", "4": "Low_Garn", "5": "Garn_sau",
                "6": "Kwun_sau", "7": "Lap_sau", "8": "Pak_sau", "9": "Gum_sau", "10": "Biu_sau"}

# chi sau redirections
cs_redirections = {"1": "Tan", "2": "Bong", "3": "Gum", "4": "Garn", "5": "Kwun", "6": "Pak"}

# session redirections
global session_list
session_list = []

global function_stop
function_stop = False



######################################### AUDIO ##################################


# change of guard redirections
tan_sau = SoundLoader.load("audio/guard/Tan_sau.wav")
bong_sau = SoundLoader.load("audio/guard/Bong_sau.wav")
kau_sau = SoundLoader.load("audio/guard/Kau_sau.wav")
low_garn = SoundLoader.load("audio/guard/Low_Garn.wav")
garn_sau = SoundLoader.load("audio/guard/Garn_sau.wav")
kwun_sau = SoundLoader.load("audio/guard/Kwun_sau.wav")
lap_sau = SoundLoader.load("audio/guard/Lap_sau.wav")
pak_sau = SoundLoader.load("audio/guard/Pak_sau.wav")
biu_sau = SoundLoader.load("audio/guard/Biu_sau.wav")
gum_sau = SoundLoader.load("audio/guard/Gum_sau.wav")

# chi sau redirections
tan = SoundLoader.load("audio/chisau/Tan.wav")
bong = SoundLoader.load("audio/chisau/Bong.wav")
gum = SoundLoader.load("audio/chisau/Gum.wav")
garn = SoundLoader.load("audio/chisau/Garn.wav")
kwun = SoundLoader.load("audio/chisau/Kwun.wav")
pak = SoundLoader.load("audio/chisau/Pak.wav")


cog_dict = {"Tan_sau": tan_sau, "Bong_sau": bong_sau, "Kau_sau": kau_sau, "Low_Garn": low_garn,
            "Garn_sau": garn_sau, "Kwun_sau": kwun_sau, "Lap_sau": lap_sau, "Pak_sau": pak_sau,
            "Gum_sau": gum_sau, "Biu_sau": biu_sau, "Tan": tan, "Bong": bong, "Gum": gum,
            "Garn": garn, "Kwun": kwun, "Pak": pak}





global step
step = 1

################################ Buttons and Layouts ###################################

class Widgets(Widget):
    pass

class MainMenu(Screen): # Main Menu

    def red_notes(self):
        RedirectionsNotes().open()

    def chisau_notes(self):
        ChisauNotes().open()


class CSMenu(Screen): # Chi Sau Menu

    def btn(self):
        show_popup()

    def btnt2(self):
        global session_list
        session_list = []
        show_popupt2()

class COGMenu(Screen): # Change of Guard Menu

    def btn(self):
        show_popup()

    def btnt(self):
        global session_list
        session_list = []
        show_popupt()

class InSessionMenu(Screen): # Further Training Session Menu

    def stop_function(self):
        global function_stop
        function_stop = True




class COGSessionMenu(Screen): # Training Session Menu
    def button_press(self):
        # create the thread to invoke other_func with arguments (2, 5)
        t = Thread(target=self.in_session)
        # set daemon to true so the thread dies when app is closed
        t.daemon = True
        # start the thread
        t.start()

    def progress(self):
        # create the thread to invoke other_func with arguments (2, 5)
        t = Thread(target=self.in_progress)
        # set daemon to true so the thread dies when app is closed
        t.daemon = True
        # start the thread
        t.start()


    def in_progress(self):
        global step
        time.sleep(6)
        while function_stop == False:
            if step == 1:
                Pr1().open()
                time.sleep(1)
                step += 1
            elif step == 2:
                Pr2().open()
                time.sleep(1)
                step += 1
            elif step == 3:
                Pr3().open()
                time.sleep(1)
                step = 1


        

    def play_tech(self, new_dict):
        technique = (random.choice(session_list))
        print(technique)
        new_dict[technique].play()


    def in_session(self):
        global function_stop
        function_stop = False
        Gr5().open()
        time.sleep(1)
        Gr4().open()
        time.sleep(1)
        Gr3().open()
        time.sleep(1)
        Gr2().open()
        time.sleep(1)
        Gr1().open()
        time.sleep(1)
        Gr().open()
        now = time.time()
        timer = 0
        while timer < session_length and function_stop == False:
            self.play_tech(cog_dict)
            end = time.time()
            timer = round(end - now)
            print(timer)
            time.sleep((cooldown + random.randint(0, 4)))
            
            
        return


    def stop_function(self):
        global function_stop
        function_stop = True

class DiffMenu(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

################## Popup Menus #########################

################## Progress Popups #################

class Pr1(Popup):

    def __init__(self, **kwargs):
        super(Pr1, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()

class Pr2(Popup):

    def __init__(self, **kwargs):
        super(Pr2, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()

class Pr3(Popup):

    def __init__(self, **kwargs):
        super(Pr3, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()

################## Notes Popups ######################

class RedirectionsNotes(Popup):
    def __init__(self, **kwargs):
        super(RedirectionsNotes, self).__init__(**kwargs)


    def dismiss_popup(self):
        self.dismiss()


class ChisauNotes(Popup):
    def __init__(self, **kwargs):
        super(ChisauNotes, self).__init__(**kwargs)


    def dismiss_popup(self):
        self.dismiss()



################ Get Ready Popups ############

class Gr5(Popup):

    def __init__(self, **kwargs):
        super(Gr5, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()
class Gr4(Popup):
    def __init__(self, **kwargs):
        super(Gr4, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()
class Gr3(Popup):
    def __init__(self, **kwargs):
        super(Gr3, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()
class Gr2(Popup):
    def __init__(self, **kwargs):
        super(Gr2, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()
class Gr1(Popup):
    def __init__(self, **kwargs):
        super(Gr1, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()
class Gr(Popup):
    def __init__(self, **kwargs):
        super(Gr, self).__init__(**kwargs)
        Clock.schedule_once(self.dismiss_popup, 1)

    def dismiss_popup(self, dt):
        self.dismiss()

################ Session Length Menu ###############
class P(FloatLayout):

    def session_time_60(self):
        global session_length
        session_length = 60
        print(session_length)

    def session_time_120(self):
        global session_length
        session_length = 120
        print(session_length)

    def session_time_300(self):
        global session_length
        session_length = 300
        print(session_length)

    def session_time_600(self):
        global session_length
        session_length = 600
        print(session_length)


################ Change of Guard Techniques Menu ##########
class Pt(FloatLayout):
    def populate_pt(self, technique):
        if technique in session_list:
            session_list.remove(technique)
            print(session_list)
        else:
            session_list.append(technique)
            print(session_list)




################ Chi Sau Techniques Menu #################
class Pt2(FloatLayout):
    def populate_pt2(self, technique):
        if technique in session_list:
            session_list.remove(technique)
            print(session_list)
        else:
            session_list.append(technique)
            print(session_list)



class Wing_Chun_Training_AssistantApp(App):

    def build(self):
        return kv



##################################### Functions #############################################



def show_popup():
    show = P()

    popupWindow = Popup(background_color = [1, 0.0, 0.0, 1], separator_color =  [0.9, 0.0, 0.0, 1], title = "Choose Length of Session, then click outside to close", content = show, size_hint = (0.8, 0.8), size = (400, 400))


    popupWindow.open()




def show_popupt():
    showt = Pt()

    popupWindowt = Popup(background_color = [1, 0.0, 0.0, 1], separator_color =  [0.9, 0.0, 0.0, 1], title = "Select Techniques to Train, then click outside to close", content = showt, size_hint = (0.8, 0.8), size = (400, 400))

    popupWindowt.open()


def show_popupt2():
    showt2 = Pt2()

    popupWindowt2 = Popup(background_color = [1, 0.0, 0.0, 1], separator_color =  [0.9, 0.0, 0.0, 1], title = "Select Techniques to Train, then click outside to close", content = showt2, size_hint = (0.8, 0.8), size = (400, 300))

    popupWindowt2.open()



##################################### Main Functions #####################################

##################################### Change of Guard #####################################




###################################### Run Loop ##############################################

if __name__ == "__main__":
    Wing_Chun_Training_AssistantApp().run()
