from fluentcheck.assertions_is.base_is import IsBase


class __IsStrings(IsBase):
    @property
    def string(self) -> "Is":
        self.check.is_string()
        return self
    
    @property
    def not_string(self) -> "Is":
        self.check.is_not_string()
        return self

    @property
    def contains_numbers(self) -> "Is":
        self.check.contains_numbers()
        return self

    @property
    def not_contains_numbers(self) -> "Is":
        self.check.not_contains_numbers()
        return self

    @property
    def only_numbers(self) -> "Is":
        self.check.contains_numbers_only()
        return self

    @property
    def contains_chars(self) -> "Is":
        self.check.contains_chars()
        return self

    @property
    def not_contains_chars(self) -> "Is":
        self.check.not_contains_chars()
        return self

    @property
    def only_chars(self) -> "Is":
        self.check.contains_chars_only()
        return self

    @property
    def contains_spaces(self) -> "Is":
        self.check.contains_spaces()
        return self

    @property
    def lowercase(self) -> "Is":
        self.check.is_lowercase()
        return self

    @property
    def not_lowercase(self) -> "Is":
        self.check.is_not_lowercase()
        return self

    @property
    def uppercase(self) -> "Is":
        self.check.is_uppercase()
        return self

    @property
    def not_uppercase(self) -> "Is":
        self.check.is_not_uppercase()
        return self

    @property
    def camelcase(self) -> "Is":
        self.check.is_camelcase()
        return self

    @property
    def not_camelcase(self) -> "Is":
        self.check.is_not_camelcase()
        return self

    @property
    def snakecase(self) -> "Is":
        self.check.is_snakecase()
        return self

    @property
    def not_snakecase(self) -> "Is":
        self.check.is_not_snakecase()
        return self

    @property
    def unicode(self) -> "Is":
        self.check.is_unicode()
        return self

    @property
    def not_unicode(self) -> "Is":
        self.check.is_not_unicode()
        return self

    @property
    def json(self) -> "Is":
        self.check.is_json()
        return self

    @property
    def not_json(self) -> "Is":
        self.check.is_not_json()
        return self

    @property
    def yaml(self) -> "Is":
        self.check.is_yaml()
        return self

    @property
    def not_yaml(self) -> "Is":
        self.check.is_not_yaml()
        return self

    @property
    def xml(self) -> "Is":
        self.check.is_xml()
        return self

    @property
    def not_xml(self) -> "Is":
        self.check.is_not_xml()
        return self

    def matches(self, pattern: str) -> "Is":
        self.check.matches(pattern)
        return self

    def not_matches(self, pattern: str) -> "Is":
        self.check.not_matches(pattern)
        return self

    def contains_char(self, char: str) -> "Is":
        self.check.contains_char(char)
        return self

    def same_as(self, char:str) -> "Is":
        self.check.same_as(char)
        return self

    def not_same_as(self, char:str) -> "Is":
        self.check.not_same_as(char)
        return self
        
    def not_contains_char(self, char: str) -> "Is":
        self.check.not_contains_char(char)
        return self

    def shorter_than(self, max_length: int) -> "Is":
        self.check.is_shorter_than(max_length)
        return self

    def longer_than(self, min_length: int) -> "Is":
        self.check.is_longer_than(min_length)
        return self

    def length(self, exact_length: int) -> "Is":
        self.check.has_length(exact_length)
        return self

    def not_length(self, exact_length: int) -> "Is":
        self.check.has_not_length(exact_length)
        return self
