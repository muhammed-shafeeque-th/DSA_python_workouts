from typing import Generic, Iterable, List, Optional, Sequence, TypeVar, Tuple

T = TypeVar("T")


class Stack(Generic[T]):
    """
    Simple stack implementation backed by a Python list.

    Parameters
    - capacity: Optional[int] - maximum number of items the stack can hold.
      If None, the stack is unbounded.

    Behavior
    - push raises OverflowError if capacity is set and reached.
    - pop and peek raise IndexError if the stack is empty.
    """

    def __init__(self, capacity: Optional[int] = None, items: Optional[Iterable[T]] = None) -> None:
        if capacity is not None and capacity < 0:
            raise ValueError("capacity must be >= 0 or None for unbounded stack")
        self._capacity: Optional[int] = capacity
        self._items: List[T] = list(items) if items is not None else []

        if self._capacity is not None and len(self._items) > self._capacity:
            raise ValueError("initial items exceed specified capacity")

    def push(self, value: T) -> None:
        """Push a value onto the stack. Raises OverflowError if capacity is reached."""
        if self._capacity is not None and len(self._items) >= self._capacity:
            raise OverflowError("stack overflow: capacity reached")
        self._items.append(value)

    def pop(self) -> T:
        """Pop and return the top value. Raises IndexError if empty."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top value without removing it. Raises IndexError if empty."""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()

    def capacity(self) -> Optional[int]:
        """Return configured capacity (None if unbounded)."""
        return self._capacity

    def __len__(self) -> int:
        """Current number of items in the stack."""
        return len(self._items)

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return not self._items

    def to_list(self) -> List[T]:
        """Return a shallow copy of the stack's contents (bottom-to-top)."""
        return list(self._items)

    def to_tuple(self) -> Tuple[T, ...]:
        """Return an immutable tuple copy of the stack's contents (bottom-to-top)."""
        return tuple(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __repr__(self) -> str:
        cap = self._capacity if self._capacity is not None else "unbounded"
        return f"Stack(capacity={cap}, size={len(self._items)}, top={self._items[-1] if self._items else None})"
