"""
OOP Example to review principles of abstraction, encapsulation, inheritance,
and polymorphism.
"""

from abc import ABC, abstractmethod

class Camera(ABC):

    """
    Camera abstract class. Represents general features and camara behaviours.
    """

    def __init__(self, brand: str, model: str, resolution: float):
        self._brand = brand
        self._model = model
        self._resolution = resolution

    @abstractmethod
    def take_picture(self):
        pass

    @abstractmethod
    def record_video(self):
        pass

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

    def get_resolution(self) -> str:
        return self._resolution

    def __str__(self) -> str:
        return f'{self._brand} {self._model} with {self._resolution}MP ' \
            'resolution'


class DSLR(Camera):
    
    """Digital Single-Lens Reflex (DSLR) Camera."""

    def __init__(
            self, brand: str, model: str, resolution: float, lens_type: str):
        super().__init__(brand, model, resolution)
        self._lens_type = lens_type

    def take_picture(self) -> str:
        return 'DSLR photo captured.'

    def record_video(self) -> str:
        return 'DSLR video recording initiated.'
    
    def change_lens(self, lens_type: str) -> None:
        self._lens_type = lens_type
        print(f'Lens changed to {lens_type}')

    def __str__(self) -> str:
        return f'DSLR: {self._brand} {self._model}, {self._resolution}MP, ' \
               f'Lens Type: {self._lens_type}'


class Mirrorless(Camera):

    """Mirrorless Camera."""

    def __init__(self, brand: str, model: str, resolution: float, evf_type: str):
        super().__init__(brand, model, resolution)
        self._evf_type = evf_type

    def take_picture(self):
        return 'Mirrorless photo captured.'

    def record_video(self):
        return 'Mirrorless video recording initiated.'

    def __str__(self):
        return f'Mirrorless: {self._brand} {self._model}, {self._resolution}' \
               f'MP, EVF Type: {self._evf_type}'


class ActionCamera(Camera):

    """Acion Camera."""


    def __init__(
            self, brand: str, model: str, resolution: float, waterproof: bool):
        super().__init__(brand, model, resolution)
        self._waterproof = waterproof

    def take_picture(self):
        return 'Action camera photo captured.'

    def record_video(self):
        return 'Action camera video recording initiated.'

    def __str__(self):
        return f'Action Camera: {self._brand} {self._model}, ' \
               f'{self._resolution}MP, Waterproof: {self._waterproof}'


def describe_camera(camera: Camera):
    """
    Describe camera characteristics, functionalities.

    :param camera: Camera instance.
    """
    print(f'Camera: {camera}')
    print(f'Take picture: {camera.take_picture()}')
    print(f'Record video: {camera.record_video()}')
    print('------------------')


if __name__ == '__main__':
    """Example execution."""
    dslr_camera = DSLR(
        'Nikon', 'D5600', 24.2, 'AF-P DX NIKKOR 18-55mm f/3.5-5.6G VR')
    dslr_camera.change_lens('AF-S DX NIKKOR 35mm f/1.8G')
    mirrorless_camera = Mirrorless('Sony', 'Alpha A7 III', 24.2, 'OLED')
    action_camera_camera = ActionCamera('GoPro', 'Hero9', 20, True)
    
    describe_camera(dslr_camera)
    describe_camera(mirrorless_camera)
    describe_camera(action_camera_camera)
