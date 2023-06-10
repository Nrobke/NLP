from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from Ai.ai import answer
from data import gold_and_wax
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelTwoLine
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime
from kivy.core.window import Window


class AI(MDApp):
    title = "መሪጌታ"

    def build(self):
        LabelBase.register("AmharicFont", "./PGUNICODE1.ttf")
        self.theme_cls.theme_style_switch_animation = False
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')

    # def switch_theme(self):
    #     if self.theme_cls.theme_style == "Dark":
    #         self.theme_cls.theme_style = "Light"
    #     else:
    #         self.theme_cls.theme_style = "Dark"

    def open_tab(self, tab_name, question, incoming=False):

        bottom_navigation = self.root.ids.bottom_navigation
        bottom_navigation.switch_tab(tab_name)

        question_answer = answer(question)
        self.add_conversation(False, question)
        self.add_conversation(True, question_answer)

    def add_conversation(self, incoming, text):
        if incoming:
            self.root.ids.ask_ai_message.add_widget(
                MDExpansionPanel(
                    icon='robot',
                    content=Builder.load_string('''
MDBoxLayout:
    adaptive_height: True
    font_name: 'AmharicFont'
    orientation: 'vertical'
    MDLabel:
        font_name: 'AmharicFont'
        padding: (20, 0, 10, 0)
        text: "the_word"
    MDLabel:
        font_name: 'AmharicFont'
        padding: (20, 0, 10, 0)
        text: "the_wax"
        
    MDLabel:
        font_name: 'AmharicFont'
        padding:(20, 0, 10, 0)
        text: "the_gold"
'''.replace('the_word', text.get('word')).replace('the_wax', text.get('wax')).replace('the_gold', text.get('gold'))),

                    panel_cls=MDExpansionPanelThreeLine(
                        text="Ai ",
                        secondary_text=f"Confidence: {text.get('confidence')}",
                    )
                )
            )
        else:
            self.root.ids.ask_ai_message.add_widget(
                MDExpansionPanel(
                    icon='account',
                    content=Builder.load_string('''
MDBoxLayout:
    adaptive_height: True
    font_name: 'AmharicFont'
    MDLabel:
        font_name: 'AmharicFont'
        padding:(20, 0, 10, 0)
        text: "gold_wax_text"
'''.replace("gold_wax_text", text)),
                    panel_cls=MDExpansionPanelTwoLine(
                        text="Question",
                        secondary_text=str(datetime.now().strftime('%d/%m/%Y %H:%M'))
                    )
                )
            )

    def send_message(self, incoming=False, incoming_text=None):
        if not incoming:
            text_input = self.root.ids.text_input
            message = text_input.text
            if not message.isspace():
                label = Builder.load_string('''
MDCard:
    size_hint: 0.5, None
    height: self.minimum_height
    padding: dp(10)
    md_bg_color: "#453939"
    pos_hint: {'center_x': .7}
    MDLabel:
        text: 'question'
        adaptive_height: False,
        padding_x: '15dp'
        font_name: 'AmharicFont'
        halign: 'right'
        '''.replace('question', message.strip()))

                self.root.ids.chat_messages.add_widget(label)
                text_input.text = ""
                api_answer = answer(message.strip())
                if api_answer.get("success") is True:
                    self.send_message(True, f"---> {api_answer.get('word')} ---> {api_answer.get('wax')} ---> {api_answer.get('gold')} ---> Confidence: {api_answer.get('confidence')}")
                    self.add_conversation(False, message.strip())
                    self.add_conversation(True, api_answer)
                else:
                    self.send_message(True, api_answer.get('response'))


            else:
                text_input.text = ""
        else:
            label = Builder.load_string("""
MDCard:
    size_hint: 0.5, None
    height: self.minimum_height
    padding: dp(10)
    md_bg_color: "#2B2C36"
    pos_hint: {'center_x': .3}
    MDLabel:
        text: 'ai_answer'
        adaptive_height: True,
        padding_x: '15dp'
        font_name: 'AmharicFont'
        halign: 'left'
        """.replace('ai_answer', incoming_text.strip()))
            self.root.ids.chat_messages.add_widget(label)

    def on_start(self):
        Window.set_icon('ai_icon.ico')
        for text in [item.get('phrase') for item in gold_and_wax]:
            card = """
MDCard:
    size_hint: None, None
    size: "250dp", "180dp"
    pos_hint: {'center_x': .5}

    BoxLayout:
        orientation: 'vertical'
        padding: '10dp'
        spacing: '10dp'

        MDLabel:
            id: question_1
            font_name: 'AmharicFont'
            text: "gold_and_wax_text"

        MDRelativeLayout:
            size_hint_y: None
            height: dp(48)
            spacing: '10dp'
            pos_hint: {'left': 1}

            MDIconButton:
                icon: 'help-circle'
                theme_text_color: "Secondary"
                on_release: app.open_tab('screen 2', "gold_and_wax_text", False)
""".replace("gold_and_wax_text", text)

            self.root.ids.question_container.add_widget(Builder.load_string(card))


AI().run()
