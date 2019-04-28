from mycroft import MycroftSkill, intent_file_handler


class MycroftBlenderControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.blender.mycroft.intent')
    def handle_control_blender_mycroft(self, message):
        self.speak_dialog('control.blender.mycroft')


def create_skill():
    return MycroftBlenderControl()

