from fluentcheck.assertions_is.base_is import IsBase


class __IsGeo(IsBase):
    @property
    def latitude(self) -> "Is":
        self.check.is_latitude()
        return self

    @property
    def longitude(self) -> "Is":
        self.check.is_longitude()
        return self

    @property
    def azimuth(self) -> "Is":
        self.check.is_azimuth()
        return self

    # noinspection SpellCheckingInspection
    @property
    def geopoint(self) -> "Is":
        self.check.is_geopoint()
        return self
