#!/usr/bin/env python3
def greet(name: str) -> str:
    """Повертає вітальне повідомлення."""
    return f"Привіт, {name}!"

def farewell(name: str) -> str:
    """Повертає прощальне повідомлення."""
    return f"До побачення, {name}!"

if __name__ == "__main__":
    print(greet("Студент"))
