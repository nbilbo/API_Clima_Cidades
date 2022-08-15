from app import constants
from app import utils
from app.interface import Interface


class Controller:
    def __init__(self) -> None:
        self.interface = Interface()
        self.interface.button.config(command=self.show_weather)
        self.interface.inp_city.bind(
            '<Return>', lambda event: self.show_weather()
        )

    def start(self) -> None:
        self.interface.mainloop()

    def show_weather(self) -> None:
        city = self.interface.city().strip()
        self.interface.set_feedback('')
        self.interface.hide_info()
        self.interface.clear_info()

        if city:
            info = utils.weather_info(constants.API_KEY, city)
            if info is None:
                self.interface.set_feedback(
                    f'Cannot find "{city}", try latter.'
                )
            else:
                self.interface.show_info()
                for key, value in info.items():
                    self.interface.add_info(key, str(value))
        else:
            self.interface.set_feedback('Required field.')
