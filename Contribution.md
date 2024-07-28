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

# Setup
- Clone the repo: `git clone git@github.com:akhildevelops/foss-wisdom.git`
- Run `pip install -e .` for developing application.
- Run `python main.py` to analyse sample instore video and generate artifacts.