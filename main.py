#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.popup import Popup 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.floatlayout import FloatLayout 
from kivy.lang import Builder 


Builder.load_file("pop.kv")


class pop(Widget):
    def show_it(self):
        self.box=FloatLayout()
        
        self.lab=(Label(text="Do you want to quit? ",font_size=30,
        	size_hint=(None,None),pos_hint={'x':.25,'y':.6}))
        self.box.add_widget(self.lab)
        
        self.but=(Button(text="No",size_hint=(None,None),
        	width=self.width/3,height=70,pos_hint={'x':0,'y':0}))
        self.box.add_widget(self.but)

        self.but2=(Button(text="Yes",size_hint=(None,None),
        	width=self.width/3,height=70,pos_hint={'right':1,'y':0}))
        self.box.add_widget(self.but2)
       
        self.main_pop = Popup(title="QUIT GAME ?",content=self.box,
        	size_hint=(.8,.5),auto_dismiss=False,title_size=25)
        	
        self.but.bind(on_release=self.main_pop.dismiss)
        self.but2.bind(on_release=self.quit_popup)
        self.main_pop.open()
        

    @staticmethod
    def quit_popup(self):
        exit()




class PopApp(App):
    def build(self):
        return pop()




PopApp().run()

