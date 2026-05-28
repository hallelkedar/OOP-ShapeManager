# OOP Shape Manager

A concise and efficient Command-Line Interface (CLI) system to manage geometric shapes using Object-Oriented Programming (OOP) principles and persistent JSON storage.

## 🚀 Features
- **Full CRUD Support:** Create, Read, Update, and Delete shapes dynamically.
- **OOP Architecture:** Uses a base class (`Shape`) with polymorphic methods for areas and perimeters.
- **Persistent Storage:** Synchronizes runtime object states to `shapes.json`.
- **Robust Validation:** Error and input handling for non-existent IDs or invalid dimensions.

---

## 📁 Directory Structure
```text
OOP-Shape-Manager/
│
├── main.py              # Application entry point & CLI Menu
├── shape.py             # Base Class (Shape)
├── shape_manager.py     # Business logic & JSON core handler
├── shapes.json          # Persistent JSON storage database
├── utils.py             # Validate input
└── shapes/              # Subclasses folder
    ├── square.py
    ├── rectangle.py
    ├── circle.py
    ├── triangle.py
    └── hexagon.py