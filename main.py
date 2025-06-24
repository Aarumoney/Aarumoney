services:
  - type: worker
    name: SnjuPatternBot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
