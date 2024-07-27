# In VSCode:
For debugging the code choose below config in the launch.json file
```json
 {
            "name": "Python: Debug Tests",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "purpose": [
                "debug-test"
            ],
            "console": "integratedTerminal",
            "justMyCode": false
}
```