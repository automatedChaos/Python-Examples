import toga # import the widget library
from toga.style.pack import * # import the style library
from toga.color import rgb


class Converter(toga.App):

    def startup(self):
        """ Initialise the window """
        self.main_window = toga.MainWindow(
            title=self.name,
            size=(400,400)
        )

        self.scaleFactor = 0.3048

        logoImage = toga.Image('joke.png')
        logo = toga.ImageView(id='header', image=logoImage)
        headerBox = toga.Box(
            children=[logo],
            style=Pack(direction=ROW, padding=10, height=170)
        )

        # create input elements
        inputLabel = self.createLabel('Feet to Metres: ') # this never changes
        self.inputValue = self.createInput('feetVal', 'Feet...') # this does
        # create an array for the input elements
        inputElements = [inputLabel, self.inputValue]
        # package the input elements in a box
        inputBox = self.createBox(ROW, inputElements)

        # create action elements
        actionButton = self.createButton('CONVERT', self.convert)
        actionBox = self.createBox(ROW, [actionButton])

        self.result = self.createLabel('[Results]')
        resultBox = self.createBox(ROW, [self.result])

        # create main Box
        mainBox = self.createBox(COLUMN, [headerBox, inputBox, actionBox, resultBox])

        self.main_window.content = mainBox

        self.main_window.show()

    def createBox(self, type, children):
        return toga.Box(
            children=children,
            style=Pack(direction=type, padding=10)
        )

    def createButton(self, value, func):
        return toga.Button(
            label=value,
            on_press=func,
            style=Pack(flex=1)
        )

    def createInput(self, id, placeholder):
        """returns a standard input with an id of id param."""
        return toga.TextInput(
            id=id,
            placeholder=placeholder,
            style=Pack(flex=1, padding=2)
        )

    def createLabel(self, text):
        """returns a standard label with the text passed in."""
        return toga.Label(
            text=text,
            style=Pack(flex=1, padding=1, font_size=14, text_align='center')
        )

    def convert(self, widget):
        calc = float(self.inputValue.value) * self.scaleFactor
        self.result.text = str(calc) + 'm'

def main():
    return Converter('Converter', 'org.miningsearches.converter', icon='dino.ico')


if __name__ == '__main__':
    main().main_loop()
