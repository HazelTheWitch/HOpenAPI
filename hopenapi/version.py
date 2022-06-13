import re
from typing import Generator, Union, overload, Optional
from functools import total_ordering

__all__ = [
    'Version'
]

VERSION_LIKE = Union[str, tuple[int, int, int], 'Version']

# Matches any version with a simple major.minor.patch with optional v prefix
VERSION_PATTERN = re.compile(r'^v?(\d+)\.(\d+)\.(\d+)$')


@total_ordering
class Version:
    @overload
    def __init__(self, version: str) -> None:
        ...

    @overload
    def __init__(self, version: tuple[int, int, int]) -> None:
        ...

    @overload
    def __init__(self, major: int, minor: int, patch: int) -> None:
        ...

    def __init__(self, majorOrVersion: Union[str, int, tuple[int, int, int]], minor: Optional[int] = None, patch: Optional[int] = None) -> None:
        if type(majorOrVersion) == tuple and all(map(lambda p: type(p) == int, majorOrVersion)):
            self.major, self.minor, self.patch = majorOrVersion
        elif all(map(lambda p: type(p) == int, (majorOrVersion, minor, patch))):
            self.major = majorOrVersion
            self.minor = minor
            self.patch = patch
        elif type(majorOrVersion) == str and all(map(lambda v: v is None, (minor, patch))):
            match = VERSION_PATTERN.match(majorOrVersion.strip())
            self.major = int(match.group(1))
            self.minor = int(match.group(2))
            self.patch = int(match.group(3))
        else:
            raise ValueError(f'{majorOrVersion}, {minor}, or {patch} is an invalid data type.')

    def __iter__(self) -> Generator[int, None, None]:
        yield self.major
        yield self.minor
        yield self.patch

    @property
    def tuple(self) -> tuple[int, int, int]:
        return self.major, self.minor, self.patch

    @staticmethod
    def _processVersionLike(other: VERSION_LIKE) -> 'Version':
        match other:
            case Version():
                return other
            case (major, minor, patch):
                return Version(major, minor, patch)
            case str():
                return Version(other)
            case _:
                raise ValueError(f'Invalid version type: {type(other)}')

    def __lt__(self, other: VERSION_LIKE) -> bool:
        return self.tuple < self._processVersionLike(other).tuple

    def __eq__(self, other: VERSION_LIKE) -> bool:
        return self.tuple == self._processVersionLike(other).tuple

    def __repr__(self) -> str:
        return f'Version({self.major, self.minor, self.patch})'

    def __str__(self) -> str:
        return f'{self.major}.{self.minor}.{self.patch}'
