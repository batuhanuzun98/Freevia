#!/usr/bin/env python3
"""
Freevia - A simple mobile application created with Kivy
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.logger import Logger


class FreeviaApp(App):
    """Main application class for Freevia"""
    
    def build(self):
        """Build the UI for the application"""
        Logger.info("Freevia: Starting application")
        
        # Create main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Add title
        title = Label(
            text='Welcome to Freevia!',
            font_size='24sp',
            size_hint=(1, 0.2),
            color=(0.2, 0.6, 0.8, 1)
        )
        main_layout.add_widget(title)
        
        # Add description
        description = Label(
            text='A simple Python mobile app\nbuilt with Kivy framework',
            font_size='16sp',
            size_hint=(1, 0.2),
            halign='center',
            text_size=(None, None)
        )
        main_layout.add_widget(description)
        
        # Add text input
        self.text_input = TextInput(
            hint_text='Enter your message here...',
            size_hint=(1, 0.2),
            multiline=False
        )
        main_layout.add_widget(self.text_input)
        
        # Add button
        button = Button(
            text='Say Hello!',
            size_hint=(1, 0.2),
            background_color=(0.3, 0.7, 0.3, 1)
        )
        button.bind(on_press=self.on_button_press)
        main_layout.add_widget(button)
        
        # Add output label
        self.output_label = Label(
            text='Your message will appear here...',
            font_size='14sp',
            size_hint=(1, 0.2),
            color=(0.1, 0.5, 0.1, 1)
        )
        main_layout.add_widget(self.output_label)
        
        return main_layout
    
    def on_button_press(self, instance):
        """Handle button press event"""
        user_input = self.text_input.text.strip()
        if user_input:
            self.output_label.text = f"Hello, {user_input}! 👋\nWelcome to Freevia!"
            Logger.info(f"Freevia: User said hello to {user_input}")
        else:
            self.output_label.text = "Please enter your name first! 😊"
            Logger.info("Freevia: Empty input received")


if __name__ == '__main__':
    FreeviaApp().run()