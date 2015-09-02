# Readme

This is test project to show how to organize your python package correctly in small projects

# Execution & Unit Tests

Execution
```
./run xxx yyy 
```

Unit Tests
```
./launch_tests
```

# Project Tree

```
├── README.md
├── launch_tests
├── pktest
│   ├── __init__.py
│   ├── __main__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── base_controller.py
│   │   ├── controller1.py
│   │   └── controller2.py
│   ├── libs
│   │   ├── __init__.py
│   │   ├── lib1.py
│   │   └── lib2.py
│   └── main.py
├── run
└── tests
    ├── __init__.py
    ├── controllers
    │   ├── __init__.py
    │   └── controller1_tests.py
    └── libs
        ├── __init__.py
        └── lib1_tests.py
        
```

# Enjoy it :)

