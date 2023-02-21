# dna notes

## Getting started

### Representing Arguments

Youens-Clark recommends using typed named tuples to represent the arguments.

A typed named tuple can be thought of as an abstract factory for representing some data, in this case a sequence that has attributes of a name and a seq which can be used to instantiate a `Sequence` object:

```python
from typing import NamedTuple

class Sequence(NamedTuple):
    id: str
    seq: str

seq3 = Sequence('CAM_0231669729', 'GTGTTTATTCAATGCTAG')
```

This is a nice solution for taking command line arguments, but I think I prefer dataclasses to named tuples.
PEP 557 has a [brief discussion of why dataclasses may be preferred to named tuples](https://peps.python.org/pep-0557/#why-not-just-use-namedtuple).
I like to use frozen `dataclasses` to get some of the advantages of using a named tuple such as immutability (although mutable objects inside of dataclasses can still be modified) which will also make the `dataclass` hashable.
The same as above can be accomplished here using dataclasses instead:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Sequence:
    id: str
    seq: str

seq3 = Sequence(id='CAM_0231669729', seq='GTGTTTATTCAATGCTAG')
```

### Typing and `mypy`

While I am a huge fan of type checking in Python and would go so far as to say it should always be used for maintainability, readability, reusability, IDE help, etc. I am not a fan of `mypy`.
My main reasoning here, briefly, is that there are certain advantages to having a dynamically typed language like Python, and frankly it does not make much sense to me to try and turn Python into something that it is not mainly for the convenience of compile-time checking.
It is my firm belief that with proper use of the Python data model, Pythonic design practices, and proper type hinting that static type checking is not only unnecessary but is actually a hindrance.
As such, while I respect Youens-Clark's use of `mypy`, I will not be making use of it here.

### Input/Output
