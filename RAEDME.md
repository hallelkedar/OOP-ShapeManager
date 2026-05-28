# OOP Shape Manager

A modular Python command-line interface (CLI) application that implements full **CRUD** functionality for managing geometric shapes. The project leverages core **Object-Oriented Programming (OOP)** principles and uses **JSON** file handling for persistent data storage.

---

## Project Overview
This system allows users to create, view, update, and delete various geometric shapes. While shapes exist as dynamic, rich objects in memory—automatically calculating their own areas and perimeters—their state is serialized and persisted into a local JSON database so that no data is lost when the program exits.

---

## Project Architecture & Directory Structure
The project strictly follows the single-responsibility principle, separating each class into its own dedicated file:

```text
shape_crud/
│
├── main.py             # Application entry point & interactive CLI menu loop
├── shape.py            # Abstract/Base class for all geometric shapes
├── rectangle.py        # Rectangle shape subclass
├── square.py           # Square shape subclass
├── circle.py           # Circle shape subclass
├── triangle.py         # Triangle shape subclass
├── hexagon.py          # Hexagon shape subclass
├── shape_manager.py    # Data layer coordinator (CRUD logic & JSON parsing)
└── shapes.json         # Local flat-file JSON database