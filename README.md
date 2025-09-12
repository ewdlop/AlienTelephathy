# AlienTelephathy

What is this nutty Earthlings doing?
Why does it want to consume all the fuel of the universe?
A passive-aggressive bastard!
It is a bug in our program!

## 🛸 Earth Vacation System 🌍

Welcome to the Alien Telepathy Earth Vacation Planning System! Now you can plan the perfect vacation to observe those curious Earthlings in their natural habitat.

### Features

- **Multiple Vacation Packages**: Choose from various Earth observation experiences
- **Telepathic Communication**: Secure booking confirmation via telepathic channels
- **Fuel Consumption Research**: Special investigative packages to understand human energy obsession
- **Interactive CLI**: Easy-to-use command line interface for vacation planning

### Available Packages

1. **Human Settlement Observation Tour** - Watch humans in their urban environments
2. **Natural Phenomena Experience** - Enjoy Earth's wilderness without human interference  
3. **Cultural Immersion Program** - Deep dive into human civilization
4. **Fuel Consumption Investigation** - Research human energy consumption patterns

### Quick Start

```bash
# Run the interactive vacation planner
python3 vacation_cli.py

# Or run the demo
python3 earth_vacation.py
```

### Files

- `earth_vacation.py` - Main vacation planning module
- `vacation_cli.py` - Interactive command line interface
- `vacation_config.json` - Vacation packages and telepathy protocol configuration

### Usage Example

```python
from earth_vacation import EarthVacationPlanner

planner = EarthVacationPlanner()

# View available destinations
destinations = planner.list_destinations()

# Book a vacation
booking = planner.book_vacation("ALIEN_X42", "earth_001", "2024-06-15")

# Send telepathic confirmation
confirmation = planner.send_telepathic_confirmation(booking['booking_id'])
```

Remember: Always use appropriate telepathy frequency levels to avoid overwhelming the local human population!
