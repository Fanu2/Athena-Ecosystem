from .models import (
    Preference,
)


class PreferenceStore:


    def __init__(self):

        self.preferences = []


    def add(
        self,
        preference: Preference
    ):

        self.preferences.append(
            preference
        )


    def get(
        self,
        key: str
    ):

        for preference in self.preferences:

            if preference.key == key:

                return preference


        return None


    def all(self):

        return self.preferences
